from composable import pipeable
import pandas as pd


@pipeable
def capitalize(col):

    """Convert strings in the Series/Index to be capitalized.
    
    Equivalent to :meth:`str.capitalize`.
    
    Returns
    -------
    Series or Index of object
    
    See Also
    --------
    str.lower : Converts all characters to lowercase.
    str.upper : Converts all characters to uppercase.
    str.title : Converts first character of each word to uppercase and
        remaining to lowercase.
    str.capitalize : Converts first character to uppercase and
        remaining to lowercase.
    str.swapcase : Converts uppercase to lowercase and lowercase to
        uppercase.
    str.casefold: Removes all case distinctions in the string.
    
    Examples
    --------
    >>> s = pd.Series(['lower', 'CAPITALS', 'this is a sentence', 'SwApCaSe'])
    >>> s
    0                 lower
    1              CAPITALS
    2    this is a sentence
    3              SwApCaSe
    dtype: object
    
    >>> s >> capitalize
    0                 Lower
    1              Capitals
    2    This is a sentence
    3              Swapcase
    dtype: object
    
    """
    return col.str.capitalize()

@pipeable
def normalize(col):
    """
    Help on method normalize in module pandas.core.accessor:

    normalize(*args, **kwargs) method of pandas.core.indexes.accessors.DatetimeProperties instance
    Convert times to midnight.
    
    The time component of the date-time is converted to midnight i.e.
    00:00:00. This is useful in cases, when the time does not matter.
    Length is unaltered. The timezones are unaffected.
    
    This method is available on Series with datetime values under
    the ``.dt`` accessor, and directly on Datetime Array/Index.
    
    Returns
    -------
    DatetimeArray, DatetimeIndex or Series
        The same type as the original data. Series will have the same
        name and index. DatetimeIndex will have the same name.
    
    See Also
    --------
    floor : Floor the datetimes to the specified freq.
    ceil : Ceil the datetimes to the specified freq.
    round : Round the datetimes to the specified freq.
    
    Examples
    --------
    >>> idx = pd.date_range(start='2014-08-01 10:00', freq='H',
    ...                     periods=3, tz='Asia/Calcutta')
    >>> idx
    DatetimeIndex(['2014-08-01 10:00:00+05:30',
                   '2014-08-01 11:00:00+05:30',
                   '2014-08-01 12:00:00+05:30'],
                    dtype='datetime64[ns, Asia/Calcutta]', freq='H')
    >>> idx.normalize()
    DatetimeIndex(['2014-08-01 00:00:00+05:30',
                   '2014-08-01 00:00:00+05:30',
                   '2014-08-01 00:00:00+05:30'],
                   dtype='datetime64[ns, Asia/Calcutta]', freq=None)
    """
    return col.normalize()

@pipeable
def round(col):
    """
    Help on method round in module pandas.core.accessor:

    round(*args, **kwargs) method of pandas.core.indexes.accessors.DatetimeProperties instance
    Perform round operation on the data to the specified `freq`.
    
    Parameters
    ----------
    freq : str or Offset
        The frequency level to round the index to. Must be a fixed
        frequency like 'S' (second) not 'ME' (month end). See
        :ref:`frequency aliases <timeseries.offset_aliases>` for
        a list of possible `freq` values.
    ambiguous : 'infer', bool-ndarray, 'NaT', default 'raise'
        Only relevant for DatetimeIndex:
    
        - 'infer' will attempt to infer fall dst-transition hours based on
          order
        - bool-ndarray where True signifies a DST time, False designates
          a non-DST time (note that this flag is only applicable for
          ambiguous times)
        - 'NaT' will return NaT where there are ambiguous times
        - 'raise' will raise an AmbiguousTimeError if there are ambiguous
          times.
    
        .. versionadded:: 0.24.0
    
    nonexistent : 'shift_forward', 'shift_backward', 'NaT', timedelta, default 'raise'
        A nonexistent time does not exist in a particular timezone
        where clocks moved forward due to DST.
    
        - 'shift_forward' will shift the nonexistent time forward to the
          closest existing time
        - 'shift_backward' will shift the nonexistent time backward to the
          closest existing time
        - 'NaT' will return NaT where there are nonexistent times
        - timedelta objects will shift nonexistent times by the timedelta
        - 'raise' will raise an NonExistentTimeError if there are
          nonexistent times.
    
        .. versionadded:: 0.24.0
    
    Returns
    -------
    DatetimeIndex, TimedeltaIndex, or Series
        Index of the same type for a DatetimeIndex or TimedeltaIndex,
        or a Series with the same index for a Series.
    
    Raises
    ------
    ValueError if the `freq` cannot be converted.
    
    Examples
    --------
    **DatetimeIndex**
    
    >>> rng = pd.date_range('1/1/2018 11:59:00', periods=3, freq='min')
    >>> rng
    DatetimeIndex(['2018-01-01 11:59:00', '2018-01-01 12:00:00',
                   '2018-01-01 12:01:00'],
                  dtype='datetime64[ns]', freq='T')
    >>> rng.round('H')
    DatetimeIndex(['2018-01-01 12:00:00', '2018-01-01 12:00:00',
                   '2018-01-01 12:00:00'],
                  dtype='datetime64[ns]', freq=None)
    
    **Series**
    
    >>> pd.Series(rng).dt.round("H")
    0   2018-01-01 12:00:00
    1   2018-01-01 12:00:00
    2   2018-01-01 12:00:00
    dtype: datetime64[ns]

    """
    return col.round()

