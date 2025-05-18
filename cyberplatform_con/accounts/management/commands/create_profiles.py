from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Profile

class Command(BaseCommand):
    help = 'Mevcut kullanıcılar için profil oluşturur'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            Profile.objects.get_or_create(user=user)
            self.stdout.write(f'Profil oluşturuldu: {user.username}') 