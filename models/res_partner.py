# -*- coding: UTF-8 -*-

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    nif = fields.Char(string="NIF", size=32)
    stat = fields.Char(string="STAT", size=32)
    rcs = fields.Char(string="RCS", size=32)
    cin = fields.Char(string="CIN", size=32)
    date_cin = fields.Date(string="Date CIN")
    code_fisc = fields.Char(string="CIF")
    date_code_fisc = fields.Date(string="Date CIF")
    secteur = fields.Char(string="Secteur")
