# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Signaturit',
    'version': '1.0',
    'category': 'Settings',
    'summary': 'Signaturit',
    'description': """
Signaturit
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'wizard/signaturit.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
