from django.views.generic import TemplateView

from reviews import apis as review_api
from shops import apis as shop_api


class TopView(TemplateView):
    template_name = 'landings/top.html'

    def get_context_data(self, **kwargs):
        kwargs['shop_list'] = shop_api.all()
        kwargs['review_list'] = review_api.all()
        return super().get_context_data(**kwargs)
