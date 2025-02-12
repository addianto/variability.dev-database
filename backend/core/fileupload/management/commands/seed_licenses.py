from django.core.management.base import BaseCommand
from core.fileupload.models import License

class Command(BaseCommand):
    help = "Seed the database with initial License data"

    def handle(self, *args, **kwargs):
        licenses = [
            "CC BY - Mention",
            "CC BY-SA - ShareAlike",
            "CC BY-NC - NonCommercial",
            "CC BY-ND - NoDerivatives",
            "CC0 - Public Domain"
        ]

        for license_label in licenses:
            obj, created = License.objects.get_or_create(label=license_label)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created License: {license_label}"))
            else:
                self.stdout.write(self.style.WARNING(f"License already exists: {license_label}"))