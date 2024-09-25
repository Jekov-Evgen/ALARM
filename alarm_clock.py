from now_time import Time
from time import sleep


class Examination:
    def check(self, user_time_hour, user_time_minute):
        time = Time()
        system = time.get_system_time()
        user = time.get_user_time(user_time_hour, user_time_minute)
        
        while user != system:
            system = time.get_system_time()
            sleep(1)
            
        return True
            