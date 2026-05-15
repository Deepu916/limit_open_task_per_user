# -*- coding: utf-8 -*-
from odoo import api, models,fields
from odoo.exceptions import ValidationError


class ProjectTask(models.Model):
    _inherit = 'project.task'

    @api.constrains('user_ids','stage_id')
    def _check_user_ids(self):
        print("Task Limit Constrain")
        for record in self:
            if record.stage_id.name in ['Done','Cancelled']:
                continue
            for user in record.user_ids:
                limit = user.partner_id.open_task_limit
                if not limit:
                    continue
                task_count = self.env['project.task'].search_count(
                    [('user_ids', 'in', [user.id]), ('id','!=',self.id),('stage_id.name', 'not in', ['Done', 'Cancelled'])])
                if task_count >= limit:
                    raise ValidationError(f"The user {user.name} exceeds the assigning tasks limit")

    def action_request(self):
        return {
            'name':'Task Assign Request',
            'type': 'ir.actions.act_window',
            'res_model': 'project.task.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_task_id': self.id},
        }
    def action_task_request_smart_button(self):
        return {
            'name':'Task Assign Request Smart Button',
            'type': 'ir.actions.act_window',
            'res_model': 'task.request',
            'view_mode': 'list',
            'domain': [('task_id','=',self.id)]
        }
