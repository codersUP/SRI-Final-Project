from fuzzywuzzy import process

from src.vectorial.parse_document import get_importants_words


def expand_query(query_index, inverse_index):
    expanded = {}

    documents_terms = list(inverse_index.keys())

    for term in query_index["terms"]:
        if query_index["terms"][term]["tf_idf"] == 0:
            expanded[term] = process.extractOne(term, documents_terms)[0]

    return expanded


def replace_expand_in_query(query, expanded):
    query_splited = query.split()

    words = get_importants_words(query)

    result = []

    for token in words:
        word = token.lemma_.lower()

        if word in expanded:
            query_splited[query_splited.index(str(token))] = expanded[word]

    return " ".join(query_splited)
