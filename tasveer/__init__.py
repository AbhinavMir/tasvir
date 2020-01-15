"""
Tasveer unique file
It help you to download tons of images!
"""

import os
import sys

from google_images_download import google_images_download


def download(query='', count=0):
    """
    Downloads images based on query and count.
    If you do not include both a query and count, it will prompt utilizing input()
    Downloaded to <PWD>/downloads

    Arguments:
        query {str} -- image query string
        count {int} -- number of images to download
    """

    if not query:
        query = input('Enter query: ')

    if not count:
        count = input('Enter limit count images: ')

    response = google_images_download.googleimagesdownload()
    arguments = {'keywords': query, 'limit': count,
                 'print_urls': True, 'silent_mode': True}
    paths, _ = response.download(arguments)

    print('Saved at:')
    for key in paths:
        for path in paths[key]:
            print(path)
