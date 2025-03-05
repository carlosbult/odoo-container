# -*- coding: utf-8 -*-
from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def action_invoice_summary(self):
        return {
            'name': 'Invoice Payment Summary',
            'target':'new',
            'view_mode': 'form',
            "context": {'default_partner_id': self.id},
            'res_model': 'invoice.payment.summary',
            'type': 'ir.actions.act_window',
        }

