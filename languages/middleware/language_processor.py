from core.settings import DEFAULT_LANG


class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lang = request.headers.get("accept-language")
        if not lang or len(lang) != 2:
            lang = DEFAULT_LANG
        request.LANGUAGE_CODE = lang
        return self.get_response(request)
