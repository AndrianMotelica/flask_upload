#!/bin/bash

#bootstrap services
service apache2 restart

#keep container alive - run to infinity
tail -f /dev/null