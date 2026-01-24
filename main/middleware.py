# main/middleware.py
class NoTranslateMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Добавляем заголовки для запрета перевода
        response['Content-Language'] = 'ky'
        response['X-Content-Language-Override'] = 'ky'

        return response