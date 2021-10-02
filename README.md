# :octopus: Some Hydra experiments with `hydra-core`

![](https://raw.githubusercontent.com/facebookresearch/hydra/master/website/static/img/Hydra-Readme-logo2.svg)

## :hammer_and_wrench: Installation

`pip install hydra-core`

## :microscope: Experiments

### :test_tube: Simple example - `simple-example`

bla bla bla

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

### :test_tube: Comparison versus `Typer` - `hydra-vs-typer`

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

```
time python simple_example/main.py
time python vs-typer/main.py --config vs-typer/config/config.yaml
```