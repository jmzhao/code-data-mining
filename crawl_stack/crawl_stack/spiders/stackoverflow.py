# -*- coding: utf-8 -*-
import scrapy


class StackoverflowSpider(scrapy.Spider):
    name = "stackoverflow"
    allowed_domains = ["stackoverflow.com"]
    start_urls = ()
    key_word = 'python'
    for i in range(1,51):
        start_urls += ('http://stackoverflow.com/questions/tagged/' + key_word + '?page=' + str(i) + '&sort=votes',)
        #print (start_urls)

    custom_settings = {
        'DOWNLOAD_DELAY': 1.2,
    }

    def parse(self, response):
        question_urls = response.xpath('//a[@class="question-hyperlink"]/@href').extract()
        for question_url in question_urls :
          #  print ("-------------------",question_url)
            yield scrapy.Request(url='http://stackoverflow.com' + question_url, callback=self.parse_question)

    def parse_question(self, response) :
        title_node = response.xpath('//a[@class="question-hyperlink"]')[0]
       # print ("+++++++++++++++",title_node )
        yield {
                'id' : title_node.xpath('@href').extract_first().split('/')[2],
                'title' : title_node.xpath('text()').extract_first(),
                'post-text' : response.xpath('//div[@class="question"]').xpath('.//div[@class="post-text"]').extract_first(),
                'answer-text': response.xpath('//div[@class="answer"]').xpath('.//div[@class="post-text"]').extract_first(),
           # 'post-vote' : response.xpath('//div[@class="vote"]').xpath('.//span[@class="vote-count-post high-scored-post"]/text()').extract_first()
                'post-vote' : response.xpath('//span[@itemprop="upvoteCount"]').xpath('text()').extract_first(),
                'answer-vote' : response.xpath('//span[@itemprop="upvoteCount"]').xpath('text()').extract()[1]
        }
