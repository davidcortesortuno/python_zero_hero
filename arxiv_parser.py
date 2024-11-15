import urllib, urllib.request
import bs4


url = "http://export.arxiv.org/api/query?search_query=all:black+hole&start=0&max_results=10&sortBy=lastUpdatedDate"
data = urllib.request.urlopen(url).read()  # Get a Bytes object with xml content

# with open('arxivResult.xml', r) as F:
#     fileText = F.read()

bsData = bs4.BeautifulSoup(data, "xml")

arxivEntries = bsData.find_all("entry")

firstResult = arxivEntries[0]

# print(firstResult)
# author_list = []
# for author in firstResult.find_all("author"):
#     author_str = author.text.lstrip("\n").rstrip("\n")
#     author_list.append(author_str)


author_list = [a.text for a in firstResult.find_all("name")]
title = firstResult.find("title").text
title_tag = "TITLE"
author_tag = "AUTHOR"

print(f"{title_tag:<15}: {title}")
full_author_list = " | ".join(author_list)
print(f"{author_tag:<15}: {full_author_list}")

# author_list = []
# for author in firstResult.find_all("name"):
#     author_str = author.text
#     author_list.append(author_str)

# print(author_list)
