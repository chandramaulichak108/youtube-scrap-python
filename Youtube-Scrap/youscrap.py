import sys
import re
import json
import requests
import getopt

def usage():
    print("\nThis is the usage function\n")
    print('Usage: '+sys.argv[0]+' -i <file1> [option]')

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
            try:
                return(j['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']['title']['runs'][0]['text'])
            except:
                return ""
        return ""

    def get_likes(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\});', html, re.IGNORECASE )
        if matches:
            j=json.loads(matches[0])
            try:
                return(j['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']['videoActions']['menuRenderer']['topLevelButtons'][0]['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label'].split()[0])
            except:
                return ""
        return ""

    def get_dislikes(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\});', html, re.IGNORECASE )
        if matches:
            j=json.loads(matches[0])
            try:
                return(j['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']['videoActions']['menuRenderer']['topLevelButtons'][1]['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label'].split()[0])
            except:
                return ""
        return ""

    def get_views(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\});', html, re.IGNORECASE )
        if matches:
            j=json.loads(matches[0])
            try:
                return(j['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']['viewCount']['videoViewCountRenderer']['viewCount']['simpleText'].split()[0])
            except:
                return ""
        return ""

    
    def get_date(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\});', html, re.IGNORECASE )
        if matches:
            j=json.loads(matches[0])
            try:
                return(j['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']['dateText']['simpleText'])
            except:
                return ""
        return ""

    def get_subs(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\});', html, re.IGNORECASE )
        if matches:
            j=json.loads(matches[0])
            try:
                return(j['contents']['twoColumnWatchNextResults']['results']['results']['contents'][1]['videoSecondaryInfoRenderer']['owner']['videoOwnerRenderer']['subscriberCountText']['runs'][0]['text'].split()[0])
            except:
                return ""
        return ""
    
    def get_channel_name(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\});', html, re.IGNORECASE )
        if matches:
            j=json.loads(matches[0])
            try:
                return(j['contents']['twoColumnWatchNextResults']['results']['results']['contents'][1]['videoSecondaryInfoRenderer']['owner']['videoOwnerRenderer']['title']['runs'][0]['text'])
            except:
                return ""
        return ""

    def get_channel_link(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\});', html, re.IGNORECASE )
        if matches:
            j=json.loads(matches[0])
            try:
                return(j['contents']['twoColumnWatchNextResults']['results']['results']['contents'][1]['videoSecondaryInfoRenderer']['owner']['videoOwnerRenderer']['title']['runs'][0]['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url'])
            except:
                return ""
        return ""

    print("Channel:",get_channel_name(html),"\nSubscribers:",get_subs(html),"\nTitle:",get_title(html),"\nViews:",get_views(html),"\nLikes:",get_likes(html),"\nDislikes:",get_dislikes(html),"\nUpload Date\Time:",get_date(html),"\nChannel Link:","https://www.youtube.com"+get_channel_link(html))


