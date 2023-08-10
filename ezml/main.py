"""Entrypoint for ds-best-practice-example."""
import hydra
from omegaconf import DictConfig

from ezml.pipeline import linear_regression_pipeline


@hydra.main(version_base=None, config_path="../input/conf", config_name="config")
def main(cfg: DictConfig) -> None:
    """Main entrypoint.

    Parameters
    ----------
    cfg : DictConfig
        Configs read in via Hydra.

    Returns
    -------
    None
    """
    # Execute pipeline
    linear_regression_pipeline(cfg=cfg)


if __name__ == "__main__":
    main()  # pragma: no cover
