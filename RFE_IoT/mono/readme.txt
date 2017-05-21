RF Explorer IoT for Raspberry Pi
--------------------------------

Mono libraries, examples and tools

Included libraries
------------------

RFExplorerCommunicator.dll - the main proxy for RF Explorer devices, including Spectrum Analyzers, Signal Generator, and IoT modules
Raspberry.*.dll - Compiled and published versions from 

Included examples
-----------------

* RFExplorer_ScanRange -  RF Explorer Scan Range command line tool. Use this tool to quickly and easily check activity on a given frequency range.

To test this tool, run from command line:

    sudo mono RFExplorer_ScanRange.exe /IOT 200 300
    
This command will scan a frequency range from 200 to 300Mhz, using default configuration for RF Explorer 3G+ IoT module, displaying peak frequency detected in that range.

More details on readme.txt of the folder tool

* TestMono_GUI - A simple "Hello World" window to test GUI in Raspberry Pi. It should be used under X11 environment, it won't work from command line.

To test this example, run from command line:

    mono TestMono_GUI.exe
    
Alternatively you can just double-click on the TestMono_GUI.exe from the Raspberry Pi file manager.    
