from datetime import datetime
from typing import Union

from numpy.typing import ArrayLike
from pandas import Series, to_datetime
from pytz import timezone

TZ_COL = timezone('America/Bogota')
TZ_UTC = timezone('UTC')
NUMERIC = Union[ArrayLike, Series]


def _check_datetime_format(dt:str) -> bool:
    try:
        return bool(datetime.strptime(dt, '%Y-%m-%d %H:%M'))
    except:
        return False

def datetime_to_api_format(dt:str|datetime) -> str:
    dt = to_datetime(arg=dt).tz_localize(tz=TZ_COL.zone)
    dt = dt.tz_convert(tz=TZ_UTC.zone) if _check_datetime_format(dt=dt) else dt

    return dt.strftime(format='%Y-%m-%dT%H:%M:00Z')

def reverse_dict(foo:dict) -> dict:
    return dict(map(reversed, foo.items()))