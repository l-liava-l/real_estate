from django.core.management.base import BaseCommand
from adverts.parcer import ParseSearchList, CianParcer


class Command(BaseCommand):

    def handle(self, *args, **options):
        p = ParseSearchList()
        ids = p.get_flat_rent_list()

        pp = CianParcer()
        for x in ids:
            print(x)
            pp.parce_rent_flat(x)


