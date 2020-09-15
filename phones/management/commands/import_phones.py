import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):

        pass

    def handle(self, *args, **options):

        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

            for items in phones:
                name = items['name']
                image = items['image']
                price = float(items['price'])
                release_date = (items['release_date'])
                lte_exists = bool(items['lte_exists'])
                Phone.objects.create(name=name, image=image, price=price, release_date=release_date, lte_exists=lte_exists)



    def get_phones(self):
        return Phone.objects.filter()
