from datetime import date, datetime

def get_datetime():
    dt_tm_addons=''
    today = date.today()
    d = today.strftime("%b-%d-%Y")
    time_now = datetime.now()
    t = time_now.strftime("%H_%M_%S")
    dt_tm_addons = '_' + d + '_' + t
    return dt_tm_addons