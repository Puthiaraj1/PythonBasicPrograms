import pytz
import datetime

country = 'Europe/Moscow'
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country,local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

for x in sorted(pytz.country_names):
    print("{} : {} : {}".format(x, pytz.country_names[x], pytz.country_timezones.get(x)))

# local_time = datetime.datetime.now()
# utc_time = datetime.datetime.utcnow()
#
# print("Native lcoal time {}".format(local_time))
# print("Native UTC time {}".format(utc_time))
#
# aware_local_time = pytz.utc.localize(utc_time).astimezone()
# aware_utc_time = pytz.utc.localize(utc_time)
#
# print("Aware local time {}, time zone {} ".format(aware_local_time, aware_local_time.tzinfo))
# print("Aware UTC {}, time zone {}".format(aware_utc_time, aware_utc_time.tzinfo))
#
# gap_time = datetime.datetime(2020, )

