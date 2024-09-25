import datetime
import ctypes

class Time:
    def get_system_time(self):
        lib = ctypes.CDLL('TIME_P/TIME_P.dll')
        lib.GetTime.restype = ctypes.c_char_p
        str_time = str(lib.GetTime())
        list_time = []
        
        for i in range(len(str_time)):
            if str_time[i].isnumeric() == True:
                list_time.append(str_time[i])
                
        result_time = list_time[2] + list_time[3] + ':' + list_time[4] + list_time[5]
        
        return str(result_time)
    
    
    def get_user_time(self, hour, minute):
        full_user_time = str(datetime.time(hour, minute))
        
        time_trimming = full_user_time.split(':')
        user_time = time_trimming[0] + ':' + time_trimming[1]
        
        return str(user_time)