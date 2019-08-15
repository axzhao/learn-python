#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""

    >>> from osconfeed import *
    >>> feed = load()
    >>> sorted(feed['Schedule'].keys())
    ['conferences', 'events', 'speakers', 'venues']
    >>> for key, value in sorted(feed['Schedule'].items()):
    ...     print('{:3} {}'.format(len(value), key))
    ... 
    1 conferences
    1 events
    1 speakers
    1 venues
    >>> feed['Schedule']['speakers'][-1]['name']
    'Robert Lefkowitz'


    >>> from explore import *
    >>> feed = FrozenJSON(feed)
    >>> feed.Schedule
    <explore.FrozenJSON object at 0x10752e0f0>
    >>> feed.Schedule.speakers[-1].name
    'Robert Lefkowitz'

"""

from urllib.request import urlopen
import warnings
import os
import json

URL = 'http://www/oreilly.com/pub/sc/osconfeed'
JSON = 'osconfeed.json'


def load():
    data_file = os.path.join(os.getcwd(), JSON)
    if not os.path.exists(data_file):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())
    with open(JSON) as fp:
        return json.load(fp)


