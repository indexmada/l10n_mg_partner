# -*- coding: utf-8 -*-
{
    'name': "l10n_mg_partner",
    
    'summary': """
        Extend partner informations
       """,
    
    'description': """
        Add VAT and another fiscal information on partner
    """,
    
    'author': "m0r7y",
    'website': "r.radoniaina11@gmail.com",
    
    'category': 'Uncategorized',
    'version': '0.1',
    
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
