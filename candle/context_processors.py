from .models import Config,Blogpost,CandleWorkshop
def company_info(request):
    config = {
        "latest_blogs":Blogpost.objects.all()[:6],
        "latest_workshops":CandleWorkshop.objects.all()[:6]
    }
    try:
        config.update(Config.objects.first().as_dict())
    except Exception as e:
        pass
    return config