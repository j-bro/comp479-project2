

class CollectionInfo:

    def __init__(self, document_count=0, token_count=0, avg_doc_length=0):
        self.document_count = document_count
        self.token_count = token_count
        self.avg_doc_length = avg_doc_length

    @classmethod
    def from_file(cls, file_path):
        """
        Serialize the object from the given file path.
        :param file_path: the path of the file to read from.
        :return: An instance of Collection representing the file at the given path.
        """
        with open(file_path) as f:
            file_lines = f.readlines()

        for line in file_lines:
            line_split = line.split('=')
            if line_split[0] == "DocumentCount":
                document_count = line_split[1]
            elif line_split[0] == "TokenCount":
                token_count = line_split[1]
            elif line_split[0] == "AvgDocLength":
                avg_doc_length = line_split[1]

        if not (document_count and token_count and avg_doc_length):
            raise Exception("Collection file invalid, must contain all of (DocumentCount, TokenCount, AvgDocLength)")

        return cls(document_count, token_count, avg_doc_length)

    def __str__(self):
        """
        Represent the line object as a string.
        :return:
        """
        str_repr = "DocumentCount={}\n".format(self.document_count)
        str_repr += "TokenCount={}\n".format(self.token_count)
        str_repr += "AvgDocLength={}\n".format(self.avg_doc_length)
        return str_repr
