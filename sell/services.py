from sell.models import Coaches


def get_coaches():

    return Coaches.objects.all()