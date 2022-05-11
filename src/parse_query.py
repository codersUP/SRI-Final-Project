from .parse_document import get_importants_words


def create_inverse_index_query(query):
    words = get_importants_words(query)

    inverse_index = {"len": len(words), "terms": {}}
    for token in words:
        word = token.lemma_.lower()

        # adding to inverse_index
        if word not in inverse_index:
            inverse_index["terms"][word] = 0
        inverse_index["terms"][word] += 1

    return inverse_index
