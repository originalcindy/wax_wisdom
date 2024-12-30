from .models import Config
def company_info(request):
    try:
        config = Config.objects.first()
        return config.as_dict()
    except Exception as e:
        return {}