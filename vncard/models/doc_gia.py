# -*- coding: utf-8 -*-
import random

from odoo import api, fields, models
from datetime import datetime
from odoo.exceptions import UserError


class CustomerInfor(models.Model):
    _name = 'customer.infor'
    _rec_name = 'name'
    _description = 'Khách hàng'
    _order = "id desc"

    name = fields.Char(string='Tên')
    ma_kh = fields.Char(string='Mã khách hàng', readonly=True, default=lambda self: 'New')
    gioi_tinh = fields.Selection([('nam', 'Nam'), ('nu', 'Nữ')], string='Giới tính')
    img = fields.Binary(string='Hình ảnh')
    nam_sinh = fields.Date(string='Năm sinh')
    dia_chi = fields.Text(string='Địa chỉ')
    note = fields.Html(string='Ghi chú')
    mobile = fields.Char(string='Số điện thoại')
    total_click = fields.Integer(string='Tổng lượt click')

class LinkShare(models.Model):
    _name = 'link.share'
    _description = 'Link chia sẻ'
    _rec_name = 'name'

    name = fields.Char(string='Tên link')
    link = fields.Char(string='Link')
    icon = fields.Binary(string='Icon hình ảnh')
    count_click = fields.Integer(string='Tổng lượt click')
    index = fields.Integer(string='Thứ tự hiển thị')
