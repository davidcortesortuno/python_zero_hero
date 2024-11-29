import urllib, urllib.request
import bs4


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
    title = title.replace("\n", "")
    abstract = bsentry.find("summary").text
    datep = bsentry.find("published").text

    data_dict = {}
    data_dict["author_list"] = author_list
    data_dict["title"] = title
    data_dict["abstract"] = abstract
    data_dict["date"] = datep

    return data_dict


url = "http://export.arxiv.org/api/query?search_query=all:black+hole&start=0&max_results=10&sortBy=lastUpdatedDate"
data = urllib.request.urlopen(url).read()  # Get a Bytes object with xml content

# with open('arxivResult.xml', r) as F:
#     fileText = F.read()

bsData = bs4.BeautifulSoup(data, "xml")

arxivEntries = bsData.find_all("entry")

list_of_dictResults = []
for result in arxivEntries:
    dictRes = format_bs_entry(result)  # get dictionary with results
    list_of_dictResults.append(dictRes)

for d in list_of_dictResults:
    print(d["date"])
    print(d["title"])
    print("--")
