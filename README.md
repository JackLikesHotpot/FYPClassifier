# FYPClassifier
Stance classifier for my final year project.

REQUIREMENTS:

> Dataset used were the Task A train + test datasets of Mohammed et al (2016), which can be found here:
http://www.saifmohammad.com/WebPages/StanceDataset.htm

> The Word2Vec model needed for the word embedding classification can be found here:
https://github.com/FredericGodin/TwitterEmbeddings

**The `trainingdata-all-annotations` and `testdata-taskA-all-annotations` txt files from the full Stance Dataset are required to run this code.**

**Place these 2 txt files and the `word2vec_twitter_tokens.bin` file in the same directory.**

With a chosen terminal, run the main function with the command `python main.py`.

When prompted, you can choose a model with numbers:

> 1 (Naive Bayes)

> 2 (Logistic Regression)

> 3 (Support Vector Machine)

The training/testing results for all combinations of models will be outputted after a while.

Training/validation results are automatically outputted, while with testing results, you can press Enter after every post of class distribution to go to the next feature.

# References

Mohammad, S., Kiritchenko, S., Sobhani, P., Zhu, X. and Cherry, C. (2019). SemEval-2016 Task 6: Proceedings of the International Workshop on Semantic Evaluation (SemEval-2016), San Diego, California, 2016.

Godin, F. (2019). Improving And Interpreting Neural Networks For Word-Level Prediction Tasks In Natural Language Processing. 1st ed. Ghent: UGent - Faculty of Engineering and Architecture.
