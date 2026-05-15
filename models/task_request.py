# -*- coding: utf-8 -*-
from odoo import api, fields, models


class TaskRequest(models.Model):
    _name = 'task.request'
    _description = 'Task Request'

    user_id = fields.Many2one('res.users', string='User')
    task_id = fields.Many2one('project.task', string='Task')
    assignee_ids = fields.Many2many('res.users', string='Assignees')

    def action_assign_task(self):
        assignee_ids = self.assignee_ids
        for ids in assignee_ids:
            print(ids)
            ids.partner_id.open_task_limit += 1
            print(self.task_id.user_ids)
            self.task_id.user_ids = [fields.Command.link(ids.id)]
            self.unlink()
