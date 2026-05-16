# -*- coding: utf-8 -*-
"""Project task wizard model"""
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ProjectTaskWizard(models.TransientModel):
    """Project task wizard model"""
    _name = 'project.task.wizard'


    task_id = fields.Many2one('project.task')
    assignee_ids = fields.Many2many('res.users')
    user_id = fields.Many2one('res.users',default=lambda self: self.env.user.id)

    def action_send(self):
        """Send button action"""
        self.env['task.request'].create({
            'task_id': self.task_id.id,
            'assignee_ids': self.assignee_ids.ids,
            'user_id': self.user_id.id,
        })

    @api.constrains('assignee_ids','task_id')
    def _check_assignee_ids(self):
        """Checking duplicate task request"""
        task_request = self.env['task.request'].search([('task_id','=',self.task_id.id),('assignee_ids','in',self.assignee_ids.ids)])
        if task_request:
            raise ValidationError('The request for this assigner is already in progress')
