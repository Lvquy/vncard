# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Customer(http.Controller):

    @http.route(['/me'], auth='user', website=True, csrf=False)
    def index(self, **kw):
        customer = request.env['customer.infor'].sudo().search([('state','in',('0','1'))])
        current_user = request.env.user.customer
        print(current_user)

        values = {
            'customer': current_user,
        }

        return request.render('vncard.customer', values)

    @http.route(['/<model("customer.infor"):customer>'], auth='public', website=True, csrf=False)
    def customer(self, customer):
        print(customer)
        values = {'customer': customer}
        return request.render('vncard.customer_details', values)


