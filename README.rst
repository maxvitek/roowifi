Roowifi
=======

Roowifi is a module for issueing commands to and collecting data from Roomba robots via the RooWifi_ wifi-to-serial device.

Don't let your Roomba go unhacked!

Usage:
------

python roowifi.py -h
usage: roowifi.py [-h] [-u USER] [-p PASSWD] ip_address {clean,spot,dock,idle}

A commandline utility for controlling a Roomba via a RooWifi device.

positional arguments:
  ip_address                    ip address of target robot
  {clean,spot,dock,idle}        command to be issued

optional arguments:
  -h, --help                    show this help message and exit
  -u USER, --user USER          username
  -p PASSWD, --passwd PASSWD    password


It may also be imported directly, thus:

.. code-block:: pycon
    >>>import roowifi
    >>>roomba = Roomba('12.34.56.78')
    >>>roomba.clean()
    ...

Contribute:
-----------

#. It would be cool to expose more of the `iRobot SCI`_

.. _RooWifi: http://roowifi.com
.. _iRobot SCI: http://www.irobot.com/images/consumer/hacker/Roomba_SCI_Spec_Manual.pdf