import requests
from _thread import start_new_thread
import re
# from bs4 import BeautifulSoup
# import lxml

REGEX = r'<div class="c" id="M_([a-zA-Z0-9]{9})">'


def delete(ids, headers):
    for id in ids:
        payload = {'type': 'del', 'id': id, 'act': 'delc', 'rl': '1', 'st': '_st'}
        try:
            start_new_thread(delopr, (headers, payload))
        except:
            print('Error: unable to start thread')


def delopr(headers, payload):
    requests.get("https://weibo.cn/mblog/del", headers=headers, params=payload)


def getids(soup):
    idlist = []
    divs = soup.find_all('div', attrs={'class': "c"})
    print(divs)
    for div in divs:
        if div.get('id'):
            id = div['id'].replace('M_', '')
            idlist.append(id)

    return idlist


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/60.0.3112.113 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4,zh-CN;q=0.2',
        'cookie': '_cookie'
    }
    url = "https://weibo.cn/UID/profile"
    re_pattern = re.compile(REGEX)
    while True:
        request = requests.get(url, headers=headers)
        """
        with open('test2.html', 'wb') as f:
            f.write(request.content)
        content = request.content
        soup = BeautifulSoup(content, 'html5lib')
        ids = getids(soup)
        """
        ids = []
        for match in re_pattern.finditer(request.text):
            ids.append(match.group(1))

        print(ids)
        if not ids:
            print('exit')
            break
        delete(ids, headers)
        print('Deleted {} posts'.format(len(ids)))


if __name__ == '__main__':
    main()
