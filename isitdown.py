import requests

def getstatuscode(url):
    header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1'}
    s = requests.Session()
    s.headers.update(header)
    resp=s.head(url)
    return resp.status_code

for url in open('sitelist.txt').read().split(','):
    print url,'--->',getstatuscode(url)
    

