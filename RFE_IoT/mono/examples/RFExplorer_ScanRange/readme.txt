RF Explorer Scan Range tool
---------------------------

This tool is a multi-platform command line application. It can be used natively in Windows, but it also works fine in Linux and MacOS with Mono.

The tool can be used with following products:

    * RF Explorer Spectrum Analyzer Handheld units
    * RF Explorer IoT for Raspberry Pi
    * RF Explorer RackPro

Platform distribution files
---------------------------

* Windows:
    RFExplorer_ScanRange.exe    - Native Windows OS tool, required .NET 4.0 installed

* Linux:
    * RaspberryPi:
        * Light:
            rfe_scan_range      - Suggested for official RF Explorer IoT Raspberry Pi distribution images with compatible Mono already installed
        * Complete:
            rfe_scan_range      - Complete bundle with all dependencies linked, may work even if Mono is not installed
    * Others:                   - Required Mono installed
* MacOS:
    * Light:
        rfe_scan_range          - Suggested for users with Mono 4.8.0 already installed in the system
    * Complete:
        rfe_scan_range          - Complete bundle with all dependencies linked, may work even if Mono is not installed


Parameters
----------

Format:
    RFExplorer_ScanRange [/IOT | /p:PORT] [/s: [low|high]] [/csv:path] [/rfe:path] [/time:secs] StartRangeMHZ  StopRangeMHZ

Required parameters:
    StartRangeMHZ: is a number in range valid for your Analyzer model to start scan sweep
    StopRangeMHZ: is a number in range valid for your Analyzer model to stop scan sweep
    
    Note: one of /IOT or /p parameters are required
    
Optional parameters:
    /IOT: Connect to a Raspberry Pi assembled RF Explorer IoT board
    /p: Connect to a USB port such as COM3 or /dev/ttyUSB0
        Using AUTO assumes only RF Explorer connected to USB port
    /s: [low|high] Baudrate speed being high=500Kbps default, and low=2400bps
    /csv: Output CSV filename (no extension) to save consecutive scans
    /rfe: Output .RFE binary filename (no extension) to save consecutive scans
    /time: total seconds to scan before close automatically. If not specified will scan 1 hour and close automatically.
       If set to 0 will do one single scan and close automatically.
       If set to -1 will run forever.
    /res: [high|normal|low] For IOT only: resolution used for scan data eq to 4096, 1024 or 112 points
       Note: Current limit for full range scanning is up to 1000MHz
             Some models and configurations may have limited sweep points

Keyboard control:
    <Q> Finish application
    <LEFT> move scan range to low frequency equals to span
    <RIGHT> move scan range to high frequency equals to span

Examples Windows
----------------

This example connects to a RF Explorer automatically and scan 200-300MHz with output to screen only. This works if only one RF Explorer device is connected to USB.

    RFExplorer_ScanRange.exe /p:AUTO 200 300
    
Example but specifically connecting to COM3 port
    
    RFExplorer_ScanRange.exe /p:COM3 200 300
    
Example running for 10 hours (10*3600secs)
    
    RFExplorer_ScanRange.exe /p:AUTO /time:36000 200 300    
    
Example storing /csv files into c:\temp\csv folder with name samples_xxxx.csv automatically created by the tool

    RFExplorer_ScanRange.exe /p:COM3 200 300 /csv:\c:\temp\csv\samples
    
Examples Linux
--------------

Same as Windows examples, but you should use "sudo mono RFExplorer_ScanRange.exe" in replacement of RFExplorer_ScanRange.exe
    
    
Examples Raspberry Pi IOT
-------------------------

For specific RF Explorer IoT boards, you should use the available Raspberry Pi images from www.rf-explorer.com/downloads - other OS implementations may not work correctly.

For using Raspberry Pi as a USB host for a handheld RF Explorer (as opposed to IoT board) please use next section as a standard Linux box.

All examples above should work for the IoT boards, but requires /IOT switch as opposed to /p. Example below scanning 200-300 MHz with up to 60 seconds scan.
    
    sudo rfe_scan_range /IOT 200 300 /time:60
    
The IoT boards may use extended sweep points (not available yet in Handheld firmware). This example below will scan 4096 sweep points - this is slower but increase resolution scan for narrow channels and lower noise.

    sudo rfe_scan_range /IOT 200 300 /res:high /time:60
    
Examples MacOS X
----------------

Equivalent to above example, except you should use "sudo rfe_scan_range" in replacement of RFExplorer_ScanRange.exe

Example storing /csv files into /tmp/csv folder with name samples_xxxx.csv automatically created by the tool

    sudo rfe_scan_range /p:AUTO 200 300 /csv:/tmp/csv
    
Notes: There are two versions of the tool in folders Light and Complete. If you have Mono installed in your system, we suggest using Light version, but the Complete should work too. If you do not have Mono installed, try the Complete version only - if it fails you need to install Mono in your system.

Mono versions suggested:

    * Raspberry Pi: already installed in official IoT images - check www.rf-explorer.com/downloads
    * MacOS X: version 4.8.0 available on this link: http://micro-aruba.arocholl.com/download/sw/mac/MonoFramework-MDK-4.8.0.520.macos10.xamarin.universal.pkg
    * Linux: any latest version available for your Distro - check "yum", "apt-get" or equivalent tool.
