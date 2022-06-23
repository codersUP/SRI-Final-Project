import json


def frequency(count, len):
    return count / len


def save_index_and_inverse_index(namefile, index, inverse_index):
    with open(namefile, "w") as fp:
        json.dump({"index": index, "inverse_index": inverse_index}, fp)


def load_index_and_inverse_index(namefile):
    with open(namefile) as json_file:
        data = json.load(json_file)

        return (data["index"], data["inverse_index"])
