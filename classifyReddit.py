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
        print(comments[i], predictions[i])

    print('\n')
    print(model)
    printOptions(features)
    print('\n')
    print("FAVOUR: " + str(favorCount))
    print("NEUTRAL: " + str(neutralCount))
    print("AGAINST: " + str(againstCount))

def runClassifiers(modelChoice):

    title, comments = generateSub()
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

    for features in listOfFeatures:
        trainData, trainStances = processData("trainingdata-all-annotations.txt", features)
        redditData = processRedditComments(comments, features)
            #divide this data by breakFileIntoStrings

        if features[3] == True:
            X_train =prepareW2V(model, breakFileIntoStrings('trainingdata-all-annotations.txt')) #godin model takes strings
            X_test = prepareW2V(model, redditData)

        else:
            X_train = vectorizer.fit_transform(trainData)
            X_test = vectorizer.transform(redditData)

        if modelChoice == '1':
            predictions = runBayes(X_train, trainStances, X_test)  # train the classifiers and the test with data
            printDetails(title, comments, predictions, "NAIVE BAYES", features)
            input()

        elif modelChoice == '2':
            predictions = runLogReg(X_train, trainStances, X_test)
            printDetails(title, comments, predictions, "LOGISTIC REGRESSION", features)
            input()

        elif modelChoice == '3':
            predictions = runSVM(X_train, trainStances, X_test)
            printDetails(title, comments, predictions, "SUPPORT VECTOR MACHINE", features)
            input()
