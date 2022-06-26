import spacy
from src.utils import frequency
import math


def get_words_from_document(path):
    with open(path) as file:
        return file.read()


def get_importants_words(text: str):
    en = spacy.load("en_core_web_sm")

    lst = []
    for token in en(text):
        if (
            not token.is_punct
            and not token.is_currency
            and not token.is_digit
            and not token.is_space
            and not token.is_stop
            and not token.like_num
        ):
            lst.append(token)

    return lst


def create_index(index, document, word):
    if word not in index[document]["terms"]:
        index[document]["terms"][word] = {"count": 0}
    index[document]["terms"][word]["count"] += 1


def create_inverse_index(inverse_index, document, word):
    if word in inverse_index:
        if document not in inverse_index[word]["documents"]:
            inverse_index[word]["documents"][document] = 0
    else:
        inverse_index[word] = {"documents": {document: 0}}
    inverse_index[word]["documents"][document] += 1


def check_max_frequency(index, document, word):
    act_freq = frequency(
        index[document]["terms"][word]["count"], index[document]["len"]
    )
    if act_freq > index[document]["max_freq"]:
        index[document]["max_freq"] = act_freq


def create_tf(index, document):
    for term in index[document]["terms"].keys():
        index[document]["terms"][term]["tf"] = frequency(
            index[document]["terms"][term]["count"], index[document]["max_freq"]
        )


def create_idf(inverse_index, N):
    for word in inverse_index.keys():
        inverse_index[word]["idf"] = math.log(
            N / len(inverse_index[word]["documents"].keys())
        )


def create_tf_idf(index, inverse_index):
    for document in index.keys():
        for term in index[document]["terms"].keys():
            index[document]["terms"][term]["tf_idf"] = (
                index[document]["terms"][term]["tf"] * inverse_index[term]["idf"]
            )


def create_index_and_inverse_index(documents, verbose=False):
    index = {}
    inverse_index = {}

    for document in documents:
        try:
            if verbose:
                print("processing document: ", document)

            words = get_importants_words(get_words_from_document(document))

            index[document] = {"len": len(words), "terms": {}, "max_freq": 0}
            for token in words:
                word = token.lemma_.lower()

                # adding to index
                create_index(index, document, word)

                # checking max_frec
                check_max_frequency(index, document, word)

                # adding to inverse_index
                create_inverse_index(inverse_index, document, word)

            create_tf(index, document)

        except Exception as e:
            if verbose:
                print(e)

    create_idf(inverse_index, len(index.keys()))
    create_tf_idf(index, inverse_index)

    return (index, inverse_index)
