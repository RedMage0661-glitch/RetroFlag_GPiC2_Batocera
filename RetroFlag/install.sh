#!/bin/bash

# Configure variables ----------------------------------------------
source_path=/boot/RetroFlag
script_path=/userdata/RetroFlag
service_path=/userdata/system/services
config_hdmi=config_hdmi.txt
config_lcd=config_lcd.txt
script_display=RetroFlag_GPiC2_Display.py
script_shutdown=RetroFlag_GPiC2_Shutdown.py
service_display=RetroFlag_GPiC2_Display
service_shutdown=RetroFlag_GPiC2_Shutdown

# Remount FS as RW --------------------------------------------------
echo "Remounting file systems in read / write mode"
mount -o remount, rw /boot
mount -o remount, rw /
sleep 2s

# Install configuration files ---------------------------------------
echo "Installing configuration files"
cp -f "$source_path/$config_lcd" "/boot/$config_lcd"
cp -f "$source_path/$config_hdmi" "/boot/$config_hdmi"
sleep 2s

# Install python scripts --------------------------------------------
echo "Installing python scripts"
if [ ! -d "$script_path" ];
	then
		mkdir "$script_path"
fi
cp -f "$source_path/$script_display" "$script_path/$script_display"
cp -f "$source_path/$script_shutdown" "$script_path/$script_shutdown"
sleep 2s

# Install Batocera services ------------------------------------------
echo "Installing Batocera services"
if [ ! -d "$service_path" ];
	then
		mkdir "$service_path"
fi
cp -f "$source_path/$service_display" "$service_path/$service_display"
cp -f "$source_path/$service_shutdown" "$service_path/$service_shutdown"
sleep 2s

# Enable the services -----------------------------------------------
batocera-services enable $service_display
batocera-services enable $service_shutdown
sleep 2s

# Reboot ------------------------------------------------------------
echo "RetroFlag GPi CASE 2 tools installation done. Will now reboot after 3 seconds."
sleep 3
shutdown -r now
