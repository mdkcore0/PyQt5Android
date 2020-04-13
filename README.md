# PyQt5Android

## Requirements
* Qt 5.12.3
* Python 3.7.2
* sip 4.19.18 (>= 5 not supported yet!, 4.19.19 til .22 has a deprecated flag)
* PyQt 5.12.3
* pyqtdeploy 2.4
* Android SDK tools 29.0.1 (commandlinetools 6200805)
    * OpenJDK 8u242
    * Android NDK r19c
    * Android Emulator (optional)
    * Android platform-tools 29.0.6
* pyenv 1.2.18 (optional)

## Installation instructions for development
- (optional) Install python 3.7.2 and make a virtual environment
    ```
    $ pyenv install 3.7.2
    $ pyenv virtualenv 3.7.2 android-test
    $ pyenv activate android-test
    ```

- Install *pyqtdeploy*
    ```
    $ pip install -r requirements.txt
    ```

- Install **Qt**, just the *Android* libraries and toolchains, you will use the
installation path later (e.g.: `/opt/Qt5.12.3`)

- Install **Android SDK**:
    - Download [command line tools](https://developer.android.com/studio#cmdline-tools)
    and extract to a location on your computer; you will use this path later
    (e.g.: `/opt/Android`)

    - Install **NDK** and **platform-tools** (you may need to install *OpenJDK*
    too):
        ```
        $ export JAVA_HOME=/usr/lib64/java
        $ export ANDROID_HOME=/opt/Android/sdk
        $ export ANDROID_SDK_ROOT=$ANDROID_HOME
        $ export PATH=$ANDROID_HOME/tools/bin:$PATH
        $ sdkmanager --sdk_root=$ANDROID_HOME --install "tools"
        $ sdkmanager --sdk_root=$ANDROID_HOME --install "platforms;android-26"
        $ sdkmanager --sdk_root=$ANDROID_HOME --install "ndk;19.2.5345600"
        ```

    Optional: install *Android Emulator*:
        ```
        $ sdkmanager --sdk_root=$ANDROID_HOME --install "emulator"
        ```

## Development
- (Optional if you have installed *pyqtdepoy* on a virtual environment):
    ```
    $ pyenv activate android-test
    ```

- Export *Android* environment variables:
    ```
    $ export JAVA_HOME=/usr/lib64/java
    $ export ANDROID_HOME=/opt/Android/sdk
    $ export ANDROID_SDK_ROOT=$ANDROID_HOME
    $ export ANDROID_NDK_ROOT=$ANDROID_HOME/ndk/19.2.5345600
    $ export ANDROID_NDK_PLATFORM=android-26
    $ export PATH=$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-tools:$ANDROID_HOME/emulator:$ANDROID_NDK_ROOT:$PATH
    ```

## Building TODO
Building depends on your target. It can be **android-32** or **android-64**;
using *android-64* on the following commands.

TODO downloads
TODO source env

- Create system root:
    ```
    $ pyqtdeploy-sysroot --source-dir downloads --source-dir /opt/Qt5.12.3/5.12.3 --target android-64 sysroot.json --verbose
    ```

- Build the application:
    ```
    $ pyqtdeploy-build --target android-64 --sysroot sysroot-android-64 android-test.pdy --verbose
    $ cd build-android-64
    $ ../sysroot-android-64/host/bin/qmake
    $ make
    $ make INSTALL_ROOT=Test install
    ```

- Create the apk file, it wil be available at `build-android-64/Test/build/outputs/apk/debug/Test-debug.apk`:
    ```
    $ ../sysroot-android-64/host/bin/androiddeployqt --gradle --input android-libTest.so-deployment-settings.json --output Test --verbose
    ```

## Running
- Install on you device or emulator
    ```
    $ adb install Test/build/outputs/apk/debug/Test-debug.apk
    ```

- Run it on device or emulator from the app icon. Or from the development
machine:
    ```
    $ adb shell am start -n org.qtproject.example.Test/org.qtproject.qt5.android.bindings.QtActivity
    ```

## Misc
- Uninstall from the command line
    ```
    $ adb uninstall org.qtproject.example.Test
    ```

## References
- [pyqtdeploy User Guide](https://www.riverbankcomputing.com/static/Docs/pyqtdeploy/index.html)
- [pyqt-demo source](https://pypi.org/project/pyqtdeploy/#files)
- [Packaging PyQt application using pyqtdeploy for both Linux and Android](https://medium.com/@Lola_Dam/packaging-pyqt-application-using-pyqtdeploy-for-both-linux-and-android-32ac7824708b)
- [Using pyqtdeploy0.5 on Linux to cross compile a PyQt app for Android](https://plashless.wordpress.com/2014/08/19/using-pyqtdeploy0-5-on-linux-to-cross-compile-a-pyqt-app-for-android/)
- [PyBMAndroidQt](https://github.com/Bitmessage/PyBMAndroidQt/blob/master/pyqt5_androiddeploy_instruct.rst)

## TODO/CHECK
copy $ANDROID_HOME/platform-tools/source.properties to $ANDROID_HOME/tools
