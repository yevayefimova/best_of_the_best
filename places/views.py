from django.shortcuts import render

from .data import INITIAL_PLACES

from django.http import Http404

def get_places(request):
    if "places" not in request.session:
        request.session["places"] = INITIAL_PLACES

    return request.session["places"]

def home(request):
    return render(request, "places/home.html")

def place_list(request):
    places = get_places(request)

    return render(request, "places/place_list.html", {
        "places": places,
    })

def place_detail(request, place_id):
    places = get_places(request)

    for place in places:
        if place["id"] == place_id:
            return render(request, "places/place_detail.html", {
                "place": place,
            })

    raise Http404("Place not found")
    