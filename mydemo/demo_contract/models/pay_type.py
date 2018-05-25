# -*- coding: utf-8 -*-
##############################################################################
#
#    author: hsx
#    用于收付款可选择
#
#
##############################################################################
from odoo import fields, osv
from odoo import models, api
from datetime import datetime
from odoo.tools.translate import _

class pay_type(models.Model):
    _description=u'收付款方式'
    _name='pay.type'


    sequence=fields.Integer(u'序号')
    name=fields.Char(u'类别名称')
    spay_type_jc=fields.Char(u'简称')