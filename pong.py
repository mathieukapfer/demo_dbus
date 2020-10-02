#!/usr/bin/python

"""Receiver related functionality."""
import dbus
import dbus.service
import dbus.glib

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GObject

# naming
service_name   = 'my.service' # 'sub.domain.tld'
object_path    = '/my/object/path' # '/tld/domain/sub/Test'
interface_name = 'my.interface' #'tld.domain.sub.TestInterface'

class Test(dbus.service.Object):
    """Reciever test class."""

    loop = None

    def __init__(self, bus_name, object_path, loop):
        """Initialize the DBUS service object."""
        dbus.service.Object.__init__(self, bus_name, object_path)
        self.loop = loop

    @dbus.service.method(interface_name)
    def foo(self):
        """Return a string."""
        return 'FooOOOooo'

    # Stop the main loop
    @dbus.service.method(interface_name)
    def stop(self):
        """Stop the receiver."""
        self.loop.quit()
        return 'Quit loop'

    # Pass an exception through dbus
    @dbus.service.method(interface_name)
    def fail(self):
        """Trigger an exception."""
        raise Exception('FAIL!')


def catchall_handler(*args, **kwargs):
    """Catch all handler.

    Catch and print information about all singals.
    """
    print('---- Caught signal ----')
    print('%s:%s\n' % (kwargs['dbus_interface'], kwargs['member']))

    print('Arguments:')
    for arg in args:
        print('* %s' % str(arg))

    print("\n")


def quit_handler():
    """Signal handler for quitting the receiver."""
    print('Quitting....')
    loop.quit()

loop = GObject.MainLoop()

"""
First we get the bus to attach to. This may be either the session bus, of the
system bus. For system bus root permission is required.

We claim a bus name on the chosen bus. The name should be in form of a
domain name.
"""

bus = dbus.SessionBus()
# bus = dbus.SystemBus()
bus_name = dbus.service.BusName(service_name, bus=bus)

"""
We initialize our service object with our name and object path. Object
path should be in form of a reverse domain dame, delimited by / instead of .
and the Class name as last part.

The object path we set here is of importance for our invoker, since it will to
call it exactly as defined here.
"""
obj = Test(bus_name, object_path, loop)


"""
Attach signal handler.

Signal handlers may be attached in different ways, either by interface keyword
or DBUS interface and a signal name or member keyword.

You can easily gather all information by running the DBUS monitor.
"""
bus.add_signal_receiver(catchall_handler,
                        interface_keyword='dbus_interface',
                        member_keyword='member')
bus.add_signal_receiver(quit_handler,
                        dbus_interface=service_name + "." + interface_name,
                        signal_name='quit_signal')

loop.run()
