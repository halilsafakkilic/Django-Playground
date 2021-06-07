from django.http import HttpResponse


class AccessTokenMiddleware:
    TOKEN_KEY = "X-Access-Token"
    TOKEN_VAL = "always-better"

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not ('/api/' in request.path and request.method == 'POST'):
            return self.get_response(request)

        if self.TOKEN_KEY not in request.headers:
            return HttpResponse(status=401)

        token = request.headers[self.TOKEN_KEY]
        if token != self.TOKEN_VAL:
            return HttpResponse(status=401)

        return self.get_response(request)
