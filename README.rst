Roowifi
=======

Roowifi is a module for issueing commands to and collecting data from Roomba robots via the RooWifi_ wifi-to-serial device.

Don't let your Roomba go unhacked!

Usage:
------

.. code-block:: bash
    $ python roowifi.py -h

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