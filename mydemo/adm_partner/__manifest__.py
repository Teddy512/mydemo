# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'management  partner',
    'category': 'partner',
    'author':'teddy',
    'summary': 'your can add and delete partner',
    'website': 'https://www.odoo.com/menu',
    'version': '1.0',
    'description': """
management your partner
========================

        """,
    'depends': ['base'],
    'data': [
        # 'security/ir.model.access.csv',
        # 'data/website_twitter_data.xml',
        'views/res_partner_views.xml',
        # 'views/website_twitter_snippet_templates.xml'
    ],
    'demo':[],
    'test':[],
    'installable': True,
    'auto_install':False,
    'application':True,

}
