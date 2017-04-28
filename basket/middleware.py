from django.core.signing import BadSignature, Signer
from django.utils.functional import SimpleLazyObject, empty
from django.conf import settings

from .models import Basket


class BasketMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        self.process_request(request)
        response = self.get_response(request)
        self.process_response(request, response)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_request(self, request):
        request.cookies_to_delete = []
        request._basket_cache = None
        request.basket = self.get_basket(request)

        return request


    def process_response(self, request, response):
        # Delete any surplus cookies
        cookies_to_delete = getattr(request, 'cookies_to_delete', [])
        for cookie_key in cookies_to_delete:
            response.delete_cookie(cookie_key)

        if not hasattr(request, 'basket'):
            return response

        cookie_key = 'basket'
        # Check if we need to set a cookie. If the cookies is already available
        # but is set in the cookies_to_delete list then we need to re-set it.
        has_basket_cookie = (
            cookie_key in request.COOKIES
            and cookie_key not in cookies_to_delete)

        # If a basket has had products added to it, but the user is anonymous
        # then we need to assign it to a cookie
        if (request.basket and not has_basket_cookie):

            cookie = self.get_basket_hash(request.basket.id)
            response.set_cookie(
                cookie_key, cookie,
                max_age=settings.BASKET_COOKIE_LIFETIME,
                httponly=True)
        return response

    def get_basket(self, request):
        """
        Return the open basket for this request
        """
        if request._basket_cache is not None:
            return request._basket_cache


        cookie_basket = self.get_cookie_basket(request)

        if cookie_basket:
            # Anonymous user with a basket tied to the cookie
            basket = cookie_basket
        else:
            # Anonymous user with no basket - instantiate a new basket
            # instance.  No need to save yet.
            basket = Basket()
            basket.save()
        # Cache basket instance for the during of this request
        request._basket_cache = basket

        return basket

    def get_cookie_basket(self, request):

        basket = None
        if 'basket' in request.COOKIES:
            basket_hash = request.COOKIES['basket']

            try:
                basket_id = Signer().unsign(basket_hash)
                basket = Basket.objects.get(pk=basket_id, status=Basket.OPEN)
            except (BadSignature, Basket.DoesNotExist):
                request.cookies_to_delete.append('basket')
        return basket

    def get_basket_hash(self, basket_id):
        return Signer().sign(basket_id)
