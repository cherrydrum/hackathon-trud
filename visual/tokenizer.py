import pymorphy2
import re

def tokenize(text):
    # List of allowed POS, others won't be included
    # in the final set.
    allowedPOS = ['NOUN', 'VERB']
    
    morpher = pymorphy2.MorphAnalyzer()
    
    text = re.sub(r'[^а-я0-9 ]', ' ', text.lower())
    while '  ' in text:
        text = text.replace('  ', ' ')
    words = (word.lower() for word in text.split())
    
    result = []
    for word in words:

        word = morpher.parse(word)[0]

        if word.tag.POS in allowedPOS:

            normal = word.normal_form

            # Preventing duplicates.
            if normal not in result:
                result.append(word.normal_form)

    return tuple(result)