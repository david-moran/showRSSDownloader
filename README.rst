DESCRIPTION
===========

Shows downloader for showrss.info

INSTALLATION
============

Download the project with:
git clone https://github.com/david-moran/showRSSDownloader.git

And install it with:
cd showRSSDownloader && python setup.py install

You must need at least python 3.5

USAGE
=====

After installation you will have following command:

```
showRSSDownloader
```

If you execute it, it will stay in foreground, if you want to launch in background use
systemd, supervisor or simply:

```
setsid showRSSDownloader
```


CONFIGURATION FILE
==================

Configuration file is located on ~/.showrssdownloader. It's a .ini file with
following sections and properties:

Section global
--------------

database: SQLite3 database where shows are tracked
    Default value: ~/.showrss_downloader.sqlite3"

Section showrss
---------------

url: Url where feed is downloaded
    Default value: http://showrss.info/user/113156.rss?magnets=true&namespaces=true&name=null&quality=null&re=null
    (my own feed :p)

Section transmission:
---------------------

address: transmission host
    Default value: localhost

port: transmission port
    Default value: 9091

user: transmission user
    Default value: transmission

password: transmission password
    default value: transmission

Example
-------

```
[showrss]
url=http://showrss.info/user/23134.rss

[transmission]
address=192.168.1.100
password=1234
```
