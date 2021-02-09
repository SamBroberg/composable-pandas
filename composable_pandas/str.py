from composable import pipeable
import pandas as pd
import re

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
def decode(encoding, col, error='ignore'):
    """
    Help on method decode in module pandas.core.strings:

    decode(encoding, errors='strict') method of pandas.core.strings.StringMethods instance
    Decode character string in the Series/Index using indicated encoding.
    Equivalent to :meth:`str.decode` in python2 and :meth:`bytes.decode` in
    python3.
    
    Parameters
    ----------
    encoding : str
    errors : str, optional
    
    Returns
    -------
    Series or Index
    """
    return col.str.decode(encoding, error)
@pipeable
def encode(encoding,col,error='ignore'):
    """
    Help on method encode in module pandas.core.strings:

    encode(encoding, errors='strict') method of pandas.core.strings.StringMethods instance
    Encode character string in the Series/Index using indicated encoding.
    Equivalent to :meth:`str.encode`.
    
    Parameters
    ----------
    encoding : str
    errors : str, optional
    
    Returns
    -------
    encoded : Series/Index of objects
    """
    return col.str.encode(encoding,error)


@pipeable
def endswith(pat,col):
    """
    Help on method endswith in module pandas.core.strings:

    endswith(pat, na=nan) method of pandas.core.strings.StringMethods instance
    Test if the end of each string element matches a pattern.
    
    Equivalent to :meth:`str.endswith`.
    
    Parameters
    ----------
    pat : str
        Character sequence. Regular expressions are not accepted.
    na : object, default NaN
        Object shown if element tested is not a string.
    
    Returns
    -------
    Series or Index of bool
        A Series of booleans indicating whether the given pattern matches
        the end of each string element.
    
    See Also
    --------
    str.endswith : Python standard library string method.
    str.startswith : Same as endswith, but tests the start of string.
    str.contains : Tests if string element contains a pattern.
    
    Examples
    --------
    >>> s = pd.Series(['bat', 'bear', 'caT', np.nan])
    >>> s
    0     bat
    1    bear
    2     caT
    3     NaN
    dtype: object
    
    >>> s >> endswith(t)
    0     True
    1    False
    2    False
    3      NaN
    dtype: object
    
    Specifying `na` to be `False` instead of `NaN`.
    
    >>> s >> endswith('t', na=False)
    0     True
    1    False
    2    False
    3    False
    dtype: bool
    """
    return col.str.endswith(pat)
@pipeable
def extract(pat,col,flags=0,expand=True):
    """
    Help on method extract in module pandas.core.strings:

    extract(pat, flags=0, expand=True) method of pandas.core.strings.StringMethods instance
    Extract capture groups in the regex `pat` as columns in a DataFrame.
    
    For each subject string in the Series, extract groups from the
    first match of regular expression `pat`.
    
    Parameters
    ----------
    pat : str
        Regular expression pattern with capturing groups.
    flags : int, default 0 (no flags)
        Flags from the ``re`` module, e.g. ``re.IGNORECASE``, that
        modify regular expression matching for things like case,
        spaces, etc. For more details, see :mod:`re`.
    expand : bool, default True
        If True, return DataFrame with one column per capture group.
        If False, return a Series/Index if there is one capture group
        or DataFrame if there are multiple capture groups.
    
    Returns
    -------
    DataFrame or Series or Index
        A DataFrame with one row for each subject string, and one
        column for each group. Any capture group names in regular
        expression pat will be used for column names; otherwise
        capture group numbers will be used. The dtype of each result
        column is always object, even when no match is found. If
        ``expand=False`` and pat has only one capture group, then
        return a Series (if subject is a Series) or Index (if subject
        is an Index).
    
    See Also
    --------
    extractall : Returns all matches (not just the first match).
    
    Examples
    --------
    A pattern with two groups will return a DataFrame with two columns.
    Non-matches will be NaN.
    
    >>> s = pd.Series(['a1', 'b2', 'c3'])
    >>> s.str.extract(r'([ab])(\d)')
         0    1
    0    a    1
    1    b    2
    2  NaN  NaN
    
    A pattern may contain optional groups.
    
    >>> s.str.extract(r'([ab])?(\d)')
         0  1
    0    a  1
    1    b  2
    2  NaN  3
    
    Named groups will become column names in the result.
    
    >>> s.str.extract(r'(?P<letter>[ab])(?P<digit>\d)')
      letter digit
    0      a     1
    1      b     2
    2    NaN   NaN
    
    A pattern with one group will return a DataFrame with one column
    if expand=True.
    
    >>> s.str.extract(r'[ab](\d)', expand=True)
         0
    0    1
    1    2
    2  NaN
    
    A pattern with one group will return a Series if expand=False.
    
    >>> s.str.extract(r'[ab](\d)', expand=False)
    0      1
    1      2
    2    NaN
    dtype: object
    """
    return col.str.extract(pat,flags=flags,expand=True)

@pipeable
def extractall(pat,col,*,flags=0):
    """
    Help on method extractall in module pandas.core.strings:

    extractall(pat, flags=0) method of pandas.core.strings.StringMethods instance
    For each subject string in the Series, extract groups from all
    matches of regular expression pat. When each subject string in the
    Series has exactly one match, extractall(pat).xs(0, level='match')
    is the same as extract(pat).
    
    Parameters
    ----------
    pat : str
        Regular expression pattern with capturing groups.
    flags : int, default 0 (no flags)
        A ``re`` module flag, for example ``re.IGNORECASE``. These allow
        to modify regular expression matching for things like case, spaces,
        etc. Multiple flags can be combined with the bitwise OR operator,
        for example ``re.IGNORECASE | re.MULTILINE``.
    
    Returns
    -------
    DataFrame
        A ``DataFrame`` with one row for each match, and one column for each
        group. Its rows have a ``MultiIndex`` with first levels that come from
        the subject ``Series``. The last level is named 'match' and indexes the
        matches in each item of the ``Series``. Any capture group names in
        regular expression pat will be used for column names; otherwise capture
        group numbers will be used.
    
    See Also
    --------
    extract : Returns first match only (not all matches).
    
    Examples
    --------
    A pattern with one group will return a DataFrame with one column.
    Indices with no matches will not appear in the result.
    
    >>> s = pd.Series(["a1a2", "b1", "c1"], index=["A", "B", "C"])
    >>> s.str.extractall(r"[ab](\d)")
             0
      match
    A 0      1
      1      2
    B 0      1
    
    Capture group names are used for column names of the result.
    
    >>> s.str.extractall(r"[ab](?P<digit>\d)")
            digit
      match
    A 0         1
      1         2
    B 0         1
    
    A pattern with two groups will return a DataFrame with two columns.
    
    >>> s.str.extractall(r"(?P<letter>[ab])(?P<digit>\d)")
            letter digit
      match
    A 0          a     1
      1          a     2
    B 0          b     1
    
    Optional groups that do not match are NaN in the result.
    
    >>> s.str.extractall(r"(?P<letter>[ab])?(?P<digit>\d)")
            letter digit
      match
    A 0          a     1
      1          a     2
    B 0          b     1
    C 0        NaN     1
    """
    return col.str.extractall(pat,flags = flags)

