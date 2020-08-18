import scrapy
from urllib import response
from urllib.parse import urlparse
from urllib.parse import urljoin
from urllib.request import Request
from pyparsing import unicode
from datetime import datetime
from dateutil.parser import parse
from ..items import BlazesItem
from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader
import socket

class AnameSpider(scrapy.Spider):
    name = 'aname'
    start_urls = ["https://inciweb.nwcg.gov/accessible-view/"]

    def parse(self, response):
        # item = BlazesItem()
        # l = ItemLoader(item=BlazesItem(), response=response)
        # l.add_css('incident', '.footable-first-visible a::text')
        # yield l.load_item()
        # Get the next index and yield Requests
        # This code gets the links of every fire in the page we are scraping
        # Get item URLs and yield Requests
        item_selector = response.xpath('//a[contains(@class, "")]//@href')
        for url in item_selector.extract():
            yield scrapy.Request(urljoin(response.url, url), callback=self.parse_item)

    def parse_item(self, response):
        item = BlazesItem()
        l = ItemLoader(item=BlazesItem(), response=response)
        l.add_css('incident', 'h1::text')
        l.add_css('incidentype', '.col-xs-12:nth-child(1) tr:nth-child(2) td+ td::text')
        l.add_css('cause', '.col-xs-12:nth-child(1) tr:nth-child(3) td+ td::text')
        l.add_css('day', '.col-xs-12:nth-child(1) tr:nth-child(4) td+ td::text')
        l.add_css('location', '.col-xs-12:nth-child(1) tr:nth-child(5) td+ td::text')
        l.add_css('coordinates', '.col-xs-12:nth-child(1) tr:nth-child(7) td+ td::text')
        l.add_css('personnel', '.col-xs-12:nth-child(2) tr:nth-child(1) td+ td::text')
        l.add_css('size', '.col-xs-12:nth-child(2) tr:nth-child(2) td+ td::text')
        l.add_css('perimeter', '.col-xs-12:nth-child(2) tr:nth-child(3) td+ td::text')
        l.add_css('fuelsinvolved', 'tr:nth-child(4) p::text')

        yield l.load_item()

    # def parse_title(self, response):
    #     item = BlazesItem()
    #     l = ItemLoader(item=BlazesItem(), response=response)
    #     l.add_css('incident', '.footable-first-visible a::text')
    #
    #     yield l.load_item()