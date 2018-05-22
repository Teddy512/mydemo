# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from odoo.addons.base.res.res_partner import WARNING_MESSAGE, WARNING_HELP


class Res_partner_inh(models.Model):
       _inherit='res.partner'
       # customer=fields.Boolean(u'客户'),
       # supplier=fields.Boolean(u'供应商'),
       sort_name=fields.Char(string="简称")


