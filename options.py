from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def removeStopWords(tweet):
    result = []
    stopWords = set(stopwords.words('english'))
    for word in tweet.split(' '):
        if word not in stopWords:
            result.append(word)
    return (' '.join(result))


def lemmatizeTweet(tweet):
    result = []
    lemmatizer = WordNetLemmatizer()
    for word in tweet.split(' '):
        result.append(lemmatizer.lemmatize(word.lower()))
    return (' '.join(result))


def removeNoise(tweet):
    noise = ["RT", "#", "@", "rt"]
    newTweet = []

    for i in tweet.split(' '):
        if noise[0] != i and noise[1] not in i and noise[2] not in i and noise[3] not in i:
            newTweet.append(i)
    return (' '.join(newTweet))


def printOptions(features):
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
        outputString = ', '.join(output)
    else:
        outputString = 'None'
    print("Features used: " + outputString)


def processData(file, options):
    tData = []
    tStances = []

    with open(file) as f:
        for line in f:
            if line.split('\t')[2] != 'Tweet':
                tStances.append(line.split('\t')[3])
                tData.append(line.split('\t')[2])

        for i in range(len(tData)):
            if options[0]:
                tData[i] = removeStopWords(tData[i])

            if options[1]:
                tData[i] = lemmatizeTweet(tData[i])

            if options[2]:
                tData[i] = removeNoise(tData[i])

    return tData, tStances


def processRedditComments(comments, options):
    redditData = []
    for i in comments:
        redditData.append(i)

    for i in range(len(redditData)):
        if options[0]:
            redditData[i] = removeStopWords(redditData[i])

        if options[1]:
            redditData[i] = lemmatizeTweet(redditData[i])

        if options[2]:
            redditData[i] = removeNoise(redditData[i])

    return redditData
