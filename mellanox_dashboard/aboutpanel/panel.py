from django.utils.translation import ugettext_lazy as _

import horizon
from mellanox_dashboard import dashboard

class Aboutpanel(horizon.Panel):
    name = _("About")
    slug = "aboutpanel"


dashboard.MLXDashboard.register(Aboutpanel)
