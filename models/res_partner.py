# -*- coding: utf-8 -*-
"""res.partner model"""
from odoo import fields, models


class ResPartner(models.Model):
    """res.partner model"""
    _inherit = 'res.partner'


    open_task_limit = fields.Integer(string='Task Limit')
    