from django.test import TestCase
from django.shortcuts import render_to_response
from django.core.urlresolvers import resolve
from models import Subject
from views import forum, threads, thread


class ThreadsAppTest(TestCase):

    # Forum (subjects)
    # URL test
    def test_subjects_page_resolves(self):
        get_subjects_page = resolve('/forum/')
        self.assertEqual(get_subjects_page.func, forum)

    # Status code test
    def test_subjects_page_status_code_is_okay(self):
        subjects_page = self.client.get('/forum/')
        self.assertEqual(subjects_page.status_code, 200)

    # Content test
    def test_subjects_page_check_content_is_correct(self):
        subjects_page = self.client.get('/forum/')
        self.assertTemplateUsed(subjects_page, "forum/forum.html")
        subjects_page_template_output = render_to_response("forum/forum.html").content
        self.assertEqual(subjects_page.content, subjects_page_template_output)

    # Threads
    # URL test
    def test_threads_page_resolves(self):
        get_threads_page = resolve('/forum/threads/<subject_id>/')
        self.assertEqual(get_threads_page.func, threads)

    # Status code test
    def test_threads_page_status_code_is_okay(self):
        threads_page = self.client.get('/forum/threads/<subject_id>/')
        self.assertEqual(threads_page.status_code, 200)

    # Content test
    def test_threads_page_check_content_is_correct(self):
        threads_page = self.client.get('/forum/threads/<subject_id>/')
        self.assertTemplateUsed(threads_page, "forum/threads.html")
        threads_page_template_output = render_to_response("forum/threads.html").content
        self.assertEqual(threads_page.content, threads_page_template_output)

    # Thread
    # URL test
    def test_thread_page_resolves(self):
        get_thread_page = resolve('/forum/thread/<thread_id>/')
        self.assertEqual(get_thread_page.func, thread)

    # Status code test
    def test_thread_page_status_code_is_okay(self):
        thread_page = self.client.get('/forum/thread/<thread_id>/')
        self.assertEqual(thread_page.status_code, 200)

    # Content test
    def test_thread_page_check_content_is_correct(self):
        thread_page = self.client.get('/forum/thread/<thread_id>/')
        self.assertTemplateUsed(thread_page, "forum/thread.html")
        thread_page_template_output = render_to_response("forum/thread.html").content
        self.assertEqual(thread_page.content, thread_page_template_output)






    fixtures = ['subjects', 'user']

    def test_check_subject_content_is_correct(self):
        subject_page = self.client.get('/forum/')
        self.assertTemplateUsed(subject_page, "forum/forum.html")
        subject_page_template_output = render_to_response("forum/forum.html",
                                                          {'subjects': Subject.objects.all()}).content
        self.assertEqual(subject_page.content, subject_page_template_output)
