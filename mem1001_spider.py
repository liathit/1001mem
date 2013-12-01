#coding: utf-8

from grab.spider import Spider, Task
import logging

class MemSpider(Spider):

    initial_urls = ['http://1001mem.ru/best/1']

    def task_initial(self, grab, task):
    	sel = grab.doc.select('//*[@id="main"]')
    	site_url = 'http://1001mem.ru'

    	for site in sel:
    		page_next = site.select('div[@id="pagination"]/a/@href')[1].text()
    		append_url = site_url + page_next
    		image_url = site.select('//*[@id="main"]').select('div[2]/ul/li/div/a/img/@src').text_list()

    	yield Task('initial', url=append_url)

    	for image in image_url:
    		yield Task('img', url=image)
    def task_img(self, grab, task):
    	file = task.url.split('/')[-1]
    	grab.response.save('images/%s' % file)

	

if __name__ == '__main__':
		logging.basicConfig(level=logging.DEBUG)
		bot = MemSpider(thread_number=1)
		bot.run()	


