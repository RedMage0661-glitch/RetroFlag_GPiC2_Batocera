<h2>Installation procedure for Raspberry Pi firmware</h2>
<p>If your CM4 doesn't boot out of the box with any image on your SD Card or eMMC storage (like mine did), it may need to be flashed with the SD Card firmware.</p>
<ol>
   <li>Download and install the <strong>Raspberry Pi imager</strong><br />( https://www.raspberrypi.com/software/ )</li>
   <li>Plug the SD card into a card reader or USB adapter to mount it into Windows as a USB Drive</li>
   <li>
      Open <strong>Raspberry Pi imager</strong> and install the bootloader using the following settings :
      <ul>
         <li>Raspberry Pi Device => RASPBERRY PI 4</li>
         <li>Operating System => Misc Utility Images => Bootloader (Pi 4 family) => SD Card Boot</li>
         <li>Storage => USB Drive added in the previous step</li>
      </ul>
   </li>
   <li>Plug the SD card into the case</li>
   <li>Switch the case's power switch on to flash the CM4</li>
   <li>Wait until the flashing process is done and switch the case's power switch to off</li>
   <li>Remove the SD card</li>
   <li>You are now ready to install a new image on the SD card</li>
</ol>
<p>The process for eMMC is mostly the same, but you'll need to use the mass storage gadget to connect the eMMC as a USB Drive. Look at the <strong>Installation procedure for batocera 41 on Raspberry Pi CM4 eMMC</strong> section down below to see how.</p>

<h2>Installation procedure for batocera 41 on Raspberry Pi CM4 lite</h2>
<ol>
   <li>Download and install the <strong>Raspberry Pi imager</strong><br />( https://www.raspberrypi.com/software/ )</li>
   <li>Download the batocera 41 <strong>Raspberry Pi 4 B</strong> image</li>
   <li>Plug the SD card into a card reader or USB adapter to mount it into Windows as a USB Drive<br />(I will be using <strong>X</strong> as a placeholder for the SD card's drive letter through the rest of this procedure)</li>
   <li>Install the image on the SD card</li>
   <li>Unplug the SD card and replug it to remount the drive</li>
   <li>Copy the <strong>RetroFlag</strong> folder to <strong>X:\</strong></li>
   <li>Replace <strong>X:\config.txt</strong> with <strong>X:\RetroFlag\config.txt</strong></li>
   <li>Eject the USB Drive and place the SD card in the case</li>
   <li>Place the case in the dock with a working HDMI monitor and keyboard attached</li>
   <li>Switch the case's power switch on to boot into batocera</li>
   <li>When batocera is fully loaded, press <strong>Ctrl+Alt+F3</strong> to open a terminal window, or configure your WiFi in batocera and open a terminal window from another computer using SSH</li>
   <li>Execute <strong>sh /boot/RetroFlag/install.sh</strong> to install the configuration files, scripts and services</li>
   <li>System should reboot automatically at this point</li>
   <li>While connected to the docking with an HDMI display, go into <strong>SYSTEM SETTINGS</strong> and change the audio output to "BUILT-IN AUDIO DIGITAL STEREO (HDMI)"</li>
   <li>Congrats, your RetroFlag GPi Case 2 is now ready!</li>
</ol>

<h2>Installation procedure for batocera 41 on Raspberry Pi CM4 with eMMC storage</h2>
<ol>
   <li>Download and install the <strong>Compute Module Boot</strong><br />( https://github.com/raspberrypi/usbboot/tree/master/win32 )</li>
   <li>Download and install the <strong>Raspberry Pi imager</strong><br />( https://www.raspberrypi.com/software/ )</li>
   <li>Download the batocera 41 <strong>Raspberry Pi 4 B</strong> image</li>
   <li>Connect the RetroFlag GPi Case 2 to your computer using the USB micro B connector in the back of the case ( behind the fake cartridge )</li>
   <li>Place the case in the dock with a working HDMI monitor and keyboard attached</li>
   <li>Switch the case power switch on to boot the Raspberry Pi</li>
   <li>Run <strong>C:\Program Files (x86)\Raspberry Pi\rpi-mass-storage-gadget64.bat</strong> on your computer to mount the eMMC storage in Windows as a USB Drive<br />(I will be using <strong>X</strong> as a placeholder for the eMMC's drive letter through the rest of this procedure)</li>
   <li>Install the image on the on the USB Drive added in the previous step</li>
   <li>Switch the case power switch off and then back on to reboot the Raspberry Pi</li>
   <li>Rerun <strong>C:\Program Files (x86)\Raspberry Pi\rpi-mass-storage-gadget64.bat</strong> on your computer to remount the eMMC storage</li>
   <li>Copy the <strong>RetroFlag</strong> folder to <strong>X:\</strong></li>
   <li>Replace <strong>X:\config.txt</strong> with <strong>X:\RetroFlag\config.txt</strong></li>
   <li>Eject the USB Drive and switch the case's power switch to off</li>
   <li>Switch the case's power switch on to boot into batocera</li>
   <li>When batocera is fully loaded, press <strong>Ctrl+Alt+F3</strong> to open a terminal window, or configure your WiFi in batocera and open a terminal window from another computer using SSH</li>
   <li>Execute <strong>sh /boot/RetroFlag/install.sh</strong> to install the configuration files, scripts and services</li>
   <li>System should reboot automatically at this point</li>
   <li>While connected to the docking with an HDMI display, go into <strong>SYSTEM SETTINGS</strong> and change the audio output to "BUILT-IN AUDIO DIGITAL STEREO (HDMI)"</li>
   <li>Congrats, your RetroFlag GPi Case 2 is now ready!</li>
</ol>

<h2>Technical Details</h2>
<p>install.sh should copy the relevant files to these locations</p>
<pre>
/boot/config_hdmi.txt
/boot/config_hdmi.txt
/userdata/RetroFlag/RetroFlag_GPiC2_Display.py 
/userdata/RetroFlag/RetroFlag_GPiC2_Shutdown.py
/userdata/system/services/RetroFlag_GPiC2_Display
/userdata/system/services/RetroFlag_GPiC2_Shutdown
</pre>

<h3>config_hdmi.txt</h3>
<p>This is the configuration file that contains the settings for the dock + hdmi to work</p>

<h3>config_lcd.txt</h3>
<p>This is the configuration file that contains the settings for the LCD to work</p>

<h3>config.bak</h3>
<p>This is a backup of the original batocera 41 configuration file</p>

<h3>config.txt</h3>
<p>This is just a copy of the config_hdmi.txt that I renamed so I could just copy it over /config.txt instead of having to edit the content every time I tried something new.</p>

<h3>RetroFlag_GPiC2_Display.py</h3>
<p>Manages switching from LCD to HDMI display mode. It does this by detecting when HDMI is plugged in and replaces the config.txt file with config_hdmi.txt or config_lcd.txt and then rebooting. Sorry, I couldn't find a way to setup live switching between HDMI and LCD.</p>

<h3>RetroFlag_GPiC2_Shutdown.py</h3>
<p>Manages the safe shutdown switch and sleep button.</p>

<h3>RetroFlag_GPiC2_Display</h3>
<p>This is the bash script that acts as a service for switching between LCD and HDMI modes</p>

<h3>RetroFlag_GPiC2_Shutdown</h3>
<p>This is the bash script that acts as a service for performing a safe shutdown when the power switch is turned off or the sleep button is pressed</p>

<h2>Notes</h2>
<p>These instructions assume you are doing these procedures from a Windows 11 computer. If you want to do this from a Linux computer, you'll need to make some adjustments.</p>
<p>The GPi Case 2 does not automatically switch between LCD and HDMI when plugged / unplugged from the dock. The scripts and services installed by this procedure automatically replace the content of config.txt and reboot the Raspberry Pi to boot in the correct display mode. If there is a way to switch between HDMI and LCD automatically without rebooting, I'm not smart enough to find it.</p>
<p>When the GPi Case 2 is booted in LCD mode while it's configuration is still in HDMI mode (or vice-versa), it will detect that the current configuration is wrong, switch to the correct configuration and reboot. To avoid this additional delay, just plug or unplug with the dock while the unit is online so it will only reboot once.</p>

<p>&nbsp;</p>
<p>Credit to henryjfry and MrDuckHunt79 for providing their solutions on github which I used to build my own solution.</p>
<ul>
   <li>https://github.com/henryjfry/batocera_gpi2/tree/main</li>
   <li>https://github.com/MrDuckHunt79/gpic2bato</li>
</ul>
