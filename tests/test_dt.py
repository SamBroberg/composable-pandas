from datetime import datetime
from composable_pandas.dt import normalize
from composable_pandas.dt import round
from composable_pandas.dt import strftime
from composable_pandas.dt import to_period
from composable_pandas.dt import floor

from dateutil.tz import (
    tzlocal,
    tzutc,
)
from datetime import (
    date,
    datetime,
    time,
    timedelta,
    timezone,
)
from pytz import (
    FixedOffset,
    utc,
)
import pandas._testing as tm

from pandas.io.json._normalize import nested_to_record

import numpy as np
import pytest
import json
import pandas.util._test_decorators as td

from pandas import (
    DataFrame,
    Index,
    Series,
    json_normalize,
    date_range,
    DatetimeIndex,
    Timestamp,
    to_datetime
)

#@pytest.fixture
#  def state_data():
#     return [
#         {
#             "counties": [
#                 {"name": "Dade", "population": 12345},
#                 {"name": "Broward", "population": 40000},
#                 {"name": "Palm Beach", "population": 60000},
#             ],
#             "info": {"governor": "Rick Scott"},
#             "shortname": "FL",
#             "state": "Florida",
#         },
#         {
#             "counties": [
#                 {"name": "Summit", "population": 1234},
#                 {"name": "Cuyahoga", "population": 1337},
#             ],
#             "info": {"governor": "John Kasich"},
#             "shortname": "OH",
#             "state": "Ohio",
#         },
#     ]

# def test_simple_normalize(state_data):
#     result = json_normalize(state_data[0], "counties")
#     expected = DataFrame(state_data[0]["counties"])
#     tm.assert_frame_equal(result, expected)

# TIMEZONES = [
# None,
# "UTC",
# "US/Eastern",
# "Asia/Tokyo",
# "dateutil/US/Pacific",
# "dateutil/Asia/Singapore",
# "+01:15",
# "-02:15",
# "UTC+01:15",
# "UTC-02:15",
# tzutc(),
# tzlocal(),
# FixedOffset(300),
# FixedOffset(0),
# FixedOffset(-300),
# timezone.utc,
# timezone(timedelta(hours=1)),
# timezone(timedelta(hours=-1), name="foo"),
# ]
# TIMEZONE_IDS = [repr(i) for i in TIMEZONES]

# @td.parametrize_fixture_doc(str(TIMEZONE_IDS))
# @pytest.fixture(params=TIMEZONES, ids=TIMEZONE_IDS)
# def tz_naive_fixture(request):

#     """
#     Fixture for trying timezones including default (None): {0}
#     """
#     return request.param

def test_normalize():
    rng = date_range("1/1/2000 9:30", periods=10, freq="D")

    result = rng >> normalize()
    expected = date_range("1/1/2000", periods=10, freq="D")
    tm.assert_index_equal(result, expected)

@pytest.fixture
def datetime_series():
    """
    Fixture for Series of floats with DatetimeIndex
    """
    s = tm.makeTimeSeries()
    s.name = "ts"
    return s

def test_round(datetime_series):
    datetime_series.index.name = "index_name"
    result = datetime_series >> round()
    expected = Series(np.round(datetime_series.values), index=datetime_series.index, name="ts")
    tm.assert_series_equal(result, expected)
    assert result.name == datetime_series.name

def test_strftime():
    # GH 10086
    s = Series(date_range("20130101", periods=5))
    result = s.dt.strftime("%Y/%m/%d")
    expected = Series(["2013/01/01", "2013/01/02", "2013/01/03", "2013/01/04", "2013/01/05"])
    tm.assert_series_equal(result, expected)

@pytest.mark.parametrize("input_vals", [("2001"), ("NaT")])
def test_to_period(input_vals):
    # GH#21205
    expected = Series([input_vals], dtype="Period[D]")
    result = Series([input_vals], dtype="datetime64[ns]") >> to_period()
    tm.assert_series_equal(result, expected)

def test_floor():
    s = Series(Timestamp("20130101 09:10:11"))
    result = s >> floor()
    expected = Series(Timestamp("20130101"))
    tm.assert_series_equal(result, expected)