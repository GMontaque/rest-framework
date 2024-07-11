from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile


class ProfileList(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        return Response(profiles)