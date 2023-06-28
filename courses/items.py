# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class CoursesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    type = Field()
    career = Field()
    university = Field()
    startDate = Field()
    endDate = Field()
    url = Field()
