from random import choices

from django.core.management.base import BaseCommand
from myapp3.models import Author, Post

LOREM = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' \
        'Aenean pharetra vestibulum diam, non lacinia tellus eleifend at. ' \
        'Nam dapibus est quis mi egestas dapibus. Interdum et malesuada fames ac ante ipsum primis in faucibus.' \
        'Suspendisse gravida velit augue, eget rhoncus nulla pretium id. Donec sed dui nisl. ' \
        'Aenean sollicitudin eu nulla sed fringilla. Aliquam et maximus enim. In leo sapien.'


class Command(BaseCommand):
    help = 'Generate fake authors and posts.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of user')

    def handle(self, *args, **options):
        text = LOREM.split()
        count = options.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}', email=f'mail{i}@mail.ru')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title-{j}',
                    content=' '.join(choices(text, k=64)),
                    author=author
                )
                post.save()
