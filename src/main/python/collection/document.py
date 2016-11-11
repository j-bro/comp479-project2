from collections import OrderedDict


class DocumentSetInfo:

    def __init__(self):
        """

        """
        self._docset = dict()

    def add_doc_info(self, doc_id, doc_length, doc_file_path):
        """

        :param doc_id:
        :param doc_length:
        :param doc_file_path:
        :return:
        """
        self._docset[doc_id] = DocumentInfo(doc_id, doc_length, doc_file_path)

    def get_doc_info(self, doc_id):
        """

        :param doc_id:
        :return:
        """
        return self._docset[doc_id]

    @classmethod
    def from_file(cls, file_path):
        """
        Serialize the object from the given file path.
        :param file_path: the path of the file to read from.
        :return: An DocumentSet instance representing the file at the given path.
        """
        new_document_set = cls()

        with open(file_path) as f:
            file_lines = f.readlines()

        for line in file_lines:
            line_split = line.split(' ')
            new_document_set.add_doc_info(line_split[0], line_split[1], line_split[2])

        return new_document_set

    def __str__(self):
        """
        Represent the line object as a string.
        Format of the string: doc_id doc_length path_of_file_containing_doc
        :return:
        """
        ordered_docset = OrderedDict(sorted(self._docset.items()))
        return '\n'.join([str(doc_info) for doc_info in ordered_docset.itervalues()])


class DocumentInfo:

    def __init__(self, doc_id, doc_length, doc_file_path):
        """

        :param doc_id:
        :param doc_length:
        :param doc_file_path:
        """
        self.doc_id = doc_id
        self.doc_length = doc_length
        self.doc_file_path = doc_file_path

    def __str__(self):
        """

        :return:
        """
        return '{} {} {}'.format(str(self.doc_id), self.doc_length, self.doc_file_path)
