from math import log10

K1_VALUE = 0.5
B_VALUE = 0.5


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


def rank_results(keywords, results_list, collection_info, docset_info):

    total_doc_count = collection_info.document_count
    avg_doc_length = collection_info.avg_doc_length

    doc_rankings = dict()

    for doc_id in results_list:
        doc_length = docset_info.get_doc_info(doc_id).doc_length

        doc_ranking_val = 0
        for term in keywords:
            # TODO need document frequency of term (# of docs in which term appears)
            doc_freq = 0

            # TODO need term frequency (# of times term appears in chosen document
            term_freq = 0

            eq_pt1 = float(total_doc_count) / doc_freq
            eq_pt2 = float((K1_VALUE + 1) * term_freq)
            eq_pt3 = float((K1_VALUE * ((1 - B_VALUE) + B_VALUE * (float(doc_length) / avg_doc_length)) + term_freq))

            doc_length += log10(eq_pt1 * eq_pt2 / eq_pt3)

        doc_rankings[doc_id] = doc_ranking_val

    # TODO sort doc list by ranking
