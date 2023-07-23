"""
django command to wait for db to be available
"""
import time

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError

from psycopg2 import OperationalError as psycopg2error


class Command(BaseCommand):

    def handle(self, *args, **options):
        """entrypoint for command"""

        self.stdout.write('waiting for database')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (psycopg2error, OperationalError):
                self.stdout.write('database unavailable, waiting...')
                time.sleep(0.5)

        self.stdout.write(self.style.SUCCESS('database available'))
