# -*- coding: utf-8 -*-

# Copyright 2016 Mellanox Technologies, Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from horizon import forms

from horizon_mellanox.settingspanel \
    import forms as settings_forms


class SettingsView(forms.ModalFormView):
    form_class = settings_forms.SettingsForm
    form_id = "change_settings_modal_form"
    modal_header = ""
    modal_id = "change_settings_modal"
    page_title = _("Settings")
    submit_label = _("Save")
    submit_url = reverse_lazy("horizon:horizon_mellanox:settingspanel:index")
    template_name = 'horizon_mellanox/settingspanel/change.html'
