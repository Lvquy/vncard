# -*- coding: utf-8 -*-
import random

from odoo import api, fields, models
from datetime import datetime
from odoo.exceptions import UserError


class ResUsers(models.Model):
    _inherit = 'res.users'

    customer = fields.Many2one(comodel_name='customer.infor', string='Tài khoản liên kết')
class CustomerInfor(models.Model):
    _name = 'customer.infor'
    _rec_name = 'ma_kh'
    _description = 'Khách hàng'
    _order = "id desc"

    name = fields.Char(string='Tên')
    ma_kh = fields.Char(string='Mã khách hàng', readonly=True, default=lambda self: 'New')
    gioi_tinh = fields.Selection([('nam', 'Nam'), ('nu', 'Nữ')], string='Giới tính')
    img = fields.Binary(string='Hình ảnh')
    nam_sinh = fields.Date(string='Năm sinh')
    dia_chi = fields.Text(string='Địa chỉ')
    note = fields.Html(string='Lời giới thiệu')
    mobile = fields.Char(string='Số điện thoại')
    email = fields.Char(string='Email')
    total_click = fields.Integer(string='Tổng lượt click')
    link_share = fields.One2many(comodel_name='link.share', inverse_name='customer', string='Liên kết của tôi')
    state = fields.Selection([('0','Dùng thử'),('1','Đã kích hoạt'),('2','Đã hủy')],default='0', string='Trạng thái')
    link_user = fields.Many2one(comodel_name='res.users', string='Tài khoản liên kết')

    @api.model
    def create(self, vals):
        if vals.get('ma_kh', 'New' == 'New'):
            vals['ma_kh'] = self.env['ir.sequence'].next_by_code('customer.code') or 'New'
            res = super(CustomerInfor, self).create(vals)
        return res


    def confirm(self):
        for rec in self:
            if rec.state == '0':
                rec.state = '1'
            else:
                raise UserError('Làm mới trình duyệt')
    def cancel(self):
        for rec in self:
            if rec.state == '1':
                rec.state = '2'
            else:
                raise UserError('Làm mới trình duyệt')

    def retrial(self):
        for rec in self:
            rec.state = '0'

    def get_totalclick(self):
        pass

class LinkShare(models.Model):
    _name = 'link.share'
    _description = 'Link chia sẻ'
    _rec_name = 'name'

    name = fields.Char(string='Tên link')
    link = fields.Char(string='Link')
    icon = fields.Binary(string='Icon hình ảnh')
    count_click = fields.Integer(string='Tổng lượt click')
    index = fields.Integer(string='Thứ tự hiển thị')
    customer = fields.Many2one(comodel_name='customer.infor', string='Tên')
