# basictor

Minimal Tor code. Common exit node/IP changing by NEWNYM signal.

Example ipython session:

```
%load_ext autoreload
%autoreload 2
import logging
logging.info('')     # !!!!!
from toscrape.basictor import BasicTor
bt = BasicTor()
bt.new_tor_identity()
bt.new_tor_identity()
```

You can test how unique the exit nodes (IP addresses) are:

```
basictor/teszt$ python uniqueip.py
```
