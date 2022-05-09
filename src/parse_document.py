import spacy


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
