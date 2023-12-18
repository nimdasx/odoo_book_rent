from odoo import models, fields


class SfBook(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'sf_book'
    _description = 'Book'

    name = fields.Char(
        string="Book Name",
        required=True,
        tracking=True,
        help="Input book name here")
    description = fields.Text()

    _sql_constraints = [
        ('name_check', 'unique(name)', 'Book Name must unique!')
    ]
