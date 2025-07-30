def extract_usernames(models: list[dict]) -> list[str]:
    usernames = set()
    print(models)
    for model in models:
        username = model.get("owner_details", {}).get("username")
        if username:
            usernames.add(username)
    return list(usernames)
