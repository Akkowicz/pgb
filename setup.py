from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='pgb',
    version='0.2.0',
    description='PostgreSQL backups locally or to AWS S3 compatible storage.',
    long_description=readme,
    author='Mateusz',
    author_email='uamfhq@gmail.com',
    install_requires=['boto3'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        "console_scripts": [
            "pgb = pgb.cli:main",
        ]
    }
)