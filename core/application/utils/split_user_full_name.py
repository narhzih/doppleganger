from core.domain.exceptions import ImproperlyConfigured


def split_user_full_name(full_name: str | None) -> tuple[str, str]:
    if full_name is None:
        raise ImproperlyConfigured("Please provide a valid full name")

    full_name_split = full_name.split(" ")
    if len(full_name_split) == 0:
        raise ImproperlyConfigured("Full name cannot be empty")
    elif len(full_name_split) == 1:
        first_name, last_name = full_name_split[0], full_name_split[0]
    else:
        first_name, last_name = " ".join(full_name_split[:-1]), full_name_split[-1]

    return first_name, last_name
