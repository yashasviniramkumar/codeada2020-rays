import requests
from bs4 import BeautifulSoup
import twint
import pandas as pd
from collections import Counter
import time
import matplotlib.pyplot as plt




users = [
    'Trump',
    'Biden',
    'Obama',
    'Harris',
    'Pence'
]

environmental_words = ["fossil", "fuel","climate", "oil", "energy", "fracking", "climate", "change", "carbon", "footprint", "methane", "mitigation", "global", "warming", "earth", "eco", "abiotoc", "acid", "rain", "aerosols", "afforestation", "air", "pollution", "biodegradable", "biodiversity", "biofuel", "biogas", "biomass", "carcinogen"]
immigration_words = ["foreign", "policy", "immigration", "immigrant", "cage", "border", "wall", "muslim", "mexico", "mexican", "citizenship", "ICE", "DACA", "visa", "China", "deport"]
healthcare_words = ["pandemic", "health", "obamacare", "euthanasia", "social security", "covid", "mask", "mental health", "medicaid", "welfare", "pension", "nurse", "doctor", "hospital", "coronavirus", "corona", "insurance", "affordable", "medical", "plans"]
womens_rights_words = ["abortion", "pro-life", "women", "equal pay", "gender", "planned parenthood", "tampon", "pad"]
lgbtq_rights_words = ["gay", "marriage", "gender", "identity", "homosexual", "lgbtq", "lesbian", "gay", "bisexual", "transgender", "orientation",
    "sexuality","sexual", "non-binary", "pride","ally","androgynous", "asexual", "closeted", "coming out", "identity", "gender queer", "transition",
    "homophobia", "intersex", "outing", "pansexual", "questioning", "transphobia"]
#overseas_policies_words = ["tariff", "china", "russia", "united nations", "foreign aid", "north korea", "united nations", "iran", "israel",
    #"military spending", "NATO", "afghanistan", "torture", "terrorism", "drone"]
racial_awareness_words = ["black", "blm", "black lives matter", "racial justice", "racial equality", "race", "defunding", "all lives matter",
    "body camera", "poc", "antiracist", "cultural", "appropriation", "bipoc", "equity", "diversity", "inclusion", "insitutionalized",
    "microagression", "white privilege", "supremacy"]



class TwitterHashTagPosts:

    def __init__(self, hashtag):
        self.hashtag = hashtag
        self.tweets = []
        self.url = "https://mobile.twitter.com/hashtag/" + self.hashtag.strip()

    def scrape_tweets(self):

        content = requests.get(self.url)
        soup = BeautifulSoup(content.text, "html.parser")
        tweet_divs = soup.select("#main_content")[0].select(".tweet")
        for tweet in tweet_divs:
            #handle = tweet.find("div", {"class": "username"}).text.replace("\n", " ").strip()
            post = tweet.find("div", {"class": "tweet-text"}).text.replace("\n", " ").strip()
            self.tweets.append(post)
        #print(self.tweets)
        return self.tweets

finalTweets = []
for i in range(len(users)):
    x = TwitterHashTagPosts(users[i])
    finalTweets.append(x.scrape_tweets())





ct_array = [[0, 0, 0,0,0,0,], [0, 0, 0,0,0,0,], [0, 0, 0,0,0,0,], [0, 0, 0,0,0,0,], [0, 0, 0,0,0,0,]]
twitter_arr =[]
for i in range(5):
    twitter_arr.append([])
    for l in range(6):
        twitter_arr[i].append([])
    for j in range(len(finalTweets[i])):
        for k in environmental_words:
            if k in finalTweets[i][j]:
                ct_array[i][0] +=1
                twitter_arr[i][0].append(finalTweets[i][j])
        for k in immigration_words:
            if k in finalTweets[i][j]:
                ct_array[i][1] +=1
                twitter_arr[i][1].append(finalTweets[i][j])
        for k in healthcare_words:
            if k in finalTweets[i][j]:
                ct_array[i][2] +=1
                twitter_arr[i][2].append(finalTweets[i][j])
        for k in womens_rights_words:
            if k in finalTweets[i][j]:
                ct_array[i][3] +=1
                twitter_arr[i][3].append(finalTweets[i][j])
        for k in lgbtq_rights_words:
            if k in finalTweets[i][j]:
                ct_array[i][4] +=1
                twitter_arr[i][4].append(finalTweets[i][j])
        #for k in overseas_policies_words:
            #if k in finalTweets[i][j]:
                #ct_array[i][5] +=1
                #twitter_arr[i][5].append(finalTweets[i][j])
        for k in racial_awareness_words:
            if k in finalTweets[i][j]:
                ct_array[i][5] +=1
                twitter_arr[i][5].append(finalTweets[i][j])

print(ct_array)




# table = []

# for i in range(5):
#     nested_politicians = []
#     for j in range(6):
#         nested_politicians.append(twitter_arr[i][j])
#     table.append(nested_politicians)

# # output_tweets_table = 

# print(tabulate(table, tablefmt='html'))




for i in range(6):
    #Environ Tweets by Politician
    plt.plot(users, [3,2,0,1,0])
    #Immigration
    plt.plot(users, [2,2,2,2,0])
    #Healthcare
    plt.plot(users, [1,1,0,1,1])
    #Womens Rights
    plt.plot(users, [1,0,0,0,0])
    #LGBTQ Rights
    plt.plot(users, [3,0,1,1,7])
    #Racial Awareness
    plt.plot(users, [0,0,1,1,0])

plt.legend(["Environmental", "Immigration", "Healthcare", "Womens Rights", "LGBTQ Rights", "Racial Awareness"])
plt.suptitle('Political Public Policies Tweet Visualization')
plt.show()

plt.savefig('my_plot.png')

