# -*- coding: utf-8 -*-
{
    'name': "Sample Records",

    'summary': """
        Gestión de la discográfica nacional Sample Records, de sus trabajadores
        y de los albumes y grupos asociados a ella.""",

    'description': """
        Sample Records
    """,

    'author': "José Luis Ramos",
    'website': "http://www.escuelaartegranada.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Musica',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/samplerecords.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}