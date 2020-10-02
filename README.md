# Demo_dbus
dbus communication between C++ QT and python [WORK IN PROGRESS]

# Dependencies
sudo apt-get install qtbase5-dev 

# Concept

n° | Level        | Name
--|---------- | -------------
1 | bus | session
2 | service | org.example.QtDBus.PingExample
3 | object path | /path/to/object
4 | interface | local.pong.Pong
5 | method | Ping

# Run Qt sample with dbus-monitor

Extract of full log (see output.log)

```
$ dbus-monitor --session &
$ make
...
<node>
  <interface name="local.pong.Pong">
    <method name="ping">
      <arg type="s" direction="out"/>
      <arg name="arg" type="s" direction="in"/>
    </method>
    <method name="ping_void">
    </method>
  </interface>
...
method call time=1601639817.776780 sender=:1.103 -> destination=org.freedesktop.DBus serial=3 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=AddMatch
   string "type='signal',sender='org.freedesktop.DBus',interface='org.freedesktop.DBus',member='NameOwnerChanged',arg0='org.example.QtDBus.PingExample'"
method call time=1601639817.777572 sender=:1.103 -> destination=org.freedesktop.DBus serial=4 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=GetNameOwner
   string "org.example.QtDBus.PingExample"
method return time=1601639817.777611 sender=org.freedesktop.DBus -> destination=:1.103 serial=3 reply_serial=4
   string ":1.102"
method call time=1601639817.777623 sender=:1.103 -> destination=org.example.QtDBus.PingExample serial=5 path=/path/to/object; interface=(null); member=ping
   string ""
method return time=1601639817.778610 sender=:1.102 -> destination=:1.103 serial=4 reply_serial=5
   string "ping("") got called"
Reply was: ping("") got called
...
```
