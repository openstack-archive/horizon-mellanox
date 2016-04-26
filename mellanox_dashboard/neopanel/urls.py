from django.conf.urls import patterns
from django.conf.urls import url

from mellanox_dashboard.neopanel.views \
    import IndexView


urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='index'),
)
