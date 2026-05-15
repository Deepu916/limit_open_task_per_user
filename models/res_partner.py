# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'


    open_task_limit = fields.Integer(string='Task Limit')
    