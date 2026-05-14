# -*- coding: utf-8 -*-
from odoo import api,models
from odoo.exceptions import ValidationError


class ProjectTask(models.Model):
    _inherit = 'project.task'


    @api.constrains('user_ids')
    def _check_user_ids(self):
        for record in self:
            for user in record.user_ids:
                limit = user.partner_id.open_task_limit
                task_count = self.env['project.task'].search_count([('user_ids','in',[user.id]),('id','!=',self.id)])
            if limit and task_count >= limit:
                raise ValidationError("This user exceeds the number of open tasks")
            