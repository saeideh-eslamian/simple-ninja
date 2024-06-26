from django.urls import reverse
from django.http import HttpResponse

def my_view(request):
    url = reverse('crud_ninja:api')  # Use the correct namespace and URL name
    return HttpResponse(f"API URL: {url}")
