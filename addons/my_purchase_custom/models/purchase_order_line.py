from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    
    qty_forecast = fields.Float(string='Forecast', compute='_compute_forecast', digits='Product Unit of Measure')

    @api.depends('product_id')
    def _compute_forecast(self):
        for line in self:
            if line.product_id:
                product = line.product_id
               
                line.qty_forecast = product.qty_available + product.incoming_qty - product.outgoing_qty
            else:
                
                line.qty_forecast = 0
