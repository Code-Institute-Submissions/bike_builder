import arrow
from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.filter
def get_total_subject_posts(subject):
    total_posts = 0
    for thread in subject.threads.all():
        total_posts += thread.posts.count()

    return total_posts


@register.filter
def started_time(created_at):
    return arrow.get(created_at).humanize()


@register.simple_tag
def last_posted_user_name(thread):
    posts = thread.posts.all().order_by('created_at')
    return posts[posts.count()-1].user.username


@register.simple_tag
def last_posted_timing(thread):
    posts = thread.posts.all().order_by('created_at')
    _posts = posts[posts.count()-1].created_at
    return arrow.get(_posts).humanize()


# @register.filter
# def threads_ordered_by_latest_post(subject):
#     latest_posts = []
#     for thread in subject.threads.all():
#         thread_posts = thread.posts.all().order_by('created_at')
#         latest_posts.append(latest_posts[latest_posts.count() - 1])
#     subject_list = []
#     for post in latest_posts:
#         subject_list
#     return


# @register.simple_tag
# def forum_display_name(username):
#     return username.split("@")[0]


# @register.simple_tag
# def last_subject_post(subject):
#     posts = subject.threads.posts.all().order_by('created_at')
#     return posts[posts.count()-1].comment


@register.simple_tag
def subject_thread_with_last_post(subject):

    def latest_thread_date(t):
        return t.posts.all().order_by('-created_at')[0].created_at

    thread_list = list(subject.threads.all())
    thread_list.sort(reverse=True, key=latest_thread_date)
    full_thread_name = thread_list[0].name[:60]
    if len(full_thread_name) >= 60:
        return full_thread_name[:60] + '...'
    else:
        return full_thread_name


@register.simple_tag
def latest_subject_post_comment(subject):

    def latest_thread_date(t):
        return t.posts.all().order_by('-created_at')[0].created_at

    thread_list = list(subject.threads.all())
    thread_list.sort(reverse=True, key=latest_thread_date)
    full_post_comment = thread_list[0].posts.all().order_by('-created_at')[0].comment
    abbreviated_post_comment = full_post_comment[3:(len(full_post_comment)-4)]
    if len(abbreviated_post_comment) >= 150:
        return abbreviated_post_comment[:150] + '...'
    else:
        return abbreviated_post_comment


@register.simple_tag
def latest_subject_post_date(subject):

    def latest_thread_date(t):
        return t.posts.all().order_by('-created_at')[0].created_at

    thread_list = list(subject.threads.all())
    thread_list.sort(reverse=True, key=latest_thread_date)
    latest_post_date = thread_list[0].posts.all().order_by('-created_at')[0].created_at
    return arrow.get(latest_post_date).humanize()


@register.simple_tag
def latest_post_thread_id(subject):

    def latest_thread_date(t):
        return t.posts.all().order_by('-created_at')[0].created_at

    thread_list = list(subject.threads.all())
    thread_list.sort(reverse=True, key=latest_thread_date)
    print thread_list[0].id
    return thread_list[0].id


# @register.simple_tag
# def last_subject_post(subject):
#     latest_posts = []
#     for thread in subject.threads.all():
#         post_list = thread.posts.all().order_by('created_at')
#         latest_posts.append(post_list[post_list.count()-1])
#     last_posts = latest_posts.order_by('created_at')
#     last_post = last_posts[last_posts.count()-1]
#     return last_post


@register.simple_tag
def user_vote_button(thread, subject, user):
    vote = thread.poll.votes.filter(user_id=user.id).first()

    if not vote:
        if user.is_authenticated():
            link = """
                <div class="col-xs-3 btn-vote">
                    <a href="%s" class="btn btn-default btn-sm">
                        Add my vote!
                    </a>
                </div>
            """ % reverse('cast_vote', kwargs={
                'thread_id': thread.id,
                'subject_id': subject.id
            })

            return link
    return ""


@register.filter
def vote_percentage(subject):
    count = subject.votes.count()
    if count == 0:
        return 0
    total_votes = subject.poll.votes.count()
    return (100 / total_votes) * count
