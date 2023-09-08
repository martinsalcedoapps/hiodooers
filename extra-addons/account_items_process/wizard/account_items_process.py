from odoo import api, models, fields, _


class AccountItemsProcess(models.TransientModel):
    _name = 'account.items.process'
    _description = 'Account Items Process'

    actions = fields.Selection(
            [
                ('purchase-order', 'Generate Purchase Order'),
                ('stock-check', 'Check Stock'),
            ], default='purchase-order', string="Actions"
    )
    product_ids = fields.One2many('account.items.process.line', 'parent_id', string="Products")

    def process(self):
        pass


class AccountItemsProcessLine(models.TransientModel):
    _name = 'account.items.process.line'
    _description = 'Account Items Process Line'

    parent_id = fields.Many2one('account.items.process', string="Processor", ondelete='cascade')
    selected = fields.Boolean('Selected')
    product_id = fields.Many2one('product.product', string="Product")
    qty = fields.Float("Qty")
