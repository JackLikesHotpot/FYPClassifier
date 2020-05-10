# Testing phase.
# With a given model go through the following:
# Model name, features, Reddit submission title, comments, their stance, distribution of stances, and features used.

from generateSubmission import generateSub
from loadGodinModel import loadGodin
from options import processRedditComments, processData
from prepareW2V import prepareW2V
from models import *

from sklearn.feature_extraction.text import TfidfVectorizer

from readProcessFiles import breakFileIntoStrings


def printDetails(title, comments, predictions, model, features):
    favorCount = 0
    againstCount = 0
    neutralCount = 0

    print(model)
    print('\n')
    print(title)
    print('--------------------------------------------------------------------------')
    print("Total: " + str(len(comments)) + " comments. \n")

    for i in range(len(comments)):

        if predictions[i] == 'FAVOR':
            favorCount += 1
        elif predictions[i] == 'AGAINST':
            againstCount += 1
        else:
            neutralCount += 1

        print('\n')
        print(comments[i], predictions[i])                      # print each comment followed by a predicted stance

    print('\n')
    print(model)                                                # print model name
    printOptions(features)                                      # print the features used
    print('\n')
    print("FAVOUR: " + str(favorCount))                         # print the distribution of songs in each class
    print("NEUTRAL: " + str(neutralCount))
    print("AGAINST: " + str(againstCount))

def runClassifiers(modelChoice):                                # Go through each combination of features and print out the results.

    title, comments = generateSub()                             # Get the submission's title and comments
    model = loadGodin()

    vectorizer = TfidfVectorizer()
    listOfFeatures = ([False, False, False, True],
                     [False, False, True, False],
                     [False, True, False, False],
                     [True, False, False, False],
                     [True, False, True, False],
                     [False, True, True, False],
                     [True, True, False, False],
                     [True, True, True, False])

    for features in listOfFeatures:                                         # for each combinations of features, train and test models
        trainData, trainStances = processData("trainingdata-all-annotations.txt", features)
        redditData = processRedditComments(comments, features)
            #divide this data by breakFileIntoStrings

        if features[3] == True:                                             # if embeddings used, prepare w2v model instead
            X_train =prepareW2V(model, breakFileIntoStrings('trainingdata-all-annotations.txt')) 
            X_test = prepareW2V(model, redditData)

        else:                                                               # otherwise do not
            X_train = vectorizer.fit_transform(trainData)
            X_test = vectorizer.transform(redditData)

        if modelChoice == '1':                                              # if naive bayes then train naive bayes and print details
            predictions = runBayes(X_train, trainStances, X_test)  # train the classifiers and the test with data
            printDetails(title, comments, predictions, "NAIVE BAYES", features)
            input()

        elif modelChoice == '2':                                            # if log reg then train log reg and print details
            predictions = runLogReg(X_train, trainStances, X_test)
            printDetails(title, comments, predictions, "LOGISTIC REGRESSION", features)
            input()

        elif modelChoice == '3':                                            # if svm then train svm and print details
            predictions = runSVM(X_train, trainStances, X_test)
            printDetails(title, comments, predictions, "SUPPORT VECTOR MACHINE", features)
            input()
