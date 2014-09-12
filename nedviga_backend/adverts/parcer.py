import string

from grab import Grab
from grab.error import GrabNetworkError, GrabTimeoutError, GrabConnectionError, GrabAuthError

from .models import Advert


class CianParcer(object):

    def check_extra_options(self, class_name):
        el = self.g.doc.select('//*[@class="{}"]'.format(class_name))
        if len(el) > 0:
            return Advert.EXTRA_YES
        else:
            return Advert.EXTRA_NO

    def normalize_integer(self, x):
        if not isinstance(x, int):
            return x
        if x > 2147483647:
            return 2147483647
        else:
            return x

    def extract_digits(self, str):
        return ''.join([x for x in str if x in string.digits])

    def parce_rent_suburban(self, cian_id, is_rent=True, section=Advert.SECTION_HOUSE):
        self.g = Grab()
        try:
            url = 'http://www.cian.ru/rent/suburban/{}/'.format(cian_id)
            print(url)
            self.g.go(url)
        except (GrabNetworkError, GrabTimeoutError, GrabConnectionError, GrabAuthError) as details:
            print(details)
            return False

        raw_advert = {}

        #дом, часть дома, таунхауз, участок
        el = self.g.doc.select('//*[@class="object_descr_title"]')[0]
        raw_text = el.node.text.strip()
        if 'дом' in raw_text:
            set_room = 'Дом'
        elif 'часть' in raw_text:
            set_room = 'Часть дома'
        elif 'таунхаус' in raw_text:
            set_room = 'Таунхаус'
        elif 'участок' in raw_text:
            set_room = 'Участок'
        else:
            set_room = False


        el = self.g.doc.select('//*[@class="object_descr_addr"]')[0]
        raw_advert['street'] = el.node.text.strip()

        el = self.g.doc.select('//*[@class="object_descr_price"]')[0]
        raw_price = el.node.text.strip()
        price = [x for x in raw_price if x in string.digits]
        raw_advert['price'] = int(''.join(price))
        if 'в сутки' in raw_price:
            raw_advert['price_period'] = Advert.PERIOD_DAY
        elif 'в месяц' in raw_price:
            raw_advert['price_period'] = Advert.PERIOD_MONTH
        else:
            print('Не смог вычислить период оплаты')

        el = self.g.doc.select('//*[@class="object_descr_text"]')[0]
        description = el.node.text.strip()
        if not description:
            #если так не нашли описания - поищем в потомках
            cc = el.node.iterchildren()
            description = ''
            for c in cc:
                raw_text = c.text or ' '
                raw_tail = c.tail or ' '
                if 'Телефоны' in raw_text:
                    continue
                description += raw_text.strip()
                description += raw_tail.strip()
        raw_advert['description'] = description

        try:
            advert = Advert.objects.get(cian_id=cian_id)
            for key, value in raw_advert.items():
                setattr(advert, key, value)
        except Advert.DoesNotExist:
            advert = Advert(**raw_advert)
        advert.is_rent = is_rent
        advert.section = section
        advert.cian_id = cian_id
        advert.rooms_count = 0
        advert.house_type = 0
        if set_room:
            setattr(advert.house_type, set_room, set_room)
        advert.save()

    def parce_rent_flat(self, cian_id, is_rent=True, section=Advert.SECTION_APARTMENT):
        self.g = Grab()
        try:
            url = 'http://www.cian.ru/rent/flat/{}/'.format(cian_id)
            # url = 'http://www.cian.ru/rent/suburban/{}/'.format(cian_id)
            print(url)
            self.g.go(url)
        except (GrabNetworkError, GrabTimeoutError, GrabConnectionError, GrabAuthError) as details:
            print(details)
            return False

        raw_advert = {}

        #комната или количество комнат
        el = self.g.doc.select('//*[@class="object_descr_title"]')[0]
        raw_text = el.node.text.strip()
        if 'комната' in raw_text:
            set_room = 'room'
        elif 'комн.' in raw_text:
            for x in range(1, 7):
                print(x)
                if str(x) in raw_text:
                    set_room = str(x)
        else:
            set_room = False


        el = self.g.doc.select('//*[@class="object_descr_addr"]')[0]
        raw_advert['street'] = el.node.text.strip()

        el = self.g.doc.select('//*[@class="object_descr_props"]')[0]
        for tr in el.node.findall('tr'):
            th = tr.findall('th')
            td = tr.findall('td')
            th_text = th[0].text
            try:
                td_text = td[0].text
            except IndexError:
                td_text = ''
            if th_text == 'Этаж:':
                raw_storey, raw_number_of_storeys = td_text.split('/')
                raw_advert['storey'] = int(raw_storey.strip())
                raw_advert['number_of_storeys'] = int(raw_number_of_storeys.strip())
            elif th_text == 'Общая площадь:':
                raw_area_all = td[0].findall('i')[0].tail.strip()
                raw_area_all_clean = self.extract_digits(raw_area_all)
                if not raw_area_all_clean:
                    raw_advert['area_all'] = None
                else:
                    raw_advert['area_all'] = int(raw_area_all_clean)
            elif th_text == 'Площадь комнат:':
                raw_area = td[0].findall('i')[0].tail.strip()
                raw_area = raw_area.split('-')[-1]
                raw_area_clean = self.extract_digits(raw_area)
                if not raw_area_clean:
                    raw_advert['area_rooms'] = None
                else:
                    raw_advert['area_rooms'] = int(raw_area_clean)

            elif th_text == 'Жилая площадь:':
                raw_area_living = td[0].findall('i')[0].tail.strip()
                raw_area_living_clean = self.extract_digits(raw_area_living)
                if not raw_area_living_clean:
                    raw_advert['area_living'] = None
                else:
                    raw_advert['area_living'] = int(raw_area_living_clean)
            elif th_text == 'Площадь кухни:':
                raw_area = td[0].findall('i')[0].tail.strip()
                raw_area_clean = self.extract_digits(raw_area)
                if not raw_area_clean:
                    raw_advert['area_kitchen'] = None
                else:
                    raw_advert['area_kitchen'] = int(raw_area_clean)

            raw_advert['area_all'] = self.normalize_integer(raw_advert.get('area_all', 0))
            raw_advert['area_rooms'] = self.normalize_integer(raw_advert.get('area_rooms', 0))
            raw_advert['area_living'] = self.normalize_integer(raw_advert.get('area_living', 0))
            raw_advert['area_kitchen'] = self.normalize_integer(raw_advert.get('area_kitchen', 0))


        el = self.g.doc.select('//*[@class="metro_icon"]')[0]
        raw_metro = el.node.tail.strip()
        raw_advert['metro'] = ''.join(x for x in raw_metro if x not in string.punctuation)

        el = self.g.doc.select('//*[@class="object_descr_price"]')[0]
        raw_price = el.node.text.strip()
        price = [x for x in raw_price if x in string.digits]
        raw_advert['price'] = int(''.join(price))
        if 'в сутки' in raw_price:
            raw_advert['price_period'] = Advert.PERIOD_DAY
        elif 'в месяц' in raw_price:
            raw_advert['price_period'] = Advert.PERIOD_MONTH
        else:
            print('Не смог вычислить период оплаты')

        el = self.g.doc.select('//*[@class="object_descr_text"]')[0]
        raw_advert['description'] = el.node.text.strip()

        raw_advert['furniture'] = self.check_extra_options('objects_item_details_i_living_furnished')
        raw_advert['tv'] = self.check_extra_options('objects_item_details_i_tv')
        raw_advert['balcony'] = self.check_extra_options('objects_item_details_i_balcony')
        raw_advert['kitchen_furniture'] = self.check_extra_options('objects_item_details_i_kitchen_furnished')
        raw_advert['fridge'] = self.check_extra_options('objects_item_details_i_fridge')
        raw_advert['animals'] = self.check_extra_options('objects_item_details_i_animals')
        raw_advert['phone'] = self.check_extra_options('objects_item_details_i_phone')
        raw_advert['washing_machine'] = self.check_extra_options('objects_item_details_i_washing_machine')
        raw_advert['children'] = self.check_extra_options('objects_item_details_i_children')

        try:
            advert = Advert.objects.get(cian_id=cian_id)
            for key, value in raw_advert.items():
                setattr(advert, key, value)
        except Advert.DoesNotExist:
            advert = Advert(**raw_advert)
        advert.is_rent = is_rent
        advert.section = section
        advert.cian_id = cian_id
        advert.rooms_count = 0
        if set_room:
            setattr(advert.rooms_count, set_room, set_room)
        advert.save()


class ParseSearchList(object):
    totime = 300

    def __init__(self, totime=totime):
        self.totime = totime

    def get_flat_rent_list(self):
        url = 'http://www.cian.ru/cat.php?deal_type=1&obl_id=1&city[0]=1'
        self.g = Grab()
        try:
            print(url)
            self.g.go(url)
        except (GrabNetworkError, GrabTimeoutError, GrabConnectionError, GrabAuthError) as details:
            print(details)
            return False

        a_tag_list = self.g.doc.select('//a[@target="_blank"]')
        count = 0
        ids = []
        for a_tag in a_tag_list:
            #нужны не все ссылки, а только те, в которых есть 1 тег font
            font_tag_list = a_tag.node.findall('font')
            if len(font_tag_list) == 1:
                count += 1
                href = a_tag.node.attrib.get('href')
                ids.append(int(href.split('/')[-1]))
        print(count)
        print(ids)
        return ids

