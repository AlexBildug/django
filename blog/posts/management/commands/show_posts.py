from django.core.management.base import BaseCommand

from posts.models import Post

from django.conf import settings


class Command(BaseCommand):
    help = "Show all posts from DB"

    def handle(self, *args, **options):
        import csv

        with open(settings.BASE_DIR / "posts.csv", "w") as file:
            writer = csv.writer(file)
            for post in Post.objects.all():
                writer.writerow([post.id, post.title])
