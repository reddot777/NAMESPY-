import requests

snap_base_url = "https://www.snapchat.com/add/"

yt_base_url = "https://www.youtube.com/@"

wiki_base_url = "https://en.wikipedia.org/wiki/"

git_base_url = "https://github.com/"

chess_base_url = "https://www.chess.com/member/"

X_base_url = "https://twitter.com/"

pin_base_url = "https://www.pinterest.com/"

linkd_base_url = "https://www.linkedin.com/in/"

reddit_base_url = "https://www.reddit.com/user/"

vero_base_url = "https://vero.co/"

wehearit_base_url = "https://weheartit.com/"

foursquare_base_url = "https://foursquare.com/user/"

nextdoor_base_url = "https://nextdoor.com/profile/"

roblox_base_url = "https://www.roblox.com/fr/search/users?keyword=username"

behance_base_url = "https://www.behance.net/"

dribble_base_url = "https://dribbble.com/"

devian_base_url = "https://www.deviantart.com/"

artstation_base_url = "https://www.artstation.com/"

px_base_url = "https://500px.com/"

soundcloud_base_url = "https://soundcloud.com/"

spotify_base_url = "https://open.spotify.com/user/"

vimeo_base_url = "https://vimeo.com/"

twitch_base_url = "https://www.twitch.tv/"

dailymotion_base_url = "https://www.dailymotion.com/"

whatsapp_base_url = "https://wa.me/"

telegram_base_url = "https://t.me/"

skype_base_url = "https://join.skype.com/invite/"

discord_base_url = "https://discord.com/user/"

tinder_base_url = "https://www.tinder.com/@"

bumble_base_url = "https://bumble.com/"

okcupid_base_url = "https://www.okcupid.com/profile/"

grindr_base_url = "https://www.grindr.com/"

hinge_base_url = "https://hinge.co/"

pof_base_url = "https://www.pof.com/viewprofile.aspx?profile_id=username"

gitlab_base_url = "https://gitlab.com/"

stackoverflow_base_url = "https://stackoverflow.com/users/"

bitbukcet_base_url = "https://bitbucket.org/"

sourceforge_base_url = "https://sourceforge.net/users/"

hackaday_base_url = "https://hackaday.io/"

xing_base_url = "https://xing.com/profile/"

angelList_base_url = "https://angel.co/u/"

glassdoor_base_url = "https://www.glassdoor.com/Overview/Working-at-username"

indeed_base_url = "https://www.indeed.com/r/"

quora_base_url = "https://www.quora.com/profile/"

stackexchange_base_url = "https://stackexchange.com/users/"

fark_base_url = "https://www.fark.com/user/"

coursera_base_url = "https://www.coursera.org/user/"

udemy_base_url = "https://www.udemy.com/user/"

skillshare_base_url = "https://www.skillshare.com/profile/"

edx_base_url = "https://www.edx.org/scholar/"

khanacademy_base_url = "https://www.khanacademy.org/profile/"

ebay_base_url = "https://www.ebay.com/usr/"

amazon_base_url = "https://www.amazon.com/"

etsy_base_url = "https://www.etsy.com/shop/"

depop_base_url = "https://www.depop.com/"

mercari_base_url = "https://www.mercari.com/u/"

medium_base_url = "https://medium.com/@"

blogger_base_url = "https://username.blogspot.com"

dopbox_base_url = "https://www.dropbox.com/users/"

googledrive_base_url = "https://drive.google.com/drive/folders/"

onedrive_base_url = "https://onedrive.live.com/?id=username"

box_base_url = "https://app.box.com/s/"

coinbase_base_url = "https://www.coinbase.com/profiles/"

binance_base_url = "https://www.binance.com/en/user/"

ethereum_base_url = "https://etherscan.io/address/"

crypto_base_url = "https://crypto.com/users/"

paypal_base_url = "https://www.paypal.com/paypalme/"

eventbrite_base_url = "https://www.eventbrite.com/o/"

meetup_base_url = "https://www.meetup.com/members/"

steam_base_url = "https://steamcommunity.com/id/"

epicgames_base_url = "https://www.epicgames.com/id/"

origin_base_url = "https://origin.com/"

battlenet_base_url = "https://us.battle.net/"

gog_base_url = "https://www.gog.com/account/"

uplay_base_url = "https://www.ubisoft.com/account/"

