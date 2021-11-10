import re
import pandas as pd


def tokenize(text):
    return re.findall(r'\w+', text)


bad_words = pd.read_csv("/home/ashita/PycharmProjects/Profanity_check/Terms-to-Block.csv")
list_of_bad_words = bad_words.iloc[3:, 1].str.replace(',','').astype(str).values.tolist()
tweets = "/home/ashita/PycharmProjects/Profanity_check/tweets.txt"
with open(tweets) as quotes:
    for line in quotes:  # parse it line by line
        line=line.lower()
        tokens = tokenize(line)
        # Rate: number of occurrences normalized by total number
        degree_of_profanity = sum(1 for t in tokens if t in list_of_bad_words) / len(tokens)
        print(degree_of_profanity)
