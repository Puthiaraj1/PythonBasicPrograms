import pytz
import datetime

tz_list = ["quit", "Asia/kolkata","America/New_York", "Europe/London", "Asia/Shanghai", "Europe/Paris","Asia/Tokyo","Europe/Moscow" ]

for i in range(len(tz_list)):
    print("{} - {}".format(i, tz_list[i]))

selected_tz = int(input("Please select the time zone number to display :"))
while True:
    if selected_tz == 0:
        break
    if selected_tz < len(tz_list):
        tz_cnt_set = pytz.timezone(tz_list[selected_tz])
        tz_cnt_local_time = datetime.datetime.now(tz=tz_cnt_set)
        print(" The time in {} is {} {}".format(tz_list[selected_tz], tz_cnt_local_time.strftime('%A %x %X %z'), tz_cnt_local_time.tzname()))
    selected_tz = int(input())