slack_base_url = "https://slack.com/"

trello_base_url = "https://trello.com/"

asana_base_url = "https://app.asana.com/0/"

basecamp_base_url = "https://basecamp.com/"

monday_base_url = "https://monday.com/"

xhamster_base_url = "https://xhamster.com/users/"

venmo_base_url = "https://venmo.com/u/"


def ascii_art():
    ascii = """
 ███▄    █  ▄▄▄       ███▄ ▄███▓▓█████   ██████  ██▓███ ▓██   ██▓
 ██ ▀█   █ ▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ ▒██    ▒ ▓██░  ██▒▒██  ██▒
▓██  ▀█ ██▒▒██  ▀█▄  ▓██    ▓██░▒███   ░ ▓██▄   ▓██░ ██▓▒ ▒██ ██░
▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄   ▒   ██▒▒██▄█▓▒ ▒ ░ ▐██▓░
▒██░   ▓██░ ▓█   ▓██▒▒██▒   ░██▒░▒████▒▒██████▒▒▒██▒ ░  ░ ░ ██▒▓░
░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░  ██▒▒▒
░ ░░   ░ ▒░  ▒   ▒▒ ░░  ░      ░ ░ ░  ░░ ░▒  ░ ░░▒ ░     ▓██ ░▒░
   ░   ░ ░   ░   ▒   ░      ░      ░   ░  ░  ░  ░░       ▒ ▒ ░░
         ░       ░  ░       ░      ░  ░      ░           ░ ░
                                                         ░ ░
"""
    print(ascii)


ascii_art()


username = input(" USERNAME ---- > ")

def send_snap(name):
    snap_url = f"{snap_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(snap_url, headers=headers)
    if response.status_code == 200 :
        print("[+]",snap_url)
    else :
        print("[-]",snap_url)

send_snap(username)

def send_yt(name):
    yt_url = f"{yt_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(yt_url, headers=headers)
    if response.status_code == 200 :
        print("[+]",yt_url)
    else :
        print("[-]",yt_url)


send_yt(username)


def send_wiki(name):

    wiki_url = f"{wiki_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(wiki_url, headers=headers)
    if response.status_code == 200 :
        print("[+]",wiki_url)
    else :
        print("[-]",wiki_url)


send_wiki(username)

def send_git(name):

    git_url = f"{git_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(git_url, headers=headers)
    if response.status_code == 200 :
        print("[+]",git_url)
    else :
        print("[-]",git_url)


send_git(username)

def send_chess(name):
    chess_url = f"{chess_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(chess_url, headers=headers)
    if response.status_code == 200 :
        print("[+]",chess_url)
    else :
        print("[-]",chess_url)


send_chess(username)


def send_twitter(name):
    X_url = f"{X_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(X_url, headers=headers)
    if response.status_code == 200 :
        print("[+]",X_url)
    else :
        print("[-]",X_url)


send_twitter(username)

def send_pinterest(name):
    pin_url = f"{pin_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(pin_url, headers=headers)
    if response.status_code == 200 :
        print("[+]",pin_url)

    else :
        print("[-]",pin_url)


send_pinterest(username)

def send_linkedin(name):
    linkd_url = f"{linkd_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(linkd_url, headers=headers)
    if response.status_code == 200:
        print("[+]", linkd_url)
    else:
        print("[-]", linkd_url)

send_linkedin(username)

def send_reddit(name):
    reddit_url = f"{reddit_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(reddit_url, headers=headers)
    if response.status_code == 200:
        print("[+]", reddit_url)
    else:
        print("[-]", reddit_url)

send_reddit(username)

def send_vero(name):
    vero_url = f"{vero_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(vero_url, headers=headers)
    if response.status_code == 200:
        print("[+]", vero_url)
    else:
        print("[-]", vero_url)

send_vero(username)

def send_wehearit(name):
    wehearit_url = f"{wehearit_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(wehearit_url, headers=headers)
    if response.status_code == 200:
        print("[+]", wehearit_url)
    else:
        print("[-]", wehearit_url)

send_wehearit(username)

def send_foursquare(name):
    foursquare_url = f"{foursquare_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(foursquare_url, headers=headers)
    if response.status_code == 200:
        print("[+]", foursquare_url)
    else:
        print("[-]", foursquare_url)

send_foursquare(username)

