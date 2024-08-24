from django.test import TestCase
from django.contrib.auth.hashers import make_password
from accounts.models import SurveyAdmin
from accounts.repository import SurveyAdminRepository

class SurveyAdminRepositoryTests(TestCase):
    
    def setUp(self):
        # Create a test SurveyAdmin instance
        self.admin = SurveyAdmin.objects.create(
            username="testuser",
            password=make_password("password123")
        )

    def test_get_by_id_success(self):
        admin = SurveyAdminRepository.get_by_id(self.admin.admin_id)
        self.assertEqual(admin, self.admin)

    def test_get_by_id_not_found(self):
        admin = SurveyAdminRepository.get_by_id("nonexistent_id")
        self.assertIsNone(admin)

    def test_get_by_username_success(self):
        admin = SurveyAdminRepository.get_by_username(self.admin.username)
        self.assertEqual(admin, self.admin)

    def test_get_by_username_not_found(self):
        admin = SurveyAdminRepository.get_by_username("nonexistentuser")
        self.assertIsNone(admin)

    def test_create(self):
        admin = SurveyAdminRepository.create("newuser", "newpassword")
        self.assertEqual(admin.username, "newuser")
        self.assertTrue(admin.check_password("newpassword"))

    def test_update_success(self):
        updated_admin = SurveyAdminRepository.update(self.admin.admin_id, username="updateduser", password="newpassword")
        self.assertEqual(updated_admin.username, "updateduser")
        self.assertTrue(updated_admin.check_password("newpassword"))

    def test_update_not_found(self):
        updated_admin = SurveyAdminRepository.update("nonexistent_id", username="updateduser")
        self.assertIsNone(updated_admin)

    def test_delete_success(self):
        result = SurveyAdminRepository.delete(self.admin.admin_id)
        self.assertTrue(result)
        self.assertIsNone(SurveyAdminRepository.get_by_id(self.admin.admin_id))

    def test_delete_not_found(self):
        result = SurveyAdminRepository.delete("nonexistent_id")
        self.assertFalse(result)
