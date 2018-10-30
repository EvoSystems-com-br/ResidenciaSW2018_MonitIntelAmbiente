import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings")

django.setup()

from users_service.models import User

u = User(email='admin@admin', cpf='1234567890')
u.set_password('password')
u.is_superuser = True
u.is_staff = True
u.save()

