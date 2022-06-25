import math
from .utils import frequency


def find_terms_in_query_and_document(query_terms, document_terms):
    ret = []

    for term_q in query_terms.keys():
        if term_q in document_terms:
            ret.append(term_q)

    return ret


def rank_query_document(query_index, document_features):
    query_len = query_index["len"]
    if query_len == 0:
        return 0
    query_terms = query_index["terms"]

    document_len = document_features["len"]
    document_terms = document_features["terms"]

    common_terms = find_terms_in_query_and_document(query_terms, document_terms)

    num = 0
    for term in common_terms:
        num += frequency(query_terms[term], query_len) * frequency(
            document_terms[term], document_len
        )

    dem_1 = math.sqrt(
        sum([frequency(value, query_len) ** 2 for value in query_terms.values()])
    )
    dem_2 = math.sqrt(
        sum([frequency(value, query_len) ** 2 for value in document_terms.values()])
    )

    return num / (dem_1 * dem_2)


def calculate_rank(query_index, index, rank_N):
    rank = []

    for document, document_features in index.items():

        rank.append((rank_query_document(query_index, document_features), document))

    rank.sort(reverse=True)

    return rank[:rank_N]
