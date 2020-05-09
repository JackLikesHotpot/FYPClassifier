from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import sklearn.metrics as metrics


# MULTINOMIAL NAIVE BAYES MODEL
from options import printOptions


def runBayes(X_train, trainStances, X_test):
    model = MultinomialNB()
    model.fit(X_train, trainStances)
    return model.predict(X_test)


def evalBayes(predictions, testStances, features):
    print("Naive Bayes Model")
    print("F1 Score / Accuracy: ", metrics.f1_score(testStances, predictions, average='micro'))
    print("Number of instances correctly determined: ",
          metrics.accuracy_score(testStances, predictions, normalize=False))
    print("Naive Bayes Model")
    printOptions(features)

# LOGISTIC REGRESSION MODEL

def runLogReg(X_train, trainStances, X_test):
    model = LogisticRegression(solver='lbfgs', multi_class='auto')
    model.fit(X_train, trainStances)
    return model.predict(X_test)


def evalLogReg(predictions, testStances, features):
    print("Logistic Regression Model")
    print("Micro F1-score: ", metrics.f1_score(testStances, predictions, average='micro'))
    print("Macro F1-score: ", metrics.f1_score(testStances, predictions, average='macro'))

    print("Number of instances correctly determined: ",
          metrics.accuracy_score(testStances, predictions, normalize=False))
    print("Logistic Regression Model")
    printOptions(features)


# SUPPORT VECTOR MACHINE MODEL

def runSVM(X_train, trainStances, X_test):
    model = SVC(kernel='rbf', C=1, gamma=1)
    model.fit(X_train, trainStances)
    return model.predict(X_test)


def evalSVM(predictions, testStances, features):
    print("Support Vector Machine")
    print("F1 Score / Accuracy: ", metrics.f1_score(testStances, predictions, average='micro'))
    print("Number of instances correctly determined: ",
          metrics.accuracy_score(testStances, predictions, normalize=False))
    
    print("Support Vector Machine")
    printOptions(features)
