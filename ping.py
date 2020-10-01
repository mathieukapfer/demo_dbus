#!/usr/bin/python
"""Emmitter functionality."""
import dbus
import dbus.service
import dbus.glib

# matk param
service_name = 'sub.domain.tld'
service_name_ = 'tld.domain.sub.'
service_name__ = '/tld/domain/sub/'
interface_name = 'event'
# service_name = 'org.example.QtDBus.PingExample"'

class Emitter(dbus.service.Object):
    """Emitter DBUS service object."""

    def __init__(self, bus_name, object_path):
        """Initialize the emitter DBUS service object."""
        dbus.service.Object.__init__(self, bus_name, object_path)

    @dbus.service.signal(service_name_ + interface_name)
    #@dbus.service.signal('tld.domain.sub.event') #service_name_ + interface_name)
    def test(self):
        """Emmit a test signal."""
        print('Emitted a test signal')

    @dbus.service.signal(service_name_ + interface_name)
    #@dbus.service.signal('tld.domain.sub.event') 
    def quit_signal(self):
        """Emmit a quit signal."""
        print('Emitted a quit signal')

"""
Emit a test signal on the dbus.
Emit a receiver_quit signal which should stop the receiver.
"""
session_bus = dbus.SessionBus()
bus_name = dbus.service.BusName('sub.domain.tld', bus=session_bus) # (service_name, bus=session_bus)
emitter = Emitter(bus_name, '/tld/domain/sub/event')# service_name__ + interface_name)
emitter.test()
emitter.quit_signal()
