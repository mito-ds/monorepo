#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Mito.
# Distributed under the terms of the Modified BSD License.

"""
Contains tests for changing the type of a column.

We test on a variety of new_dtype inputs, as the goal is that this step 
accepts inputs flexibly, even if it does not send them from frontend.

Kinda inspired by this: https://en.wikipedia.org/wiki/Robustness_principle
"""
from typing import Optional
from mitosheet.tests.test_utils import create_mito_wrapper, create_mito_wrapper_dfs
import pandas as pd
import pytest

BOOL_ARRAY = [True, False, True]
INT_ARRAY = [1, 2, 3]
FLOAT_ARRAY = [4.0, 5.1, 6.2]
STRING_ARRAY = ["$1", "2.1", "(3.2)"]
DATETIME_ARRAY = [pd.to_datetime(x, unit='s') for x in [100, 200, 300]]
TIMEDELTA_ARRAY = [pd.to_timedelta(x, unit='s') for x in [100, 200, 300]]

BOOL_TESTS = [
    ('bool', BOOL_ARRAY, 'df1[\'A\'] = df1[\'A\']'), 
    ('int', [1, 0, 1], 'df1[\'A\'] = df1[\'A\'].astype(\'int\')'), 
    ('int64', [1, 0, 1], 'df1[\'A\'] = df1[\'A\'].astype(\'int\')'), 
    ('float', [1.0, 0.0, 1.0], 'df1[\'A\'] = df1[\'A\'].astype(\'float\')'), 
    ('float64', [1.0, 0.0, 1.0], 'df1[\'A\'] = df1[\'A\'].astype(\'float\')'), 
    ('str', ['True', 'False', 'True'], 'df1[\'A\'] = df1[\'A\'].astype(\'str\')'), 
    ('object', ['True', 'False', 'True'], 'df1[\'A\'] = df1[\'A\'].astype(\'str\')'), 
    ('string', ['True', 'False', 'True'], 'df1[\'A\'] = df1[\'A\'].astype(\'str\')'), 
    ('datetime', BOOL_ARRAY, None), 
    ('datetime64[ns]', BOOL_ARRAY, None), 
    ('timedelta', BOOL_ARRAY, None), 
]
@pytest.mark.parametrize("new_dtype, result, code", BOOL_TESTS)
def test_bool_to_other_types(new_dtype, result, code):
    mito = create_mito_wrapper(BOOL_ARRAY)
    mito.change_column_dtype(0, 'A', new_dtype)
    assert mito.get_column(0, 'A', as_list=True) == result
    if code is not None:
        assert mito.transpiled_code == [
                code
        ]
    else:
        assert len(mito.transpiled_code) == 0


INT_TESTS = [
    ('bool', [True, True, True], 'df1[\'A\'] = df1[\'A\'].fillna(False).astype(\'bool\')'), 
    ('int', [1, 2, 3], 'df1[\'A\'] = df1[\'A\']'), 
    ('int64', [1, 2, 3], 'df1[\'A\'] = df1[\'A\']'), 
    ('float', [1.0, 2.0, 3.0], 'df1[\'A\'] = df1[\'A\'].astype(\'float\')'), 
    ('float64', [1.0, 2.0, 3.0], 'df1[\'A\'] = df1[\'A\'].astype(\'float\')'), 
    ('str', ['1', '2', '3'], 'df1[\'A\'] = df1[\'A\'].astype(\'str\')'), 
    ('object', ['1', '2', '3'], 'df1[\'A\'] = df1[\'A\'].astype(\'str\')'), 
    ('string', ['1', '2', '3'], 'df1[\'A\'] = df1[\'A\'].astype(\'str\')'), 
    ('datetime', [pd.to_datetime(x, unit='s') for x in [1, 2, 3]], 'df1[\'A\'] = pd.to_datetime(df1[\'A\'], unit=\'s\', errors=\'coerce\')'), 
    ('datetime64[ns]', [pd.to_datetime(x, unit='s') for x in [1, 2, 3]], 'df1[\'A\'] = pd.to_datetime(df1[\'A\'], unit=\'s\', errors=\'coerce\')'), 
    ('timedelta', [pd.to_timedelta(x, unit='s') for x in [1, 2, 3]], 'df1[\'A\'] = pd.to_timedelta(df1[\'A\'], unit=\'s\', errors=\'coerce\')'), 
]
@pytest.mark.parametrize("new_dtype, result, code", INT_TESTS)
def test_int_to_other_types(new_dtype, result, code):
    mito = create_mito_wrapper(INT_ARRAY)
    mito.change_column_dtype(0, 'A', new_dtype)
    assert mito.get_column(0, 'A', as_list=True) == result
    if code is not None:            
        assert len(mito.transpiled_code) > 0
    else:
        assert len(mito.transpiled_code) == 0


