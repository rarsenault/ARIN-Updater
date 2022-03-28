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

### Very Important Safety Tip

_The script defaults to testing against the_ [ARIN OTE environment](https://www.arin.net/reference/tools/testing/?msclkid=f88c8e5aaedd11ec837b672505346c2e). I highly recommend testing in this manner until it returns the correct results. 

* To publish/update objects in the public ARIN IRR, modify the "target_url" variable from "https://reg.ote.arin.net" to "https://reg.arin.net"

## Caveats

* I am not a developer and this mostly works by accident
* Only works for ARIN IRR as that's all I need it to do
* Only adds/updates route/route6 IRR objects
* Performs very little sanity-checking
* Expects a very specific format in the CSV file and in particular will only allow a single descr element

## Future Work

This may never happen, at least not by me, because I don't particularly need it.

* Allow multiple descr entries (maybe someone wants to put a multi-line address for each object)\
* Better error reporting and sanity checking of the input CSV
* Add a script to delete objects
* Document some simple processes to check your advertisements, generate the info required by prefixes.txt, verify, clean legacy IRR objects, etc

## References
* [ARIN IRR RESTful API](https://www.arin.net/resources/manage/irr/irr-restful/)
