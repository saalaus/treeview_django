from rest_framework import routers, viewsets, mixins

from .serializer import PageSerializer

from .models import Page


class PageViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def get_queryset(self):
        params_url = self.request.query_params.get("url")
        url = ""
        if params_url:
            url = params_url.split("/")
            url = "" if not url[-2:-1] else url[-2] if not url[-1] else url[-1]

        return Page.objects.filter(slug=url).select_related("parent")


router = routers.DefaultRouter()
router.register("pages", PageViewSet)

urlpatterns = router.urls
