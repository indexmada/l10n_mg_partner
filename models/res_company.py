# -*- coding: utf-8 -*-

from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'
    
    nif = fields.Char(string="NIF")
    stat = fields.Char(string="STAT")
    rcs = fields.Char(string="RCS")
    code_fisc = fields.Char(string="CIF")
    date_code_fisc = fields.Date(string="Date CIF")