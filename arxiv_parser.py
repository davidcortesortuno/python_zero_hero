import urllib, urllib.request
import bs4


url = 'http://export.arxiv.org/api/query?search_query=all:black+hole&start=0&max_results=10&sortBy=lastUpdatedDate'
data = urllib.request.urlopen(url).read()  # Get a Bytes object with xml content

bsData = bs4.BeautifulSoup(data, 'xml')

arxivEntries = bsData.find_all('entry')

firstResult = arxivEntries[0]

# print(firstResult)
author_list = []
for author in firstResult.find_all('author'):
    author_list.append(author.text)

print(author_list)
