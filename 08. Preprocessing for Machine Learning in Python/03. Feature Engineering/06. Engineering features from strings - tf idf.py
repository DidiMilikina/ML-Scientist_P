'''
Engineering features from strings - tf/idf
Let's transform the volunteer dataset's title column into a text vector, to use in a prediction task in the next exercise.

Instructions
100 XP
Store the volunteer["title"] column in a variable named title_text.
Use the tfidf_vec vectorizer's fit_transform() function on title_text to transform the text into a tf-idf vector.
'''
SOLUTION
# Take the title text
title_text = volunteer['title']

# Create the vectorizer method
tfidf_vec = TfidfVectorizer()

# Transform the text into tf-idf vectors
text_tfidf = tfidf_vec.fit_transform(title_text)