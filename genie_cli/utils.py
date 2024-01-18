from datetime import datetime, timedelta, timezone

def is_token_expired(valid_from: datetime):
    return valid_from + timedelta(hours=1) <= datetime.now(timezone.utc)

