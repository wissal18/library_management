# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Loan(models.Model):
    _name = 'library.loan'
    _description = 'Loan'

    book_id = fields.Many2one("library.book",string="Book")
    borrower_id = fields.Many2one("library.borrower", string="Borrower")
    borrow_date = fields.Date("Borrow Date", default=fields.Date.today)
    return_date = fields.Date("Return Date")

    @api.constrains("borrower_id")
    def _check_borrower_limit(self):
        for record in self:
            borrow_count = self.env["library.loan"].search_count([("borrower_id","=",record.borrower_id.id),
                                                                  ("return_date","=",False)])
            if borrow_count >= 5 :
                raise ValidationError("You cannot borrow more than 5 books simultaneously")

