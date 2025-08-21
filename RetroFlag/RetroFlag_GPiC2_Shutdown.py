import os
import time
import signal
import logging
import RPi.GPIO as GPIO

# Constants
POWER_PIN = 26
POWEREN_PIN = 27
SHUTDOWN_COMMAND = "poweroff"
KILL_COMMAND = "batocera-es-swissknife --emukill"

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

# Graceful exit handler
def signal_handler(sig, frame):
    logging.info("Terminating program...")
    GPIO.cleanup()
    exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)  # Handle Ctrl+C
    signal.signal(signal.SIGTERM, signal_handler)  # Handle termination signals

    # Initialize GPIO settings
    logging.info("Initializing GPIO")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(POWER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(POWEREN_PIN, GPIO.OUT)
    GPIO.output(POWEREN_PIN, GPIO.HIGH)
    GPIO.setwarnings(False)
    
    # Monitor the power button
    logging.info("Monitoring power button")
    while True:
        #GPIO.wait_for_edge(POWER_PIN, GPIO.FALLING)
        wait_for_edge(POWER_PIN, GPIO.FALLING, 1)
        
        logging.error("Powering off the system")
        try:
            os.system("batocera-es-swissknife --emukill")
            time.sleep(1)
            os.system("poweroff")
            exit(0)
            
        except Exception as e:
            logging.error(f"Unable to complete power off sequence: {e}")
            
        finally:
            GPIO.cleanup()
            
        time.sleep(1)