import wget
import tarfile

URL = 'http://www.daviddlewis.com/resources/testcollections/reuters21578/reuters21578.tar.gz'


def fetch_reuters():
    print("Fetching Reuters corpus")

    filename = wget.download(URL)
    print("Saved Reuters corpus to {}".format(filename))

    untar_dir = 'reuters21578'
    tar = tarfile.open(filename)
    tar.extractall(path=untar_dir)
    tar.close()
    print("Extracted Reuters corpus to {}".format(untar_dir))

if __name__ == '__main__':
    fetch_reuters()
