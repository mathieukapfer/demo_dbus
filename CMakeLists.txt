# exe
add_executable (ping
ping.cpp
  )

add_executable (pong
pong.cpp
  )

set_target_properties(ping PROPERTIES AUTOMOC TRUE)
set_target_properties(pong PROPERTIES AUTOMOC TRUE)

find_package(Qt5 COMPONENTS Core DBus CONFIG REQUIRED)

set(QT_LIB Qt5::Core Qt5::DBus)

target_link_libraries(ping ${QT_LIB})
target_link_libraries(pong ${QT_LIB})
