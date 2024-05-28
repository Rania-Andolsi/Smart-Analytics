{
    'name': 'Smart Analytics',
    'version': '1.0',
    'summary': 'Integration of BI tools with Odoo',
    'description': 'A module to integrate Business Intelligence tools with Odoo.',
    'author': 'Votre Nom',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/smart_analytics_views.xml',
        'data/smart_analytics_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
