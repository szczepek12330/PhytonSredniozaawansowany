import zoneinfo
from datetime import datetime
from zoneinfo import ZoneInfo

today = datetime.today()
dt = datetime(2022, 11, 29, tzinfo=ZoneInfo("Europe/Warsaw"))
print(zoneinfo.available_timezones())
print(dt)