import gensim
from gensim.models import Word2Vec
import numpy as np


def prepareW2V(model, data):                                    # code to produce a mean vector for the model and a tweet
    p = []
    for tweet in data:
        p.append(get_mean_vector(model, tweet))
    return p


def get_mean_vector(word2vec_model, words):                     # mean vector of the embeddings
    words = [word for word in words if word in word2vec_model.wv.vocab]
    if len(words) >= 1:
        return np.mean(word2vec_model[words], axis=0)
    else:
        return []
