from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

url1 = "https://feeds.feedburner.com/TheMotherJonesPodcast"
url2 = "http://feeds.feedburner.com/bite-podcast"

plugin = Plugin()
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts113/v4/e4/c4/ad/e4c4ad13-6cf5-1c40-5f3d-aba90668db18/mza_3523615710896971529.jpeg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts113/v4/e4/c4/ad/e4c4ad13-6cf5-1c40-5f3d-aba90668db18/mza_3523615710896971529.jpeg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://www.motherjones.com/wp-content/themes/motherjones/img/bite-logo-615-615.png"},
        {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://www.motherjones.com/wp-content/themes/motherjones/img/bite-logo-615-615.png"},
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

@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

@plugin.route('/episodes3/')
def episodes3():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup2)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items

if __name__ == '__main__':
    plugin.run()
