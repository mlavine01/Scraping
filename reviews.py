from requests_html import HTMLSession
import json
import time

class Rewiews:
    def __init__(self, asin) -> None:
        self.asin = asin
        self.session = HTMLSession()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}
        self.url = f'https://www.amazon.com/product/reviews/{self.asin}/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewsType=all_reviews&sortBy=recent&pageNumber='

    def pagination(self, page):
        r = self.session.get(self.url+str(page))
        if not r.html.find('div[data-hook=review]'):
            return self.url
        else:
            return r.html.find('div[data-hook=review]')

    def parse(self, reviews):
        total = []
        for review in reviews:
            title = review.find('a[data-hook=review-title]', first=True).text
            rating = review.find('i[data-hook=review-star-rating] span', first=True).text
            body = review.find('span[data-hook=review-body] span', first=True).text.replace('\n','').strip()


            data = {
                'title': title,
                'rating': rating,
                'body': body[:100]
            }
            total.append(data)
        return total

    def save(self, results):
       with open(self.asin + '-reviews.json', 'w') as f:
           json.dump(results,f) 

if __name__ == '__main__':
    amz = Rewiews('B07T24T7PT')
    results =[]
    for x in range(1,10):
        print('getting page ', x)
        time.sleep(0.3)
        reviews = amz.pagination(x)
        if reviews is not False:
            results.append(amz.parse(reviews))
        else:
            print('no more pages')
            break
    print(results)

    
    amz.save(results)