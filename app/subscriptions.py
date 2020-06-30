'''
    This module is used to process user's subscriptions
    It searches for keywords in raw text and compares them
    with the keys dictionary.

'''

from tokenizer import tokenize

# TODO: Maybe we should add some nice
# and clean way to parse dicts?

def exact_search(raw):
    pass

def best_matches(raw):
    pass

def process(raw):
    
    # Here we set the number of
    # probable occupations we want to return
    filtered_amount = 3

    title = raw[0]
    status = raw[1]
    desc = raw[2]

    # Search for exact matches in
    # occupations list
    exact_matches = exact_search(title)
    if exact_matches:
        # If found, we should add it as
        # the most valuable match.
        pass

    tokens = tokenize(raw)
    best_matches = find_tags_matches(tokens)
    best_matches = best_matches[:filtered_amount]

    return tokens


