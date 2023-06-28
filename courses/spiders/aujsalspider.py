import scrapy
from courses.items import CoursesItem


class AujsalSpider(scrapy.Spider):
    name = 'aujsal'
    start_urls = ['https://cursos.leon.uia.mx/intercambiovirtual/index.php']

    def parse(self, response):
        item = CoursesItem()
        for countries in response.css('#accordionExample > .accordion-item'):
            for universities in countries.css('.accordion-collapse > .accordion-body > .accordion > .card'):
                university = universities.css(
                    'h5 > button::text').get().strip()

                for courses in universities.css('table tbody tr'):
                    course = courses.css('td::text').getall()
                    item['title'] = course[1]
                    item['type'] = course[0]
                    item['career'] = course[2]
                    item['university'] = university
                    item['startDate'] = course[4]
                    item['endDate'] = course[5]
                    item['url'] = courses.css('td a::attr(href)').get()

                    yield item
