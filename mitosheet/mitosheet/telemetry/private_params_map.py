#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Saga Inc.
# Distributed under the terms of the GPL License.

"""
This file contains sets of keys that let the rest of the logging infrastructure
know if this data is private or not. See the README.md file in this folder for
more details.
"""

# Params that do not need to be anonyimized
LOG_PARAMS_PUBLIC = { 'action', 'column_header_index', 'created_non_empty_dataframe', 'destination_sheet_index', 'df_index_type', 'export_type', 'feedback_id', 'field', 'filter_location', 'flatten_column_headers', 'format_type', 'fullscreen', 'graph_id', 'graph_type', 'has_headers', 'has_non_empty_filter', 'height', 'how', 'ignore_index', 'join', 'jupyterlab_theme', 'keep', 'level', 'log_event', 'move_to_deprecated_id_algorithm', 'new_column_index', 'new_dataframe_name', 'new_dtype', 'new_graph_id', 'new_signup_step', 'new_version', 'num_args', 'num_df_args', 'num_str_args', 'num_usages', 'number_rendered_sheets', 'old_dtype', 'old_graph_id', 'old_signup_step', 'old_version', 'operator', 'paper_bgcolor', 'param_filtered', 'path_parts_length', 'plot_bgcolor', 'questions_and_answers', 'safety_filter_turned_on_by_user', 'search_string', 'selected_element', 'sheet_index', 'sheet_index_one', 'sheet_index_two', 'sheet_indexes', 'showlegend', 'skiprows', 'sort', 'sort_direction', 'step_id_to_match', 'step_idx', 'step_type', 'steps_manager_analysis_name', 'title_font_color', 'user_serch_term', 'value', 'view_df', 'visible', 'width', 'row_index'}

# Parameters that need to be anonyimized, so that no private data is taken
LOG_PARAMS_TO_ANONYIMIZE = { 'analysis_name', 'args', 'color', 'column_header', 'column_id', 'column_ids', 'execution_data_to_match', 'file_name', 'file_names', 'filters', 'merge_key_column_id_one', 'merge_key_column_id_two', 'new_column_header', 'new_graph_tab_name', 'new_value', 'old_dataframe_name', 'old_value', 'path_parts', 'pivot_columns_column_ids', 'pivot_rows_column_ids', 'selected_column_ids_one', 'selected_column_ids_two', 'sheet_names', 'title', 'values_column_ids_map', 'x_axis_column_ids', 'y_axis_column_ids', 'old_graph_tab_name'}

# Parameters that are formulas, and so need to be anonyimized in a special way
LOG_PARAMS_FORMULAS = {'new_formula', 'old_formula'}

# Parameters that are nested dicts but should not be
LOG_PARAMS_TO_LINEARIZE = {'graph_creation', 'graph_preprocessing', 'graph_rendering', 'graph_styling', 'rangeslider', 'xaxis', 'yaxis'}

# We do sanity checks to make sure that there is no overlap between these sets
assert len(LOG_PARAMS_PUBLIC.intersection(LOG_PARAMS_TO_ANONYIMIZE)) == 0
assert len(LOG_PARAMS_PUBLIC.intersection(LOG_PARAMS_FORMULAS)) == 0
assert len(LOG_PARAMS_PUBLIC.intersection(LOG_PARAMS_TO_LINEARIZE)) == 0
assert len(LOG_PARAMS_TO_ANONYIMIZE.intersection(LOG_PARAMS_FORMULAS)) == 0
assert len(LOG_PARAMS_TO_ANONYIMIZE.intersection(LOG_PARAMS_TO_LINEARIZE)) == 0
assert len(LOG_PARAMS_FORMULAS.intersection(LOG_PARAMS_TO_LINEARIZE)) == 0


# Keys from execution data that do not need to be anonyimized
LOG_EXECUTION_DATA_PUBLIC = {'was_series', 'num_cols_deleted', 'column_header_index', 'pandas_processing_time', 'file_delimeters', 'destination_sheet_index', 'file_encodings', 'num_cols_formatted'}

# Keys from execution data need to be anonyimized, so that no private data is taken
LOG_EXECUTION_DATA_ANONYIMIZE = {'old_level_value', 'column_header_renames_list', 'type_corrected_new_value'}

# Sanity checks on the execution data as well
assert len(LOG_EXECUTION_DATA_PUBLIC.intersection(LOG_EXECUTION_DATA_ANONYIMIZE)) == 0
