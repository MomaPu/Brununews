from django.shortcuts import render

from sell.services import get_coaches


def coach_info(request):

    coaches = get_coaches()

    return render(request,'coaches/coach_info.html', {'coach': coaches})