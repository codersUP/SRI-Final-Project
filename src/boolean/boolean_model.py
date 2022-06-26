from src.boolean.query_parser import get_parser
from src.boolean.query_lexer import get_lexer


def get_documents(query, inverse_index, documents):
    lexer = get_lexer()
    parser = get_parser()

    boolean_expression_dict = parser.parse(query)

    return calculate_set(boolean_expression_dict, inverse_index, documents)


def calculate_set(boolean_expression_dict, inverse_index, documents):
    if boolean_expression_dict["type"] == "TERM":
        try:
            return set(inverse_index[boolean_expression_dict["word"]]["documents"].keys())
        except KeyError:
            return set()

    if boolean_expression_dict["type"] == "EXPR":
        if boolean_expression_dict["func"] == "AND":
            return calculate_set(
                boolean_expression_dict["childrens"][0], inverse_index, documents
            ).intersection(
                calculate_set(
                    boolean_expression_dict["childrens"][1], inverse_index, documents
                )
            )

        if boolean_expression_dict["func"] == "OR":
            return calculate_set(
                boolean_expression_dict["childrens"][0], inverse_index, documents
            ).union(
                calculate_set(
                    boolean_expression_dict["childrens"][1], inverse_index, documents
                )
            )

        if boolean_expression_dict["func"] == "TERM":
            return calculate_set(
                boolean_expression_dict["childrens"][0], inverse_index, documents
            )

        if boolean_expression_dict["func"] == "PAREN":
            return calculate_set(
                boolean_expression_dict["childrens"][0], inverse_index, documents
            )

        if boolean_expression_dict["func"] in ["NOT", "NOTPAREN"]:
            return documents.difference(
                calculate_set(
                    boolean_expression_dict["childrens"][0], inverse_index, documents
                )
            )

    # never reach this
    assert 1 == 0
