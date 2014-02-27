Roowifi
=======

Roowifi is a module for issueing commands to and collecting data from Roomba robots via the RooWifi_ wifi-to-serial device.

Commandline Usage:

python roowifi.py -h
usage: roowifi.py [-h] [-u USER] [-p PASSWD] ip_address {clean,spot,dock,idle}

A commandline utility for controlling a Roomba via a RooWifi device.

positional arguments:
  ip_address            ip address of target robot
  {clean,spot,dock,idle}
                        command to be issued

optional arguments:
  -h, --help            show this help message and exit
  -u USER, --user USER  username
  -p PASSWD, --passwd PASSWD
                        password


It may also be imported directly, thus:

>>>import roowifi
>>>roomba = Roomba('1.0.0.1')
>>>roomba.clean()


.. _RooWifi: http://roowifi.com