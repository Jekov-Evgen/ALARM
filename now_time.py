import datetime

class Time:
    def get_system_time(self):
        data = str(datetime.datetime.now())
        full_time = data.split(' ')
        time = full_time[1].split('.')
        return str(time[0][0:5:1])
    
    def get_user_time(self, hour, minute):
        full_user_time = str(datetime.time(hour, minute))
        time_trimming = full_user_time.split(':')
        user_time = time_trimming[0] + ':' + time_trimming[1]
        return str(user_time)
