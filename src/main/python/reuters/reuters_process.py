#!/usr/bin/env python2

import os
import sys
import argparse

from parse import ReutersParser
from fetch import fetch_reuters
from spimi.merger import SpimiMerger
from spimi.inverter import SpimiInverter

REUTERS_MODULE_DIR = os.path.dirname(os.path.realpath(__file__))
OUTPUT_DIR = os.path.join(REUTERS_MODULE_DIR, '..', 'out')
REUTERS_DL_DIR = os.path.join(REUTERS_MODULE_DIR, 'reuters21578')


def main(args):
    if not os.path.exists(REUTERS_DL_DIR) or args.download_corpus:
        print("Could not find Reuters corpus, downloading it now.")
        fetch_reuters()

    output_file_prefix = determine_output_file_prefix(args)

    # Parse
    parser = ReutersParser(REUTERS_DL_DIR, case_folding=args.case_folding, no_numbers=args.no_numbers, stem=args.stem,
                           remove_stopwords=args.remove_stopwords, output_directory=OUTPUT_DIR)
    tokens_list = parser.parse()

    # Invert
    inverter = SpimiInverter(tokens_list, args.limit_block_size, output_file_prefix=output_file_prefix,
                             output_directory=OUTPUT_DIR)
    output_files = inverter.run()

    # Merge
    merger = SpimiMerger(output_files, output_file_prefix, output_directory=OUTPUT_DIR)
    master_file = merger.merge()

    # Show results
    print("{} total terms.".format(master_file.term_count))
    return master_file


def determine_output_file_prefix(args):
    output_file_prefix = ''
    if args.no_numbers:
        output_file_prefix += 'no_numbers_'
    if args.case_folding:
        output_file_prefix += 'case_folding_'
    if args.remove_stopwords:
        output_file_prefix += 'stopwords_removed_'
    if args.stem:
        output_file_prefix += 'stemmed_'
    if output_file_prefix == '':
        output_file_prefix = 'no_compression_'
    return output_file_prefix


def parse_args(sys_args):
    parser = argparse.ArgumentParser(description="Query the Reuters corpus.")
    parser.add_argument('-l', '--limit-block-size', type=int, help="The block size limit in Mb", default=2)
    parser.add_argument('-d', '--download-corpus', action='store_true', required=False,
                        help="Force download the corpus even if it is already downloaded.")
    parser.add_argument('-s', '--stem', action='store_true', help="Use stemming.")
    parser.add_argument('-r', '--remove-stopwords', action='store_true', help="Remove stopwords.")
    parser.add_argument('-c', '--case-folding', action='store_true', help="Use case folding.")
    parser.add_argument('-n', '--no-numbers', action='store_true', help="Remove numbers.")
    return parser.parse_args(sys_args)


if __name__ == '__main__':
    parsed_args = parse_args(sys.argv[1:])
    main(parsed_args)
