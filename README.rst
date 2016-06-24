====================================
hms_irc, the HAUM’s IRC microservice
====================================

A microservice that follows routing keys on a RabbitMQ direct exchanger and
publish messages on IRC depending on the messages received.

Using
=====

Debian-like systems
-------------------

First build the `.deb` file::

    $ dpkg-buildpackage -us -uc -b

Then install it on the system as superuser::

    # dpkg -i ../hms-irc*.deb

And that's it. A systemd `.service` is also installed and for starting and
stopping the microservice in a convenient way::

    # systemctl start hms-irc

Also, for debugging purposes, you can send messages to the microservice that
will relay it on the IRC chan it is connected to::

    $ /usr/share/python/hms-irc/bin/hms_irc hello world

Other distributions
-------------------

There is no other supported distribution at the moment ; however this program
can be run in userspace using the following commands::

    $ virtualenv -ppython3 venv
    $ source venv/bin/activate
    $ pip install .
    $ hms_irc &
    $ hms_irc_debug hello world

License
=======

This project is brought to you under MIT license. For further information,
please read the provided ``LICENSE.txt`` file.
