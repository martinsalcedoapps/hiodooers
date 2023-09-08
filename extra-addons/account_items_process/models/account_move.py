from odoo import api, models, fields, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    def process_items(self):
        vals = {}
        vals['product_ids'] = [(5,0,0)]
        for line in self.invoice_line_ids:
            ivals = {}
            ivals['selected'] = True
            ivals['product_id'] = line.product_id.id
            ivals['qty'] = line.quantity
            vals['product_ids'].append((0,0,ivals))
        wizard = self.env['account.items.process'].create(vals)
        return {
            'type'     : 'ir.actions.act_window',
            'name'     : _('Process Items'),
            'res_model': 'account.items.process',
            'target'   : 'new',
            'view_mode': 'form',
            'res_id'   : wizard.id,
        }
