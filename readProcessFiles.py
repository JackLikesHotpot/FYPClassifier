def readFile(file):
    tweetList = []

    with open(file) as f:
        for line in f:
            if line.split('\t')[0] != 'ID':
                tweet = line.split('\t')
                tweetList.append(tweet[2])
        return tweetList


def breakFileIntoStrings(file):  # divides file of strings into individual words
    return removeNestings(readFile(file))

def breakArray(arr):
    arrayString = []
    for string in arr:
        words = string.split(' ')
        for word in words:
            arrayString.append(word)
    return arrayString

def breakArrayIntoStrings(arr):
    return removeNestings(breakArray(arr))

def removeNestings(lis):
    tweets = []

    for i in range(len(lis)):
        tweets.append(lis[i])
    return tweets
