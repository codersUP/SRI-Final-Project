from .parse_document import get_importants_words


def create_index_query(query):
    words = get_importants_words(query)

    index = {"len": len(words), "terms": {}}
    for token in words:
        word = token.lemma_.lower()

        # adding to index
        if word not in index["terms"]:
            index["terms"][word] = 0
        index["terms"][word] += 1

    return index
