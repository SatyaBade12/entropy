from pathlib import Path


""" Project related functions.

An Entropy *project* is a filesystem directory containing a '.entropy' directory
which itself contains an 'entropy.db' SQLite database file and an 'entropy.hdf5'
HDF5 file.

project
    .entropy
        entropy.db
        entropy.hdf5
"""


def project_name(path: str) -> str:
    """Returns a project name for the given path

    :path: A filesystem path to a directory. Directory does not have to contain an
    actual Entropy project"""
    return Path(path).absolute().name


def project_path(path: str) -> str:
    """Returns the absolute path for the given path, as a string

    :path: A filesystem path to a directory. Directory does not have to contain an
    actual Entropy project"""
    return Path(path).absolute()
