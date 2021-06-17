def search_cookbook(cookbook: dict, recipe: str, section: str) -> str:
    if isinstance(cookbook, dict):
        if cookbook.get(recipe):
            if cookbook.get(recipe).get(section):
                return cookbook.get(recipe).get(section)
            else:
                return f'There is no section "{section}" in the "{recipe}" recipe.'
        else:
            return f'There is no "{recipe}" recipe in the cookbook.'
