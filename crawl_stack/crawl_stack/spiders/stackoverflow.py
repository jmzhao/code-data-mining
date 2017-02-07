# -*- coding: utf-8 -*-
import scrapy


class StackoverflowSpider(scrapy.Spider):
    name = "stackoverflow"
    allowed_domains = ["stackoverflow.com"]
    start_urls = (
        'http://stackoverflow.com/questions/tagged/python?sort=votes&pageSize=15',
    )
    custom_settings = {
        'DOWNLOAD_DELAY': 0.2,
    }

    def parse(self, response):
        question_urls = response.xpath('//a[@class="question-hyperlink"]/@href').extract()
        for question_url in question_urls :
            yield scrapy.Request(url='http://stackoverflow.com' + question_url, callback=self.parse_question)

    def parse_question(self, response) :
        title_node = response.xpath('//a[@class="question-hyperlink"]')[0]
        yield {
            'id' : title_node.xpath('@href').extract_first().split('/')[2],
            'title' : title_node.xpath('text()').extract_first(),
            'post-text' : response.xpath('//div[@class="post-text"]').extract()[0],
        }
