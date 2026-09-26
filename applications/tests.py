from django.test import TestCase
from django.contrib.auth.models import User
from companies.models import Companies
from candidates.models import Candidate
from jobs.models import Job
from applications.models import Application


class ApplicationPermissionTests(TestCase):
    """
    Tests confirming that only candidates can apply, candidates cannot
    apply twice, and companies can only review/manage applicants for
    their own jobs.
    """
    # setup mock data 
    def setUp(self):
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
            skills='Python, Django',
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

    def test_company_cannot_apply_to_job(self):
        """
        A company account should be denied access to the apply endpoint.
        """
        self.client.login(username='companya', password='testpass123')
        response = self.client.post(f'/applications/apply/{self.job.slug}/', {
            'cover_note': 'Test cover note',
            'uk_working_status': True,
        })
        self.assertEqual(response.status_code, 403)

    def test_candidate_can_apply_to_job(self):
        """
        A candidate should be able to successfully submit an application.
        """
        self.client.login(username='candidate1', password='testpass123')
        self.client.post(f'/applications/apply/{self.job.slug}/', {
            'cover_note': 'Test cover note',
            'uk_working_status': True,
        })
        self.assertTrue(
            Application.objects.filter(job=self.job, candidate=self.candidate).exists()
        )

    def test_candidate_cannot_apply_twice(self):
        """
        A second application to the same job by the same candidate must not create a duplicate row.
        """
        self.client.login(username='candidate1', password='testpass123')
        self.client.post(f'/applications/apply/{self.job.slug}/', {
            'cover_note': 'First application',
            'uk_working_status': True,
        })
        self.client.post(f'/applications/apply/{self.job.slug}/', {
            'cover_note': 'Second application attempt',
            'uk_working_status': True,
        })
        count = Application.objects.filter(job=self.job, candidate=self.candidate).count()
        self.assertEqual(count, 1)

    def test_company_can_review_own_job_applicants(self):
        """
        A company should be able to view the applicants list for its own job.
        """
        Application.objects.create(
            job=self.job,
            candidate=self.candidate,
            cover_note='Test',
            uk_working_status=True
        )
        self.client.login(username='companya', password='testpass123')
        response = self.client.get(f'/applications/review/{self.job.slug}/')
        self.assertEqual(response.status_code, 200)

    def test_company_cannot_review_another_companys_applicants(self):
        """
        Company B must not be able to view applicants for a job owned by Company A.
        """
        Application.objects.create(
            job=self.job,
            candidate=self.candidate,
            cover_note='Test',
            uk_working_status=True
        )
        self.client.login(username='companyb', password='testpass123')
        response = self.client.get(f'/applications/review/{self.job.slug}/')
        self.assertEqual(response.status_code, 403)

    def test_candidate_can_withdraw_own_application(self):
        """
        Withdrawing an application should set its status to withdrawn, not delete it."
        """

        application = Application.objects.create(
            job=self.job,
            candidate=self.candidate,
            cover_note='Test',
            uk_working_status=True
        )
        self.client.login(username='candidate1', password='testpass123')
        self.client.post(f'/applications/withdraw/{application.pk}/')
        application.refresh_from_db()
        self.assertEqual(application.status, 'withdrawn')
        self.assertTrue(Application.objects.filter(pk=application.pk).exists())

    def test_candidate_cannot_withdraw_another_candidates_application(self):
        """
        A candidate must not be able to withdraw someone else's application.
        """
        other_candidate_user = User.objects.create_user(username='candidate2', password='testpass123')
        other_candidate = Candidate.objects.create(
            account=other_candidate_user,
            first_name='Other',
            last_name='Candidate',
            personal_statement='Test',
            skills='Test',
            experience='Test'
        )
        application = Application.objects.create(
            job=self.job,
            candidate=other_candidate,
            cover_note='Test',
            uk_working_status=True
        )
        self.client.login(username='candidate1', password='testpass123')
        response = self.client.post(f'/applications/withdraw/{application.pk}/')
        self.assertEqual(response.status_code, 403)