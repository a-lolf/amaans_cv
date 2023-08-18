import random
import string
from django.shortcuts import render, redirect
from .models import ShortURL


def generate_short_code():
    # Generate a random short code of length 6
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))


def index(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']

        # Generate a unique short code
        while True:
            short_code = generate_short_code()
            if not ShortURL.objects.filter(short_code=short_code).exists():
                break

        short_url = ShortURL(original_url=original_url, short_code=short_code)
        short_url.save()
        return render(request, 'shorturl_app/index.html', {'short_url': short_url})

    return render(request, 'shorturl_app/index.html')


def redirect_to_original(request, short_code):
    short_url = ShortURL.objects.get(short_code=short_code)
    return redirect(short_url.original_url)
