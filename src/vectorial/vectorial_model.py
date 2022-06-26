from src.utils import frequency


def find_terms_in_query_and_document(query_terms, document_terms):
    ret = []

    for term_q in query_terms.keys():
        if term_q in document_terms:
            ret.append(term_q)

    return ret


def rank_query_document(query_index, document_features):
    if query_index["weight"] == 0 or document_features["weight"] == 0:
        return 0

    query_terms = query_index["terms"]
    document_terms = document_features["terms"]

    common_terms = find_terms_in_query_and_document(query_terms, document_terms)

    num = 0
    for term in common_terms:
        num += query_terms[term]["tf_idf"] * document_terms[term]["tf_idf"]

    return num / (document_features["weight"] * query_index["weight"])


def calculate_rank(query_index, index, rank_N):
    rank = []

    for document, document_features in index.items():

        rank.append((rank_query_document(query_index, document_features), document))

    rank.sort(reverse=True)

    return rank[:rank_N]
