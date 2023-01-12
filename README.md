# genie-cli
A simple to use CLI for interacting with EnvGenie, since cURL is not so convenient.

## Installation
First, install `pipx`:
```
> brew install pipx
```
Then install `genie-cli` using `pipx`:
```
> pipx install git+https://github.com/parikshit-parspec/genie-cli.git
```

## Usage
```
> genie-cli --help

 Usage: genie-cli [OPTIONS] COMMAND [ARGS]...

╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.      │
│ --show-completion             Show completion for the current shell, to copy │
│                               it or customize the installation.              │
│ --help                        Show this message and exit.                    │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ add-env                                                                      │
│ delete-env                                                                   │
│ display-env                                                                  │
│ list-apps                                                                    │
│ list-envs                                                                    │
│ login                                                                        │
╰──────────────────────────────────────────────────────────────────────────────╯

```