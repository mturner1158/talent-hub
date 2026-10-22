from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from companies.models import Companies
from jobs.models import Job
from applications.models import Application
from candidates.models import Candidate


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


class JobEditCrossRoleTests(TestCase):
    """
    Invalid and cross-role edit attempts: these previously caused a 500 for candidates.
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

    def valid_job_data(self, **overrides):
        data = {
            'title': 'New Job',
            'description': '<p>Description</p>',
            'location': 'Leeds',
            'salary_min': 30000,
            'salary_max': 40000,
            'job_type': 'full_time',
        }
        data.update(overrides)
        return data

 
    def edit_data(self, **overrides):
        data = self.valid_job_data(title='Hacked title', is_active='on')
        data.update(overrides)
        return data
 
    def test_anonymous_user_redirected_from_edit_job(self):
        response = self.client.get(reverse('edit_job', args=[self.job.slug]))
        self.assertEqual(response.status_code, 302)
 
    def test_candidate_gets_403_on_edit_job_get(self):
        self.client.login(username='candidate1', password='testpass123')
        response = self.client.get(reverse('edit_job', args=[self.job.slug]))
        self.assertEqual(response.status_code, 403)
 
    def test_candidate_gets_403_on_edit_job_post_and_job_unchanged(self):
        self.client.login(username='candidate1', password='testpass123')
        response = self.client.post(reverse('edit_job', args=[self.job.slug]), self.edit_data())
        self.assertEqual(response.status_code, 403)
        self.job.refresh_from_db()
        self.assertEqual(self.job.title, 'Junior Developer')
 
    def test_other_company_gets_403_on_edit_job_post_and_job_unchanged(self):
        self.client.login(username='companyb', password='testpass123')
        response = self.client.post(reverse('edit_job', args=[self.job.slug]), self.edit_data())
        self.assertEqual(response.status_code, 403)
        self.job.refresh_from_db()
        self.assertEqual(self.job.title, 'Junior Developer')
 
    def test_owner_can_edit_job(self):
        self.client.login(username='companya', password='testpass123')
        response = self.client.post(
            reverse('edit_job', args=[self.job.slug]),
            self.edit_data(title='Updated title'),
        )
        self.assertEqual(response.status_code, 302)
        self.job.refresh_from_db()
        self.assertEqual(self.job.title, 'Updated title')
 
    def test_owner_can_deactivate_job_and_record_is_retained(self):
        self.client.login(username='companya', password='testpass123')
        data = self.valid_job_data(title='Junior Developer')
        # omitting is_active from POST data unchecks the box
        self.client.post(reverse('edit_job', args=[self.job.slug]), data)
        self.job.refresh_from_db()
        self.assertFalse(self.job.is_active)
        self.assertTrue(Job.objects.filter(pk=self.job.pk).exists())
 
 
class JobDeleteTests(TestCase):
    """
    A company can only delete their own job and this is a post-only deletion.
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
        self.candidate = Candidate.objects.create(
            account=self.candidate_user,
            first_name='Test',
            last_name='Candidate',
            personal_statement='Test',
            skills='Python',
            experience='Test'
        )
    
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
 
    def delete_url(self):
        return reverse('delete_job', args=[self.job.slug])
 
    def test_anonymous_user_redirected_and_job_kept(self):
        response = self.client.post(self.delete_url())
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)
        self.assertTrue(Job.objects.filter(pk=self.job.pk).exists())
 
    def test_candidate_gets_403_and_job_kept(self):
        self.client.login(username='candidate1', password='testpass123')
        response = self.client.post(self.delete_url())
        self.assertEqual(response.status_code, 403)
        self.assertTrue(Job.objects.filter(pk=self.job.pk).exists())
 
    def test_other_company_gets_403_and_job_kept(self):
        self.client.login(username='companyb', password='testpass123')
        response = self.client.post(self.delete_url())
        self.assertEqual(response.status_code, 403)
        self.assertTrue(Job.objects.filter(pk=self.job.pk).exists())
 
    def test_get_request_does_not_delete_job(self):
        """
        Visiting the delete URL directly must never delete anything.
        """
        self.client.login(username='companya', password='testpass123')
        response = self.client.get(self.delete_url())
        self.assertEqual(response.status_code, 405)
        self.assertTrue(Job.objects.filter(pk=self.job.pk).exists())
 
    def test_owner_post_deletes_job_and_its_applications(self):
        Application.objects.create(
            job=self.job,
            candidate=self.candidate,
            cover_note='Test',
            uk_working_status=True
        )
        self.client.login(username='companya', password='testpass123')
        response = self.client.post(self.delete_url())
        self.assertRedirects(response, reverse('company_dashboard'), fetch_redirect_response=False)
        self.assertFalse(Job.objects.filter(pk=self.job.pk).exists())
        self.assertEqual(Application.objects.count(), 0)
 
    def test_deleting_missing_job_returns_404(self):
        self.client.login(username='companya', password='testpass123')
        response = self.client.post(reverse('delete_job', args=['no-such-job']))
        self.assertEqual(response.status_code, 404)