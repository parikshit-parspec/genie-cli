from datetime import datetime, timedelta, timezone

import pkg_resources


def is_token_expired(valid_from: datetime):
    return valid_from + timedelta(hours=1) <= datetime.now(timezone.utc)


def get_version():
    return pkg_resources.get_distribution("genie_cli").version
