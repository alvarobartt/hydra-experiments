# :octopus: Some Hydra experiments with `hydra-core`

![](https://raw.githubusercontent.com/facebookresearch/hydra/master/website/static/img/Hydra-Readme-logo2.svg)

## :hammer_and_wrench: Installation

`pip install hydra-core`

## :microscope: Experiments

### :test_tube: Simple example - `simple-example`

Initial tests of `hydra-core` when it comes to configuration loading, as 
specified in the Hydra Documentation at https://hydra.cc/docs/intro/.

So on, the configuration has to be specified as a YAML file inside the
`config/` directory in the same workspace, so that it will be loaded automatically
using `hydra-core`. A default/basic configuration file could look like:

```yaml
train:
  batch_size: 16
  do_train: True
  eval_batch_size: 16
  do_eval: True
```

And, since it's a YAML you can define as much nested parameters as you wish,
and `hydra-code` will load them by default using `omegaconf`, including the
typing of those parameters. So that then the function that loads the config
looks like:

```python
import hydra
from omegaconf import DictConfig

@hydra.main(config_path="config", config_name="config")
def main(cfg: DictConfig):
    print(cfg)

if __name__ == "__main__":
    main()
```

As you can see, you just need to define the `@hydra.main` decorator with the
config path and file, so that the function with that decorator will automatically
load it into the `omegaconf.DictConf` object.

Also note that those parameters can either be accessed using as `cfg["param"]` or
as `cfg.param`.

### :test_tube: Replace values from CLI - `values-from-cli`

Configuration needs to be defined as it follows, with the `???` placeholder
so as to specify the mandatory values that need to be introduced via CLI.

```yaml
train:
  batch_size: ???
```

But even though, setting a default value instead of `???` will still let you
modify it through the CLI.

```bash
python values-from-cli/main.py train.batch_size=32
```

### :test_tube: Comparison versus `Typer` - `vs-typer`

Basically this experiment will compare the default `hydra-core` application
when it comes to loading the configuration, with `typer`'s way to do it. Since
`typer` is one of the best CLI frameworks right now, whilst `hydra-core` is also
a nice CLI framework but its main strengh is regarding the configuration loading.

This is a workaround to load the configuration from CLI, Path as a parameter,
and replace those values in a dict.

```bash
python vs-typer/main.py --config vs-typer/config/config.yaml
```

But the idea is that providing also the actual CLI parameters should override the
ones loaded from the configuration file. Even though it has a counterpart and it's that
every parameter needs to be checked before actually replacing the one loaded from
the configuration.

```bash
python vs-typer/main.py --config vs-typer/config/config.yaml --batch-size=32 
```

The main pros are that `typer` is easier to use and cleaner, but regarding the configuration
loading from the CLI, `hydra-core` seems to be more robust. Also to mention that the usage
of `hydra-core` is intended to replace the usage of other CLI frameworks such as `Click`,
`typer`, `argparse`, etc.

Additionally, you can use the following commands to compare the execution time
of a mirror script written in `hydra-core` and `typer`, respectively:

```bash
time python simple_example/main.py
time python vs-typer/main.py --config vs-typer/config/config.yaml
```

### :test_tube: Using a `dataclass` instead of `omegaconf.DictConfig` - `structured-config`

Additionally, instead of using the default `omegaconf.DictConfig` which loads by default the
parameters from the YAML file (including types), we can just define our own `dataclass` with
the expected fields in the YAML file.

This is a nice feature, since `hydra-core`'s decorator will be the one fulfulling the attributes
of that `dataclass` with the parameters retrived from the YAML, also checking that the input data
matches the structure defined in the `dataclass`.

So on, for the following configuration file in YAML:

```yaml
batch_size: 16
do_train: True
eval_batch_size: 16
do_eval: True
```

we'll create a `dataclass` as it follows:

```python
from dataclasses import dataclass

@dataclass
class TrainConfig:
    batch_size: int
    do_train: bool
    eval_batch_size: int
    do_eval: bool
```

so that the `hydra-core` code will look like:

```python
import hydra

@hydra.main(config_path="config", config_name="config")
def main(cfg: TrainConfig):
    ...
```