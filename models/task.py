from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class SimpleTask(models.Model):
    _name = 'simple.task'
    _description = 'Simple Task Management'
    _order = 'deadline asc, id desc'

    name = fields.Char(
        string='Task Name',
        required=True,
    )

    description = fields.Text(
        string='Description',
    )

    assigned_to = fields.Many2one(
        'res.users',
        string='Assigned To',
        default=lambda self: self.env.user,
        required=True,
    )

    deadline = fields.Date(
        string='Deadline',
        required=True,
    )

    priority = fields.Selection(
        [
            ('0', 'Low'),
            ('1', 'Normal'),
            ('2', 'High'),
            ('3', 'Urgent'),
        ],
        string='Priority',
        default='1',
        required=True,
    )

    state = fields.Selection(
        [
            ('todo', 'To Do'),
            ('progress', 'In Progress'),
            ('done', 'Done'),
        ],
        string='Status',
        default='todo',
        required=True,
    )

    is_overdue = fields.Boolean(
        string='Overdue',
        compute='_compute_is_overdue',
    )

    @api.depends('deadline', 'state')
    def _compute_is_overdue(self):
        today = fields.Date.today()

        for task in self:
            task.is_overdue = (
                task.deadline < today
                and task.state != 'done'
                if task.deadline
                else False
            )

    @api.constrains('deadline')
    def _check_deadline(self):
        for task in self:
            if not task.deadline:
                raise ValidationError(
                    _('Deadline is required.')
                )

    def action_start(self):
        for task in self:
            task.state = 'progress'

    def action_done(self):
        for task in self:
            task.state = 'done'

    def action_reset(self):
        for task in self:
            task.state = 'todo'