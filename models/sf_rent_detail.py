from odoo import models, fields


class SfRentDetail(models.Model):
    _name = 'sf_rent_detail'
    _description = 'Iki data buku buku sik dijileh per orang'

    sf_rent_id = fields.Many2one("sf_rent", required=True, ondelete='cascade')
    sf_book_id = fields.Many2one("sf_book", required=True, ondelete='cascade', string="Book")
