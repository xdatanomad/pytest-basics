import pytest
from datetime import datetime as dt
from datetime import timezone as tz
from pytz import timezone

import pytz

@pytest.mark.tz
def test_utcnow():
    
    print()

    # get the current time in UTC
    now = dt.now(tz.utc)
    # print the current time in yyyy-mm-dd hh:mm:ss format
    print("utc time: ", now.strftime('%Y-%m-%d %I:%M:%S %p %Z'))

    assert now.tzinfo == tz.utc
    assert now.utcoffset() == tz.utc.utcoffset(now)

@pytest.mark.tz
def test_current_tz_to_utc():
    
    print()

    # get the current time in UTC
    now = dt.now(tz.utc)
    # print the current time in yyyy-mm-dd hh:mm:ss format
    print("utc time:", now.strftime('%Y-%m-%d %I:%M:%S %p %Z'))

    # get the current time in the local timezone
    now_local = dt.now()
    # print the current time in yyyy-mm-dd hh:mm:ss format
    print("local time:", now_local.strftime('%Y-%m-%d %I:%M:%S %p %Z'), "tzinfo:", now_local.tzinfo, "utcoffset:", now_local.utcoffset(), "tzname:")

    # convert the local time to UTC
    now_local_utc = now_local.astimezone(tz.utc)
    # print the current time in yyyy-mm-dd hh:mm:ss format
    print("local time converted to utc:", now_local_utc.strftime('%Y-%m-%d %I:%M:%S %p %Z'))

    assert now_local_utc.tzinfo == tz.utc
    assert now_local_utc.utcoffset() == tz.utc.utcoffset(now_local_utc)
    

@pytest.mark.tz
@pytest.mark.parametrize("tzname", ["US/Eastern", "US/Pacific", "Europe/London", "Asia/Kolkata"])
def test_assign_timezone_and_convert_to_utc(tzname: str):
    
    print()

    local_time = dt.now()

    
    # print the current time in yyyy-mm-dd hh:mm:ss format
    print("time without timezone:", local_time.strftime('%Y-%m-%d %I:%M:%S %p %Z'))

    # local_tz = pytz.timezone(tzname)

    # get the timezone object
    to_tz = timezone(tzname)
    
    # assign the timezone to the datetime object
    # dt_with_timezone = local_time.replace(tzinfo=to_tz)
    dt_with_timezone = to_tz.localize(local_time)
    
    # print the current time in yyyy-mm-dd hh:mm:ss format
    print("time with timezone:", dt_with_timezone.strftime('%Y-%m-%d %I:%M:%S %p %Z'))

    # convert the time with timezone to UTC
    dt_with_timezone_utc = dt_with_timezone.astimezone(pytz.utc)

    # print the current time in yyyy-mm-dd hh:mm:ss format
    print("time with timezone converted to utc:", dt_with_timezone_utc.strftime('%Y-%m-%d %I:%M:%S %p %Z'))

    assert dt_with_timezone_utc.tzinfo == pytz.utc
    assert dt_with_timezone_utc.utcoffset() == tz.utc.utcoffset(dt_with_timezone_utc)
