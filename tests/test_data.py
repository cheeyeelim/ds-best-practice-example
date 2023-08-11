"""Tests for ezml.data.

Contains tests on synthetic data frame.
"""
import logging

import hypothesis
import hypothesis.strategies as st
import pandas as pd
import pytest
from hydra import compose, initialize
from hypothesis.extra.pandas import column, data_frames

from ezml.data import _check_data, prepare_data


def test_prepare_data():
    """Test the prepare_data function, with default data."""
    with initialize(version_base=None, config_path="../input/conf"):
        cfg = compose(config_name="config")

        X_train, X_test, y_train, y_test = prepare_data(cfg=cfg)

        assert isinstance(X_train, pd.DataFrame) and not X_train.empty
        assert isinstance(X_test, pd.DataFrame) and not X_test.empty
        assert isinstance(y_train, pd.Series) and not y_train.empty
        assert isinstance(y_test, pd.Series) and not y_test.empty


@hypothesis.given(
    df=data_frames(
        columns=[
            column("colA", elements=st.floats(min_value=1.0, max_value=10.0)),
            column("colB", elements=st.floats(min_value=-1.0, max_value=1.0)),
        ]
    )
)
@hypothesis.settings(suppress_health_check=[hypothesis.HealthCheck.function_scoped_fixture])
def test_check_data_float(df: pd.DataFrame, caplog: pytest.LogCaptureFixture):
    """Test the _check_data function, with float data.

    Hypothesis healthcheck is suppresed as caplog is manually cleared for each run.

    Excludes empty dataframe from testing.

    Parameters
    ----------
    df : pd.DataFrame
        Synthetic dataframe to be tested.
    caplog : pytest.LogCaptureFixture
        Pytest captured logging output.
    """
    if not df.empty:
        # Set logging at lowest level to capture everything
        with caplog.at_level(logging.DEBUG):
            _check_data(df)
        assert "All data checks passed!" in caplog.text

    # Should manually clear caplog
    # as it is not cleared by hypothesis between runs
    caplog.clear()


@hypothesis.given(
    df=data_frames(
        columns=[
            column("colA", elements=st.integers(min_value=1, max_value=10)),
            column("colB", elements=st.floats(min_value=-1.0, max_value=1.0)),
        ]
    )
)
@hypothesis.settings(suppress_health_check=[hypothesis.HealthCheck.function_scoped_fixture])
def test_check_data_int(df: pd.DataFrame, caplog: pytest.LogCaptureFixture):
    """Test the _check_data function, with int data.

    Hypothesis healthcheck is suppresed as caplog is manually cleared for each run.

    Excludes empty dataframe from testing.

    Parameters
    ----------
    df : pd.DataFrame
        Synthetic dataframe to be tested.
    caplog : pytest.LogCaptureFixture
        Pytest captured logging output.
    """
    if not df.empty:
        # Set logging at lowest level to capture everything
        with pytest.warns(Warning, match="Data contains integer."), caplog.at_level(logging.DEBUG):
            _check_data(df)
        assert "Data contains integer." in caplog.text

    # Should manually clear caplog
    # as it is not cleared by hypothesis between runs
    caplog.clear()


@hypothesis.given(
    df=data_frames(
        columns=[
            column("colA", elements=st.from_regex("str_[a-z]", fullmatch=True)),
            column("colB", elements=st.floats(min_value=-1.0, max_value=1.0)),
        ]
    )
)
@hypothesis.settings(suppress_health_check=[hypothesis.HealthCheck.function_scoped_fixture])
def test_check_data_str(df: pd.DataFrame, caplog: pytest.LogCaptureFixture):
    """Test the _check_data function, with str data.

    Hypothesis healthcheck is suppresed as caplog is manually cleared for each run.

    Excludes empty dataframe from testing.

    Parameters
    ----------
    df : pd.DataFrame
        Synthetic dataframe to be tested.
    caplog : pytest.LogCaptureFixture
        Pytest captured logging output.
    """
    if not df.empty:
        # Set logging at lowest level to capture everything
        with pytest.raises(Exception, match="Data contains string or mixed type."), caplog.at_level(logging.DEBUG):
            _check_data(df)
        assert "Data contains string or mixed type." in caplog.text

    # Should manually clear caplog
    # as it is not cleared by hypothesis between runs
    caplog.clear()


@hypothesis.given(
    df=data_frames(
        columns=[
            column("colA", dtype=float),
            column("colB", dtype=float),
        ]
    )
)
@hypothesis.example(df=pd.DataFrame(columns=["colA", "colB"]))
@hypothesis.settings(suppress_health_check=[hypothesis.HealthCheck.function_scoped_fixture])
def test_check_data_empty(df: pd.DataFrame, caplog: pytest.LogCaptureFixture):
    """Test the _check_data function, with empty dataframe.

    Hypothesis healthcheck is suppresed as caplog is manually cleared for each run.

    Parameters
    ----------
    df : pd.DataFrame
        Synthetic dataframe to be tested.
    caplog : pytest.LogCaptureFixture
        Pytest captured logging output.
    """
    if df.empty:
        # Set logging at lowest level to capture everything
        with pytest.raises(Exception, match="Empty dataframe."), caplog.at_level(logging.DEBUG):
            _check_data(df)
        assert "Empty dataframe." in caplog.text

    # Should manually clear caplog
    # as it is not cleared by hypothesis between runs
    caplog.clear()
