# -*- coding: utf-8 -*-
{
    'name': "dental_care",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Raihan Satya Natha Hamzah",
    'website': "https://www.infinyscloud.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Health',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'web'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/menu.xml',
        'views/service_views.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/appointment_views.xml',
        'views/res_partner.xml',


        'reports/appointment_report.xml',
    ],

    'qweb': [
        'static/change_state.js'
    ],

    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}

