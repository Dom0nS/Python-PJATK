import requests
from urllib.parse import urlparse

def get_webpage(pageurl, date):
    url = "http://archive.org/wayback/available?url=" + pageurl + "&timestamp=" + str(date)
    response = requests.get(url)
    d = response.json()
    page = d["archived_snapshots"]["closest"]["url"]
    return page

if __name__ == '__main__':
    print("hello world")
    pageurl = input("Podaj stronę internetową: ")
    date = int(input("Poda date: "))
    # pageurl = 'https://google.com/'
    # date = 20230126

    for i in range(0,3):
        print(get_webpage(pageurl, date - i))
        r = requests.get(get_webpage(pageurl, date-i))
        open(urlparse(pageurl).netloc+'-version-'+str(i+1)+'.html', 'wb').write(r.content)


