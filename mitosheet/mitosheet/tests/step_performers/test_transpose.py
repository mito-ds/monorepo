#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Saga Inc.
# Distributed under the terms of the GPL License.
"""
Contains tests for Transpose
"""

import pandas as pd
import pytest
from mitosheet.tests.test_utils import create_mito_wrapper_dfs

TRANSPOSE_TESTS = [
    (
        [
            pd.DataFrame({'A': [1, 2, 3]}),
        ],
        0,
        [
            pd.DataFrame({'A': [1, 2, 3]}),
            pd.DataFrame({0: [1], 1: [2], 2: [3]}, index=['A'])
        ]
    ),
    (
        [
            pd.DataFrame({1: [1, 2, 3]}),
        ],
        0,
        [
            pd.DataFrame({1: [1, 2, 3]}),
            pd.DataFrame({0: [1], 1: [2], 2: [3]}, index=[1])
        ]
    ),
    (
        [
            pd.DataFrame({True: [1, 2, 3]}),
        ],
        0,
        [
            pd.DataFrame({True: [1, 2, 3]}),
            pd.DataFrame({0: [1], 1: [2], 2: [3]}, index=[True])
        ]
    ),
    (
        [
            pd.DataFrame({pd.to_datetime('12-22-1997'): [1, 2, 3]}),
        ],
        0,
        [
            pd.DataFrame({pd.to_datetime('12-22-1997'): [1, 2, 3]}),
            pd.DataFrame({0: [1], 1: [2], 2: [3]}, index=[pd.to_datetime('12-22-1997')])
        ]
    ),
    (
        [
            pd.DataFrame({pd.to_datetime('12-22-1997'): [1, 2, 3]}, index=[pd.to_datetime('12-23-1997'), pd.to_datetime('12-24-1997'), pd.to_datetime('12-25-1997')]),
        ],
        0,
        [
            pd.DataFrame({pd.to_datetime('12-22-1997'): [1, 2, 3]}, index=[pd.to_datetime('12-23-1997'), pd.to_datetime('12-24-1997'), pd.to_datetime('12-25-1997')]),
            pd.DataFrame({pd.to_datetime('12-23-1997'): [1], pd.to_datetime('12-24-1997'): [2], pd.to_datetime('12-25-1997'): [3]}, index=[pd.to_datetime('12-22-1997')])
        ]
    ),
    (
        [
            pd.DataFrame({pd.to_timedelta('1 days'): [1, 2, 3]}),
        ],
        0,
        [
            pd.DataFrame({pd.to_timedelta('1 days'): [1, 2, 3]}),
            pd.DataFrame({0: [1], 1: [2], 2: [3]}, index=[pd.to_timedelta('1 days')])
        ]
    ),
    (
        [
            pd.DataFrame({pd.to_timedelta('1 days'): [1, 2, 3]}, index=[pd.to_timedelta('2 days'), pd.to_timedelta('3 days'), pd.to_timedelta('4 days')]),
        ],
        0,
        [
            pd.DataFrame({pd.to_timedelta('1 days'): [1, 2, 3]}, index=[pd.to_timedelta('2 days'), pd.to_timedelta('3 days'), pd.to_timedelta('4 days')]),
            pd.DataFrame({pd.to_timedelta('2 days'): [1], pd.to_timedelta('3 days'): [2], pd.to_timedelta('4 days'): [3]}, index=[pd.to_timedelta('1 days')])
        ]
    ),
    (
        [
            pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}),
        ],
        0,
        [
            pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}),
            pd.DataFrame({0: [1, 4], 1: [2, 5], 2: [3, 6]}, index=['A', 'B'])
        ]
    ),
    (
        [
            pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['new', 'things', 'here']),
        ],
        0,
        [
            pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['new', 'things', 'here']),
            pd.DataFrame({'new': [1, 4], 'things': [2, 5], 'here': [3, 6]}, index=['A', 'B'])
        ]
    ),
]
@pytest.mark.parametrize("input_dfs, sheet_index, output_dfs", TRANSPOSE_TESTS)
def test_transpose(input_dfs, sheet_index, output_dfs):
    mito = create_mito_wrapper_dfs(*input_dfs)

    mito.transpose(sheet_index)

    assert len(mito.dfs) == len(output_dfs)
    for actual, expected in zip(mito.dfs, output_dfs):
        print(actual)
        print(expected)
        assert actual.equals(expected)