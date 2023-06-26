from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "404.html", status=404)


def handler500(request):
    """ Handles error pages 500 """

    return render(request, '500.html', status=500)