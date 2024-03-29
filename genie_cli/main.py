import json
from typing import Annotated

import typer

from genie_cli import api, db, utils

app = typer.Typer()


@app.callback()
def callback():
    """
    Genie-Cli
    """


@app.command()
def login(username: str, password: str):
    err, token = api.login(username, password)
    if err:
        print(f"EnvGenie refused to login: {err}")
    db.store_token(token)
    print(f"Hello, {username}! You're logged in for 1 hour!")


@app.command()
def list_apps(format_json: Annotated[bool, typer.Option(default=False)] = False):
    err, token, valid_from = db.get_token()
    if err:
        print(f"Couldn't list apps: {err}\nDid you login?")
        return
    if utils.is_token_expired(valid_from):
        print(f"Your session has expired, please login again!")
        return
    err, apps = api.list_apps(token)
    if err:
        print(f"Could not fetch apps: {err}")
        return
    if format_json:
        print(json.dumps(apps, indent=2))
        return
    for app in apps:
        print(app["Name"])


@app.command()
def list_envs(
    app: str, format_json: Annotated[bool, typer.Option(default=False)] = False
):
    err, token, valid_from = db.get_token()
    if err:
        print(f"Couldn't list envs: {err}\nDid you login?")
        return
    if utils.is_token_expired(valid_from):
        print(f"Your session has expired, please login again!")
        return
    err, envs = api.list_envs(token, app)
    if err:
        print(f"Could not fetch envs: {err}")
        return
    if format_json:
        print(json.dumps(envs, indent=2))
        return
    for env in envs:
        print(env["URI"])


@app.command()
def display_env(app: str, tag: str):
    err, token, valid_from = db.get_token()
    if err:
        print(f"Couldn't fetch env: {err}\nDid you login?")
        return
    if utils.is_token_expired(valid_from):
        print(f"Your session has expired, please login again!")
        return
    err, text = api.display_env(token, app, tag)
    if err:
        print(f"Could not fetch env: {err}")
        return
    print(text)


@app.command()
def add_app(app: str):
    err, token, valid_from = db.get_token()
    if err:
        print(f"Couldn't add app: {err}\nDid you login?")
        return
    if utils.is_token_expired(valid_from):
        print(f"Your session has expired, please login again!")
        return
    err = api.add_app(token, app)
    if err:
        print(f"Could not add app: {err}")
        return
    print(f"Added new app: {app}")


@app.command()
def add_env(app: str, tag: str, file: str):
    err, token, valid_from = db.get_token()
    if err:
        print(f"Couldn't add env: {err}\nDid you login?")
        return
    if utils.is_token_expired(valid_from):
        print(f"Your session has expired, please login again!")
        return
    err = api.add_env(token, app, tag, file)
    if err:
        print(f"Could not add env: {err}")
        return
    print(f"Added new env: {app}:{tag}")


@app.command()
def delete_env(app: str, tag: str):
    err, token, valid_from = db.get_token()
    if err:
        print(f"Couldn't delete env: {err}\nDid you login?")
        return
    if utils.is_token_expired(valid_from):
        print(f"Your session has expired, please login again!")
        return
    err = api.delete_env(token, app, tag)
    if err:
        print(f"Could not delete env: {err}")
        return
    print(f"Deleted env: {app}:{tag}")


@app.command()
def list_users():
    err, token, valid_from = db.get_token()
    if err:
        print(f"Couldn't list users: {err}\nDid you login?")
        return
    if utils.is_token_expired(valid_from):
        print(f"Your session has expired, please login again!")
        return
    err, users = api.list_users(token)
    if err:
        print(f"Could not fetch users: {err}")
        return
    print(json.dumps(users, indent=2))


@app.command()
def add_user(name: str, pwd: str, permissions: str):
    err, token, valid_from = db.get_token()
    if err:
        print(f"Couldn't add user: {err}\nDid you login?")
        return
    if utils.is_token_expired(valid_from):
        print(f"Your session has expired, please login again!")
        return
    err = api.add_user(token, name, pwd, permissions)
    if err:
        print(f"Could not add user: {err}")
        return
    print(f"Added user {name}.")


@app.command()
def delete_user(name: str):
    err, token, valid_from = db.get_token()
    if err:
        print(f"Couldn't delete user: {err}\nDid you login?")
        return
    if utils.is_token_expired(valid_from):
        print(f"Your session has expired, please login again!")
        return
    err = api.delete_user(token, name)
    if err:
        print(f"Could not delete user: {err}")
        return
    print(f"Deleted user {name}.")

