def readFile(file):
    tweetList = []                                              # open the datasets, divide by tab and add to tweetList

    with open(file) as f:
        for line in f:
            if line.split('\t')[0] != 'ID':
                tweet = line.split('\t')
                tweetList.append(tweet[2])
        return tweetList


def breakFileIntoStrings(file):  # divides file of strings into individual words
    return removeNestings(readFile(file))

def breakArray(arr):                                            # break and array into separate words
    arrayString = []
    for string in arr:
        words = string.split(' ')
        for word in words:
            arrayString.append(word)
    return arrayString

def breakArrayIntoStrings(arr):                                 # breaks and array into strings
    return removeNestings(breakArray(arr))

def removeNestings(lis):                                        # removes the nestings on strings
    tweets = []

    for i in range(len(lis)):
        tweets.append(lis[i])
    return tweets
