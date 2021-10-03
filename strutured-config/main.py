import logging
from dataclasses import dataclass

import hydra

LOGGER = logging.getLogger(__name__)


@dataclass
class TrainConfig:
    batch_size: int
    do_train: bool
    eval_batch_size: int
    do_eval: bool


@hydra.main(config_path="config", config_name="config")
def main(cfg: TrainConfig):
    LOGGER.info(f"Training batch size => {cfg.batch_size}")


if __name__ == "__main__":
    main()