FLOAT_TESTS = [
    ('bool', [True, True, True], 'df1[\'A\'] = df1[\'A\'].fillna(False).astype(\'bool\')'), 
    ('int', [4, 5, 6], 'df1[\'A\'] = df1[\'A\'].astype(\'int\')'), 
    ('int64', [4, 5, 6], 'df1[\'A\'] = df1[\'A\'].astype(\'int\')'), 
    ('float', [4.0, 5.1, 6.2], 'df1[\'A\'] = df1[\'A\']'), 
    ('float64', [4.0, 5.1, 6.2], 'df1[\'A\'] = df1[\'A\']'), 
    ('str', ['4.0', '5.1', '6.2'], 'df1[\'A\'] = df1[\'A\'].astype(\'str\')'), 
    ('object', ['4.0', '5.1', '6.2'], 'df1[\'A\'] = df1[\'A\'].astype(\'str\')'), 
    ('string', ['4.0', '5.1', '6.2'], 'df1[\'A\'] = df1[\'A\'].astype(\'str\')'), 
    ('datetime', [pd.to_datetime(x, unit='s') for x in [4.0, 5.1, 6.2]], 'df1[\'A\'] = pd.to_datetime(df1[\'A\'], unit=\'s\', errors=\'coerce\')'), 
    ('datetime64[ns]', [pd.to_datetime(x, unit='s') for x in [4.0, 5.1, 6.2]], 'df1[\'A\'] = pd.to_datetime(df1[\'A\'], unit=\'s\', errors=\'coerce\')'), 
    ('timedelta', [pd.to_timedelta(x, unit='s') for x in [4.0, 5.1, 6.2]], 'df1[\'A\'] = pd.to_timedelta(df1[\'A\'], unit=\'s\', errors=\'coerce\')'), 
]
@pytest.mark.parametrize("new_dtype, result, code", FLOAT_TESTS)
def test_float_to_other_types(new_dtype, result, code):
    mito = create_mito_wrapper(FLOAT_ARRAY)
    mito.change_column_dtype(0, 'A', new_dtype)
    assert mito.get_column(0, 'A', as_list=True) == result
    if code is not None:            
        assert len(mito.transpiled_code) > 0
    else:
        assert len(mito.transpiled_code) == 0


STRING_TESTS = [
    ('bool', [False, False, False], 'df1[\'A\'] = to_boolean_series(df1[\'A\'])'), 
    ('int', [1, 2, -3], 'df1[\'A\'] = to_number_series(df1[\'A\']).astype(\'int\')'), 
    ('int64', [1, 2, -3], 'df1[\'A\'] = to_number_series(df1[\'A\']).astype(\'int\')'), 
    ('float', [1.0, 2.1, -3.2], 'df1[\'A\'] = to_number_series(df1[\'A\'])'), 
    ('float64', [1.0, 2.1, -3.2], 'df1[\'A\'] = to_number_series(df1[\'A\'])'),  
    ('str', ["$1", "2.1", "(3.2)"], 'df1[\'A\'] = df1[\'A\']'), 
    ('object', ["$1", "2.1", "(3.2)"], 'df1[\'A\'] = df1[\'A\']'), 
    ('string', ["$1", "2.1", "(3.2)"], 'df1[\'A\'] = df1[\'A\']'),
    ('datetime', [pd.to_datetime('A', errors='coerce') for x in [None, None, None]], 'df1[\'A\'] = pd.to_datetime(df1[\'A\'], format=\'%m-%d-%Y\', errors=\'coerce\')'), 
    ('datetime64[ns]', [pd.to_datetime('A', errors='coerce') for x in [None, None, None]], 'df1[\'A\'] = pd.to_datetime(df1[\'A\'], format=\'%m-%d-%Y\', errors=\'coerce\')'), 
    ('timedelta', [pd.to_timedelta('A', errors='coerce') for x in [None, None, None]], 'df1[\'A\'] = pd.to_timedelta(df1[\'A\'], errors=\'coerce\')'), 
]
@pytest.mark.parametrize("new_dtype, result, code", STRING_TESTS)
def test_string_to_other_types(new_dtype, result, code):
    mito = create_mito_wrapper(STRING_ARRAY)
    mito.change_column_dtype(0, 'A', new_dtype)
    assert mito.get_column(0, 'A', as_list=True) == result
    if code is not None:            
        assert len(mito.transpiled_code) > 0
    else:
        assert len(mito.transpiled_code) == 0