def send_nextdoor(name):
    nextdoor_url = f"{nextdoor_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(nextdoor_url, headers=headers)
    if response.status_code == 200:
        print("[+]", nextdoor_url)
    else:
        print("[-]", nextdoor_url)

send_nextdoor(username)

def send_roblox(name):
    roblox_url = f"{roblox_base_url.replace('username', name)}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(roblox_url, headers=headers)
    if response.status_code == 200:
        print("[+]", roblox_url)
    else:
        print("[-]", roblox_url)

send_roblox(username)

def send_behance(name):
    behance_url = f"{behance_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(behance_url, headers=headers)
    if response.status_code == 200:
        print("[+]", behance_url)
    else:
        print("[-]", behance_url)

send_behance(username)

def send_dribble(name):
    dribble_url = f"{dribble_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(dribble_url, headers=headers)
    if response.status_code == 200:
        print("[+]", dribble_url)
    else:
        print("[-]", dribble_url)

send_dribble(username)

def send_deviantart(name):
    deviant_url = f"{devian_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(deviant_url, headers=headers)
    if response.status_code == 200:
        print("[+]", deviant_url)
    else:
        print("[-]", deviant_url)

send_deviantart(username)

def send_artstation(name):
    artstation_url = f"{artstation_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(artstation_url, headers=headers)
    if response.status_code == 200:
        print("[+]", artstation_url)
    else:
        print("[-]", artstation_url)

send_artstation(username)

def send_500px(name):
    px_url = f"{px_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(px_url, headers=headers)
    if response.status_code == 200:
        print("[+]", px_url)
    else:
        print("[-]", px_url)

send_500px(username)


def send_soundcloud(name):
    soundcloud_url = f"{soundcloud_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(soundcloud_url, headers=headers)
    if response.status_code == 200:
        print("[+]", soundcloud_url)
    else:
        print("[-]", soundcloud_url)

send_soundcloud(username)

def send_spotify(name):
    spotify_url = f"{spotify_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(spotify_url, headers=headers)
    if response.status_code == 200:
        print("[+]", spotify_url)
    else:
        print("[-]", spotify_url)

send_spotify(username)

def send_vimeo(name):
    vimeo_url = f"{vimeo_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(vimeo_url, headers=headers)
    if response.status_code == 200:
        print("[+]", vimeo_url)
    else:
        print("[-]", vimeo_url)

send_vimeo(username)

def send_twitch(name):
    twitch_url = f"{twitch_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(twitch_url, headers=headers)
    if response.status_code == 200:
        print("[+]", twitch_url)
    else:
        print("[-]", twitch_url)

send_twitch(username)

def send_dailymotion(name):
    dailymotion_url = f"{dailymotion_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(dailymotion_url, headers=headers)
    if response.status_code == 200:
        print("[+]", dailymotion_url)
    else:
        print("[-]", dailymotion_url)

send_dailymotion(username)

def send_whatsapp(name):
    whatsapp_url = f"{whatsapp_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(whatsapp_url, headers=headers)
    if response.status_code == 200:
        print("[+]", whatsapp_url)
    else:
        print("[-]", whatsapp_url)

send_whatsapp(username)

def send_telegram(name):
    telegram_url = f"{telegram_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(telegram_url, headers=headers)
    if response.status_code == 200:
        print("[+]", telegram_url)
    else:
        print("[-]", telegram_url)

send_telegram(username)

def send_skype(name):
    skype_url = f"{skype_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(skype_url, headers=headers)
    if response.status_code == 200:
        print("[+]", skype_url)
    else:
        print("[-]", skype_url)

send_skype(username)

def send_discord(name):
    discord_url = f"{discord_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(discord_url, headers=headers)
    if response.status_code == 200:
        print("[+]", discord_url)
    else:
        print("[-]", discord_url)

send_discord(username)

def send_tinder(name):
    tinder_url = f"{tinder_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(tinder_url, headers=headers)
    if response.status_code == 200:
        print("[+]", tinder_url)
    else:
        print("[-]", tinder_url)

send_tinder(username)

def send_bumble(name):
    bumble_url = f"{bumble_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(bumble_url, headers=headers)
    if response.status_code == 200:
        print("[+]", bumble_url)
    else:
        print("[-]", bumble_url)

send_bumble(username)

def send_okcupid(name):
    okcupid_url = f"{okcupid_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(okcupid_url, headers=headers)
    if response.status_code == 200:
        print("[+]", okcupid_url)
    else:
        print("[-]", okcupid_url)

