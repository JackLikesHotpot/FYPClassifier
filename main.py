from classifyReddit import runClassifiers
from classifyTestData import validate


def main():
    choice = ""
    models = ['Naive Bayes', 'Logistic Regression', 'Support Vector Machine']

    for i in range(len(models)):
        print(str(i+1) + ') ' + models[i])
    while choice < '1' or choice > '3':
        choice = input("Choose a model with numbers.")
    validate(choice) #########
    print("Validation completed! Onto testing...")
    runClassifiers(choice) #########


main()