from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from companies.models import Companies
from jobs.models import Job


class JobPermissionTests(TestCase):
    """
    Tests confirming that only companies can create/edit jobs,
    and that a company can never edit another company's job.
    """

    #setup mock data
    def setUp(self):
        # Two separate companies, so we can test cross-company permission checks
        self.company_user_a = User.objects.create_user(username='companya', password='testpass123')
        self.company_a = Companies.objects.create(
            owner=self.company_user_a,
            company_name='Company A',
            description='Test',
            sectors='Tech'
        )

        self.company_user_b = User.objects.create_user(username='companyb', password='testpass123')
        self.company_b = Companies.objects.create(
            owner=self.company_user_b,
            company_name='Company B',
            description='Test',
            sectors='Tech'
        )

        self.candidate_user = User.objects.create_user(username='candidate1', password='testpass123')

        self.job = Job.objects.create(
            company=self.company_a,
            title='Junior Developer',
            description='Test description',
            location='York, UK',
            salary_min=25000,
            salary_max=30000,
            job_type='full_time',
            is_active=True
        )

    def test_anonymous_user_cannot_access_post_job(self):
        """
        An anonymous visitor should be redirected to login, not shown the form.
        """
        response = self.client.get(reverse('post_job'))
        self.assertEqual(response.status_code, 302)

    def test_candidate_cannot_post_job(self):
        """
        A logged-in candidate should be denied access to the post job form.
        """
        self.client.login(username='candidate1', password='testpass123')
        response = self.client.get(reverse('post_job'))
        self.assertEqual(response.status_code, 403)

    def test_company_can_access_post_job_form(self):
        """
        A logged-in company should be able to access the post job form.
        """
        self.client.login(username='companya', password='testpass123')
        response = self.client.get(reverse('post_job'))
        self.assertEqual(response.status_code, 200)

    def test_company_can_edit_own_job(self):
        """
        A company should be able to access the edit form for its own job.
        """
        self.client.login(username='companya', password='testpass123')
        response = self.client.get(reverse('edit_job', args=[self.job.slug]))
        self.assertEqual(response.status_code, 200)

    def test_company_cannot_edit_another_companys_job(self):
        """
        Company B must not be able to edit a job owned by Company A.
        """
        self.client.login(username='companyb', password='testpass123')
        response = self.client.get(reverse('edit_job', args=[self.job.slug]))
        self.assertEqual(response.status_code, 403)

    def test_inactive_job_returns_404_on_detail_page(self):
        """
        A deactivated job should not be viewable via its detail page.
        """
        self.job.is_active = False
        self.job.save()
        response = self.client.get(reverse('job_detail', args=[self.job.slug]))
        self.assertEqual(response.status_code, 404)

    def test_active_job_appears_in_job_list(self):
        """
        An active job should appear in the public job list.
        """
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Junior Developer')

    def test_inactive_job_does_not_appear_in_job_list(self):
        """
        A deactivated job should not appear in the public job list.
        """
        self.job.is_active = False
        self.job.save()
        response = self.client.get(reverse('home'))
        self.assertNotContains(response, 'Junior Developer')