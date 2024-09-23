# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Borrower(models.Model):
    _name = 'library.borrower'
    _description = 'Borrower'

    name = fields.Char("Name", required=True)
    email = fields.Char("Email", required=True)
    user_id = fields.Many2one("res.users", string= "User")