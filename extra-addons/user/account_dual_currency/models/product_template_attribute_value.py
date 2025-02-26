# -*- coding: utf-8 -*-

from itertools import groupby
from odoo import api, fields, models, _
from odoo.tools.float_utils import float_compare, float_is_zero, float_round
from odoo.exceptions import AccessError, UserError, ValidationError


class ProductTemplateAttributeValue(models.Model):
    _inherit = "product.template.attribute.value"

    currency_id_dif = fields.Many2one(
        "res.currency",
        string="Currency USD",
        default=lambda self: self.env.user.company_id.currency_id_dif.id,
    )

    price_extra_usd = fields.Monetary(
        string="Precio Extra $",
        currency_field="currency_id_dif",
        digits="Dual_Currency",
    )

    price_extra = fields.Float(
        string="Value Price Extra",
        default=0.0,
        digits="Product Price",
        help="Extra price for the variant with this attribute value on sale price."
        " eg. 200 price extra, 1000 + 200 = 1200.",
        compute="_compute_price_extra",
        inverse="_set_price_extra_usd",
        store=True,
    )

    @api.depends("price_extra_usd")
    def _compute_price_extra(self):
        for rec in self:
            if rec.currency_id_dif.rate > 0:
                rec.price_extra = rec.price_extra_usd / rec.currency_id_dif.rate

    def _set_price_extra_usd(self):
        for rec in self:
            rec.price_extra_usd = rec.price_extra * rec.currency_id_dif.rate
