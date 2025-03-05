# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime


class InvoicePaymentSummary(models.TransientModel):
    _name = "invoice.payment.summary"

    partner_id = fields.Many2one("res.partner", string="Customer", required=True)
    start_date = fields.Date(
        string="Start Date", default=datetime.today().replace(day=1), required=True
    )
    end_date = fields.Date(string="End Date", default=datetime.today(), required=True)
    company_id = fields.Many2one("res.company", default=lambda self: self.env.company)

    def get_invoice_payment_summary(self):
        # Get the currency object
        currency = (
            self.partner_id.property_product_pricelist.currency_id
            or self.env.company.currency_id
        )

        # Filter invoices and payments
        domain_invoices = [
            "|",
            ("move_type", "=", "out_invoice"),
            ("move_type", "=", "out_refund"),
            ("partner_id", "=", self.partner_id.id),
            ("invoice_date", ">=", self.start_date),
            ("invoice_date", "<=", self.end_date),
        ]
        domain_payments = [
            ("partner_id", "=", self.partner_id.id),
            ("date", ">=", self.start_date),
            ("date", "<=", self.end_date),
            ("payment_type", "=", "inbound"),
        ]

        invoices = self.env["account.move"].search(domain_invoices)
        payments = self.env["account.payment"].sudo().search(domain_payments)

        # Initialize results
        inv_list = []
        total = 0

        # Function to format monetary values
        def format_currency(amount):
            return f"{currency.symbol} {amount:,.2f}"

        # Process payments
        for payment in payments:
            amount = payment.amount
            inv_list.append(
                {
                    "create_date": payment.date.strftime("%m/%d/%Y"),
                    "name": f"{payment.name}-{payment.date.strftime('%B %Y')}",
                    "debit": 0,
                    "credit": format_currency(amount),
                    "balance": format_currency(amount),
                }
            )
            total += amount

        # Process invoices
        for invoice in invoices:
            residual = invoice.amount_total_signed
            inv_list.append(
                {
                    "create_date": invoice.invoice_date.strftime("%m/%d/%Y"),
                    "name": f"{invoice.name}-{invoice.invoice_date.strftime('%B %Y')}",
                    "debit": format_currency(residual),
                    "credit": 0,
                    "balance": format_currency(residual),
                }
            )
            total -= residual

        # Combine results
        return {
            "inv_list": inv_list,
            "total": format_currency(total),
        }
