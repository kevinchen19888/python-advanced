# datetime:是Python处理日期和时间的标准库。

from datetime import datetime, timedelta, timezone


def get_date_time():
    # 获取当前日期和时间
    print(datetime.now())
    print(type(datetime.now()))
    # 获取指定日期和时间
    time = datetime(2021, 1, 30, 12, 20, 1)
    print(time)


# get_date_time()
def datetime_timestamp():
    global time
    # datetime转换为timestamp
    time = datetime(2020, 1, 22, 2, 10, 22)
    # 将datetime转换为 timestamp
    print(datetime.timestamp(time))
    # 时间戳转为日期(默认本地时间)
    t = 1429417200.0
    print(datetime.fromtimestamp(t))
    # 转为utc时间
    print(datetime.utcfromtimestamp(t))


# datetime_timestamp()


def datetime_str_fm():
    # 字符串转日期
    format = '%Y-%m-%d %H:%M:%S'
    print(datetime.strptime('2015-06-01 18:20:20', format))
    # 日期对象转为字符串
    print(datetime.now().strftime(format))


# datetime_str_fm()
def user_timedelta_cal():
    global time
    now = datetime.now()
    time = datetime(2020, 1, 28, 15, 40)
    print(now - timedelta(days=10))
    print(now - timedelta(days=2, hours=24))


# 通过timedelta这个类进行日期加减
# user_timedelta_cal()

# 本地时间转utc时间

def timezone_transfer():
    tz_utc8 = timezone(timedelta(hours=8))
    now = datetime.now()
    dt = now.replace(tzinfo=tz_utc8)
    print(dt)
    # 时区转换
    # 拿到utc时间,并强制设置时区为utc+0:00
    utc_dt = datetime.now().replace(tzinfo=timezone.utc)
    print(utc_dt)
    # 将时区转为北京时间
    bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
    print(bj_dt)


# timezone_transfer()

""""
时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。

datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关
"""