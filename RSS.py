import feedparser
 
def test(url):
    print('url:%s' % one_url)
    page_dict = feedparser.parse(url)
    print(page_dict.feed.title,' ',page_dict.feed.subtitle)
    print(len(page_dict.entries))
    for e in page_dict.entries:
        print(e.title)
if __name__ == '__main__':
    url_list=[
              'http://www.leiphone.com/feed/',
              'http://www.geekpark.net/rss',
              'http://cn.engadget.com/rss.xml',
              'http://www.36kr.com/feed'
              ]
    for one_url in url_list:
        try:
            test(one_url)
        except:
            print ('EXCEPTIONAL')
