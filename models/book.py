# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Book(models.Model):
    _name = 'library.book'
    _description = 'Books'

    title = fields.Char("Title", required=True)
    writer = fields.Char("Writer", required=True)
    type = fields.Selection([("science","Science"),
                             ("fiction","Fiction"),
                             ("romantic","Romantic"),
                             ("tragedy","Tragedy"),
                             ("poetry","Poetry")], string="Type")
    edition_date = fields.Date("Edition Date")
    edition_house = fields.Char("Edition House")
    isbn_code = fields.Char("ISBN Code")