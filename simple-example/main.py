import hydra
from omegaconf import DictConfig


@hydra.main(config_path="config", config_name="config")
def main(cfg: DictConfig):
    print(cfg)
    print(cfg.train)


if __name__ == "__main__":
    main()
