from django.utils.translation import ugettext_lazy as _

import horizon
from mellanox_dashboard import dashboard

class Neopanel(horizon.Panel):
    name = _("NEO")
    slug = "neopanel"


dashboard.MLXDashboard.register(Neopanel)
