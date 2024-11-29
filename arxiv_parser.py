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

# author_list = [a.text for a in firstResult.find_all("name")]
# title = firstResult.find("title").text
# abstract = firstResult.find("summary").text
#
# data_dict = {}
# data_dict["author_list"] = author_list
# data_dict["title"] = title
# data_dict["abstract"] = abstract

# title_tag = "TITLE"
# author_tag = "AUTHOR"

# print("TITLE: {0}".format(data_dict["title"]))


def format_bs_entry(bsentry: bs4.element.Tag) -> dict:
    """Format an entry of a BS result

    This function process a BS entry and outputs a dictionary with
    title, author list and abstract.

    Arguments
    ---------
    bsentry
        A BS entry result to be processed
    """

    author_list = [name.text for name in bsentry.find_all("name")]
    title = bsentry.find("title").text
    abstract = bsentry.find("summary").text

    data_dict = {}
    data_dict["author_list"] = author_list
    data_dict["title"] = title
    data_dict["abstract"] = abstract

    return data_dict


res_dict = format_bs_entry(firstResult)
print(res_dict)
