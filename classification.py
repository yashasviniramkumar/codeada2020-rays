import requests
import json 

environmental_words = ["fossil fuel","climate", "oil", "energy", "fracking", "climate change", "carbon footprint", "methan", "mitigation", ""]
immigration_words = ["foreign policy", "immigration", "immigrant", "cage", "border", "wall", "muslim", "mexico", "mexican", "citizenship"]
healthcare_words = ["pandemic", "health", "obamacare", "euthanasia", "social security", "covid", "mask", "mental health", "medicaid", "welfare", "pension"]
womens_rights_words = ["abortion", "pro-life", "women", "equal pay", "gender", "planned parenthood", "tampon", "pad"]
lgbtq_rights_words = ["gay marriage", "gender identity", "homosexual", "lgbtq", "lesbian", "gay", "bisexual", "transgender", "orientation", 
    "sexuality","sexual", "non-binary", "pride","ally","androgynous", "asexual", "closeted", "coming out", "identity", "gender queer", "transition", 
    "homophobia", "intersex", "outing", "pansexual", "questioning", "transphobia"]
overseas_policies_words = ["tariff", "china", "russia", "united nations", "foreign aid", "north korea", "united nations", "iran", "israel", 
    "military spending", "NATO", "afghanistan", "torture", "terrorism", "drone", "", ""]
racial_awareness_words = ["black", "blm", "black lives matter", "racial justice", "racial equality", "race", "defunding", "all lives matter", 
    "body camera", "poc", "antiracist", "cultural appropriation", "bipoc", "equity", "diversity", "inclusion", "insitutionalized", 
    "microagression", "white privilege", "supremacy"]

# environmental_tweets_count = 0
# immigration_tweets_count = 0
# healhtcare_tweets_count = 0
# womens_rights_tweets_count = 0
# lgbtq_rights_tweets_count = 0

users = [
    'Trump',
    'Biden',
    'Obama',
    'Harris',
    'Pence'
]

policies = ['environmental', 'immigration', 'healthcare', 'womens_rights', 'lgbtq', 'overseas_policies', 'racial_awareness']


environmental_count = {}
immigration_count = {}
healthcare_count = {}
womens_rights_count = {}
lgbtq_rights_count = {}
overseas_policies_count = {}
racial_awareness_count = {}

environmental_displayed_tweets = {}
immigration_displayed_tweets = {}
healthcare_displayed_tweets = {}
womens_rights_displayed_tweets = {}
lgbtq_rights_displayed_tweets = {}
overseas_policies_displayed_tweets = {}
racial_awareness_displayed_tweets = {}

trump_tweets = {}
biden_tweets = {}
obama_tweets = {}
harris_tweets = {}
pence_tweets = {}

for x in policies:
    trump_tweets[x] = 0
    biden_tweets[x] = 0
    obama_tweets[x] = 0
    harris_tweets[x] = 0
    pence_tweets[x] = 0


for x in users:
    environmental_count[x] = 0
    immigration_count[x] = 0
    healthcare_count[x] = 0
    womens_rights_count[x] = 0
    lgbtq_rights_count[x] = 0
    overseas_policies_count[x] = 0
    racial_awareness_count[x] = 0

    environmental_displayed_tweets[x] = 0
    immigration_displayed_tweets[x] = 0
    healthcare_displayed_tweets[x] = 0
    womens_rights_displayed_tweets[x] = 0
    lgbtq_rights_displayed_tweets[x] = 0
    overseas_policies_displayed_tweets[x] = 0
    racial_awareness_displayed_tweets[x] = 0


def num_environment_tweets(dataset, environmental_words):
    for list in dataset:
        environmental_tweets_count = 0
        for element in list:

            for y in environmental_words:
                if (y in element.lower()):
                    environmental_tweets_count += 1
        environmental_count[list] = environmental_tweets_count

    return environmental_count

def num_immigration_tweets(dataset, immigration_words):
    for list in dataset:
        immigration_tweets_count = 0
        for element in list:
            for y in immigration_words:
                if (y in element.lower()):
                    immigration_tweets_count += 1
        immigration_count[list] = immigration_tweets_count
    return immigration_count

def num_healthcare_tweets(dataset, healthcare_words):
    for list in dataset:
        healthcare_tweets_count = 0
        for element in list:
            for y in healthcare_words:
                if (y in element.lower()):
                    healthcare_tweets_count += 1
        healthcare_count[list] = healthcare_tweets_count
    return healthcare_count

def num_womens_rights_tweets(dataset, womens_rights_words):
    for list in dataset:
        womens_rights_tweets_count = 0
        for element in list:
            for y in womens_rights_words:
                if (y in element.lower()):
                    womens_rights_tweets_count += 1
        womens_rights_count[list] = womens_rights_tweets_count
    return womens_rights_count
    
def num_lgbtq_rights_tweets(dataset, lgbtq_rights_words):
    for list in dataset:
        lgbtq_rights_tweets_count = 0
        for element in list:
            for y in lgbtq_rights_words:
                if (y in element.lower()):
                    lgbtq_rights_tweets_count += 1
        lgbtq_rights_count[list] = lgbtq_rights_tweets_count
    return lgbtq_rights_count

def num_foreign_policies_tweets(dataset, overseas_policies_words):
    for list in dataset:
        overseas_policies_tweets_count = 0
        for element in list: 
            for y in overseas_policies_words:
                if (y in element.lower()):
                    overseas_policies_tweets_count += 1
        overseas_policies_count[list] = overseas_policies_tweets_count
    return overseas_policies_count

def num_racial_awareness_tweets(dataset, racial_awareness_words):
    for list in dataset:
        racial_awareness_tweets_count = 0
        for element in list: 
            for y in racial_awareness_words:
                if (y in element.lower()):
                    racial_awareness_tweets_count += 1
        racial_awareness_count[list] = racial_awareness_tweets_count
    return racial_awareness_count


#this is displaying the 

