"""Similar to what @tiangolo proposed at
https://github.com/tiangolo/typer/issues/86#issuecomment-619553358
"""

from pathlib import Path

import typer
import yaml


def main(config: Path = None, batch_size: int = None):
    cfg = {}
    if config:
        cfg = yaml.load(config.read_text(), Loader=yaml.Loader)
    if batch_size:
        cfg["train"]["batch_size"] = batch_size
    typer.echo(f"Training batch size => {cfg['train']['batch_size']}")


if __name__ == "__main__":
    typer.run(main)
