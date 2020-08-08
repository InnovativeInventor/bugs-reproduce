import subprocess
import time
import logger

last_tried = time.time()
try:
    while True:
        if last_tried + 5 < time.time():
            ping = subprocess.run(["ping", "1.1.1.1", "-c", "1", "-w", "1"], stdout=subprocess.PIPE)
            if ", 100% packet loss" in ping.stdout.decode():
                logger.Logger.log_info("DOWN")
            elif ", 0% packet loss" in ping.stdout.decode():
                logger.Logger.log_info("UP")
            last_tried = time.time()

except KeyboardInterrupt:
    pass
