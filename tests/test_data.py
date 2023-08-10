"""Tests for ezml.data.

Contains tests on synthetic data frame.
"""
import logging

import hypothesis
import hypothesis.strategies as st
import pandas as pd
import pytest
from hypothesis.extra.pandas import columns, data_frames

from ezml.data import _check_data


@hypothesis.given(
    df=data_frames(
        columns=columns(["colA", "colB"], dtype=str),
        rows=st.tuples(st.from_regex("str_[a-z]", fullmatch=True), st.floats(min_value=-1.0, max_value=1.0)),
    )
)
@hypothesis.settings(suppress_health_check=[hypothesis.HealthCheck.function_scoped_fixture])
def test_check_data(caplog: pytest.LogCaptureFixture, df: pd.DataFrame):
    """Test the check data function.

    Hypothesis healthcheck is suppresed as caplog is manually cleared for each run.
    """
    with pytest.raises(Exception, match="Data contains string or mixed type."), caplog.at_level(logging.DEBUG):
        _check_data(df)
    assert "Data contains string or mixed type." in caplog.text

    # Should manually clear caplog
    # as it is not cleared by hypothesis between runs
    caplog.clear()
