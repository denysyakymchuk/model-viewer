def extract_usernames(models: list[dict]) -> list[str]:
    usernames = set()
    for model in models:
        owner_details = model.get("owner_details")
        if owner_details and isinstance(owner_details, dict):
            username = owner_details.get("username")
            if username:
                usernames.add(username)
    return list(usernames)
