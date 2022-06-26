import math
from src.utils import frequency
from src.parse_document import get_importants_words


def check_max_frequency(index, word):
    act_freq = frequency(index["terms"][word]["count"], index["len"])
    if act_freq > index["max_freq"]:
        index["max_freq"] = act_freq


def create_tf(index):
    for term in index["terms"].keys():
        index["terms"][term]["tf"] = frequency(
            index["terms"][term]["count"], index["max_freq"]
        )


def create_tf_idf(index, a, document_inverse_index):
    for term in index["terms"].keys():
        if term in document_inverse_index:
            index["terms"][term]["tf_idf"] = (
                a + (1 - a) * index["terms"][term]["tf"]
            ) * document_inverse_index[term]["idf"]
        else:
            index["terms"][term]["tf_idf"] = 0


def create_weight_of_query(index):
    sum = 0
    for term in index["terms"].keys():
        sum += index["terms"][term]["tf_idf"] ** 2
    index["weight"] = math.sqrt(sum)


def create_index_query(query, a, document_inverse_index):
    words = get_importants_words(query)

    index = {"len": len(words), "terms": {}, "max_freq": 0}
    for token in words:
        word = token.lemma_.lower()

        # adding to index
        if word not in index["terms"]:
            index["terms"][word] = {"count": 0}
        index["terms"][word]["count"] += 1

        # checking max frequency
        check_max_frequency(index, word)

    create_tf(index)
    create_tf_idf(index, a, document_inverse_index)
    create_weight_of_query(index)

    return index
