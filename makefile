# helper to build and run the sample test

BUILD_PATH=build_x86
#LD_LIBRARY_PATH=../../../../../externals/install/qt5/x86/lib

all: build-test test

$(BUILD_PATH)/Makefile:
	mkdir $(BUILD_PATH) && cd $(BUILD_PATH) && cmake ..

build-test: $(BUILD_PATH)/Makefile
	cd $(BUILD_PATH) && make

test:
	export LD_LIBRARY_PATH=$(LD_LIBRARY_PATH) && $(BUILD_PATH)/pong &
	sleep 1
	export LD_LIBRARY_PATH=$(LD_LIBRARY_PATH) && $(BUILD_PATH)/ping

test-pong:  build-test
	export LD_LIBRARY_PATH=$(LD_LIBRARY_PATH) && $(BUILD_PATH)/pong &
	sleep 1
	gdbus introspect --session --dest "org.example.QtDBus.PingExample" --object-path "/path/to/object"
	gdbus call       --session --dest "org.example.QtDBus.PingExample" --object-path "/path/to/object" --method "local.pong.Pong.ping_void"
	gdbus call       --session --dest "org.example.QtDBus.PingExample" --object-path "/path/to/object" --method "local.pong.Pong.ping" "helloo"

test-pong-py:
	python pong.py &
	sleep 1
	gdbus introspect --session --dest "sub.domain.tld" --object-path "/tld/domain/sub/Test"
	gdbus call --session --dest "sub.domain.tld" --object-path "/tld/domain/sub/Test"  --method "tld.domain.sub.TestInterface.foo"

test-ping:
	export LD_LIBRARY_PATH=$(LD_LIBRARY_PATH) && $(BUILD_PATH)/ping

test-py:
	echo "run pong.py"
	python pong.py &
	sleep 1
	echo "call foo method"
	gdbus call --session  --dest "sub.domain.tld" --object-path "/tld/domain/sub/Test" --method tld.domain.sub.TestInterface.foo
	echo "run ping.py"
	python ping.py

echo:
	echo export LD_LIBRARY_PATH=$(LD_LIBRARY_PATH) && $(BUILD_PATH)/pong &

clean:
	cd  $(BUILD_PATH) && make clean
