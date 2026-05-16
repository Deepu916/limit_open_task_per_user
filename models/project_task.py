# -*- coding: utf-8 -*-
"""Project Task Model"""
from odoo import api, models,fields
from odoo.exceptions import ValidationError


class ProjectTask(models.Model):
    """Project Task Model"""
    _inherit = 'project.task'

    task_request = fields.Boolean(string='Task Request',compute='_compute_task_request')
    @api.constrains('user_ids','stage_id')
    def _check_user_ids(self):
        """Check if users can assign tasks"""
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

    def _compute_task_request(self):
        """Compute method for checking the task present in the task request model"""
        for record in self:
            task_count = self.env['task.request'].search_count([('task_id','=',record.id)])
            if task_count > 0:
                self.task_request = True
            else:
                self.task_request = False
    def action_request(self):
        """Assign task request button action"""
        return {
            'name':'Task Assign Request',
            'type': 'ir.actions.act_window',
            'res_model': 'project.task.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_task_id': self.id},
        }
    def action_task_request_smart_button(self):
        """Assign task request smart button action"""
        return {
            'name':'Task Assign Request Smart Button',
            'type': 'ir.actions.act_window',
            'res_model': 'task.request',
            'view_mode': 'list',
            'domain': [('task_id','=',self.id)]
        }
