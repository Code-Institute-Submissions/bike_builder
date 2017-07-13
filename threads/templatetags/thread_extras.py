import arrow
from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.filter
def get_total_subject_posts(subject):
    """
    Calculate total number of posts for subject
    """
    total_posts = 0
    for thread in subject.threads.all():
        total_posts += thread.posts.count()
    return total_posts


@register.filter
def started_time(created_at):
    """
    Convert created_at field to human-readable format
    eg 'two weeks ago'
    """
    return arrow.get(created_at).humanize()


@register.simple_tag
def last_posted_user_name(thread):
    """
    Who was the last poster in a thread?
    """
    posts = thread.posts.all().order_by('created_at')
    return posts[posts.count()-1].user.public_name


@register.simple_tag
def last_posted_timing(thread):
    """
    When was the last postmade in a thread?
    """
    posts = thread.posts.all().order_by('created_at')
    _posts = posts[posts.count()-1].created_at
    return arrow.get(_posts).humanize()


@register.simple_tag
def subject_thread_with_last_post(subject):
    """
    For a subject, return name of thread
    which has most recent post
    """
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
    """
    For a subject, return abbreviated comment
    of most recent post
    """
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
    """
    For a subject, return date of most recent post
    """
    def latest_thread_date(t):
        return t.posts.all().order_by('-created_at')[0].created_at

    thread_list = list(subject.threads.all())
    thread_list.sort(reverse=True, key=latest_thread_date)
    latest_post_date = thread_list[0].posts.all().order_by('-created_at')[0].created_at
    return arrow.get(latest_post_date).humanize()


@register.simple_tag
def user_vote_button(thread, subject, user):
    """
    Take user's vote if not yet voted
    """
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
    """
    Calculate vote percentage
    """
    count = subject.votes.count()
    if count == 0:
        return 0
    total_votes = subject.poll.votes.count()
    return (100 / total_votes) * count
