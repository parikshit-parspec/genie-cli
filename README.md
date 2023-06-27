# genie-cli
A simple to use CLI for interacting with EnvGenie, since cURL is not so convenient.

## Installation
First, install `pipx`:
```
brew install pipx
```
Then install `genie-cli` using `pipx`:
```
pipx install git+https://github.com/parikshit-parspec/genie-cli.git
```

You can update an existing installation like so:
```
pipx install git+https://github.com/parikshit-parspec/genie-cli.git --force
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
│ add-user                                                                     │
│ delete-env                                                                   │
│ delete-user                                                                  │
│ display-env                                                                  │
│ list-apps                                                                    │
│ list-envs                                                                    │
│ list-users                                                                   │
│ login                                                                        │
╰──────────────────────────────────────────────────────────────────────────────╯

```

## Development
```
genie-cli> cd genie_cli
genie_cli> poetry install
Installing dependencies from lock file

No dependencies to install or update

Installing the current project: genie-cli (1.0.1)
genie_cli> poetry run genie-cli
Usage: genie-cli [OPTIONS] COMMAND [ARGS]...
Try 'genie-cli --help' for help.
╭─ Error ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Missing command.                                                                                           │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
genie_cli>
```