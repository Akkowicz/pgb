pgb
===

CLI for backing up remote PostgreSQL databases either locally or to S3 compatible storage.

Preparing for Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone the repository: ``git clone git@github.com:akkowicz/pgb``
3. ``cd`` into the repository.
4. Fetch development dependencies ``make install``
5. Activate virtualenv: ``pipenv shell``


Usage
-----

Pass in a full DB URL, the storage driver, and the destination.

S3 Example with bucket name:

::

    $ pgb postgres://adam@example.com:5432/test_db --driver s3 backups

Local Example with local path:

::

    $ pgb postgres://adam@example.com:5432/test_db --driver local /var/local/test_db/backups/dump.sql

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active.

::

    $ make

If virtualenv isn't active then use:

::

    $ pipenv run make