send_okcupid(username)

def send_grindr(name):
    grindr_url = f"{grindr_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(grindr_url, headers=headers)
    if response.status_code == 200:
        print("[+]", grindr_url)
    else:
        print("[-]", grindr_url)

send_grindr(username)

def send_hinge(name):
    hinge_url = f"{hinge_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(hinge_url, headers=headers)
    if response.status_code == 200:
        print("[+]", hinge_url)
    else:
        print("[-]", hinge_url)

send_hinge(username)

def send_pof(name):
    pof_url = f"{pof_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(pof_url, headers=headers)
    if response.status_code == 200:
        print("[+]", pof_url)
    else:
        print("[-]", pof_url)

send_pof(username)

def send_gitlab(name):
    gitlab_url = f"{gitlab_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(gitlab_url, headers=headers)
    if response.status_code == 200:
        print("[+]", gitlab_url)
    else:
        print("[-]", gitlab_url)

send_gitlab(username)

def send_stackoverflow(name):
    stackoverflow_url = f"{stackoverflow_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(stackoverflow_url, headers=headers)
    if response.status_code == 200:
        print("[+]", stackoverflow_url)
    else:
        print("[-]", stackoverflow_url)

send_stackoverflow(username)

def send_bitbucket(name):
    bitbucket_url = f"{bitbukcet_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(bitbucket_url, headers=headers)
    if response.status_code == 200:
        print("[+]", bitbucket_url)
    else:
        print("[-]", bitbucket_url)

send_bitbucket(username)

def send_sourceforge(name):
    sourceforge_url = f"{sourceforge_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(sourceforge_url, headers=headers)
    if response.status_code == 200:
        print("[+]", sourceforge_url)
    else:
        print("[-]", sourceforge_url)

send_sourceforge(username)

def send_hackaday(name):
    hackaday_url = f"{hackaday_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(hackaday_url, headers=headers)
    if response.status_code == 200:
        print("[+]", hackaday_url)
    else:
        print("[-]", hackaday_url)

send_hackaday(username)

def send_xing(name):
    xing_url = f"{xing_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(xing_url, headers=headers)
    if response.status_code == 200:
        print("[+]", xing_url)
    else:
        print("[-]", xing_url)

send_xing(username)

def send_angellist(name):
    angellist_url = f"{angelList_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(angellist_url, headers=headers)
    if response.status_code == 200:
        print("[+]", angellist_url)
    else:
        print("[-]", angellist_url)

send_angellist(username)

def send_glassdoor(name):
    glassdoor_url = f"{glassdoor_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(glassdoor_url, headers=headers)
    if response.status_code == 200:
        print("[+]", glassdoor_url)
    else:
        print("[-]", glassdoor_url)

send_glassdoor(username)

def send_indeed(name):
    indeed_url = f"{indeed_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(indeed_url, headers=headers)
    if response.status_code == 200:
        print("[+]", indeed_url)
    else:
        print("[-]", indeed_url)

send_indeed(username)

def send_quora(name):
    quora_url = f"{quora_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(quora_url, headers=headers)
    if response.status_code == 200:
        print("[+]", quora_url)
    else:
        print("[-]", quora_url)

send_quora(username)

def send_stackexchange(name):
    stackexchange_url = f"{stackexchange_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(stackexchange_url, headers=headers)
    if response.status_code == 200:
        print("[+]", stackexchange_url)
    else:
        print("[-]", stackexchange_url)

send_stackexchange(username)

def send_fark(name):
    fark_url = f"{fark_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(fark_url, headers=headers)
    if response.status_code == 200:
        print("[+]", fark_url)
    else:
        print("[-]", fark_url)

send_fark(username)

def send_coursera(name):
    coursera_url = f"{coursera_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(coursera_url, headers=headers)
    if response.status_code == 200:
        print("[+]", coursera_url)
    else:
        print("[-]", coursera_url)

send_coursera(username)

def send_udemy(name):
    udemy_url = f"{udemy_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(udemy_url, headers=headers)
    if response.status_code == 200:
        print("[+]", udemy_url)
    else:
        print("[-]", udemy_url)

send_udemy(username)

def send_skillshare(name):
    skillshare_url = f"{skillshare_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(skillshare_url, headers=headers)
    if response.status_code == 200:
        print("[+]", skillshare_url)
    else:
        print("[-]", skillshare_url)

