import logging

import hydra
from omegaconf import DictConfig

LOGGER = logging.getLogger(__name__)


@hydra.main(config_path="config", config_name="config")
def main(cfg: DictConfig):
    LOGGER.info(f"Training batch size => {cfg.train.batch_size}")


if __name__ == "__main__":
    main()
