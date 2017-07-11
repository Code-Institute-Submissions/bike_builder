from django.test import TestCase
from django.shortcuts import render_to_response
from django.core.urlresolvers import resolve
from models import Subject
from views import forum, threads, thread


class ThreadsAppTest(TestCase):

    # Forum (subjects)
    # URL test
    def test_subjects_page_resolves(self):
        subjects_page = resolve('/forum/')
        self.assertEqual(subjects_page.func, forum)

    # Status code test
    def test_subjects_page_status_code_is_okay(self):
        subjects_page = self.client.get('/forum/')
        self.assertEqual(subjects_page.status_code, 200)

    # Content test
    # def test_check_subjects_page_content_is_correct(self):
    #     self.maxDiff = None
    #     subjects_page = self.client.get('/forum/')
    #     self.assertTemplateUsed(subjects_page, "forum/forum.html")
    #     subjects_page_template_output = render_to_response("forum/forum.html").content
    #     self.assertHTMLEqual(subjects_page.content, subjects_page_template_output)
    # # FAIL: AssertionError: It's like the logged in / not logged in issue, but different:
    # # A div has a space and forward slash at the end, whereas the comparison doesn't.

    # Threads
    # URL test
    def test_threads_page_resolves(self):
        threads_page = resolve('/forum/threads/1/')
        self.assertEqual(threads_page.func, threads)

    # Status code test
    def test_threads_page_status_code_is_okay(self):
        threads_page = self.client.get('/forum/threads/1/')
        self.assertEqual(threads_page.status_code, 200)

    # Content test
    # def test_check_threads_page_content_is_correct(self):
    #     self.maxDiff = None
    #     threads_page = self.client.get('/forum/threads/1/')
    #     self.assertTemplateUsed(threads_page, "forum/threads.html")
    #     threads_page_template_output = render_to_response("forum/threads.html").content
    #     self.assertHTMLEqual(threads_page.content, threads_page_template_output)
    # # FAIL: AssertionError: It's like the logged in / not logged in issue, but different:
    # # Differences seem to be the forum nav and pagination

    # Thread
    # URL test
    def test_thread_page_resolves(self):
        thread_page = resolve('/forum/thread/1/')
        self.assertEqual(thread_page.func, thread)

    # Status code test
    def test_thread_page_status_code_is_okay(self):
        thread_page = self.client.get('/forum/thread/1/')
        self.assertEqual(thread_page.status_code, 200)

    # Content test
    # def test_check_thread_page_content_is_correct(self):
    #     self.maxDiff = None
    #     thread_page = self.client.get('/forum/thread/1/')
    #     self.assertTemplateUsed(thread_page, "forum/thread.html")
    #     thread_page_template_output = render_to_response("forum/thread.html").content
    #     self.assertHTMLEqual(thread_page.content, thread_page_template_output)
    # # ERROR: NoReverseMatch: Reverse for 'threads' with arguments '('',)' and keyword arguments '{}' not found.
    # # 1 pattern(s) tried: ['forum/threads/(?P<subject_id>\\d+)/$']

    fixtures = ['subjects', 'user']

    def test_check_subject_content_is_correct(self):
        self.maxDiff = None
        subject_page = self.client.get('/forum/')
        self.assertTemplateUsed(subject_page, "forum/forum.html")
        subject_page_template_output = render_to_response("forum/forum.html",
                                                          {'subjects': Subject.objects.all()}).content
        self.assertHTMLEqual(subject_page.content, subject_page_template_output)
