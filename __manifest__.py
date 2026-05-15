# -*- coding: utf-8 -*-
{
    'name': 'Limit Open Task',
    'version': '19.0.1.0.0',
    'description': 'Limit Open Task per user',
    'depends': [
        'project',
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/task_assign_user_groups.xml',
        'wizard/project_task_wizard_views.xml',
        'views/task_request_views.xml',
        'views/project_task_views.xml',
        'views/partner_views.xml',
    ]

}
