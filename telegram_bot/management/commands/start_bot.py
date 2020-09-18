from django.core.management.base import BaseCommand
from telegram_bot.start_bot import start


class Command(BaseCommand):
    help = '--start -st'

    def handle(self, *args, **options):
        if options['start_bot']:
            start()
        else:
            print('argument is not found')

    def add_arguments(self, parser):
        parser.add_argument(
            '-st',
            '--start_bot',
            action='store_true',
            default=False,
            help='Вывод короткого сообщения'
        )
