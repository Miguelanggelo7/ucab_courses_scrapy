import scrapy
from courses.items import CoursesItem

class EmoviesSpider(scrapy.Spider):
    name = 'emovies'
    start_urls = ['https://emovies.oui-iohe.org/nuestros-cursos/']

    def parse(self, response):
        # Obtener los elementos div.course__inner de la página actual
        div_elements = response.xpath('//div[contains(@class, "course__inner")]')

        for div_element in div_elements:
            try:
                # Obtener el título
                title = div_element.xpath('.//h3/text()').get()

                # Obtener los elementos div.details__item dentro del div.course__inner
                details_elements = div_element.xpath('.//div[contains(@class, "details__item")]')

                # Inicializar variables para los campos de información
                university = ""
                career = ""
                typeOf = ""
                startDate = ""
                endDate = ""
                url = ""

                # Iterar sobre los elementos div.details__item
                for details_element in details_elements:
                    # Obtener el texto dentro de la etiqueta strong
                    strong_text = details_element.xpath('.//sup[@class="light"]/text()').get()
                    text = details_element.xpath('normalize-space(string(.//strong))').get()

                    # Identificar el campo y asignar el valor correspondiente
                    if "IES / HEI" in strong_text:
                        university = text
                    elif "Programa académico / Academic Program" in strong_text:
                        career = text
                    elif "Nivel des programa / Program Level" in strong_text:
                        typeOf = text
                    elif "Fecha de inicio curso / Course start date" in strong_text:
                        startDate = text.strip()
                    elif "Fecha de terminación / Course finish date" in strong_text:
                        endDate = text.strip()

                # Obtener el href de la etiqueta a.button--white
                url = div_element.css('a.button--white::attr(href)').get()

                # Crear el objeto con la información
                item = CoursesItem()
                item['title'] = title
                item['type'] = typeOf
                item['career'] = career
                item['university'] = university
                item['startDate'] = startDate
                item['endDate'] = endDate
                item['url'] = url
    
                yield item
            except:
                pass

        # Obtener el enlace de la siguiente página
        next_page = response.css('a.next::attr(href)').get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)
