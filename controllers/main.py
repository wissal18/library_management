# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
# import jwt

class LibraryController(http.Controller):

    @http.route("/api/borrower/<int:id>/loans", type="json", methods=['GET'], auth="public", csrf=False)
    def borrower_loans(self, id):
        print("here")
        # token = request.httprequest.headers.get('Authorization')
        # try:
        #     jwt.decode(token, 'secret_key', algorithms=['HS256'])
        # except jwt.ExpiredSignatureError:
        #     return request.make_response('Token has expired', 401)
        # except jwt.InvalidTokenError:
        #     return request.make_response('Invalid token', 403)

        loan_records = request.env["library.loan"].search([("borrower_id","=",id)])
        loans = []
        for loan in loan_records:
            loans += [{"book": loan.book_id.title,
                       "borrow_date": str(loan.borrow_date),
                       "return_date": str(loan.return_date) or "Not returned yet"
            }]
        return loans


