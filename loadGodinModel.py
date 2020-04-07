from gensim.models.keyedvectors import KeyedVectors

def loadGodin():
    print("Loading w2v model! Will take a while...")
    gModel = KeyedVectors.load_word2vec_format('word2vec_twitter_tokens.txt', binary = True, unicode_errors='ignore')
    return gModel