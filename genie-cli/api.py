import requests

GENIE_URL = "https://envgenie-4t2uvfecua-uc.a.run.app/"


def login(username: str, password: str):
    payload = {"username": username, "password": password}
    response = requests.post(GENIE_URL + "login", data=payload)
    if response.status_code != requests.codes["OK"]:
        return response.status_code, ""
    return False, response.json()["token"]


def list_apps(token: str):
    auth_header = {"Authorization": f"Bearer {token}"}
    response = requests.get(GENIE_URL + "apps", headers=auth_header)
    if response.status_code != requests.codes["OK"]:
        return response.status_code, ""
    return False, response.json()


def list_envs(token: str, app: str):
    auth_header = {"Authorization": f"Bearer {token}"}
    response = requests.get(GENIE_URL + f"apps/{app}/envs", headers=auth_header)
    if response.status_code != requests.codes["OK"]:
        return response.status_code, ""
    return False, response.json()


def display_env(token: str, app: str, tag: str):
    auth_header = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        GENIE_URL + f"apps/{app}/envs/{tag}/download", headers=auth_header
    )
    if response.status_code != requests.codes["OK"]:
        return response.status_code, ""
    return False, response.text


def add_env(token: str, app: str, tag: str, file: str):
    auth_header = {"Authorization": f"Bearer {token}"}
    files = {"file": open(f"{file}", "rb")}
    response = requests.post(
        GENIE_URL + f"apps/{app}/envs/{tag}", headers=auth_header, files=files
    )
    if response.status_code != requests.codes["created"]:
        return response.status_code
    return False


def delete_env(token: str, app: str, tag: str):
    auth_header = {"Authorization": f"Bearer {token}"}
    response = requests.delete(
        GENIE_URL + f"apps/{app}/envs/{tag}", headers=auth_header
    )
    if response.status_code != requests.codes["OK"]:
        return response.status_code
    return False
