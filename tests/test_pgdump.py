import pytest
import subprocess

from pgb import pgdump

url = "postgres://alex:password@example.com:5432/test_db"

def test_dump_calls_pg_dump(mocker):
    """
    Utilize pg_dump with the new database URL
    """
    mocker.patch('subprocess.Popen')
    assert pgdump.dump(url)
    subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprocess.PIPE)