from django.utils.translation import ugettext_lazy as _
import horizon

import mellanox_dashboard.api.rest

class MLXDashboard(horizon.Dashboard):
    name = _("Mellanox Technologies")
    slug = "mellanox_dashboard"
    panels = ('settingspanel', 'neopanel', 'ufmpanel', 'aboutpanel')  # Add your panels here.
    default_panel = 'settingspanel'  # Specify the slug of the dashboard's default panel.

horizon.register(MLXDashboard)
