from django.utils.translation import ugettext_lazy as _

import horizon
from mellanox_dashboard import dashboard

class UFMpanel(horizon.Panel):
    name = _("UFM")
    slug = "ufmpanel"


dashboard.MLXDashboard.register(UFMpanel)
