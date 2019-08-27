# Imports from Django.
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Bootstrap development."

    def handle(self, *args, **options):
        call_command("bootstrap_geography")
        call_command("bootstrap_jurisdictions")
        call_command("bootstrap_fed")
        call_command("bootstrap_offices")
        call_command("bootstrap_parties")
        call_command("bootstrap_election_events")
        call_command("schedule_elections")
