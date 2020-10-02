# demo_dbus
dbus communication between C++ QT and python

```
$ dbus-monitor --session &
[1] 21204
$ make test
pong &
sleep 1
method call time=1601566251.016168 sender=:1.92 -> destination=org.freedesktop.DBus serial=1 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=Hello
method return time=1601566251.016209 sender=org.freedesktop.DBus -> destination=:1.92 serial=1 reply_serial=1
   string ":1.92"
signal time=1601566251.016220 sender=org.freedesktop.DBus -> destination=(null destination) serial=130 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=NameOwnerChanged
   string ":1.92"
   string ""
   string ":1.92"
signal time=1601566251.016233 sender=org.freedesktop.DBus -> destination=:1.92 serial=2 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=NameAcquired
   string ":1.92"
method call time=1601566251.017941 sender=:1.92 -> destination=org.freedesktop.DBus serial=2 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=RequestName
   string "org.example.QtDBus.PingExample"
   uint32 4
signal time=1601566251.017996 sender=org.freedesktop.DBus -> destination=(null destination) serial=131 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=NameOwnerChanged
   string "org.example.QtDBus.PingExample"
   string ""
   string ":1.92"
signal time=1601566251.018013 sender=org.freedesktop.DBus -> destination=:1.92 serial=3 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=NameAcquired
   string "org.example.QtDBus.PingExample"
method return time=1601566251.018065 sender=org.freedesktop.DBus -> destination=:1.92 serial=4 reply_serial=2
   uint32 1   
export LD_LIBRARY_PATH=../../../../../externals/install/qt5/x86/lib && ../../../../../../build_x86/src/apps/linux_a7/sandbox/dbus/pingpong/ping
method call time=1601566252.019037 sender=:1.93 -> destination=org.freedesktop.DBus serial=1 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=Hello
method return time=1601566252.019101 sender=org.freedesktop.DBus -> destination=:1.93 serial=1 reply_serial=1
   string ":1.93"
signal time=1601566252.019179 sender=org.freedesktop.DBus -> destination=(null destination) serial=132 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=NameOwnerChanged
   string ":1.93"
   string ""
   string ":1.93"
signal time=1601566252.019226 sender=org.freedesktop.DBus -> destination=:1.93 serial=2 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=NameAcquired
   string ":1.93"
method call time=1601566252.019428 sender=:1.93 -> destination=org.example.QtDBus.PingExample serial=2 path=/path/to/object; interface=org.freedesktop.DBus.Introspectable; member=Introspect
method return time=1601566252.019913 sender=:1.92 -> destination=:1.93 serial=3 reply_serial=2
   string "<!DOCTYPE node PUBLIC "-//freedesktop//DTD D-BUS Object Introspection 1.0//EN"
"http://www.freedesktop.org/standards/dbus/1.0/introspect.dtd">
<node>
  <interface name="local.pong.Pong">
    <method name="ping">
      <arg type="s" direction="out"/>
      <arg name="arg" type="s" direction="in"/>
    </method>
    <method name="ping_void">
    </method>
  </interface>
  <interface name="org.freedesktop.DBus.Properties">
    <method name="Get">
      <arg name="interface_name" type="s" direction="in"/>
      <arg name="property_name" type="s" direction="in"/>
      <arg name="value" type="v" direction="out"/>
    </method>
    <method name="Set">
      <arg name="interface_name" type="s" direction="in"/>
      <arg name="property_name" type="s" direction="in"/>
      <arg name="value" type="v" direction="in"/>
    </method>
    <method name="GetAll">
      <arg name="interface_name" type="s" direction="in"/>
      <arg name="values" type="a{sv}" direction="out"/>
      <annotation name="org.qtproject.QtDBus.QtTypeName.Out0" value="QVariantMap"/>
    </method>
    <signal name="PropertiesChanged">
      <arg name="interface_name" type="s" direction="out"/>
      <arg name="changed_properties" type="a{sv}" direction="out"/>
      <annotation name="org.qtproject.QtDBus.QtTypeName.Out1" value="QVariantMap"/>
      <arg name="invalidated_properties" type="as" direction="out"/>
    </signal>
  </interface>
  <interface name="org.freedesktop.DBus.Introspectable">
    <method name="Introspect">
      <arg name="xml_data" type="s" direction="out"/>
    </method>
  </interface>
  <interface name="org.freedesktop.DBus.Peer">
    <method name="Ping"/>
    <method name="GetMachineId">
      <arg name="machine_uuid" type="s" direction="out"/>
    </method>
  </interface>
</node>
"
method call time=1601566252.021026 sender=:1.93 -> destination=org.freedesktop.DBus serial=3 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=AddMatch
   string "type='signal',sender='org.freedesktop.DBus',interface='org.freedesktop.DBus',member='NameOwnerChanged',arg0='org.example.QtDBus.PingExample'"
method call time=1601566252.021223 sender=:1.93 -> destination=org.freedesktop.DBus serial=4 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=GetNameOwner
   string "org.example.QtDBus.PingExample"
method return time=1601566252.021251 sender=org.freedesktop.DBus -> destination=:1.93 serial=3 reply_serial=4
   string ":1.92"
method call time=1601566252.021649 sender=:1.93 -> destination=org.example.QtDBus.PingExample serial=5 path=/path/to/object; interface=(null); member=ping
   string ""
Reply was: ping("") got called
method return time=1601566252.024291 sender=:1.92 -> destination=:1.93 serial=4 reply_serial=5
   string "ping("") got called"
signal time=1601566252.024322 sender=org.freedesktop.DBus -> destination=:1.92 serial=5 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=NameLost
   string "org.example.QtDBus.PingExample"
signal time=1601566252.024332 sender=org.freedesktop.DBus -> destination=(null destination) serial=4 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=NameOwnerChanged
   string "org.example.QtDBus.PingExample"
   string ":1.92"
   string ""
signal time=1601566252.024376 sender=org.freedesktop.DBus -> destination=:1.92 serial=6 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=NameLost
   string ":1.92"
signal time=1601566252.024384 sender=org.freedesktop.DBus -> destination=(null destination) serial=133 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=NameOwnerChanged
   string ":1.92"
   string ":1.92"
   string ""
method call time=1601566252.024396 sender=:1.93 -> destination=org.freedesktop.DBus serial=6 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=RemoveMatch
   string "type='signal',sender='org.freedesktop.DBus',interface='org.freedesktop.DBus',member='NameOwnerChanged',arg0='org.example.QtDBus.PingExample'"
method call time=1601566252.024406 sender=:1.93 -> destination=org.freedesktop.DBus serial=7 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=RemoveMatch
   string "type='signal',sender='org.freedesktop.DBus',interface='org.freedesktop.DBus',member='NameOwnerChanged',arg0='org.freedesktop.DBus'"
error time=1601566252.024434 sender=org.freedesktop.DBus -> destination=:1.93 error_name=org.freedesktop.DBus.Error.MatchRuleNotFound reply_serial=7
   string "The given match rule wasn't found and can't be removed"
signal time=1601566252.024446 sender=org.freedesktop.DBus -> destination=:1.93 serial=8 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=NameLost
   string ":1.93"
signal time=1601566252.024470 sender=org.freedesktop.DBus -> destination=(null destination) serial=134 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=NameOwnerChanged
   string ":1.93"
   string ":1.93"
   string ""
user@debian:~/Project/project_evlink_v3@test_ci_dbus/src/apps/linux_a7/sandbox/dbus/pingpong$ 

```
