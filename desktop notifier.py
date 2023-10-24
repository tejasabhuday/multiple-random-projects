import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title="ABBE YE DEKH",
            message="Tu ruk mat jaio aalsi",
            timeout= 10
        )
        time.sleep(3600)
