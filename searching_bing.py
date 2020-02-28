import urllib.request
import urllib.parse as urlparse
from bs4 import BeautifulSoup
import re

def parsed_url():
    word_searched = input('Enter a word to search: ')
    if re.search(r"\s", word_searched):
        #word = re.split('\s+', word_searched)
        single_word = word_searched.replace(' ', '+')
        url_complet = 'https://www.bing.com/search?q=' + single_word
    else:
        url_complet = 'https://www.bing.com/search?q=' + word_searched

    #print(url_complet)
    parsed_url = urlparse.urlparse(url_complet)
    par = urlparse.parse_qs(parsed_url.query)['q']

    html = urllib.request.urlopen(url_complet)
    html_str = html.read().decode("utf-8")
    soup = BeautifulSoup(html_str, 'html.parser')

    # work with files
    '''f=codecs.open("file.html", 'r')
    #print (f.read())
    html_str = f.read()

    soup = BeautifulSoup(html_str, 'html.parser')
    #print(soup.prettify())

    fout = codecs.open("output.html", 'w')
    fout.write(soup.prettify())'''

    # parsing html requested
    ##matches = re.findall('<.*?>', html_str)
    #for link in soup.find_all('a'):
    #    print(link.get('href'))

    try:
        urls = []
        for h in soup.find_all('h2'):
            a = h.find('a')
            url = a.attrs['href']
            urls.append(url)
            if len(urls) == 5:
                for i in urls:
                    print(i)
    except:
        pass

    return True

def main():
    parsed_url()

if __name__ == '__main__':
	main()
