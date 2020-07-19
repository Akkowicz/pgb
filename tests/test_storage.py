import tempfile
from pgb import storage

def test_storing_file_locally():
    """
    Writes content from one file-like to another.
    """
    infile = tempfile.TemporaryFile()
    infile.write(b'Testing')
    infile.seek(0)

    outfile = tempfile.NamedTemporaryFile(delete=False)

    storage.local(infile, outfile)

    with open(outfile.name, 'rb') as f:
        assert f.read() == b'Testing'