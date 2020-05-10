from classifyReddit import runClassifiers
from classifyTestData import validate
from gensim.models.keyedvectors import KeyedVectors


def main():
    choice = ""
    try:                                                                        # test if files exist
        f = open('word2vec_twitter_tokens.bin')
        f.close()
        f = open('trainingdata-all-annotations.txt')
        f.close()
        f = open('testdata-taskA-all-annotations.txt')
        f.close()
    except FileNotFoundError:                                                   # if not, print message and return
        print("Unable to find the datasets or the word2vec bin file in the directory. Please check if they exist.")
        return
    
    try:                                                                        # test if the model in .txt form exists
        f = open('word2vec_twitter_tokens.txt')
        f.close()
    except FileNotFoundError:                                                   # else load the file
        print("Pre-loading w2v model! Can take 15 minutes to 1 hour.")          # CAN TAKE UP TO AN HOUR
        print("Press Enter to continue when a txt file of 14GB file with the same name.")
        model = KeyedVectors.load_word2vec_format('word2vec_twitter_tokens.bin', binary=True, unicode_errors='ignore')
        model.save_word2vec_format('word2vec_twitter_tokens.txt', binary=False) # save into same directory for easier access
    
    models = ['Naive Bayes', 'Logistic Regression', 'Support Vector Machine']

    for i in range(len(models)):                        
        print(str(i+1) + ') ' + models[i])                                      # print options 
    while choice < '1' or choice > '3':
        choice = input("Choose a model with numbers.")
    validate(choice)                                                            # train + validate
    print("Validation completed! Onto testing...")     
    runClassifiers(choice)                                                      # run reddit data

if __name__ == "__main__":
    main()
