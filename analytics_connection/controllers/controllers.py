# -*- coding: utf-8 -*-
connector ={
    'name': "PowerBI Odoo Connector",

    'summary': """
       	  Odoo to Power BI Connecter. Create PowerBI reports, bi dashboards. Publish to Power BI Service
  """,
        
    'maintainer': 'Odoo AI',
    'author': "Odoo AI",
    

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '2.1',
    'price': 0,
    
    # any module necessary for this one to work correctly
 
    'images': ['static/description/banner.png'],

    # always loaded
   
    # only loaded in demonstration mode
    "application": True,
    "installable": True,

   'depends': ['base'],
}
