# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 22:35:42 2019

@author: tryit163281
"""
from ..items import RentHouseItem

import scrapy

class RentSpider(scrapy.Spider):
    name = "rent_house"
    pages = 2
    start_urls = ["https://www.rakuya.com.tw/search/rent_search/index?display=list&con=&tab=def&sort=11&ds=&page=1"]
    
    def parse(self, response):
        print(response)
        RHI = RentHouseItem()
        title_list = response.xpath("/html/body/div[8]/div/div[1]/div[3]/div/div/div/div/h6/a/text()").extract()
        money_list = response.xpath("/html/body/div[8]/div/div[1]/div[3]/div/div/div/ul[1]/li[1]/span/text()").extract()
        for i,j in zip(title_list, money_list):
            RHI["title"] = i
            RHI["money"] = j
            yield RHI
    
        next_page = "https://www.rakuya.com.tw/search/rent_search/index?display=list&con=&tab=def&sort=11&ds=&page="+str(RentSpider.pages)
        if RentSpider.pages <= 3:
            RentSpider.pages = RentSpider.pages + 1
            yield response.follow(next_page, callback = self.parse)