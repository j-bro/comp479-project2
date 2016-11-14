from collections import OrderedDict


class DocumentSetInfo:

    def __init__(self):
        """
        Class representing the information related to a document set.
        """
        self._docset = dict()

    def add_doc_info(self, doc_id, doc_length, doc_file_path):
        """
        Add the information for a new document.
        :param doc_id: the document ID of the new document.
        :param doc_length: the length of the new document.
        :param doc_file_path: the path to the file containing the document.
        """
        self._docset[doc_id] = DocumentInfo(doc_id, doc_length, doc_file_path)

    def get_doc_info(self, doc_id):
        """
        Get the info for the document with the given document ID.
        :param doc_id: the document ID of the desired document.
        :return: the document info.
        """
        return self._docset[doc_id]

    @classmethod
    def from_file(cls, file_path):
        """
        Serialize the a DocumentSetInfo instance from the given file path.
        :param file_path: the path of the file to read from.
        :return: An DocumentSet instance read from the file at the given path.
        """
        new_document_set = cls()

        with open(file_path) as f:
            file_lines = f.readlines()

        for line in file_lines:
            line_split = line.split(' ')
            doc_id = int(line_split[0])
            doc_length = int(line_split[1])
            doc_file_path = line_split[2]
            new_document_set.add_doc_info(doc_id, doc_length, doc_file_path)

        return new_document_set

    def __str__(self):
        """
        Give a string representation of the set of documents.
        Format of the string: doc_id doc_length path_of_file_containing_doc.
        :return: a string representation of the document set.
        """
        ordered_docset = OrderedDict(sorted(self._docset.items()))
        return '\n'.join([str(doc_info) for doc_info in ordered_docset.itervalues()])


class DocumentInfo:

    def __init__(self, doc_id, doc_length, doc_file_path):
        """
        Class representing the document info for one document.
        :param doc_id: the document ID of the document.
        :param doc_length: the length of the document.
        :param doc_file_path: the path to the file containing the document.
        """
        self.doc_id = doc_id
        self.doc_length = doc_length
        self.doc_file_path = doc_file_path

    def __str__(self):
        """
        Give a string representation of the document.
        Format of the string: doc_id doc_length path_of_file_containing_doc.
        :return: a string representation of the document.
        """
        return '{} {} {}'.format(str(self.doc_id), self.doc_length, self.doc_file_path)
