from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def removeStopWords(tweet):                                     # remove commonly occurring english words 
    result = []
    stopWords = set(stopwords.words('english'))
    for word in tweet.split(' '):                               # divide each word in a sentence and remove stopwords
        if word not in stopWords:  
            result.append(word)                                 # put remaining words together
    return (' '.join(result))


def lemmatizeTweet(tweet):                                      # lemmatize - reduce words to their base form
    result = []
    lemmatizer = WordNetLemmatizer()
    for word in tweet.split(' '):                               # split and put them together
        result.append(lemmatizer.lemmatize(word.lower()))
    return (' '.join(result))


def removeNoise(tweet):                                         # remove twitter noise
    noise = ["RT", "#", "@", "rt"]
    newTweet = []

    for i in tweet.split(' '):                                  # divide words and check for noise; add to list
        if noise[0] != i and noise[1] not in i and noise[2] not in i and noise[3] not in i:
            newTweet.append(i)
    return (' '.join(newTweet))


def printOptions(features):                                         # print features based on what is true in the array
    output = []
    if features[0] == True:
        output.append('Stopwords removed')
    if features[1] == True:
        output.append('Lemmatization applied')
    if features[2] == True:
        output.append('Twitter noise removed')
    if features[3] == True:
        output.append('Using word embeddings')

    if output != []:
        outputString = ', '.join(output)                            # join feature strings together into a string 
    else:
        outputString = 'None'                                       # otherwise display none
    print("Features used: " + outputString)


def processData(file, options):
    tData = []
    tStances = []                                                   # arrays for training

    with open(file) as f:
        for line in f:
            if line.split('\t')[2] != 'Tweet':
                tStances.append(line.split('\t')[3])                # add training data
                tData.append(line.split('\t')[2])

        for i in range(len(tData)):                                 # remove features accordingly
            if options[0]:
                tData[i] = removeStopWords(tData[i])

            if options[1]:
                tData[i] = lemmatizeTweet(tData[i])

            if options[2]:
                tData[i] = removeNoise(tData[i])

    return tData, tStances


def processRedditComments(comments, options):                           # remove the same features for reddit data
    redditData = []
    for i in comments:
        redditData.append(i)                                            # add comments to redditData 

    for i in range(len(redditData)):
        if options[0]:
            redditData[i] = removeStopWords(redditData[i])

        if options[1]:
            redditData[i] = lemmatizeTweet(redditData[i])

        if options[2]:
            redditData[i] = removeNoise(redditData[i])

    return redditData
