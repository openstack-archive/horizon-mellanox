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

from datetime import datetime
from datetime import timedelta

from django.forms import ValidationError  # noqa
from django import shortcuts
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.debug import sensitive_variables  # noqa

from horizon import forms


def _one_year():
    now = datetime.utcnow()
    return now + timedelta(days=365)


class SettingsForm(forms.SelfHandlingForm):
    neo_host = forms.CharField(label=_('NEO Server'), required=False)
    ufm_host = forms.CharField(label=_('UFM Server'), required=False)
    neo_host_user = forms.CharField(label=_('NEO Username'), required=False)
    n_a_ = forms.CharField(label=_('a'), required=False)
    neo_host_password = forms.CharField(label=_('NEO Password'),
                                        required=False,
                                        widget=forms.PasswordInput(
                                            render_value=False))
    no_autocomplete = False

    def handle(self, request, data):
        response = shortcuts.redirect(request.build_absolute_uri())
        request.session['mellanox_neo_host'] = data['neo_host']
        response.set_cookie('mellanox_neo_host', data['neo_host'],
                            expires=_one_year())

        request.session['mellanox_neo_host_user'] = data['neo_host_user']
        response.set_cookie('mellanox_neo_host_user', data['neo_host_user'],
                            expires=_one_year())

        request.session['mellanox_neo_host_password'] = \
            data['neo_host_password']
        response.set_cookie('mellanox_neo_host_password',
                            data['neo_host_password'],
                            expires=_one_year())

        request.session['mellanox_ufm_host'] = data['ufm_host']
        response.set_cookie('mellanox_ufm_host', data['ufm_host'],
                            expires=_one_year())

        return response
