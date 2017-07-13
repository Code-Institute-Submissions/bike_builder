from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.context_processors import csrf
from threads.models import Subject, Post, Thread
from threads.forms import ThreadForm, PostForm
from django.forms import formset_factory
from polls.forms import PollSubjectForm, PollForm
from polls.models import PollSubject


def forum(request):
    """
    List all subjects
    """
    return render(request, 'forum/forum.html',
                  {'subjects': Subject.objects.all()})


def threads(request, subject_id):
    """
    List the subject threads, subject to pagination
    """
    def latest_thread_date(t):
        return t.posts.all().order_by('-created_at')[0].created_at

    subject = get_object_or_404(Subject, pk=subject_id)
    thread_list = list(subject.threads.all())
    thread_list.sort(reverse=True, key=latest_thread_date)
    paginator = Paginator(thread_list, 10)  # 10 in each page
    page = request.GET.get('page')
    try:
        threads_ = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        threads_ = paginator.page(1)
    except EmptyPage:
        #  If page is out of range (e.g. 9999), deliver last page of results
        threads_ = paginator.page(paginator.num_pages)

    return render(request, 'forum/threads.html', {'subject': subject, 'page': page, 'threads_': threads_})


@login_required
def new_thread(request, subject_id):
    """
    Create new thread with accompanying post
    """
    subject = get_object_or_404(Subject, pk=subject_id)

    poll_subject_formset = formset_factory(PollSubjectForm, extra=3)

    if request.method == "POST":
        thread_form = ThreadForm(request.POST)
        post_form = PostForm(request.POST)
        poll_form = PollForm(request.POST)
        poll_subject_formset = poll_subject_formset(request.POST)

        if request.POST.get('is_a_poll', None):

            # save the thread with a poll
            if thread_form.is_valid() and post_form.is_valid()\
                    and poll_form.is_valid() \
                    and poll_subject_formset.is_valid():
                thread = thread_form.save(False)
                thread.subject = subject
                thread.user = request.user
                thread.save()

                post = post_form.save(False)
                post.user = request.user
                post.thread = thread
                post.save()

                poll = poll_form.save(False)
                poll.thread = thread
                poll.save()

                for subject_form in poll_subject_formset:
                    subject = subject_form.save(False)
                    subject.poll = poll
                    subject.save()

                messages.success(request, "You have created a new thread!")

                return redirect(reverse('thread', args={thread.pk}))

        else:
            # save the thread without a poll
            if thread_form.is_valid() and post_form.is_valid() and poll_subject_formset.is_valid():
                thread = thread_form.save(False)
                thread.subject = subject
                thread.user = request.user
                thread.save()

                post = post_form.save(False)
                post.user = request.user
                post.thread = thread
                post.save()

                messages.success(request, "You have created a new thread!")

                return redirect(reverse('thread', args={thread.pk}))

    else:
        thread_form = ThreadForm()
        post_form = PostForm(request.POST)
        poll_form = PollForm()
        poll_subject_formset = poll_subject_formset()

    args = {
        'thread_form': thread_form,
        'post_form': post_form,
        'subject': subject,
        'poll_form': poll_form,
        'poll_subject_formset': poll_subject_formset
    }

    args.update(csrf(request))

    return render(request, 'forum/thread_form.html', args)


def thread(request, thread_id):
    """
    Show thread message plus all associated posts,
    subject to pagination
    """
    thread_ = get_object_or_404(Thread, pk=thread_id)
    post_list = thread_.posts.all()
    paginator = Paginator(post_list, 10)  # 10 in each page
    page = request.GET.get('page')
    try:
        thread_posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        thread_posts = paginator.page(1)
        thread_.views += 1  # clock up the number of thread views every time a user visits page 1
        thread_.save()

    except EmptyPage:
        #  If page is out of range (e.g. 9999), deliver last page of results
        thread_posts = paginator.page(paginator.num_pages)

    args = {'thread': thread_, 'page': page, 'thread_posts': thread_posts}
    args.update(csrf(request))

    return render(request, 'forum/thread.html', args)


@login_required
def new_post(request, thread_id):
    """
    Create new post then return to previous (paginated) page
    """
    thread = get_object_or_404(Thread, pk=thread_id)
    redirect_to = request.GET.get('next', '')

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(False)
            post.thread = thread
            post.user = request.user
            post.save()

            messages.success(request,
                             "Your post has been added to the thread!")

            return redirect(redirect_to)

    else:
        form = PostForm()

    args = {
        'form': form,
        'button_text': 'Save Post'
    }

    args.update(csrf(request))

    return render(request, 'forum/post_form.html', args)


@login_required
def edit_post(request, thread_id, post_id):
    """
    Edit post if created by user, then return to previous
    (paginated) page
    """
    thread = get_object_or_404(Thread, pk=thread_id)
    post = get_object_or_404(Post, pk=post_id)
    redirect_to = request.GET.get('next', '')

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "You have updated your post!")

            return redirect(redirect_to)
    else:
        form = PostForm(instance=post)

    args = {
        'form': form,
        'button_text': 'Update Post'
    }

    args.update(csrf(request))

    return render(request, 'forum/post_form.html', args)


@login_required
def delete_post(request, thread_id, post_id):
    """
    Delete post if created by user, then return to previous
    (paginated) page
    """
    post = get_object_or_404(Post, pk=post_id)
    thread_id = post.thread.id
    post.delete()

    messages.success(request, "Your post was deleted!")

    print request.get_full_path()
    print request.META.get('HTTP_REFERER', '/')
    print request.META.get('HTTP_REFERER')

    # return to current paginator page. If user has disabled referrer info,
    # it will redirect to home page
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def thread_vote(request, thread_id, subject_id):
    """
    Take user vote if not yet voted
    """
    thread = Thread.objects.get(id=thread_id)
    subject = thread.poll.votes.filter(user=request.user)

    if subject:
        messages.error(request, "You already voted on this!... "
                                "You're not trying to cheat are you?")
        return redirect(reverse('thread', args={thread_id}))

    subject = PollSubject.objects.get(id=subject_id)
    subject.votes.create(poll=subject.poll, user=request.user)

    messages.success(request, "We've registered your vote!")

    return redirect(reverse('thread', args={thread_id}))
