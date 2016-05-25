import sys
import subprocess
from pkg_resources import resource_filename


def get_jar_filename():
    """Return the full path to the Closure Compiler Java archive."""
    return resource_filename(__name__, "closure.jar")


def main():
    return subprocess.call(['java', '-jar', get_jar_filename()] + sys.argv[1:])

