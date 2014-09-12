# coding: utf-8





def parse():
    g = Grab()
    try:
        g.go('http://www.cian.ru/cat.php?deal_type=1&obl_id=1&city[0]=1&totime=300', log_file='./log')
    except (GrabNetworkError, GrabTimeoutError, GrabConnectionError, GrabAuthError) as details:
        print(details)
        return False

    reals = dict()
    for tr in g.doc.select('//*[@id="tbody"]//fieldset//table[@class="cat"]/tr'):
        cian_id = tr.node.get('id')
        real = dict()
        if cian_id:
            real['cian_id'] = cian_id
            for td in tr.select('//td'):
                td_id = td.node.get('id')
                if td_id:
                    if 'metro' in td_id:
                        real['city'] = td.node.findall('a')[0].text
                        print(td.node.findall('a')[len(td.node.findall('a'))-1].text)
            if cian_id not in reals:
                reals[cian_id] = real




if __name__ == '__main__':
    p = CianParcer()
    p.parce_adv(adv_id=11359831)
    # parse()