@pipeable
def strftime(col):
    """
    Help on method strftime in module pandas.core.accessor:

    strftime(*args, **kwargs) method of pandas.core.indexes.accessors.DatetimeProperties instance
    Convert to Index using specified date_format.
    
    Return an Index of formatted strings specified by date_format, which
    supports the same string format as the python standard library. Details
    of the string format can be found in `python string format
    doc <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior>`__.
    
    Parameters
    ----------
    date_format : str
        Date format string (e.g. "%Y-%m-%d").
    
    Returns
    -------
    ndarray
        NumPy ndarray of formatted strings.
    
    See Also
    --------
    to_datetime : Convert the given argument to datetime.
    DatetimeIndex.normalize : Return DatetimeIndex with times to midnight.
    DatetimeIndex.round : Round the DatetimeIndex to the specified freq.
    DatetimeIndex.floor : Floor the DatetimeIndex to the specified freq.
    
    Examples
    --------
    >>> rng = pd.date_range(pd.Timestamp("2018-03-10 09:00"),
    ...                     periods=3, freq='s')
    >>> rng.strftime('%B %d, %Y, %r')
    Index(['March 10, 2018, 09:00:00 AM', 'March 10, 2018, 09:00:01 AM',
           'March 10, 2018, 09:00:02 AM'],
          dtype='object')
    """
    return col.dt.strftime()

@pipeable
def to_period(col,freq= 'D'):
    """
    Help on method to_period in module pandas.core.accessor:

    to_period(*args, **kwargs) method of pandas.core.indexes.accessors.DatetimeProperties instance
    Cast to PeriodArray/Index at a particular frequency.
    
    Converts DatetimeArray/Index to PeriodArray/Index.
    
    Parameters
    ----------
    freq : str or Offset, optional
        One of pandas' :ref:`offset strings <timeseries.offset_aliases>`
        or an Offset object. Will be inferred by default.
    
    Returns
    -------
    PeriodArray/Index
    
    Raises
    ------
    ValueError
        When converting a DatetimeArray/Index with non-regular values,
        so that a frequency cannot be inferred.
    
    See Also
    --------
    PeriodIndex: Immutable ndarray holding ordinal values.
    DatetimeIndex.to_pydatetime: Return DatetimeIndex as object.
    
    Examples
    --------
    >>> df = pd.DataFrame({"y": [1, 2, 3]},
    ...                   index=pd.to_datetime(["2000-03-31 00:00:00",
    ...                                         "2000-05-31 00:00:00",
    ...                                         "2000-08-31 00:00:00"]))
    >>> df.index.to_period("M")
    PeriodIndex(['2000-03', '2000-05', '2000-08'],
                dtype='period[M]', freq='M')
    
    Infer the daily frequency
    
    >>> idx = pd.date_range("2017-01-01", periods=2)
    >>> idx.to_period()
    PeriodIndex(['2017-01-01', '2017-01-02'],
                dtype='period[D]', freq='D')
    """
    return col.dt.to_period(freq=freq)

@pipeable
def floor(col,freq = 'D'):
    """
    Help on method floor in module pandas.core.accessor:

    floor(*args, **kwargs) method of pandas.core.indexes.accessors.DatetimeProperties instance
    Perform floor operation on the data to the specified `freq`.
    
    Parameters
    ----------
    freq : str or Offset
        The frequency level to floor the index to. Must be a fixed
        frequency like 'S' (second) not 'ME' (month end). See
        :ref:`frequency aliases <timeseries.offset_aliases>` for
        a list of possible `freq` values.
    ambiguous : 'infer', bool-ndarray, 'NaT', default 'raise'
        Only relevant for DatetimeIndex:
    
        - 'infer' will attempt to infer fall dst-transition hours based on
          order
        - bool-ndarray where True signifies a DST time, False designates
          a non-DST time (note that this flag is only applicable for
          ambiguous times)
        - 'NaT' will return NaT where there are ambiguous times
        - 'raise' will raise an AmbiguousTimeError if there are ambiguous
          times.
    
        .. versionadded:: 0.24.0
    
    nonexistent : 'shift_forward', 'shift_backward', 'NaT', timedelta, default 'raise'
        A nonexistent time does not exist in a particular timezone
        where clocks moved forward due to DST.
    
        - 'shift_forward' will shift the nonexistent time forward to the
          closest existing time
        - 'shift_backward' will shift the nonexistent time backward to the
          closest existing time
        - 'NaT' will return NaT where there are nonexistent times
        - timedelta objects will shift nonexistent times by the timedelta
        - 'raise' will raise an NonExistentTimeError if there are
          nonexistent times.
    
        .. versionadded:: 0.24.0
    
    Returns
    -------
    DatetimeIndex, TimedeltaIndex, or Series
        Index of the same type for a DatetimeIndex or TimedeltaIndex,
        or a Series with the same index for a Series.
    
    Raises
    ------
    ValueError if the `freq` cannot be converted.
    
    Examples
    --------
    **DatetimeIndex**
    
    >>> rng = pd.date_range('1/1/2018 11:59:00', periods=3, freq='min')
    >>> rng
    DatetimeIndex(['2018-01-01 11:59:00', '2018-01-01 12:00:00',
                   '2018-01-01 12:01:00'],
                  dtype='datetime64[ns]', freq='T')
    >>> rng.floor('H')
    DatetimeIndex(['2018-01-01 11:00:00', '2018-01-01 12:00:00',
                   '2018-01-01 12:00:00'],
                  dtype='datetime64[ns]', freq=None)
    
    **Series**
    
    >>> pd.Series(rng).dt.floor("H")
    0   2018-01-01 11:00:00
    1   2018-01-01 12:00:00
    2   2018-01-01 12:00:00
    dtype: datetime64[ns]
    """
    return col.dt.floor(freq = freq)


