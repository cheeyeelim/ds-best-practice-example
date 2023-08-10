"""Main module."""
from omegaconf import DictConfig

from ezml.data import prepare_data
from ezml.diagnostic import diagnose_model
from ezml.model import train_model


def linear_regression_pipeline(cfg: DictConfig) -> None:
    """Pipeline to create a linear regression model based on input data.

    Parameters
    ----------
    cfg : DictConfig
        Configs read in via Hydra.

    Returns
    -------
    None
    """
    X_train, X_test, y_train, y_test = prepare_data(cfg)
    model = train_model(cfg, X_train, y_train)
    diagnose_model(X_test, y_test, model)
