from django.core.management.base import BaseCommand
from core.fileupload.models import *
from django.db.utils import IntegrityError
from django.core import files
import os
import datetime

class TempFile():
    def __init__(self, name, file):
        self.name = name
        self.file = file


class Command(BaseCommand):
    help = "Seed the database with initial License data"

    def add_arguments(self, parser):
        parser.add_argument('folder', type=str, help='Path to the folder')
        parser.add_argument('owner_id', type=int, help='Owner User ID')
        parser.add_argument('family_id', type=int, help='Family ID')
        parser.add_argument('license_id', type=int, help='License ID')

    def handle(self, *args, **kwargs):
        licenses = [
            "CC BY - Mention",
            "CC BY-SA - ShareAlike",
            "CC BY-NC - NonCommercial",
            "CC BY-ND - NoDerivatives",
            "CC0 - Public Domain",
            "MIT License"
        ]

        families = [
            'Automotive',
            'Games',
            'BusyBox',
            'Pc-Richmond',
            'Amanah'
        ]

        families_id = [
            0,
            0,
            0,
            0,
            0,
        ]

        tags =[
            'feature model'
        ]

        try:
            instance, created = User.objects.get_or_create(
                email = "firstuser@user.com",
                is_active = True,
                is_staff = True,
                institute = "Universitas Indonesia",
                bio = "Hi there :D",
                defaults={
                    "id" : 1,
                },
            )
            if created:  # Only set password when creating
                instance.set_password(os.getenv('PASSWORD_FIRST_USER'))
                instance.save()
                self.stdout.write("Added first user to the database.")
            else:
                self.stdout.write("User already exists. No changes made.")
        except IntegrityError:
            print("User already exist")

        for license_label in licenses:
            obj, created = License.objects.get_or_create(label=license_label)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created License: {license_label}"))
            else:
                self.stdout.write(self.style.WARNING(f"License already exists: {license_label}"))
        
        for family in families:
            obj, created = Family.objects.get_or_create(
                owner = User.objects.get(id=1),
                label = family,
                description = " ",
                slug = True,
                )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created Family: {family}"))
            obj.save()

        tag, created = Tag.objects.get_or_create(
            owner = User.objects.get(id=1),
            label = tags[0],
            description = "This is a feature map",
            is_public = True,
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f"Created TAG: {tag}"))
        else:
            self.stdout.write(self.style.SUCCESS(f"TAG already exists: {tag}"))

        tag.save()

        folder_path = kwargs['folder']
        owner = User.objects.get(id=1)
        family = Family.objects.get(id=kwargs['family_id'])
        license = License.objects.get(id=kwargs['license_id'])
        tag = Tag.objects.get(id=1)

        if not os.path.exists(folder_path):
            self.stderr.write(f"Folder {folder_path} does not exist.")
            return

        for root, _, filess in os.walk(folder_path):
            for file_name in filess:
                label = os.path.splitext(file_name)[0]
                version = "1.0"  # Default version, modify as needed
                
                family = Family.objects.filter(label = families[0]).first()
                if "Kn" in file_name:
                    family = Family.objects.filter(label = families[0]).first()
                    version = families_id[0]+1
                    families_id[0]+=1
                elif "Schulze" in file_name:
                    family = Family.objects.filter(label = families[1]).first()
                    version = families_id[0]+1
                    families_id[0]+=1
                elif "Pett" in file_name:
                    family = Family.objects.filter(label = families[2]).first()
                    version = families_id[0]+1
                    families_id[0]+=1
                elif "Sprey" in file_name:
                    family = Family.objects.filter(label = families[3]).first()
                    version = families_id[0]+1
                    families_id[0]+=1
                elif "Amanah" in file_name:
                    family = Family.objects.filter(label = families[4]).first()
                    version = families_id[0]+1
                    families_id[0]+=1
                else:
                    continue

                with open(os.path.join(folder_path, file_name), 'rb') as f:
                    
                    instance, created = File.objects.get_or_create(
                        owner=User.objects.get(id=1),
                        family=family,
                        label=label,
                        version=version,  # Use only identifying fields here
                        defaults={
                            "description": f"Auto-imported file {file_name}",
                            "local_file": files.File(f),
                            "license": license
                        }
                    )

                    if created:
                        instance.save()
                        self.stdout.write(f"Added {file_name} to the database.")