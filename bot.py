from bs4 import BeautifulSoup
import requests
from random import randint
from time import sleep
import tweepy

header ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

API_KEY = ''
API_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET =''
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

def tweet_word_counter(sentence):
    c = 0
    for i in range(len(sentence)):
        c = c + 1
    return c
def urlShortener(link):
    try:
        url = 'https://rel.ink/api/links/'
        myobj = {'url':link}
        x = requests.post(url, data = myobj)
        return 'https://rel.ink/'+x.json()['hashid']
    except Exception as e:
        return 'https://rel.ink'
def tweet_this_news(mes):
    api.update_status(status=mes)
    print('done')
    sleep(600)

print("BOT STARTED")
while True:
	# fourfourtwo
	try:
	    news =[]
	    articles = []
	    link = []
	    pageNo = randint(9000,15180)
	    url = 'https://www.fourfourtwo.com/news/page/'+str(pageNo)
	    source = requests.get(url ,headers=header).text
	    soup = BeautifulSoup(source,'lxml')
	    find_container = soup.find('section',class_="listingResultsWrapper news")
	    find_news = find_container.find('div',class_="listingResults news")
	    for div in find_news.find_all('div',class_='listingResult'):
	        for news_text in div.find_all('a',href=True):
	            if news_text.text:
	                #if(news_text['aria-label'] != '*** Links For News Stories ***'):
	                try:
	                    article = news_text.find('p',class_='synopsis').text
	                except:
	                    article = ''
	                news.append(news_text['aria-label'])
	                link.append(news_text['href'])
	                articles.append(article.replace('\n',''))
	    index = randint(0,9)
	    #print(link[index])
	    tweet_url = urlShortener(link[index])
	    sent = '📰 |'+news[index]+'\n\n'+articles[index]+'\n\n'+str(tweet_url)
	    tweet_limit = tweet_word_counter(sent)
	    if(tweet_limit > 280):
	        sent ='📰 |'+news[index]+'\n\n'+str(tweet_url)
	        tweet_this_news(sent)
	    else:
	        tweet_this_news(sent)
	except Exception as e:
	    print(e)

	#mirror
	try:
	    newz = []
	    links = []
	    url_index = randint(3997,7400)
	    url = 'https://www.mirror.co.uk/sport/football/news/?pageNumber={}'.format(url_index)
	    source = requests.get(url ,headers=header).text
	    soup = BeautifulSoup(source,'lxml')
	    find_container = soup.find('main',class_='mod-pancakes')
	    for trez in find_container.find_all('div',class_='pancake use-image-placeholders duet primary channel-sport'):
	        find_tres = trez.find_all('div',class_='teaser')
	        for news in find_tres:
	            find_a = news.find('a',href=True)
	            newz.append(find_a['aria-label'])
	            links.append(find_a['href'])
	    length_of_newz = len(newz)-1
	    index = randint(0,length_of_newz)
	    tweet_url = urlShortener(links[index])
	    sent = "📰 |{} \n {}".format(newz[index],tweet_url)
	    tweet_this_news(sent)
	except:
	    print("Err")

	#talksport
	try:
	    newz = []
	    links = []
	    url_index = randint(2170,4184)
	    url = 'https://talksport.com/football/page/{}/'.format(url_index)
	    source = requests.get(url ,headers=header).text
	    soup = BeautifulSoup(source,'lxml')
	    find_container = soup.find('section',class_='football football--landing theme-football')
	    find_te = find_container.findAll('div',class_='sun-row teaser')
	    find_te=find_te[1]
	    for fst_te in find_te.find_all('div',class_='col sun-col-2'):
	        find_a = fst_te.find('a',href=True)
	        find_p = fst_te.find('p',class_='teaser__subdeck')
	        art = find_p.text.replace('			','')
	        art = art.replace('\n','')
	        newz.append(art)
	        links.append(find_a['href'])
	    length_of_newz = len(newz)-1
	    index = randint(0,length_of_newz)
	    tweet_url = urlShortener(links[index])
	    sent = "📰 |{} \n {}".format(newz[index],tweet_url)
	    tweet_this_news(sent)
	except:
	    print('err')

	#caughtoffside
	try:
	    newz = []
	    links=[]
	    url_index = randint(2400,4150)
	    url = 'https://www.caughtoffside.com/tags/transfer-rumours/page/{}/'.format(url_index)
	    source = requests.get(url ,headers=header).text
	    soup = BeautifulSoup(source,'lxml')
	    find_body = soup.find('body')
	    find_container = find_body.findAll('div',class_='container')
	    find_container =find_container[4]
	    find_row = find_container.findAll('div',class_='row')
	    find_row =find_row[0]
	    find_sec = find_row.find('section',{"id": "team-news"})
	    find_another_row = find_sec.find('div',class_='row')
	    for article in find_another_row.findAll('article',class_='col-l-12'):
	        if len(article) > 2:
	            find_a = article.find('a',href=True)
	            find_img =article.find('img')
	            newz.append(find_img['title'])
	            links.append(find_a['href'])
	    length_of_newz = len(newz)-1
	    index = randint(0,length_of_newz)
	    tweet_url = urlShortener(links[index])
	    sent = "📰 |{} \n {}".format(newz[index],tweet_url)
	    tweet_this_news(sent)
	except:
	    print("err")

	#tribalfootball transfer news
	try:
	    newz = []
	    links = []
	    url_index = randint(1999,3817)
	    url = 'https://www.tribalfootball.com/transfers?page={}'.format(url_index)
	    source = requests.get(url ,headers=header).text
	    soup = BeautifulSoup(source,'lxml')
	    find_container = soup.find('div',class_='switcher js-anchor list')
	    find_grid = find_container.find('div',class_='grid grid--narrow')
	    for news in find_grid.findAll('div',class_='grid__item palm-one-half desk-wide-one-third'):
	        find_a = news.find('a',href=True)
	        find_h3 = news.find('h3',class_='card__title')
	        #find_time =  news.find('time',class_='card__date fromnow')
	        #print(find_time.text[0:10])
	        newz.append(find_h3.text)
	        links.append('https://www.tribalfootball.com'+find_a['href'])
	    length_of_newz = len(newz)-1
	    index = randint(0,length_of_newz)
	    tweet_url = urlShortener(links[index])
	    sent = "📰 |{} \n {}".format(newz[index],tweet_url)
	    tweet_this_news(sent)
	except:
	    print('err')

	#tribalfootball news
	try:
	    newz = []
	    links =[]
	    url_index = randint(3000,3500)
	    url = 'https://www.tribalfootball.com/news?page={}'.format(url_index)
	    source = requests.get(url ,headers=header).text
	    soup = BeautifulSoup(source,'lxml')
	    find_container = soup.find('div',class_='switcher js-anchor list')
	    find_grid = find_container.find('div',class_='grid grid--narrow')
	    for news in find_grid.findAll('div',class_='grid__item palm-one-half desk-wide-one-third'):
	        find_a = news.find('a',href=True)
	        find_h3 = news.find('h3',class_='card__title')
	        newz.append(find_h3.text)
	        links.append('https://www.tribalfootball.com'+find_a['href'])
	    length_of_newz = len(newz)-1
	    index = randint(0,length_of_newz)
	    tweet_url = urlShortener(links[index])
	    sent = "📰 |{} \n {}".format(newz[index],tweet_url)
	    tweet_this_news(sent)
	except:
	    print('err')

	try:
	    newz =[]
	    articles = []
	    links = []
	    url_index = randint(2800,3800)
	    url = 'https://www.football-italia.net/news?page={}'.format(url_index)
	    source = requests.get(url ,headers=header).text
	    soup = BeautifulSoup(source,'lxml')
	    find_container = soup.find('div',class_='view-content')
	    for news in find_container.findAll('div',class_ ='views-row'):
	        # title
	        find_title = news.find('div',class_='news-idx-item')
	        find_a  = find_title.find('a',href=True)
	        newz.append(find_a.text)
	        links.append('https://www.football-italia.net'+find_a['href'])
	        #Article
	        find_article = news.find('div',class_='news-idx-item-body')
	        articles.append(find_article.text)
	    length_of_newz = len(newz)-1
	    index = randint(0,length_of_newz)
	    tweet_url = urlShortener(links[index])
	    sent =  "📰 |{} \n\n {} \n🔗 {}".format(newz[index],articles[index],tweet_url)
	    tweet_limit = tweet_word_counter(sent)
	    if(tweet_limit > 280):
	        sent = "📰 |{} \n\n🔗 {}".format(newz[index],tweet_url)
	        tweet_this_news(sent)
	    else:
	        tweet_this_news(sent)
	except:
	    print('err')

	#101greatgoals
	try:
	    newz = []
	    links = []
	    url_index = randint(1802,3502)
	    url ='https://www.101greatgoals.com/news/page/{}/'.format(url_index)
	    source = requests.get(url ,headers=header).text
	    soup = BeautifulSoup(source,'lxml')
	    find_container = soup.find('div',class_="row category-posts")
	    for news in find_container.find_all('div',class_='col-md-4 category-post'):
	        find_a = news.find('a',href=True)
	        find_p = news.find('p')
	        newz.append(find_p.text)
	        links.append(find_a['href'])
	    length_of_newz = len(newz)-1
	    index = randint(0,length_of_newz)
	    tweet_url = urlShortener(links[index])
	    sent = "📰 |{} \n {}".format(newz[index],tweet_url)
	    tweet_this_news(sent)
	except:
	    print('err')
	#soccernews
	try:
	    newz = []
	    links = []
	    url_index = randint(220,370)
	    url = 'https://www.soccernews.com/category/general-soccer-news/page/{}/'.format(url_index)
	    source = requests.get(url ,headers=header).text
	    soup = BeautifulSoup(source,'lxml')
	    find_container = soup.find('div',class_='main-container')
	    find_blackList = find_container.findAll('div',class_='top-videos-container transfers black')
	    find_blackList = find_blackList[1]
	    find_headline = find_blackList.find('div',class_='latest-news-list headline')
	    for news in find_headline.findAll('li'):
	        find_a = news.find('a',href=True)
	        newz.append(find_a.text)
	        links.append(find_a['href'])
	    length_of_newz = len(newz)-1
	    index = randint(0,length_of_newz)
	    tweet_url = urlShortener(links[index])
	    sent = "📰 | {} \n\n {}".format(newz[index],tweet_url)
	    tweet_this_news(sent)
	except:
	    print('error')
