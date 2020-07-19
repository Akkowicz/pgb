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

def test_dump_handles_oserror(mocker):
    """
    pgdump.dump returns a reasonable error if pg_dump isn't installed
    """
    mocker.patch('subprocess.Popen', side_effect=OSError('no such file'))
    with pytest.raises(SystemExit):
        pgdump.dump(url)

def test_dump_file_name_without_timestamp():
    """
    pgdump.dump_file_name returns the name of the database
    """
    assert pgdump.dump_file_name(url) == "test_db.sql"

def test_dump_file_name_with_timestamp():
    """
    pgdump.dump_file_name returns the name of the database with timestamp
    """
    timestamp = "2020-07-19T15:30:30"
    assert pgdump.dump_file_name(url, timestamp) == f"test_db-{timestamp}.sql"