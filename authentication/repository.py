from authentication.choices import USER_TYPES


def create_related_role(profile):
    USER_TYPES[profile.user_type].objects.create(profile=profile)