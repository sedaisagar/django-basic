import re

from django.utils.deprecation import MiddlewareMixin

class MyMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__(get_response)
        

    def process_request(self, request):
        # path = request.path.lstrip("/")
        # if (
        #     self.redirect
        #     and not request.is_secure()
        #     and not any(pattern.search(path) for pattern in self.redirect_exempt)
        # ):
        #     host = self.redirect_host or request.get_host()
        #     return HttpResponsePermanentRedirect(
        #         "https://%s%s" % (host, request.get_full_path())
        #     )
        breakpoint()

    def process_response(self, request, response):
        breakpoint()
        
        return response
