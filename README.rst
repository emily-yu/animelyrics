# animelyric
-------------

Description
~~~~~~~~~~~

Animelyric is a python library for retrieving lyrics for anime songs
from animelyrics dot com.

Table of Contents
~~~~~~~~~~~~~~~~~

-  Requirements_
-  Installation_
-  Usage_

Requirements
~~~~~~~~~~~~

-  urllib.request
-  bs4
-  requests
-  google
-  urllib.parse

Installation
~~~~~~~~~~~~

Using pip

::

    pip install animelyric

or clone and install:
::

    git clone https://github.com/emily-yu/animelyrics.git
    cd animelyric
    python setup.py

Usage
~~~~~

::

    from animelyric import AnimeLyrics
    al = AnimeLyrics('[keyword-to-search]')

+------------+------------------------------------+
| Function   | Parameter                          |
+============+====================================+
| init       | keyword-to-search                  |
+------------+------------------------------------+
| lyrics     | lang (en: English, jp: Japanese)   |
+------------+------------------------------------+
| song_title | n/a                                |
+------------+------------------------------------+
