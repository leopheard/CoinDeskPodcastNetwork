from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://rss.art19.com/late-confirmation"
url2 = "https://rss.art19.com/coindesk-reports"
url3 = "https://rss.art19.com/markets-daily"
url4 = "https://rss.art19.com/coindesks-money-reimagined"
url5 = "https://rss.art19.com/mapping-out-eth-20"
url6 = "https://rss.art19.com/hard-problems-with-bram-cohen"

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://content.production.cdn.art19.com/images/90/02/1e/e5/90021ee5-ee71-49ec-8dee-4bb74febbe02/6da5837f399bae77fa0e90f94daae54bc1175ea0550ca8f8c388e82efd3349d9e89441d7c9474249e80a216b2f2a9f9a0cf722f8ff53304c06aa16804669ef05.jpeg"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://content.production.cdn.art19.com/images/90/02/1e/e5/90021ee5-ee71-49ec-8dee-4bb74febbe02/6da5837f399bae77fa0e90f94daae54bc1175ea0550ca8f8c388e82efd3349d9e89441d7c9474249e80a216b2f2a9f9a0cf722f8ff53304c06aa16804669ef05.jpeg"},
        {
            'label': plugin.get_string(30003), 
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://static.coindesk.com/wp-content/uploads/2020/09/podcast-cover-3fa4c53c5e702bca96b8100b1e1e821b-400x400.jpeg"},
        {
            'label': plugin.get_string(30004), 
            'path': plugin.url_for('episodes4'),
            'thumbnail': "https://static.coindesk.com/wp-content/uploads/2020/10/podcast-cover-19a5b4f9dd7641000db1844bc66413b9-400x400.jpeg?format=webp"},
        {
            'label': plugin.get_string(30005), 
            'path': plugin.url_for('episodes5'),
            'thumbnail': "https://static.coindesk.com/wp-content/uploads/2021/02/MOE_3000x3000_v6-400x400.jpg?format=webp"},
        {
            'label': plugin.get_string(30006),
            'path': plugin.url_for('episodes6'),
            'thumbnail': "https://static.coindesk.com/wp-content/uploads/2021/05/podcast-cover-745cc4af1412b3a27c30bc3d5a21e035-400x400.jpeg?format=webp"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items
@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(url3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items
@plugin.route('/episodes4/')
def episodes4():
    soup4 = mainaddon.get_soup4(url4)   
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
    items = mainaddon.compile_playable_podcast4(playable_podcast4)
    return items
@plugin.route('/episodes5/')
def episodes5():
    soup5 = mainaddon.get_soup5(url5)
    playable_podcast5 = mainaddon.get_playable_podcast5(soup5)
    items = mainaddon.compile_playable_podcast5(playable_podcast5)
    return items
@plugin.route('/episodes6/')
def episodes6():
    soup6 = mainaddon.get_soup6(url6)
    playable_podcast6 = mainaddon.get_playable_podcast6(soup6)
    items = mainaddon.compile_playable_podcast6(playable_podcast6)
    return items

if __name__ == '__main__':
    plugin.run()
