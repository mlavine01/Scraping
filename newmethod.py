from requests_html import HTMLSession

urls = ['https://www.amazon.com/TCL-40-inch-Class-Smart-Android/dp/B08P4XJKLQ/ref=sr_1_5?crid=38PRINBBZYGPL&keywords=tv&qid=1654551875&sprefix=tv%2Caps%2C96&sr=8-5',
 'https://www.amazon.com/SAMSUNG-85-Inch-Class-QLED-Built/dp/B08WFS951Y/ref=sr_1_10?crid=38PRINBBZYGPL&keywords=tv&qid=1654551875&sprefix=tv%2Caps%2C96&sr=8-10',
 'https://www.amazon.com/Pioneer-43-inch-4k-UHD-Smart-Fire-TV/dp/B09F3TW5CP/ref=sr_1_13?crid=38PRINBBZYGPL&keywords=tv&qid=1654551875&sprefix=tv%2Caps%2C96&sr=8-13',
 ]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
    'Referer': 'http://google.com',
    'DNT': '1',
}


def getPrice(url):
    s = HTMLSession()
    r = s.get(url, headers=headers)
    r.html.render(sleep=1)

    product = {
        'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
        'price': r.html.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[1]', first=True).text
    }                          
    print(product)
    return product
tvprices = []
for url in urls:
    tvprices.append(getPrice(url))
print(len(tvprices))