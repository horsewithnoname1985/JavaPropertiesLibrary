from invoke import task
from robot.libdoc import libdoc
from pathlib import Path


@task
def create_kw_docs(c):
    """Generates the library keyword documentation

    Documentation is generated by using the Libdoc tool.
    """
    libdoc(str(
        Path('src/JavaPropertiesLibrary/keywords/JavaPropertiesLibrary.py')),
           str(Path('docs/JavaPropertiesLibrary.html')))