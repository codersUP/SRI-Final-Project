import json
from pprint import pprint

from src.parse_query import create_index_query
from src.parse_directory import get_files_from_path_list
from src.parse_document import create_index
from src.vectorial_model import calculate_rank
from src.utils import load_index_and_inverse_index, save_index_and_inverse_index
from src.boolean.boolean_model import get_documents


def main():
    f = open("files_path.json")
    json_files_path = json.load(f)

    files = get_files_from_path_list(json_files_path["paths"])
    index, inverse_index = create_index(files[:10], verbose=True)

    save_index_and_inverse_index(
        "results.json", index=index, inverse_index=inverse_index
    )

    index, inverse_index = load_index_and_inverse_index("results.json")

    while True:
        # -----Vectorial-----------------
        query = input("query: ")

        query_index = create_index_query(query)

        result = calculate_rank(query_index, index, 3)

        pprint(result)

        # ------Boolean------------------

        query = input("boolean query: ")

        result = get_documents(query, inverse_index, set(index.keys()))

        pprint(result)


if __name__ == "__main__":
    main()
