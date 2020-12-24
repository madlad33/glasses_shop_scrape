import scrapy


class GlassesSpider(scrapy.Spider):
    name = 'glasses'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['http://www.glassesshop.com/bestsellers/']

    def parse(self, response):

        for product in response.xpath("//div[@class='col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item']"):

            yield {
                'product_url':product.xpath(".//div[@class='product-img-outer']/a/@href").get(),
                'image_url':product.xpath(".//img[@class='lazy d-block w-100 product-img-default']/@data-src").get(),
                'product_price':product.xpath(".//div[@class='p-price']/div/span/text()").get(),
                'color':product.xpath(("normalize-space(.//div[@class='p-title']/a/@title)")).get(),

            }
        next_page=response.xpath("//a[@class='page-link' and text()='Next']/@href").get()
        if next_page:
                yield scrapy.Request(url=next_page,callback=self.parse)