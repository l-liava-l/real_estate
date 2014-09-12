from django.core.management.base import BaseCommand
from adverts.parcer import CianParcer


class Command(BaseCommand):

    def handle(self, adv_type='suburban', cian_id=2386544, *args, **options):
        print(adv_type)
        print(cian_id)
        p = CianParcer()
        if adv_type == 'flat':
            p.parce_rent_flat(cian_id=cian_id)
        elif adv_type == 'suburban':
            p.parce_rent_suburban(cian_id=cian_id)


