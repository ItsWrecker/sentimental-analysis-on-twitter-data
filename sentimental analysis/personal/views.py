from django.shortcuts import render
import sentiment_mod as s



def index(request):
    api=s.TwitterClient()
    tweets = api.get_tweets(query = "bhubaneswar", count = 2000)
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    pos=format(100*len(ptweets)/len(tweets))
    

    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    neg=format(100*len(ntweets)/len(tweets))

    nut=format(80-(len(ptweets)+len(ntweets)))


    for ptweet in ptweets[:2]:
        ptweet['text']
    for p1 in ptweets[:5]:
        p1['text']
    for p2 in ptweets[:8]:
        p2['text']
    for p3 in ptweets[:15]:
        p3['text']
    for p4 in ptweets[:20]:
        p4['text']
    for p5 in ptweets[:25]:
        p5['text']
    for p6 in ptweets[:30]:
        p6['text']
    for p7 in ptweets[:5]:
        p7['text']
    for p8 in ptweets[:9]:
        p8['text']
    for p9 in ptweets[:50]:
        p9['text']
    for p10 in ptweets[:50]:
        p10['text']
    for ntweet in ntweets[:2]:
        ntweet['text']
    for n1 in ntweets[:5]:
        n1['text']
    for n2 in ntweets[:4]:
        n2['text']
    for n3 in ntweets[:6]:
        n3['text']
    for n4 in ntweets[:8]:
        n4['text']
    for n5 in ntweets[:8]:
        n5['text']
    for n6 in ntweets[:30]:
        n6['text']
    for n7 in ntweets[:3]:
        n7['text']
    for n8 in ntweets[:40]:
        n8['text']
    for n9 in ntweets[:4]:
        n9['text']
    for n10 in ntweets[:7]:
        n10['text']
 

    return render(request, 'personal/home.html',{ 'neutral':nut,'positive': pos,'negative': neg, 'ptweets':ptweet['text'],'ntweets':ntweet['text'],'n1':n1['text'],'n2':n2['text'],'n3':n3['text'],'n4':n4['text'],'n5':n5['text'],'n6':n6['text'],'n7':n7['text'],'n8':n8['text'],'n9':n9['text'],'n10':n10['text'],'p1':p1['text'],'p2':p2['text'],'p3':p3['text'],'p4':p4['text'],'p5':p5['text'],'p6':p6['text'],'p7':p7['text'],'p8':p8['text'],'p9':p9['text'],'p10':p10['text'],})
