from authentication.models import Profile
from manager.models import Developer, ProductManager


def get_developer_by_profile(profile: Profile):
    return Developer.objects.filter(profile=profile).first()


def get_product_manager_by_profile(profile_id):
    return ProductManager.objects.filter(profile_id=profile_id).first()
