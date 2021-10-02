# :octopus: Some Hydra experiments with `hydra-core`

## :hammer_and_wrench: Installation

`pip install hydra-core`

## :test_tube: Experiments

### Replace values from CLI - `values_from_cli`

Configuration needs to be defined as it follows, with the `???` placeholder
so as to specify the mandatory values that need to be introduced via CLI.

```
train:
  batch_size: ???
```

But even though, setting a default value instead of `???` will still let you
modify it through the CLI.

```
python values_from_cli/main.py train.batch_size=32
```