# Little helper function for less writing
def ts(y: Optional[int]=None, m: Optional[int]=None, d: Optional[int]=None) -> pd.Timestamp:
    return pd.Timestamp(year=y, month=m, day=d)
     

# NOTE: we do not get perfect conversions on this, as we use pandas conversion behavior
# by default. 
COMPLEX_DATE_STRINGS = [
    # DD-MM-YYYY (common format, pandas defaults here when unsure)
    (['1-1-2020', '1-1-2020'], [ts(y=2020, d=1, m=1), ts(y=2020, m=1, d=1)], 'df1[\'A\'] = pd.to_datetime(df1[\'A\'], infer_datetime_format=True, errors=\'coerce\')'),
    (['1-1-2020', '1-2-2020'], [ts(y=2020, d=1, m=1), ts(y=2020, m=1, d=2)], 'df1[\'A\'] = pd.to_datetime(df1[\'A\'], infer_datetime_format=True, errors=\'coerce\')'),
    (['1-1-2020', '1-20-2020'], [ts(y=2020, d=1, m=1), ts(y=2020, m=1, d=20)], 'df1[\'A\'] = pd.to_datetime(df1[\'A\'], infer_datetime_format=True, errors=\'coerce\')'),
    
    # MM-DD-YYYY (common format, pandas does not default here if the first value is not in this format)
    (['1-1-2020', '1-1-2020'], [ts(y=2020, d=1, m=1), ts(y=2020, m=1, d=1)], 'df1[\'A\'] = pd.to_datetime(df1[\'A\'], infer_datetime_format=True, errors=\'coerce\')'),
    (['1-1-2020', '1-20-2020'], [ts(y=2020, d=1, m=1), ts(y=2020, m=1, d=20)], 'df1[\'A\'] = pd.to_datetime(df1[\'A\'], infer_datetime_format=True, errors=\'coerce\')'),
    
    # YYYY-MM-DD (seen from users, specifically MB)
    (['2020-12-20', '2020-12-1'], [ts(y=2020, m=12, d=20), ts(y=2020, m=12, d=1)], 'df1[\'A\'] = pd.to_datetime(df1[\'A\'], infer_datetime_format=True, errors=\'coerce\')'),
    # A more complex YYYY-MM-DD, also from MB
    (['2016-01-31T19:29:50.000+0000', '2016-01-31T19:29:50.000+0000'], [pd.Timestamp(year=2016, month=1, day=31, hour=19, minute=29, second=50, tz='UTC'), pd.Timestamp(year=2016, month=1, day=31, hour=19, minute=29, second=50, tz='UTC')], 'df1[\'A\'] = pd.to_datetime(df1[\'A\'], infer_datetime_format=True, errors=\'coerce\')'),
    # M/DD/YYY
    (['4/14/2015', '4/15/2015'], [ts(y=2015, m=4, d=14), ts(y=2015, m=4, d=15)], 'df1[\'A\'] = pd.to_datetime(df1[\'A\'], infer_datetime_format=True, errors=\'coerce\')'),

]
@pytest.mark.parametrize("strings, result, code", COMPLEX_DATE_STRINGS)
def test_complex_date_strings(strings, result, code):
    mito = create_mito_wrapper(strings)
    mito.change_column_dtype(0, 'A', 'datetime')
    assert mito.get_column(0, 'A', as_list=True) == result
    if code is not None:            
        assert len(mito.transpiled_code) > 0
    else:
        assert len(mito.transpiled_code) == 0


