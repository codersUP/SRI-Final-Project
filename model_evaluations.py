import json
from pprint import pprint
from src.constants import A
from src.boolean.boolean_model import get_documents
from src.parse_directory import get_files_from_path_list
from src.vectorial.parse_document import create_index_and_inverse_index
from src.utils import load_index_and_inverse_index, save_index_and_inverse_index
from src.vectorial.parse_query import create_index_query
from src.vectorial.vectorial_model import calculate_rank
import ir_datasets


def extract_querys(dateset_name):
    dataset = ir_datasets.load(dateset_name)

    querys = {}
    for query in dataset.queries_iter():
        querys[query[0]] = {"text": query[1], "documents": []}

    for qrel in dataset.qrels_iter():
        if qrel[0] in querys:
            if qrel[2] > 0:
                querys[qrel[0]]["documents"].append(qrel[1])

    return querys


def get_id_of_document_path(document_path):
    return document_path.split("/")[-1].split(".")[0]


def model_evaluation(dataset_name, beta, model_function, ranks, **kwargs):
    max_rank = max(ranks)

    index, inverse_index = load_index_and_inverse_index(f"results_{dataset_name}.json")
    kwargs["index"] = index
    kwargs["inverse_index"] = inverse_index
    kwargs["rank_amount"] = max_rank

    results = {}
    for rank in ranks:
        results[rank] = {"P": 0, "R": 0, "F": 0, "F1": 0}

    querys = extract_querys(dataset_name)

    for query_id in querys.keys():
        query = querys[query_id]["text"]
        valid_documents = querys[query_id]["documents"]

        result = model_function(query, **kwargs)

        for rank in ranks:
            RR = 0
            for doc in result[:rank]:
                doc_id = get_id_of_document_path(doc)

                if doc_id in valid_documents:
                    RR += 1

            if RR == 0:
                continue

            P = RR / len(result)
            R = RR / len(valid_documents)
            F = ((1 + beta**2) * P * R) / (beta**2 * P + R)
            F1 = (2 * P * R) / (P + R)

            results[rank]["P"] += P
            results[rank]["R"] += R
            results[rank]["F"] += F
            results[rank]["F1"] += F1

    for rank in ranks:
        results[rank]["P"] /= len(querys.keys())
        results[rank]["R"] /= len(querys.keys())
        results[rank]["F"] /= len(querys.keys())
        results[rank]["F1"] /= len(querys.keys())

    return results


def vectorial_evaluations(query, A, index, inverse_index, rank_amount):
    query_index = create_index_query(query, A, inverse_index)
    result = calculate_rank(query_index, index, rank_amount)

    return list(map(lambda x: x[1], result))


def boolean_evaluation(query, index, inverse_index, rank_amount):
    query_to_low = query.lower()
    query_single_space = " ".join(query_to_low.split())
    query_fixed = query_single_space.replace("\n", "").replace(" ", " AND ")

    result = list(get_documents(query_fixed, inverse_index, set(index.keys())))

    return result[:rank_amount]


def save_results(dataset_name_path):
    for dataset_name, dataset_path in dataset_name_path:
        files = get_files_from_path_list([dataset_path])
        index, inverse_index = create_index_and_inverse_index(files, verbose=True)

        save_index_and_inverse_index(
            f"results_{dataset_name}.json", index=index, inverse_index=inverse_index
        )


def main():
    result = {}

    beta = 0.5

    # cranfield = ("cranfield", "Test Collections/Cran/documents")
    # vaswani = ("vaswani", "Test Collections/Vaswani/documents")
    # save_results([cranfield, vaswani])

    # cranfield vectorial
    result["cranfield_vectorial"] = model_evaluation(
        dataset_name="cranfield",
        beta=beta,
        model_function=vectorial_evaluations,
        A=A,
        ranks=[10, 50, 100],
    )
    with open(
        "models_comparatives_results/cranfield_vectorial_results.json", "w"
    ) as fp:
        json.dump(result["cranfield_vectorial"], fp)
    print("cranfield_vectorial done")

    # vaswani vectorial
    result["vaswani_vectorial"] = model_evaluation(
        dataset_name="vaswani",
        beta=beta,
        model_function=vectorial_evaluations,
        A=A,
        ranks=[10, 50, 100],
    )
    with open("models_comparatives_results/vaswani_vectorial_results.json", "w") as fp:
        json.dump(result["vaswani_vectorial"], fp)
    print("vaswani_vectorial done")

    # cranfield boolean
    result["cranfield_boolean"] = model_evaluation(
        dataset_name="cranfield",
        beta=beta,
        model_function=boolean_evaluation,
        ranks=[10, 50, 100],
    )
    with open("models_comparatives_results/cranfield_boolean_results.json", "w") as fp:
        json.dump(result["cranfield_boolean"], fp)
    print("cranfield_boolean done")

    # vaswani boolean
    result["vaswani_boolean"] = model_evaluation(
        dataset_name="vaswani",
        beta=beta,
        model_function=boolean_evaluation,
        ranks=[10, 50, 100],
    )
    with open("models_comparatives_results/vaswani_boolean_results.json", "w") as fp:
        json.dump(result["vaswani_boolean"], fp)
    print("vaswani_boolean done")

    with open("models_comparatives_results/model_evaluation_results.json", "w") as fp:
        json.dump(result, fp)


if __name__ == "__main__":
    main()
