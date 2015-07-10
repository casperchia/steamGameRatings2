#!/usr/bin/env python
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'steamGameRatings.settings'

import scrapy
from SGRapp.models import Game


def main():
    print 'Starting steam games web scrape...\n'

    print '\nDone.'

if __name__ == '__main__':
    main()