DATETIME_TESTS = [
    ('bool', [True, True, True], 'df1[\'A\'] = ~df1[\'A\'].isnull()'), 
    ('int', [100, 200, 300], 'df1[\'A\'] = df1[\'A\'].astype(\'int\') / 10**9'), 
    ('int64', [100, 200, 300], 'df1[\'A\'] = df1[\'A\'].astype(\'int\') / 10**9'), 
    ('float', [100.0, 200.0, 300.0], 'df1[\'A\'] = df1[\'A\'].astype(\'int\').astype(\'float\') / 10**9'), 
    ('float64', [100.0, 200.0, 300.0], 'df1[\'A\'] = df1[\'A\'].astype(\'int\').astype(\'float\') / 10**9'),  
    ('str', ['1970-01-01 00:01:40', '1970-01-01 00:03:20', '1970-01-01 00:05:00'], 'df1[\'A\'] = df1[\'A\'].dt.strftime(\'%Y-%m-%d %X\')'), 
    ('object', ['1970-01-01 00:01:40', '1970-01-01 00:03:20', '1970-01-01 00:05:00'], 'df1[\'A\'] = df1[\'A\'].dt.strftime(\'%Y-%m-%d %X\')'), 
    ('string', ['1970-01-01 00:01:40', '1970-01-01 00:03:20', '1970-01-01 00:05:00'], 'df1[\'A\'] = df1[\'A\'].dt.strftime(\'%Y-%m-%d %X\')'), 
    ('datetime', DATETIME_ARRAY, 'df1[\'A\'] = df1[\'A\']'), 
    ('datetime64[ns]', DATETIME_ARRAY, 'df1[\'A\'] = df1[\'A\']'), 
    ('timedelta', DATETIME_ARRAY, None), 
]
@pytest.mark.parametrize("new_dtype, result, code", DATETIME_TESTS)
def test_datetime_to_other_types(new_dtype, result, code):
    mito = create_mito_wrapper(DATETIME_ARRAY)
    mito.change_column_dtype(0, 'A', new_dtype)
    assert mito.get_column(0, 'A', as_list=True) == result
    if code is not None:            
        assert len(mito.transpiled_code) > 0
    else:
        assert len(mito.transpiled_code) == 0


TIMEDELTA_TESTS = [
    ('bool', [True, True, True], 'df1[\'A\'] = ~df1[\'A\'].isnull()'), 
    ('int', [100, 200, 300], 'df1[\'A\'] = df1[\'A\'].dt.total_seconds().astype(\'int\')'), 
    ('int64', [100, 200, 300], 'df1[\'A\'] = df1[\'A\'].dt.total_seconds().astype(\'int\')'), 
    ('float', [100.0, 200.0, 300.0], 'df1[\'A\'] = df1[\'A\'].dt.total_seconds()'), 
    ('float64', [100.0, 200.0, 300.0], 'df1[\'A\'] = df1[\'A\'].dt.total_seconds()'),  
    ('str', ['0 days 00:01:40', '0 days 00:03:20', '0 days 00:05:00'], 'df1[\'A\'] = df1[\'A\'].astype(\'str\')'), 
    ('object', ['0 days 00:01:40', '0 days 00:03:20', '0 days 00:05:00'], 'df1[\'A\'] = df1[\'A\'].astype(\'str\')'), 
    ('string', ['0 days 00:01:40', '0 days 00:03:20', '0 days 00:05:00'], 'df1[\'A\'] = df1[\'A\'].astype(\'str\')'), 
    ('datetime', TIMEDELTA_ARRAY, None), 
    ('datetime64[ns]', TIMEDELTA_ARRAY, None), 
    ('timedelta', TIMEDELTA_ARRAY, 'df1[\'A\'] = df1[\'A\']'), 
]
@pytest.mark.parametrize("new_dtype, result, code", TIMEDELTA_TESTS)
def test_timedelta_to_other_types(new_dtype, result, code):
    mito = create_mito_wrapper(TIMEDELTA_ARRAY)
    mito.change_column_dtype(0, 'A', new_dtype)
    assert mito.get_column(0, 'A', as_list=True) == result
    if code is not None:            
        assert len(mito.transpiled_code) > 0
    else:
        assert len(mito.transpiled_code) == 0


def test_changing_column_type_refreshed_dependants():

    mito = create_mito_wrapper_dfs(pd.DataFrame({'A': [1.2, 2.0, 3.0]}))
    mito.set_formula('=A', 0, 'B', add_column=True)

    mito.change_column_dtype(0, 'A', 'int')
    assert mito.get_column(0, 'A', as_list=True) == [1, 2, 3]
    assert mito.get_column(0, 'B', as_list=True) == [1, 2, 3]

    assert mito.transpiled_code == [
        "df1.insert(1, 'B', 0)",
        "df1['B'] = df1['A']",
        "df1['A'] = df1['A'].astype('int')",
        "df1['B'] = df1['A']"
    ]
    
def test_change_type_on_renamed_column():

    mito = create_mito_wrapper_dfs(pd.DataFrame({'A': [1.2, 2.0, 3.0]}))
    mito.rename_column(0, 'A', 'B')

    mito.change_column_dtype(0, 'B', 'int')
    assert mito.get_column(0, 'B', as_list=True) == [1, 2, 3]

    assert mito.transpiled_code == [
        "df1.rename(columns={\'A\': \'B\'}, inplace=True)",
        "df1['B'] = df1['B'].astype('int')",
    ]
    