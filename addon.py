from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://rss.art19.com/late-confirmation"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://content.production.cdn.art19.com/images/90/02/1e/e5/90021ee5-ee71-49ec-8dee-4bb74febbe02/6da5837f399bae77fa0e90f94daae54bc1175ea0550ca8f8c388e82efd3349d9e89441d7c9474249e80a216b2f2a9f9a0cf722f8ff53304c06aa16804669ef05.jpeg"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://content.production.cdn.art19.com/images/90/02/1e/e5/90021ee5-ee71-49ec-8dee-4bb74febbe02/6da5837f399bae77fa0e90f94daae54bc1175ea0550ca8f8c388e82efd3349d9e89441d7c9474249e80a216b2f2a9f9a0cf722f8ff53304c06aa16804669ef05.jpeg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
