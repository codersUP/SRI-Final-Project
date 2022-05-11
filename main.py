import json
from pprint import pprint

from src.parse_query import create_inverse_index_query
from src.parse_directory import get_files_from_path_list
from src.parse_document import create_index
from src.vectorial_model import calculate_rank


def main():
    f = open("files_path.json")
    json_files_path = json.load(f)

    files = get_files_from_path_list(json_files_path["paths"])
    index, inverse_index = create_index(files[:10], verbose=True)

    while True:
        query = input("query: ")

        query_inverse_index = create_inverse_index_query(query)

        result = calculate_rank(query_inverse_index, index, 3)

        pprint(result)


if __name__ == "__main__":
    main()
