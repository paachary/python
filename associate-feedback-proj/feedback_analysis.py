import nltk
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

#nltk.download()

train = [
     ('Hackathon should be organized', 'neg'),
     ('Need Wellness center.', 'neg'),
     ('Need More recreational places.', 'neg'),
     ('No exit interview for folks leaving the firm.', 'neg'),
     ('Good work life balance.', 'pos'),
     ('More external trainings can be conducted for latest technologies.', 'neg')
]
cl = NaiveBayesClassifier(train)
cl.classify("Good work life balance.")
'pos'

filename = "associate-data"

strs = []

with open(filename) as fn:
    for line in fn:
        description = line.strip()
        blob = TextBlob(description , classifier=cl)
        for s in blob.sentences:
            if ( s.classify() == 'neg' ):
                #print(str(s))
                strs.append(str(s))       

words = ' '.join(strs)
cleaned_word = " ".join([word for word in words.split()
                        if 'http' not in word
                            and not word.startswith('@')
                            and not word.startswith('#')
                            and word != 'RT'
                        ])
wordcloud = WordCloud(stopwords=STOPWORDS,
                  background_color='black',
                  width=2500,
                  height=2000
                 ).generate(cleaned_word)
plt.figure(1,figsize=(13, 13))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

