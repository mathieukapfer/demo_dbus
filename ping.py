#!/usr/bin/python
"""Emmitter functionality."""
import dbus
import dbus.service
import dbus.glib

# naming
service_name   = 'my.service'
object_path    = '/my/object/path'
interface_name = 'my.interface'

class Emitter(dbus.service.Object):
    """Emitter DBUS service object."""

    def __init__(self, bus_name, object_path):
        """Initialize the emitter DBUS service object."""
        dbus.service.Object.__init__(self, bus_name, object_path)

    @dbus.service.signal(interface_name)
    def test(self):
        """Emmit a test signal."""
        print('Emitted a test signal')

    @dbus.service.signal(interface_name)
    def quit_signal(self):
        """Emmit a quit signal."""
        print('Emitted a quit signal')

"""
Emit a test signal on the dbus.
Emit a receiver_quit signal which should stop the receiver.
"""
session_bus = dbus.SessionBus()
bus_name = dbus.service.BusName(service_name, bus=session_bus)
emitter = Emitter(bus_name, object_path)
emitter.test()
emitter.quit_signal()
