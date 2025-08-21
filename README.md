<h2>Notes</h2>
<p>These instructions are for batocera 41 with the Raspberry Pi CM4.</p>
<p>You may need to flash your CM4 with the appropriate firmware before you start this process. My CM4 would not boot with the eMMC storage no matter what I did until I installed a different firmware. You can do this by using the Raspberry Pi Imager and installing the "Misc utilities images > Bootloader (Pi 4 family) > SD Card Boot" image.</p>
<p>The GPi Case 2 does not automatically switch between LCD and HDMI when plugged / unplugged from the dock. The scripts and services installed by this procedure automatically replace the content of config.txt and reboot the Raspberry Pi to boot in the correct display mode. If there is a way to switch between HDMI and LCD automatically without rebooting, I'm not smart enough to find it.</p>
<p>When the GPi Case 2 booted in LCD mode while it's configuration is still in HDMI mode (or vice-versa), it will detect that the current configuration is wrong, switch to the correct configuration and reboot. To avoid this, just plug or unplug into the dock while the unit is online so it will only reboot once.</p>

<h2>Special instructions for people using eMMC storage</h2>
<p>(not needed if you're using an SD card or other external storage)</p>
<ol>
   <li>Install the Compute Module Boot Installer ( https://github.com/raspberrypi/usbboot/tree/master/win32 )</li>
   <li>Plug your <strong>GPi Case 2</strong> into your computer by using the USB port in the back of the unit and boot</li>
   <li>Flip the power switch on to boot the Raspberry Pi</li>
   <li>Run <strong>C:\Program Files (x86)\Raspberry Pi\rpi-mass-storage-gadget64.bat</strong> on your computer to mount the eMMC storage in Windows as a USB Flash Drive</li>
</ol>

<h2>Instructions for installing batocera and modifying it for the GPi Case 2<br /></h2>
<p>(note that when I write "SD card" I mean "SD card or eMMC storage")</p>
<ol>
   <li>Install the batocera 41 Raspberry Pi 4B image on the SD card</li>
   <li>Unplug the SD card and replug it to get access to the files<br />(If you are using eMMC storage, you can force a reboot here by using <strong>Putty</strong> to open a terminal session and connecting to the COM port that was added by the mass storage gadget. Rerun <strong>rpi-mass-storage-gadget64.bat</strong> after the reboot to reconnect the USB drive)</li>
   <li>Copy the RetroFlag folder to the root of the SD card</li>
   <li>Replace the content of <strong>&lt;Drive Letter&gt;:\config.txt</strong> at the root of the SD card with the content of <strong>config_hdmi.txt</strong> (or <strong>config_lcd.txt</strong> if booting without the dock / hdmi)</li>
   <li>Eject the SD card and place it in the GPi Case 2<br />(if you are using eMMC, eject the USB drive and shutdown the Raspberry Pi using Putty to avoid corrupting the files)</li>
   <li>Open a terminal console (<strong>Ctrl+Alt+F3</strong>) from inside batocera, or configure your WiFi in batocera and open an SSH terminal window from another computer</li>
   <li>Install the configuration files, scripts and services by executing the following command <strong>sh /boot/RetroFlag/install.sh</strong></li>
   <li>If you are connected to the dock with an HDMI screen, go into <strong>SYSTEM SETTINGS</strong> and change the audio output to "BUILT-IN AUDIO DIGITAL STEREO (HDMI)"</li>
   <li>Congrats, your RetroFlag GPi Case 2 should now be able to safely shutdown and reboot in the appropriate mode depending on if you are connected to HDMI or using LCD</li>
</ol>

<h2>Technical Details</h2>
<p>install.sh should copy the relevant files to these locations</p>
<pre>
/config_hdmi.txt
/config_hdmi.txt
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
<p>&nbsp;</p>
<p>Credit to henryjfry and MrDuckHunt79 for providing their solutions on github which I used to build my own solution.</p>
<ul>
   <li>https://github.com/henryjfry/batocera_gpi2/tree/main</li>
   <li>https://github.com/MrDuckHunt79/gpic2bato</li>
</ul>
