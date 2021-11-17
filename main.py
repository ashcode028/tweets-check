import re
import pandas as pd


def tokenize(text):
    return re.findall(r'\w+', text)


def profanity_check(blocked_words, tweets):
    with open(tweets) as quotes:  # open file
        for line in quotes:  # parse it line by line
            line = line.lower()
            tokens = tokenize(line)
            # print(tokens)
            # Rate: number of occurrences normalized by total number
            degree_of_profanity = sum(1 for t in tokens if t in blocked_words) / len(tokens)
            print(degree_of_profanity)


if __name__ == "__main__":
    # bad_words="Terms-to-Block.csv"
    # tweets = "tweets.txt"

    # Take input files from user
    bad_words = pd.read_csv(input("Enter full path to the file containing list of blocked words"))
    tweet_list = input("Enter full path to the file containing list of blocked words")

    # convert the words in txt into list
    list_of_bad_words = bad_words.iloc[3:, 1].str.replace(',', '').astype(str).values.tolist()
    profanity_check(list_of_bad_words, tweet_list)
