# -*- coding: utf-8 -*-
import scrapy


class DataMiningSpider(scrapy.Spider):

    name = 'datamining'

    _base_dog_url = 'http://www.dogbreedslist.info/all-dog-breeds/'
    _base_cat_url = 'http://www.catbreedslist.com/all-cat-breeds/'

    start_urls = (
            'http://www.dogbreedslist.info/all-dog-breeds/',
            # 'http://www.catbreedslist.com/all-cat-breeds/'
    )


    """Response contém o html que foi recebido como resposta"""
    def parse(self, response):
        for each_list_animal in response.css('.list > .list-01 > .right'):

            animal_info = {}
            animal_info['Name'] = each_list_animal.css('.right-t > p > a::text').extract_first()
            animal_info['Breed_definition'] = each_list_animal.css('.right-t > span::text').extract_first()
            animal_info['Hypoallergenic'] = each_list_animal.css('.right > div.right-c > div.hyp > p::text').extract_first()

            animal_url = each_list_animal.css('.right-t > p > a::attr(href)').extract_first()
            yield scrapy.Request(animal_url, callback=self.parse_animal_info, meta={'animal_info': animal_info})

        # controla paginação
        pages_list = response.css(".pages > ul > li")
        for page in pages_list:
            if page.css('a'):
                if page.css('a::text').extract_first() == 'Next':
                    next_page = response.urljoin(page.css('a::attr(href)').extract_first())
                    yield scrapy.Request(next_page, callback=self.parse)

    def parse_animal_info(self, response):
        animal_info = response.meta.get('animal_info')
        self._build_info_by_xpath_1(response, animal_info)
        yield animal_info

    def _build_info_by_xpath_1(self, response, animal_info):
        # best way to remove first element from a list
        print(response)
        try:
            animal_info['Size'] = response.css('body > div.main > div.main-r > div.content > table.table-01 > tbody > tr:nth-child(8) > td:nth-child(2) > a::text').extract_first()
            animal_info['Litter Size'] = response.xpath('/html/body/div[2]/div[2]/div[4]/table[1]/tbody/tr[15]/td[2]/text()').extract_first()
            animal_info['Lifespan'] = response.xpath('/html/body/div[2]/div[2]/div[4]/table[1]/tbody/tr[10]/td[2]/text()').extract_first()
            animal_info['Puppy Price'] = response.xpath('/html/body/div[2]/div[2]/div[4]/table[1]/tbody/tr[16]/td[2]/text()').extract_first()
            animal_info['Adaptability'] = response.xpath('/html/body/div[2]/div[2]/div[4]/table[1]/tbody/tr[19]/td[2]/span/text()').extract_first()
            animal_info['Apartment Friendly'] = response.xpath('/html/body/div[2]/div[2]/div[4]/table[1]/tbody/tr[20]/td[2]/span/text()').extract_first()
            animal_info['Barking Tendencies'] = response.xpath('/html/body/div[2]/div[2]/div[4]/table[1]/tbody/tr[21]/td[2]/span[1]/text()').extract_first()
            animal_info['Cat Friendly'] = response.xpath('/html/body/div[2]/div[2]/div[4]/table[1]/tbody/tr[22]/td[2]/span/text()').extract_first()
            animal_info['Child Friendly'] = response.xpath('/html/body/div[2]/div[2]/div[4]/table[1]/tbody/tr[23]/td[2]/span[1]/text()').extract_first()
            animal_info['Dog Friendly'] = response.xpath('/html/body/div[2]/div[2]/div[4]/table[1]/tbody/tr[24]/td[2]/span/text()').extract_first()
            animal_info['Exercise Needs'] = response.xpath('/html/body/div[2]/div[2]/div[4]/table[1]/tbody/tr[25]/td[2]/span/text()').extract_first()
            animal_info['Grooming'] = response.xpath('/html/body/div[2]/div[2]/div[4]/table[1]/tbody/tr[26]/td[2]/span[1]/text()').extract_first()
            animal_info['Health Issues'] = response.xpath('/html/body/div[2]/div[2]/div[4]/table[1]/tbody/tr[27]/td[2]/span[1]/text()').extract_first()
            animal_info['Intelligence'] = response.xpath('/html/body/div[2]/div[2]/div[4]/table[1]/tbody/tr[28]/td[2]/span[1]/text()').extract_first()
            animal_info['Playfulness'] = response.xpath('/html/body/div[2]/div[2]/div[4]/table[1]/tbody/tr[29]/td[2]/span/text()').extract_first()
            animal_info['Shedding Level'] = response.xpath('/html/body/div[2]/div[2]/div[4]/table[1]/tbody/tr[30]/td[2]/span[1]/text()').extract_first()
            animal_info['Stranger Friendly'] = response.xpath('/html/body/div[2]/div[2]/div[4]/table[1]/tbody/tr[31]/td[2]/span/text()').extract_first()
            animal_info['Trainability'] = response.xpath('/html/body/div[2]/div[2]/div[4]/table[1]/tbody/tr[32]/td[2]/span[1]/text()').extract_first()
            animal_info['Watchdog Ability'] = response.xpath('/html/body/div[2]/div[2]/div[4]/table[1]/tbody/tr[33]/td[2]/span/text()').extract_first()
        except Exception as e:
            print(e)
            input()

