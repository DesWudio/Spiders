import requests
from bs4 import BeautifulSoup

# html = soup

#Get HTML Object of Page
def getHTMLobj(url):
    UA = {'user-agent':'Mozilla/5.0'}
    try:
        html = requests.get(url, timeout = 30, headers = UA)
        print(html.status_code)
        html.raise_for_status()
        htmlcont = html.text
        html = BeautifulSoup(htmlcont, "html.parser")
        return html
    except:
        return "Network Error"

def getsrc(sp):
    true = sp.find_all('img', 'multi-photo-image')
    return true
    

def saveimage(t):
    global i
    global u
    path = "C:/abc/{}.jpg".format(i)
    try:
        for tag in t:
            print(tag['src'])
            imgurl = tag['src']
            r = requests.request('get',imgurl)
            i = i + 1
            path = "C:/abc/0{}.jpg".format(i)
            with open(path,'wb') as f:
                f.write(r.content)
        f.close()
        u = ""
        u = input('请输入文章链接 / Please input the url of article: ')
    except:
        print('网络错误请重试 / Network Unavailable, please try again：')
        u = input('请输入文章链接 / Please input the url of article: ')


#Main from there

i = 0
u = input('请输入文章链接 / Please input the url of article: ')
while u != "" :
    soup = getHTMLobj(u)
    true = getsrc(soup)
    saveimage(true)
else:
    print("程序结束 / Program shut down")