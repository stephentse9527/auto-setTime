import http.client
import time
import os
import ctypes, sys

def get_web_time(host):
    conn = http.client.HTTPConnection(host)
    conn.request("GET", "/")
    r = conn.getresponse()
    ts = r.getheader('date')  # 获取http头date部分
    print(ts)
    ltime = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
    print(ltime)
    ttime = time.localtime(time.mktime(ltime) + 8 * 60 * 60)
    print(ttime)
    dat = "date %u-%02u-%02u" % (ttime.tm_year, ttime.tm_mon, ttime.tm_mday)
    tm = "time %02u:%02u:%02u" % (ttime.tm_hour, ttime.tm_min, ttime.tm_sec)
    os.system(dat)
    os.system(tm)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    # Code of your program here
    while True:
        try:
            get_web_time('www.baidu.com')
        except Exception:
            pass
        finally:
            time.sleep(10)
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
