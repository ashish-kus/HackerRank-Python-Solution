
import calendar

def get_time_seconds(t):
    days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    t = t.split()
    t_time = t[4].split(':')
    print(t, t_time)

    # convert to time.struct_time
    t_struct_time = (int(t[3]), months.index(t[2])+1, int(t[1]), int(t_time[0]), int(t_time[1]), int(t_time[2]), days.index(t[0]), None, 0)
    # calculate seconds since 1970
    t_sec = calendar.timegm(t_struct_time)
    # time zone difference
    diff = int(t[5][1:3]) * 60 * 60 + int(t[5][3:]) * 60
    if t[5][0] == "-":
        t_sec = t_sec + diff
    else:
        t_sec = t_sec - diff

    return t_sec


# Complete the time_delta function below.
def time_delta(t1, t2):
    return str(abs(get_time_seconds(t1) - get_time_seconds(t2)))

