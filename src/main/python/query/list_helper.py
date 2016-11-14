import operator
from math import log10

K1_VALUE = float(0.5)
B_VALUE = float(0.5)


def merge_lists(lists):
    """
    Merge the specified lists (OR of a set).
    :param lists: the lists to be merged.
    :return: a list that is the result of merging the specified lists.
    """
    if lists:
        return sorted(set.union(*[set(l) for l in lists]))
        # TODO order by number of matching terms
    else:
        return list()


def intersect_lists(lists):
    """
    Intersect the specified lists (AND of a set).
    :param lists: the lists to be intersected.
    :return: a list that is the result of intersecting the specified lists.
    """
    if lists:
        return sorted(set.intersection(*[set(l) for l in lists]))
    else:
        return list()


def rank_results(keywords, query_terms_info, results_list, collection_info, docset_info):
    """
    Return a ranked list of results based on all the collection input info.
    :param keywords: the keywords in the query.
    :param query_terms_info: the results of each query term from the collection (dict of doc_id: DictionaryLine).
    :param results_list: list of all doc_id's matching the query.
    :param collection_info: the CollectionInfo instance for the collection.
    :param docset_info: the DocumentSetInfo instance for the collection.
    :return: a ranked list of results based on all the collection input info.
    """
    # Get relevant collection info
    total_doc_count = collection_info.document_count
    avg_doc_length = collection_info.avg_doc_length

    doc_rankings = dict()

    for doc_id in results_list:
        doc_length = docset_info.get_doc_info(doc_id).doc_length

        # Keep sum of ranking values for all terms ranking values for the given document --> that document's ranking value
        doc_ranking_val = 0
        for term in keywords:
            # Get term frequency & document frequency for each term x document cross product
            doc_freq = query_terms_info[term].get_document_frequency()
            term_freq = query_terms_info[term].get_term_frequency(doc_id)

            doc_ranking_val += compute_term_doc_rank(total_doc_count, avg_doc_length, doc_length, doc_freq, term_freq)

        doc_rankings[doc_id] = doc_ranking_val

    return sorted(doc_rankings.items(), key=operator.itemgetter(1), reverse=True)


def compute_term_doc_rank(total_doc_count, avg_doc_length, doc_length, doc_freq, term_freq):
    """
    Use the Okai BM25 model to compute
    :param total_doc_count: the number of documents in the collection.
    :param avg_doc_length: the average length of documents in the collection.
    :param doc_length: the length of the given document.
    :param doc_freq: the # of documents in which the given term appears in the collection.
    :param term_freq: the # of occurrences of the given term in the given document.
    :return: the computed ranking score for the given term and document.
    """
    eq_pt1 = float(total_doc_count) / doc_freq
    eq_pt2 = (K1_VALUE + 1) * term_freq

    # Handle case where term_freq could be 0
    if term_freq == 0:
        return 0

    eq_pt3 = (K1_VALUE * ((1 - B_VALUE) + B_VALUE * (float(doc_length) / avg_doc_length)) + term_freq)

    return log10(eq_pt1 * eq_pt2 / eq_pt3)
