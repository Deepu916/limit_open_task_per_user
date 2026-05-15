# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProjectTaskWizard(models.TransientModel):
    _name = 'project.task.wizard'


    task_id = fields.Many2one('project.task')
    assignee_ids = fields.Many2many('res.users')
    user_id = fields.Many2one('res.users',default=lambda self: self.env.user.id)

    def action_send(self):
        self.env['task.request'].create({
            'task_id': self.task_id.id,
            'assignee_ids': self.assignee_ids.ids,
            'user_id': self.user_id.id,
        })
