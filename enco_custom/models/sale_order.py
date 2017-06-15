# -*- coding: utf-8 -*-
# © 2017 Ainara Galdona - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import fields, models, api


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.depends('procurement_group_id', 'mark_as_shipped',
                 'procurement_group_id.procurement_ids',
                 'procurement_group_id.procurement_ids.state')
    @api.multi
    def _get_shipped(self):
        for sale in self:
            group = sale.procurement_group_id
            val = sale.mark_as_shipped
            if group and not val:
                val = all([proc.state in ['cancel', 'done'] for proc in
                           group.procurement_ids])
            sale.shipped = val

    shipped = fields.Boolean(compute='_get_shipped', string='Delivered',
                             store=True)
    mark_as_shipped = fields.Boolean(string="Mark as shipped")
