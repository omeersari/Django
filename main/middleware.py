from datetime import timedelta as td
from django.utils import timezone
from django.conf import settings
from django.db.models.expressions import F
from dateutil.parser import parse
from django.contrib.auth.models import User
from .models import UserProfile


class AccountLoginMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last-activity')

            too_old_time = timezone.now() - td(seconds=60*60)
            if not last_activity or parse(last_activity) < too_old_time:
                UserProfile.objects.filter(user=request.user).update(
                    login_last=timezone.now(),
                    login_count=F('login_count') + 1)

            request.session['last-activity'] = timezone.now().isoformat()

        response = self.get_response(request)

        return response