from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create a user with specified fields'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, required=True, help='Username')
        parser.add_argument('--email', type=str, required=True, help='Email')
        parser.add_argument('--password', type=str, required=True, help='Password')
        parser.add_argument('--age', type=int, required=True, help='Age')

    def handle(self, *args, **options):
        User = get_user_model()
        username = options['username']
        email = options['email']
        password = options['password']
        age = options['age']

        if age < 15:
            self.stdout.write(self.style.ERROR("User must be at least 15 years old"))
            return

        User.objects.create_user(username=username, email=email, password=password, age=age)
        self.stdout.write(self.style.SUCCESS(f"User '{username}' created successfully"))
