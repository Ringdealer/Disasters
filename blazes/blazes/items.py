# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class BlazesItem(scrapy.Item):
    # Primary fields
    #state = Field()
    incident = Field()
    incidentype = Field()
    cause = Field()
    day = Field()
    location = Field()
    coordinates = Field()
    personnel = Field()
    size = Field()
    perimeter = Field()
    fuelsinvolved = Field()

    # Housekeeping fields
    # url = Field()
    # project = Field()
    # spider = Field()
    # server = Field()
    # date = Field()





    pass
