from classifyReddit import runClassifiers
from classifyTestData import validate
from gensim.models.keyedvectors import KeyedVectors


def main():
    choice = ""
    try:
        f = open('word2vec_twitter_tokens.bin')
        f.close()
        f = open('trainingdata-all-annotations.txt')
        f.close()
        f = open('testdata-taskA-all-annotations.txt')
        f.close()
    except FileNotFoundError:
        print("Unable to find the datasets or the word2vec bin file in the directory. Please check if they exist.")
        return
    
    try:
        f = open('word2vec_twitter_tokens.txt')
        f.close()
    except FileNotFoundError:
        print("Pre-loading w2v model! Will take 15-20 mins...")
        model = KeyedVectors.load_word2vec_format('word2vec_twitter_tokens.bin', binary=True, unicode_errors='ignore')
        model.save_word2vec_format('word2vec_twitter_tokens.txt', binary=False)

    models = ['Naive Bayes', 'Logistic Regression', 'Support Vector Machine']

    for i in range(len(models)):
        print(str(i+1) + ') ' + models[i])
    while choice < '1' or choice > '3':
        choice = input("Choose a model with numbers.")
    validate(choice)
    print("Validation completed! Onto testing...")
    runClassifiers(choice)

if __name__ == "__main__":
    main()
