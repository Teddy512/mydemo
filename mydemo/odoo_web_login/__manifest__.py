# -*- encoding: utf-8 -*-
##############################################################################
#
# teddy 2018-05-26
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#    
#    Background Source: http://forum.xda-developers.com/showpost.php?p=37322378
#
##############################################################################
{
    'name': 'login Web odoo form',
    'summary': 'This is new login form configurable Odoo Web ',
    'version': '10.0.1.0',
    'category': 'Website',
    'summary': """
This is new login form configurable Odoo Web 
""",
    'author': "teddy",
    'website': 'http://www.xuexi.me',
    'license': 'AGPL-3',
    'depends': [
    ],
    'data': [
        'data/ir_config_parameter.xml',
        'templates/webclient_templates.xml',
        'templates/website_templates.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
}
