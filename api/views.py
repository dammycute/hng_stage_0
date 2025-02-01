from django.http import JsonResponse
from django.utils.timezone import now

def stage0_view(request):
    return JsonResponse({
        "email": "damilolaolawoore03@gmail.com",
        "current_datetime": now().isoformat(),
        "github_url": "https://github.com/dammycute/"
    })
