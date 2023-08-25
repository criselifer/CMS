import unittest
from django.conf import settings
from pathlib import Path
import sys
sys.path.append("..")
import CSM.settings as settings

class DatabaseSettingsTestCase(unittest.TestCase):
    def test_database_config(self):
        # Build paths inside the project like this: BASE_DIR / 'subdir'.
        BASE_DIR = Path(__file__).resolve().parent.parent
        expected_path_name = BASE_DIR / "db.sqlite3"
        self.assertEqual(settings.DATABASES["default"]["ENGINE"], "django.db.backends.sqlite3")
        self.assertEqual(settings.DATABASES["default"]["NAME"], expected_path_name)


if __name__ == '__main__':
    unittest.main()
