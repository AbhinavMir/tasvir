"""
Just exec
"""

from tasveer import download

try:
    download()
except KeyboardInterrupt:
    print('Bye.')
    exit(1)
