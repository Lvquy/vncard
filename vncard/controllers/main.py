# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Customer(http.Controller):

    @http.route(['/me'], auth='public', website=True, csrf=False)
    def index(self, **kw):
        customer = request.env['customer.infor'].sudo()

        values = {
            'customer': customer,
        }

        return request.render('vncard.customer', values)

    # @http.route(['/top_book/details/<model("sach.doc"):sach>'], auth='public', website=True, csrf=False)
    # def sach(self, sach):
    #     values = {'sach': sach}
    #     return request.render('vncard.sach', values)
    #
    #
