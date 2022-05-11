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


def create_index(documents, verbose=False):
    index = {}
    inverse_index = {}

    for document in documents:
        if verbose:
            print("processing document: ", document)

        words = get_importants_words(get_words_from_document(document))

        index[document] = {"len": len(words), "terms": {}}
        for token in words:
            word = token.lemma_.lower()

            # adding to index
            if word not in index[document]["terms"]:
                index[document]["terms"][word] = 0
            index[document]["terms"][word] += 1

            # adding to inverse_index
            if word in inverse_index:
                if document not in inverse_index[word]:
                    inverse_index[word][document] = 0
            else:
                inverse_index[word] = {document: 0}
            inverse_index[word][document] += 1

    return (index, inverse_index)
