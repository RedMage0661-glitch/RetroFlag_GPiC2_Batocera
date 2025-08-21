import RPi.GPIO as GPIO
import os
import time
import logging
import signal

# Constants
HDMI_PIN = 18
LCD_CONFIG_FILE = "/boot/config_lcd.txt"
HDMI_CONFIG_FILE = "/boot/config_hdmi.txt"

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Temporary replacement for broken GPIO.wait_for_edge
def wait_for_edge(pin, trigger = GPIO.BOTH, poll = 0.1):
    new_state = GPIO.input(pin)
    
    while True:
        old_state = new_state
        while new_state == old_state:
            time.sleep(poll)
            new_state = GPIO.input(pin)
        
        if new_state == GPIO.HIGH and (trigger == GPIO.RISING or trigger == GPIO.BOTH):
            return new_state
            
        elif new_state == GPIO.LOW and (trigger == GPIO.FALLING or trigger == GPIO.BOTH):
            return new_state

# Changes the configuration file
def switch_config(config_file):
    try:
        logging.info(f"Replacing config.txt with {config_file}")
        os.system("mount -o remount, rw /boot")
        os.system("mount -o remount, rw /")
        os.system(f"cp -f {config_file} /boot/config.txt")
        
        logging.info("Restarting system")
        os.system("batocera-es-swissknife --emukill")
        time.sleep(1)
        os.system("shutdown -r now")
        exit(0)
        
    except Exception as e:
        logging.error(f"Unable to complete restart sequence: {e}")
    
    finally:
        GPIO.cleanup()

# Handles termination signals
def signal_handler(sig, frame):
    logging.info("Terminating program...")
    GPIO.cleanup()
    exit(0)

if __name__ == "__main__":
    # Setup event handlers
    signal.signal(signal.SIGINT, signal_handler)  # Handle Ctrl+C
    signal.signal(signal.SIGTERM, signal_handler)  # Handle termination signals

    # Initialize GPIO settings
    logging.info("Initializing GPIO")
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(HDMI_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    # Get the HDMI pin expected state based on the config.txt file
    logging.info("Checking configured display mode vs HDMI pin state")
    configured_state = GPIO.HIGH
    with open("/boot/config.txt") as f:
        if 'enable_dpi_lcd=1' in f.read():
            configured_state = GPIO.LOW
    
    # Get the HDMI pin startup state and switch config if it doesn't match the config.txt file
    startup_state = GPIO.input(HDMI_PIN)
    if startup_state != configured_state:
        if startup_state == GPIO.HIGH:
            switch_config(HDMI_CONFIG_FILE)
        else:
            switch_config(LCD_CONFIG_FILE)
    
    # Monitor HDMI pin state
    logging.info("Monitoring HDMI pin state")
    while True:
        #current_state = GPIO.wait_for_edge(HDMI_PIN)
        current_state = wait_for_edge(HDMI_PIN, GPIO.BOTH, 1)
        logging.info("HDMI pin state changed")
        if current_state == GPIO.HIGH:
            switch_config(HDMI_CONFIG_FILE)
        else:
            switch_config(LCD_CONFIG_FILE)
            
        time.sleep(1)
