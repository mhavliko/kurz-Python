from requests_html import HTMLSession
session = HTMLSession()
stranka = session.get('https://www.mall.cz/instantni-kava')
stranka.html.render(sleep=5)