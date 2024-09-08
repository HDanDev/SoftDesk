from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = 'Create a new user manually'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('age', type=int)
        parser.add_argument('--can_be_contacted', action='store_true')
        parser.add_argument('--can_data_be_shared', action='store_true')

    def handle(self, *args, **options):
        user = User.objects.create_user(
            username=options['username'],
            email=options['email'],
            password=options['password'],
            age=options['age'],
            can_be_contacted=options['can_be_contacted'],
            can_data_be_shared=options['can_data_be_shared']
        )
        self.stdout.write(self.style.SUCCESS('User created successfully'))
