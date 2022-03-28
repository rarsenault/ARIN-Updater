# ARIN-Updater

## Purpose

Semi-automate adding/updating of ARIN auth IRR route/route6 objects

## Requirements

* Tested on Python 3.6, 3.8

## Use

* Get an API key from ARIN Online and edit the "api-key" variable in ARIN-IRR-Updater.py
* Copy conf/prefixes.example to conf/prefixes.txt
* run ARIN-IRR-Updater.py

If a route/route6 object already exists for a given prefix, the script will update it with the new info. If the object does not exist, the script will create it.

I highly recommend testing against the [ARIN OTE environment](https://www.arin.net/reference/tools/testing/?msclkid=f88c8e5aaedd11ec837b672505346c2e). You can do this by searching for and editing the URL in ARIN-IRR-Updater.py to read "https://reg.ote.arin.net..." instead of "https://reg.arin.net..."

## Caveats

* I am not a developer and this mostly works by accident
* Only works for ARIN IRR as that's all I need it to do
* Performs very little sanity-checking
* Expects a very specific format in the CSV file and in particular will only allow a single descr element

## Future Work

This may never happen, at least not by me, because I don't particularly need it.

* Allow multiple descr entries (maybe someone wants to put a multi-line address for each object)\
* Better error reporting and sanity checking of the input CSV

## References
* [ARIN IRR RESTful API](https://www.arin.net/resources/manage/irr/irr-restful/)
