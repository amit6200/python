from plyer import notification
import time

if __name__ == '_main_':
    while True:
        
       notification.notify(
           
            title="*** Take Rest ***",
            message="Rest is very useful for human being",
            app_icon="chatlogo.jpg",
            timeout=5)
            
       time.sleep(20) 