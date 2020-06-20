import sys
import re
import json
import requests
import getopt


try:
    opt=getopt.getopt(sys.argv[1:],'u:c:',["url=","channel="])
except getopt.GetoptError as err:
    # print help information and exit:
    print (str(err))  # will print something like "option -a not recognized"
    usage()
    sys.exit(2)

url=""
channel=""

for o,v in opt[0]:
    if o in ("-u","--url"):
        url=v
    else:
        channel=v


if url!="":
    h = {
    'Referer': url,
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    }
    u = h['Referer']
    html = requests.get(u,headers=h).text

    def get_title(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\});', html, re.IGNORECASE )
        if matches:
            j=json.loads(matches[0])
            return(j['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']['title']['runs'][0]['text'])
        return ""

    def get_likes(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\});', html, re.IGNORECASE )
        if matches:
            j=json.loads(matches[0])
            return(j['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']['videoActions']['menuRenderer']['topLevelButtons'][0]['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label'].split()[0])
        return ""

    def get_dislikes(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\});', html, re.IGNORECASE )
        if matches:
            j=json.loads(matches[0])
            return(j['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']['videoActions']['menuRenderer']['topLevelButtons'][1]['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label'].split()[0])
        return ""

    def get_views(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\});', html, re.IGNORECASE )
        if matches:
            j=json.loads(matches[0])
            return(j['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']['viewCount']['videoViewCountRenderer']['viewCount']['simpleText'].split()[0])
        return ""

    
    def get_date(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\});', html, re.IGNORECASE )
        if matches:
            j=json.loads(matches[0])
            return(j['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']['dateText']['simpleText'])
        return ""

    def get_subs(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\});', html, re.IGNORECASE )
        if matches:
            j=json.loads(matches[0])
            return(j['contents']['twoColumnWatchNextResults']['results']['results']['contents'][1]['videoSecondaryInfoRenderer']['owner']['videoOwnerRenderer']['subscriberCountText']['runs'][0]['text'].split()[0])
        return ""
    
    def get_channel_name(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\});', html, re.IGNORECASE )
        if matches:
            j=json.loads(matches[0])
            return(j['contents']['twoColumnWatchNextResults']['results']['results']['contents'][1]['videoSecondaryInfoRenderer']['owner']['videoOwnerRenderer']['title']['runs'][0]['text'])
        return ""

    def get_channel_link(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\});', html, re.IGNORECASE )
        if matches:
            j=json.loads(matches[0])
            return(j['contents']['twoColumnWatchNextResults']['results']['results']['contents'][1]['videoSecondaryInfoRenderer']['owner']['videoOwnerRenderer']['title']['runs'][0]['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url'])
        return ""

    print("Channel:",get_channel_name(html),"\nSubscribers:",get_subs(html),"\nTitle:",get_title(html),"\nViews:",get_views(html),"\nLikes:",get_likes(html),"\nDislikes:",get_dislikes(html),"\nUpload Date\Time:",get_date(html),"\nChannel Link:","https://www.youtube.com"+get_channel_link(html))


if channel!="":
    h = {
    'Referer': channel,
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    }
    u = h['Referer']
    html = requests.get(u,headers=h).text

    def get_subscriber(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\]\}\}\});', html, re.IGNORECASE | re.DOTALL)
        if matches:
            j = json.loads(matches[0])
            return(j['header']['c4TabbedHeaderRenderer']['subscriberCountText']['runs'][0]['text'])
        return ""

    print("Total subscriber: "+get_subscriber(html))
