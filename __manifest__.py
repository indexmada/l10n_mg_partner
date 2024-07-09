# -*- coding: utf-8 -*-
{
    'name': "l10n_mg_partner",
    
    'summary': """
        Extend partner informations
       """,
    
    'description': """
        Add VAT and another fiscal information on partner
    """,
    
    'author': "Index Mada",
    'website': "expertoerp.index-erp.net",
    
    'category': 'Uncategorized',
    'version': '16.0.1',
    
    'depends': [
        'base',
    ],
    
    'data': [
        'views/res_partner_views.xml',
        'views/res_company_views.xml',
    ],
    
    'installable': True,
    'application': False,
}
