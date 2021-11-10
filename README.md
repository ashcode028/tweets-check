# Tweets-check
Program to check profanity of twitter tweets using Python

## Requirements
- Python 3
- re
- pandas

## How to run 
- fork the repo
- use git clone / download zip file
- open the folder 
- create virtual environment 
- activate the virtual environment
- install the requirments using pip install
- replace the path to csv and txt file according to your environment
- Run the program

## Working
- Read csv as pandas dataframe containing all blocked terms
- convert that into list of words
- Open the text file containing all tweets
- then for each line
  - tokenise the line into words based on words , remove special characters etc
  - then for every word in the token check if its present in blocked terms , then add 1 
  - once u get total count of blocked words in the line , normalise it by no of words in the sentence
  - print that degree of profanity
