import json
from pprint import pprint

from src.parse_directory import get_files_from_path_list
from src.parse_document import get_importants_words, get_words_from_document


def main():
    f = open("files_path.json")
    json_files_path = json.load(f)

    files = get_files_from_path_list(json_files_path["paths"])

    inverse_index = {}
    for file in files:
        print("processing file: ", file)

        words = get_importants_words(get_words_from_document(file))
        for token in words:
            word = token.lemma_.lower()
            if word in inverse_index:
                if file not in inverse_index[word]:
                    inverse_index[word][file] = 0
            else:
                inverse_index[word] = {file: 0}

            inverse_index[word][file] += 1

        print(len(inverse_index.keys()))


if __name__ == "__main__":
    main()
