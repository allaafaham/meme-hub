from django.core.management.base import BaseCommand
from core.models import Label

class Command(BaseCommand):
    help = 'Creates initial meme labels'

    def handle(self, *args, **kwargs):
        labels = [
            {'name': 'Funny', 'description': 'Humorous and entertaining memes'},
            {'name': 'Reaction', 'description': 'Memes expressing reactions to situations'},
            {'name': 'Gaming', 'description': 'Video game related memes'},
            {'name': 'Animals', 'description': 'Memes featuring animals'},
            {'name': 'Sports', 'description': 'Sports-related memes'},
            {'name': 'Movies', 'description': 'Movie and TV show memes'},
            {'name': 'Music', 'description': 'Music-related memes'},
            {'name': 'Tech', 'description': 'Technology and programming memes'},
            {'name': 'School', 'description': 'Education and student life memes'},
            {'name': 'Work', 'description': 'Work and office life memes'},
            {'name': 'Food', 'description': 'Food and cooking memes'},
            {'name': 'Politics', 'description': 'Political memes'},
            {'name': 'Wholesome', 'description': 'Positive and uplifting memes'},
            {'name': 'Trending', 'description': 'Currently popular memes'},
            {'name': 'Classic', 'description': 'Time-tested classic memes'},
            {'name': 'Dank', 'description': 'Particularly dank memes'},
            {'name': 'Anime', 'description': 'Anime and manga related memes'},
            {'name': 'Science', 'description': 'Science-related memes'},
            {'name': 'Art', 'description': 'Art and creativity memes'},
            {'name': 'Random', 'description': 'Miscellaneous memes that defy categorization'}
        ]

        for label_data in labels:
            Label.objects.get_or_create(
                name=label_data['name'],
                defaults={'description': label_data['description']}
            )
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created label "{label_data["name"]}"')
            ) 