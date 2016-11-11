#!/usr/bin/env python2

from tabulate import tabulate

import reuters_process


class ReutersProcessConfig:
    def __init__(self, no_numbers=False, case_folding=False, remove_stopwords=False, stem=False, limit_block_size=2):
        self.no_numbers = no_numbers
        self.case_folding = case_folding
        self.download_corpus = False
        self.remove_stopwords = remove_stopwords
        self.stem = stem
        self.limit_block_size = limit_block_size


def main():
    no_compression = reuters_process.main(reuters_process.parse_args(''))
    no_numbers = reuters_process.main(ReutersProcessConfig(no_numbers=True))
    case_folding = reuters_process.main(ReutersProcessConfig(no_numbers=True, case_folding=True))
    remove_stopwords = reuters_process.main(ReutersProcessConfig(no_numbers=True, case_folding=True, remove_stopwords=True))
    # stemming = reuters_process.main(ReutersProcessConfig(no_numbers=True, case_folding=True, remove_stopwords=True, stem=True))

    headers = ['Post-processing', 'Term count']
    data = [['No compression', no_compression.term_count],
            ['No numbers', no_numbers.term_count],
            ['Case folding', case_folding.term_count],
            ['Stopwords', remove_stopwords.term_count],]
            # ['Stemming', stemming.term_count]]

    print(tabulate(data, headers=headers, tablefmt='orgtbl'))


if __name__ == '__main__':
    main()
