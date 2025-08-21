Credit to henryjfry and MrDuckHunt79 for providing their solutions on github which I used to build my own solution.
https://github.com/henryjfry/batocera_gpi2/tree/main
https://github.com/MrDuckHunt79/gpic2bato

These instructions are for batocera 41 with the Raspberry Pi CM4.

Notes
You may need to flash your CM4 with the appropriate firmware before you start this process. My CM4 would not boot with the eMMC storage no matter what I did until I installed a different firmware. You can do this by using the Raspberry Pi Imager and installing the "Misc utilities images > Bootloader (Pi 4 family) > SD Card Boot" image.
The GPi Case 2 does not automatically switch between LCD and HDMI when plugged / unplugged from the dock. The scripts and services installed by this procedure automatically replace the content of config.txt and reboot the Raspberry Pi to boot in the correct display mode. If there is a way to switch between HDMI and LCD automatically without rebooting, I'm not smart enough to find it.
When the GPi Case 2 booted in LCD mode while it's configuration is still in HDMI mode (or vice-versa), it will detect that the current configuration is wrong, switch to the correct configuration and reboot. To avoid this, just plug or unplug into the dock while the unit is online so it will only reboot once.

Special instructions for people using eMMC storage (not needed if you're using an SD card or other external storage)
1- Install the Compute Module Boot Installer ( https://github.com/raspberrypi/usbboot/tree/master/win32 )
2- Plug your GPi Case 2 into your computer by using the USB port in the back of the unit and boot
3- Flip the power switch on to boot the Raspberry Pi 
4- Run "rpi-mass-storage-gadget64.bat" on your computer from the Compute Module Boot install location ( typically C:\Program Files (x86)\Raspberry Pi ) to mount the eMMC storage in Windows as a USB Flash Drive

Instructions for installing batocera and modifying it for the GPi Case 2
(note that when I write "SD card" I mean "SD card or eMMC storage")
1- Install the batocera 41 Raspberry Pi 4B image on the SD card
2- Unplug the SD card and replug it to get access to the files
   (If you are using eMMC storage, you can force a reboot here by using Putty to open a terminal session and connecting to the COM port that was added by the mass storage gadget. Rerun "rpi-mass-storage-gadget64.bat" after the reboot to reconnect the USB drive)
2- Copy the RetroFlag folder to the root of the SD card
3- Replace the content of "<Drive Letter>:\config.txt" at the root of the SD card with the content of "config_hdmi.txt" (or "config_lcd.txt" if booting without the dock / hdmi)
4- Eject the SD card and place it in the GPi Case 2
   (if you are using eMMC, eject the USB drive and shutdown the Raspberry Pi using Putty to avoid corrupting the files)
5- Open a terminal console (Ctrl+Alt+F3) from inside batocera, or configure your WiFi in batocera and open an SSH terminal window from another computer
6- Install the configuration files, scripts and services by executing the following command "sh /boot/RetroFlag/install.sh"
7- If you are connected to the dock with an HDMI screen, go into SYSTEM SETTINGS and change the audio output to "BUILT-IN AUDIO DIGITAL STEREO (HDMI)"
8- Congrats, your RetroFlag GPi Case 2 should now be able to safely shutdown and reboot in the appropriate mode depending on if you are connected to HDMI or using LCD

install.sh should copy the relevant files to these locations
/config_hdmi.txt
/config_hdmi.txt
/userdata/RetroFlag/RetroFlag_GPiC2_Display.py 
/userdata/RetroFlag/RetroFlag_GPiC2_Shutdown.py
/userdata/system/services/RetroFlag_GPiC2_Display
/userdata/system/services/RetroFlag_GPiC2_Shutdown

config_hdmi.txt
This is the configuration file that contains the settings for the dock + hdmi to work

config_lcd.txt
This is the configuration file that contains the settings for the LCD to work

config.bak
This is a backup of the original batocera 41 configuration file

config.txt
This is just a copy of the config_hdmi.txt that I renamed so I could just copy it over /config.txt instead of having to edit the content every time I tried something new.

RetroFlag_GPiC2_Display.py 
Manages switching from LCD to HDMI display mode. It does this by detecting when HDMI is plugged in and replaces the config.txt file with config_hdmi.txt or config_lcd.txt and then rebooting. Sorry, I couldn't find a way to setup live switching between HDMI and LCD.

RetroFlag_GPiC2_Shutdown.py
Manages the safe shutdown switch and sleep button.

RetroFlag_GPiC2_Display
This is the bash script that acts as a service for switching between LCD and HDMI modes

RetroFlag_GPiC2_Shutdown
This is the bash script that acts as a service for performing a safe shutdown when the power switch is turned off or the sleep button is pressed
