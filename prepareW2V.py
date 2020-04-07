import gensim
from gensim.models import Word2Vec
import numpy as np


def prepareW2V(model, data):
    p = []
    for tweet in data:
        p.append(get_mean_vector(model, tweet))
    return p


def get_mean_vector(word2vec_model, words):
    words = [word for word in words if word in word2vec_model.wv.vocab]
    if len(words) >= 1:
        return np.mean(word2vec_model[words], axis=0)
    else:
        return []
