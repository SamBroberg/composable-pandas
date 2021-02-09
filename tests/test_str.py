from composable_pandas.str import capitalize
from composable_pandas.str import decode
from composable_pandas.str import encode
from composable_pandas.str import endswith
from composable_pandas.str import extract,extractall
from datetime import datetime
import re

import numpy as np
import pytest

from pandas import Series, _testing as tm
from pandas import DataFrame, Index, MultiIndex, Series, isna, notna

def test_capitalize():
    values = Series(["FOO", "BAR", np.nan, "Blah", "blurg"])
    result = values >> capitalize()
    exp = Series(["Foo", "Bar", np.nan, "Blah", "Blurg"])
    tm.assert_series_equal(result, exp)

    # mixed
    mixed = Series(["FOO", np.nan, "bar", True, datetime.today(), "blah", None, 1, 2.0])
    mixed = mixed >> capitalize()
    exp = Series(["Foo", np.nan, "Bar", np.nan, np.nan, "Blah", np.nan, np.nan, np.nan])
    tm.assert_almost_equal(mixed, exp)

def test_encode_decode():
    base = Series(["a", "b", "a\xe4"])
    series = base >> encode("utf-8")

    f = lambda x: x.decode("utf-8")
    result = series >> decode("utf-8")
    exp = series.map(f)

    tm.assert_series_equal(result, exp)

def test_extractall():

    subject_list = [
        "dave@google.com",
        "tdhock5@gmail.com",
        "maudelaperriere@gmail.com",
        "rob@gmail.com some text steve@gmail.com",
        "a@b.com some text c@d.com and e@f.com",
        np.nan,
        "",
    ]
    expected_tuples = [
        ("dave", "google", "com"),
        ("tdhock5", "gmail", "com"),
        ("maudelaperriere", "gmail", "com"),
        ("rob", "gmail", "com"),
        ("steve", "gmail", "com"),
        ("a", "b", "com"),
        ("c", "d", "com"),
        ("e", "f", "com"),
    ]
    named_pattern = r"""
    (?P<user>[a-z0-9]+)
    @
    (?P<domain>[a-z]+)
    \.
    (?P<tld>[a-z]{2,4})
    """
    expected_columns = ["user", "domain", "tld"]
    S = Series(subject_list)
    # extractall should return a DataFrame with one row for each
    # match, indexed by the subject from which the match came.
    expected_index = MultiIndex.from_tuples(
        [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 0), (4, 1), (4, 2)],
        names=(None, "match"),
    )
    expected_df = DataFrame(expected_tuples, expected_index, expected_columns)
    computed_df = S >> extractall(named_pattern,flags = re.VERBOSE)
    tm.assert_frame_equal(computed_df, expected_df)

def test_endswith():

    # add category dtype parametrizations for GH-36241
    values = Series(
        ["om", "foo_nom", "nom", "bar_foo", "foo"],
    )

    result = values >> endswith("foo")
    exp = Series([False, False, False, True, True])
    tm.assert_series_equal(result, exp)

    result = values >> endswith("foo")
    exp = Series([False, False, False, True,True])
    tm.assert_series_equal(result, exp)

def test_extract():
    # Contains tests like those in test_match and some others.
    values = Series(["fooBAD__barBAD", np.nan, "foo"])
    er = [np.nan, np.nan]  # empty row

    result = values >> extract(".*(BAD[_]+).*(BAD)", expand=True)
    exp = DataFrame([["BAD__", "BAD"], er, er])
    tm.assert_frame_equal(result, exp)

