

class DictionaryFile:
    def __init__(self, file_path):
        """
        Representation of a dictionary file.
        :param file_path: the path to the actual dictionary file.
        """
        self.file_path = file_path
        self.file_handle = None
        self.term_count = 0

    def open_handle(self, mode='r'):
        """
        Open the file handle of the dictionary file.
        :param mode: the file mode ('r' for read, 'w' for write, 'r+' for read & write).
        :return: the file handle of the opened file.
        """
        self.file_handle = open(self.file_path, mode)
        return self.file_handle

    def write_line(self, line_obj):
        """
        Write the line object to a file
        :param line_obj: the DictionaryFileLine object to write to the dictionary file
        """
        self.file_handle.write(str(line_obj))
        self.term_count += 1

    def read_line_to_obj(self):
        """
        Read the next line in the file.
        :return: the DictionaryFileLine representation of the line.
        """
        line_str = self.file_handle.readline()
        if line_str:
            return DictionaryFileLine.from_line_string(-1, line_str)
        else:
            return None

    def close_handle(self):
        """
        Close the file handle.
        """
        self.file_handle.close()


class DictionaryFileLine:
    def __init__(self, block_file_index_list, term, postings_list):
        """

        :param block_file_index_list: the index of the block file in the external list (use -1 if this is irrelevant).
        :param term: the term for this line.
        :param postings_list: the postings list for this line.
        """
        self.block_file_index_list = block_file_index_list
        self.term = term
        self.postings_list = postings_list

    @classmethod
    def from_line_string(cls, block_file_index_list, line_string):
        """
        Parse the data in a block file line.
        :param block_file_index_list: the index of the document in which the line is found
        :param line_string: the line text to be parsed
        :return: An instance of SpimiBlockLinetuple containing (index, term, postings_list)
        """
        split_line = line_string.split(' ')
        return cls(block_file_index_list, split_line[0], [int(doc_id) for doc_id in split_line[1:]])

    def get_document_frequency(self):
        return len(self.postings_list)

    def merge(self, other_file_line):
        """
        Merge this dictionary file line with another.
        :param other_file_line: the other dictionary file line to merge.
        :return: a new DictionaryFileLine consisting the list of block file indices, the same term, and the combined
        postings list.
        """
        new_block_file_index_list = sorted(self.block_file_index_list + other_file_line.block_file_index_list)
        new_postings_list = sorted(self.postings_list + other_file_line.postings_list)
        return DictionaryFileLine(new_block_file_index_list, self.term, new_postings_list)

    def __str__(self):
        """
        Represent the line object as a string.
        :return:
        """
        return '{} {}\n'.format(self.term, ' '.join([str(doc_id) for doc_id in self.postings_list]))
