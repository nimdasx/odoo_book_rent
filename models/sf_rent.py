from odoo import models, fields


class SfRent(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'sf_rent'
    _description = 'Book Rental'

    # name = fields.Char(
    #     string="Rent Name",
    #     required=True,
    #     tracking=True,
    #     help="Input rent name here")
    res_partner_id = fields.Many2one("res.partner", string="Renter")
    description = fields.Text()

    # list rent_detail, sf_rent_id dari tabel sf_rent_detail.sf_rent_id
    sf_rent_detail_ids = fields.One2many("sf_rent_detail", "sf_rent_id", string="Book Rental Details")

