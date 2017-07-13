from django.test import TestCase
from django.shortcuts import render_to_response
from django.core.urlresolvers import resolve
from models import Subject
from views import forum, threads, thread


class ThreadsAppTest(TestCase):

    def test_subjects_page_resolves(self):
        subjects_page = resolve('/forum/')
        self.assertEqual(subjects_page.func, forum)

    def test_subjects_page_status_code_is_okay(self):
        subjects_page = self.client.get('/forum/')
        self.assertEqual(subjects_page.status_code, 200)

    def test_threads_page_resolves(self):
        threads_page = resolve('/forum/threads/1/')
        self.assertEqual(threads_page.func, threads)

    def test_threads_page_status_code_is_okay(self):
        threads_page = self.client.get('/forum/threads/1/')
        self.assertEqual(threads_page.status_code, 200)

    def test_thread_page_resolves(self):
        thread_page = resolve('/forum/thread/1/')
        self.assertEqual(thread_page.func, thread)

    def test_thread_page_status_code_is_okay(self):
        thread_page = self.client.get('/forum/thread/1/')
        self.assertEqual(thread_page.status_code, 200)

    fixtures = ['subjects', 'user']

    def test_check_subject_content_is_correct(self):
        self.maxDiff = None
        subject_page = self.client.get('/forum/')
        self.assertTemplateUsed(subject_page, "forum/forum.html")
        subject_page_template_output = render_to_response("forum/forum.html",
                                                          {'subjects': Subject.objects.all()}).content
        self.assertHTMLEqual(subject_page.content, subject_page_template_output)
