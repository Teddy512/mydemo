# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': '  contract manager',
    'category': 'contract',
    'author':'teddy',
    'summary': 'Add twitter scroller snippet in website builder',
    'website': 'https://www.odoo.com/menu',
    'version': '1.0',
    'description': """
management your contract
========================

        """,
    'depends': ['base','hr'],
    'data': [
        'security/security_data.xml',
        'security/ir.model.access.csv',
        'views/demo_contract_lx_view.xml',
        'views/settle_account_view.xml',
        'views/sigining_contract_view.xml',
        'views/pay_type_view.xml',
        'views/seq.xml'

    ],
    'demo':[],
    'test':[],
    'installable': True,
    'auto_install':False,
    'application':True,

}
