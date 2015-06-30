import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "survey.settings")
import django
django.setup()
from survey.models import debug_response

debug_response()