send_skillshare(username)

def send_edx(name):
    edx_url = f"{edx_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(edx_url, headers=headers)
    if response.status_code == 200:
        print("[+]", edx_url)
    else:
        print("[-]", edx_url)

send_edx(username)

def send_khanacademy(name):
    khanacademy_url = f"{khanacademy_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(khanacademy_url, headers=headers)
    if response.status_code == 200:
        print("[+]", khanacademy_url)
    else:
        print("[-]", khanacademy_url)

send_khanacademy(username)

def send_ebay(name):
    ebay_url = f"{ebay_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(ebay_url, headers=headers)
    if response.status_code == 200:
        print("[+]", ebay_url)
    else:
        print("[-]", ebay_url)

send_ebay(username)

def send_amazon(name):
    amazon_url = f"{amazon_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(amazon_url, headers=headers)
    if response.status_code == 200:
        print("[+]", amazon_url)
    else:
        print("[-]", amazon_url)

send_amazon(username)

def send_etsy(name):
    etsy_url = f"{etsy_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(etsy_url, headers=headers)
    if response.status_code == 200:
        print("[+]", etsy_url)
    else:
        print("[-]", etsy_url)

send_etsy(username)

def send_depop(name):
    depop_url = f"{depop_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(depop_url, headers=headers)
    if response.status_code == 200:
        print("[+]", depop_url)
    else:
        print("[-]", depop_url)

send_depop(username)

def send_mercari(name):
    mercari_url = f"{mercari_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(mercari_url, headers=headers)
    if response.status_code == 200:
        print("[+]", mercari_url)
    else:
        print("[-]", mercari_url)

send_mercari(username)

"""def send_wordpress(name):
    wordpress_url = f"{wordpress_base_url.replace('username', name)}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(wordpress_url, headers=headers)
    if response.status_code == 200:
        print("[+]", wordpress_url)
    else:
        print("[-]", wordpress_url)

send_wordpress(username)"""

def send_medium(name):
    medium_url = f"{medium_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(medium_url, headers=headers)
    if response.status_code == 200:
        print("[+]", medium_url)
    else:
        print("[-]", medium_url)

send_medium(username)

"""def send_ghost(name):
    ghost_url = f"{ghost_base_url.replace('username', name)}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(ghost_url, headers=headers)
    if response.status_code == 200:
        print("[+]", ghost_url)
    else:
        print("[-]", ghost_url)

send_ghost(username) """

def send_blogger(name):
    blogger_url = f"{blogger_base_url.replace('username', name)}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(blogger_url, headers=headers)
    try :
        if response.status_code == 200 :
            print("[+]", blogger_url)
        else:
            print("[-]", blogger_url)
    except requests.RequestException:
        print("[-] ERROR CONNECTION TO SERVER !")
        
send_blogger(username)

def send_dropbox(name):
    dropbox_url = f"{dopbox_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(dropbox_url, headers=headers)
    if response.status_code == 200:
        print("[+]", dropbox_url)
    else:
        print("[-]", dropbox_url)

send_dropbox(username)

def send_googledrive(name):
    googledrive_url = f"{googledrive_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(googledrive_url, headers=headers)
    if response.status_code == 200:
        print("[+]", googledrive_url)
    else:
        print("[-]", googledrive_url)

send_googledrive(username)

def send_onedrive(name):
    onedrive_url = f"{onedrive_base_url.replace('username', name)}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(onedrive_url, headers=headers)
    if response.status_code == 200:
        print("[+]", onedrive_url)
    else:
        print("[-]", onedrive_url)

send_onedrive(username)

def send_box(name):
    box_url = f"{box_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(box_url, headers=headers)
    if response.status_code == 200:
        print("[+]", box_url)
    else:
        print("[-]", box_url)

send_box(username)

def send_coinbase(name):
    coinbase_url = f"{coinbase_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(coinbase_url, headers=headers)
    if response.status_code == 200:
        print("[+]", coinbase_url)
    else:
        print("[-]", coinbase_url)

send_coinbase(username)

def send_binance(name):
    binance_url = f"{binance_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(binance_url, headers=headers)
    if response.status_code == 200:
        print("[+]", binance_url)
    else:
        print("[-]", binance_url)

send_binance(username)

