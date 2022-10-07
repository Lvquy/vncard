# -*- coding: utf-8 -*-
{
    'name': 'VNCard',
    'version': '1',
    'category': 'vncard',
    'live_test_url': '#',
    'summary': 'VNCard',
    'author': 'Lv Quy',
    'company': 'Lv Quy',
    'website': 'https://#',
    'depends': ['base_setup','website'],
    'data': [
        # security
        'security/ir.model.access.csv',

        # views
        'views/template_inherit.xml',

        #template
        'template/web_template.xml',
    ],
    'assets': {
        'web.assets_backend': [],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
}
