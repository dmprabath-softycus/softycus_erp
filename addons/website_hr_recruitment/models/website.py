# -*- coding: utf-8 -*-
# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.

from flectra import models, _
from flectra.addons.http_routing.models.ir_http import url_for


class Website(models.Model):
    _inherit = "website"

    def get_suggested_controllers(self):
        suggested_controllers = super(Website, self).get_suggested_controllers()
        suggested_controllers.append((_('Jobs'), url_for('/jobs'), 'website_hr_recruitment'))
        return suggested_controllers
