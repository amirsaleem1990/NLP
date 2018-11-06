def lower_stem_punctuation_HTML_storwords(column):
    import re
    import nltk
    from nltk.corpus import stopwords 
    
    temp =[]
    snow = nltk.stem.SnowballStemmer('english')
    for sentence in column:
        sentence = sentence.lower()                 # Converting to lowercase
        cleanr = re.compile('<.*?>')
        sentence = re.sub(cleanr, ' ', sentence)        #Removing HTML tags
        sentence = re.sub(r'[?|!|\'|"|#]',r'',sentence)
        sentence = re.sub(r'[.|,|)|(|\|/]',r' ',sentence)        #Removing Punctuations

        words = [snow.stem(word) for word in sentence.split() if word not in stopwords.words('english')]   # Stemming and removing stopwords
        temp.append(' '.join(words))
    return temp

final_X = lower_stem_punctuation_HTML_storwords(final_X)