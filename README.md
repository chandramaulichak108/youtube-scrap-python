# SCRAPPING YouTube (using python)

It is a command-line python program, which has 2 flags:

``` python 
-u,--url   The video url
-c,--channel   A youtube channel
```

You can use the video url to get video info

```
$ python youscrap.py -u "https://www.youtube.com/watch?v=D__UaR5MQao&t" 
Channel: 3Blue1Brown 
Subscribers: 2.89M 
Title: Does contact tracing necessarily sacrifice privacy? (via Nicky Case) 
Views: 244,730 
Likes: 19,918 
Dislikes: 373 
Upload Date\Time: 14 May 2020 
Channel Link: https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw
```

You can also use the channel link to get channel info

```
$ python youscrap.py -c "https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw"
Channel Name: 3Blue1Brown 
Total subscriber: 2.89M
Total Views: 143,311,842 
Joined Date: 3 Mar 2015 
Country: United States 
Description:
3blue1brown, by Grant Sanderson, is some combination of math and entertainment, depending on your disposition. The goal is for explanations to be driven by animations and for difficult problems to be made simple with changes in perspective.

Contact and FAQ: https://www.3blue1brown.com/faq

Social Media Handles
Home page: /redirect?redir_token=dBNOuykzQN39iSuDLNvaqfYrDPR8MTU5MjgzNzUyNUAxNTkyNzUxMTI1&event=channel_banner&q=https%3A%2F%2Fwww.3blue1brown.com 

Patreon: https://www.youtube.com/redirect?redir_token=dBNOuykzQN39iSuDLNvaqfYrDPR8MTU5MjgzNzUyNUAxNTkyNzUxMTI1&event=channel_banner&q=https%3A%2F%2Fwww.patreon.com%2F3blue1brown 

Twitter: https://www.youtube.com/redirect?redir_token=dBNOuykzQN39iSuDLNvaqfYrDPR8MTU5MjgzNzUyNUAxNTkyNzUxMTI1&event=channel_banner&q=https%3A%2F%2Fwww.twitter.com%2F3blue1brown 

Reddit: https://www.youtube.com/redirect?redir_token=dBNOuykzQN39iSuDLNvaqfYrDPR8MTU5MjgzNzUyNUAxNTkyNzUxMTI1&event=channel_banner&q=https%3A%2F%2Fwww.reddit.com%2Fr%2F3blue1brown 

Instagram: https://www.youtube.com/redirect?redir_token=dBNOuykzQN39iSuDLNvaqfYrDPR8MTU5MjgzNzUyNUAxNTkyNzUxMTI1&event=channel_banner&q=https%3A%2F%2Fwww.instagram.com%2F3blue1brown_animations%2F 
```


Enjoy !!
