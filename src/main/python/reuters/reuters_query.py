#!/usr/bin/env python2

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # easy hack to import lib module
from argparse import ArgumentParser
from query.query_maker import QueryMaker

REUTERS_MODULE_DIR = os.path.dirname(os.path.realpath(__file__))
OUTPUT_DIR = os.path.join(REUTERS_MODULE_DIR, '..', 'out')
DICTIONARY_FILE = os.path.join(OUTPUT_DIR, 'no_compression_master.txt')
COLLECTION_FILE = os.path.join(OUTPUT_DIR, 'collection.txt')
DOCSET_FILE = os.path.join(OUTPUT_DIR, 'documents.txt')


def main(args):
    dictionary_file = args.dictionary
    collection_file = args.collection
    docset_file = args.docset
    query_type = 'or'

    query_maker = QueryMaker(dictionary_file, collection_file, docset_file, args.keywords, query_type)
    query = query_maker.make_query()

    if query.result:
        print("Documents matching query: ")
        print('\n'.join(["{}. doc_id: {}, rank_val: {}".format(str(idx + 1), str(result_tuple[0]), str(result_tuple[1]))
                         for idx, result_tuple in enumerate(query.result)]))


def parse_args(sys_args):
    parser = ArgumentParser(description="Query the Reuters corpus.")
    parser.add_argument('keywords', metavar='term', nargs='+')
    parser.add_argument('-d', '--dictionary', type=str, default=DICTIONARY_FILE)
    parser.add_argument('-c', '--collection', type=str, default=COLLECTION_FILE)
    parser.add_argument('-s', '--docset', type=str, default=DOCSET_FILE)
    return parser.parse_args(sys_args)


if __name__ == '__main__':
    parsed_args = parse_args(sys.argv[1:])
    main(parsed_args)
