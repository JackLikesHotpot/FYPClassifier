from sklearn.feature_extraction.text import TfidfVectorizer


# Runs tests on the training/testing datasets provided.

from loadGodinModel import loadGodin
from models import *
from options import processData
from prepareW2V import prepareW2V
from readProcessFiles import breakFileIntoStrings


def validate(modelChoice):

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
        testData, testStances = processData("testdata-taskA-all-annotations.txt", features)

        if features[3] == True:
            X_train =prepareW2V(model, breakFileIntoStrings('trainingdata-all-annotations.txt')) #godin model takes strings
            X_test = prepareW2V(model, breakFileIntoStrings('testdata-taskA-all-annotations.txt'))

        else:
            X_train = vectorizer.fit_transform(trainData)
            X_test = vectorizer.transform(testData)

        if modelChoice == '1':
            bayesPred = runBayes(X_train, trainStances, X_test)
            evalBayes(bayesPred, testStances, features)
            print()

        elif modelChoice == '2':
            logRegPred = runLogReg(X_train, trainStances, X_test)
            evalLogReg(logRegPred, testStances, features)
            print()

        elif modelChoice == '3':
            svmPred = runSVM(X_train, trainStances, X_test)
            evalSVM(svmPred, testStances, features)
            print()