if channel!="":
    h = {
    'Referer': channel,
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    }
    u = h['Referer']
    html = requests.get(u,headers=h).text

    def get_name(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\]\}\}\});', html, re.IGNORECASE | re.DOTALL)
        if matches:
            j = json.loads(matches[0])
            try:
                return(j['header']['c4TabbedHeaderRenderer']['title'])
            except:
                return ""
        return ""
    
    def get_subscriber(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\]\}\}\});', html, re.IGNORECASE | re.DOTALL)
        if matches:
            j = json.loads(matches[0])
            try:
                return(j['header']['c4TabbedHeaderRenderer']['subscriberCountText']['runs'][0]['text'].split()[0])
            except:
                return ""
        return ""
    
    def update_link(link):
        if link.find('youtube')!=-1:
            #print("here")
            return link
        else:
            try:
                if link.find("https")!=-1:
                    #print("link worked",link)
                    link=link[link.find("https"):]
                    link=link[:link.find("&")]
                    link=link.replace("%2F","/")
                    link=link.replace('%3A',":")
                    return link
                else:
                    return ""
            except:
                return ""



    def get_social(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\]\}\}\});', html, re.IGNORECASE | re.DOTALL)
        soc_link={}
        if matches:
            j = json.loads(matches[0])
            try:
                if 'primaryLinks' in j['header']['c4TabbedHeaderRenderer']['headerLinks']['channelHeaderLinksRenderer'].keys():
                    for c in j['header']['c4TabbedHeaderRenderer']['headerLinks']['channelHeaderLinksRenderer']['primaryLinks']:
                        soc_link[c['title']['simpleText']]=update_link(c['navigationEndpoint']['urlEndpoint']['url'])
                        

                if 'secondaryLinks' in j['header']['c4TabbedHeaderRenderer']['headerLinks']['channelHeaderLinksRenderer'].keys():
                    for c in j['header']['c4TabbedHeaderRenderer']['headerLinks']['channelHeaderLinksRenderer']['secondaryLinks']:
                        soc_link[c['title']['simpleText']]=update_link(c['navigationEndpoint']['urlEndpoint']['url'])
            except:
                return ""
        return soc_link
                
    soc_link=get_social(html)
    
    print("Channel Name:",get_name(html),"\nTotal subscriber:",get_subscriber(html))
    
    h = {
    'Referer': channel+'/about',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    }
    u = h['Referer']
    html = requests.get(u,headers=h).text

    #print(u)

    def get_description(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\]\}\}\});', html, re.IGNORECASE | re.DOTALL)
        if matches:
            j = json.loads(matches[0])
            try:
                return(j['metadata']['channelMetadataRenderer']['description'])
            except:
                return ""
        return ""

    def get_total_views(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\]\}\}\});', html, re.IGNORECASE | re.DOTALL)
        if matches:
            j = json.loads(matches[0])
            try:
                return(j['contents']['twoColumnBrowseResultsRenderer']['tabs'][5]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['channelAboutFullMetadataRenderer']['viewCountText']['runs'][0]['text'])
            except:
                try:
                   return(j['contents']['twoColumnBrowseResultsRenderer']['tabs'][5]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['channelAboutFullMetadataRenderer']['viewCountText']['simpleText'].split()[0])
                except:
                    return ""
        return ""

    def get_joined_date(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\]\}\}\});', html, re.IGNORECASE | re.DOTALL)
        if matches:
            j = json.loads(matches[0])
            try:
                return(j['contents']['twoColumnBrowseResultsRenderer']['tabs'][5]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['channelAboutFullMetadataRenderer']['joinedDateText']['runs'][1]['text'])
            except:
                return ""
        return ""

    def get_country(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\]\}\}\});', html, re.IGNORECASE | re.DOTALL)
        if matches:
            j = json.loads(matches[0])
            try:
                return(j['contents']['twoColumnBrowseResultsRenderer']['tabs'][5]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['channelAboutFullMetadataRenderer']['country']['simpleText'])
            except:
                return ""
        return ""
    '''
    def get_tot_videos(html):
        matches = re.findall(r'window\["ytInitialData"\] = (.*\}\]\}\}\});', html, re.IGNORECASE | re.DOTALL)
        if matches:
            j = json.loads(matches[0])
            try:
                return(j['contents']['twoColumnBrowseResultsRenderer']['secondaryContents']['browseSecondaryContentsRenderer']['contents'][0]['verticalChannelSectionRenderer']['items'][0]['miniChannelRenderer']['videoCountText']['runs'][0]['text'].split()[0])
            except:
                return ""
        return ""
    '''

    print("Total Views:",get_total_views(html),"\nJoined Date:",get_joined_date(html),"\nCountry:",get_country(html),"\nDescription:\n"+get_description(html))
    
    if bool(soc_link)==True:
        print("\nSocial Media Handles")
        for c in soc_link.keys():
            print(c+":",soc_link[c],"\n")
    