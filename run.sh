#!/usr/bash

chmod a+x ./src/average_degree.py
chmod a+x ./src/tweets_cleaned.py

# open tweets cleaning program    Input file                outputFile
python ./src/tweets_cleaned.py ./tweet_input/tweets.txt ./tweet_output/ft2.txt

# open average degree count program
python ./src/average_degree.py ./tweet_input/tweets.txt ./tweet_output/ft2.txt

    