def send_ethereum(name):
    ethereum_url = f"{ethereum_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(ethereum_url, headers=headers)
    if response.status_code == 200:
        print("[+]", ethereum_url)
    else:
        print("[-]", ethereum_url)

send_ethereum(username)

def send_crypto(name):
    crypto_url = f"{crypto_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(crypto_url, headers=headers)
    if response.status_code == 200:
        print("[+]", crypto_url)
    else:
        print("[-]", crypto_url)

send_crypto(username)

def send_paypal(name):
    paypal_url = f"{paypal_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(paypal_url, headers=headers)
    if response == 200:
        print("[+]", paypal_url)
    else :
        print("[-]", paypal_url)

send_paypal(username)

def send_eventbrite(name):
    eventbrite_url = f"{eventbrite_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(eventbrite_url, headers=headers)
    if response.status_code == 200:
        print("[+]", eventbrite_url)
    else:
        print("[-]", eventbrite_url)

send_eventbrite(username)

def send_meetup(name):
    meetup_url = f"{meetup_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(meetup_url, headers=headers)
    if response.status_code == 200:
        print("[+]", meetup_url)
    else:
        print("[-]", meetup_url)

send_meetup(username)

def send_steam(name):
    steam_url = f"{steam_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(steam_url, headers=headers)
    if response.status_code == 200:
        print("[+]", steam_url)
    else:
        print("[-]", steam_url)

send_steam(username)

def send_epicgames(name):
    epicgames_url = f"{epicgames_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(epicgames_url, headers=headers)
    if response.status_code == 200:
        print("[+]", epicgames_url)
    else:
        print("[-]", epicgames_url)

send_epicgames(username)

def send_origin(name):
    origin_url = f"{origin_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(origin_url, headers=headers)
    if response.status_code == 200:
        print("[+]", origin_url)
    else:
        print("[-]", origin_url)

send_origin(username)

def send_battlenet(name):
    battlenet_url = f"{battlenet_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(battlenet_url, headers=headers)
    if response.status_code == 200:
        print("[+]", battlenet_url)
    else:
        print("[-]", battlenet_url)

send_battlenet(username)

def send_gog(name):
    gog_url = f"{gog_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(gog_url, headers=headers)
    if response.status_code == 200:
        print("[+]", gog_url)
    else:
        print("[-]", gog_url)

send_gog(username)

def send_uplay(name):
    uplay_url = f"{uplay_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(uplay_url, headers=headers)
    if response.status_code == 200:
        print("[+]", uplay_url)
    else:
        print("[-]", uplay_url)

send_uplay(username)

def send_slack(name):
    slack_url = f"{slack_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(slack_url, headers=headers)
    if response.status_code == 200:
        print("[+]", slack_url)
    else:
        print("[-]", slack_url)

send_slack(username)

def send_trello(name):
    trello_url = f"{trello_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(trello_url, headers=headers)
    if response.status_code == 200:
        print("[+]", trello_url)
    else:
        print("[-]", trello_url)

send_trello(username)

def send_asana(name):
    asana_url = f"{asana_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(asana_url, headers=headers)
    if response.status_code == 200:
        print("[+]", asana_url)
    else:
        print("[-]", asana_url)

send_asana(username)

def send_basecamp(name):
    basecamp_url = f"{basecamp_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(basecamp_url, headers=headers)
    if response.status_code == 200:
        print("[+]", basecamp_url)
    else:
        print("[-]", basecamp_url)

send_basecamp(username)

def send_monday(name):
    monday_url = f"{monday_base_url}{name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(monday_url, headers=headers)
    if response.status_code == 200:
        print("[+]", monday_url)
    else:
        print("[-]", monday_url)


send_monday(username)

def send_xhamster(name):
     xhamster_url = f"{xhamster_base_url}{name}"
     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
     response = requests.get(xhamster_url, headers=headers)
     if response.status_code == 200 :
        print("[+]", xhamster_url)
     else :
        print("[-]", xhamster_url)

send_xhamster(username)

def send_venmo(name):
     venmo_url = f"{venmo_base_url}{name}"
     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
     response = requests.get(venmo_url, headers=headers)
     if response.status_code == 200 :
        print("[+]", venmo_url)
     else :
        print("[-]", venmo_url)

send_venmo(username)


print("\nNameSpy by @reddot777 on github")

print("\nI HAVE NO RESPONSABILITY OF UR ACTS")






























































