from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """The entry point for the website."""
    context = {}
    return render(request, "core/index.html", context)


def emoji_options(request: HttpRequest) -> JsonResponse:
    emojis = ["🍔", "🍕", "🥗", "🍣", "🍦", "🍩"]
    context = {"emojis": emojis}
    return JsonResponse(context)
