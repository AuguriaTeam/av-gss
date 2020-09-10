# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Stockmove(models.Model):
    _inherit = 'stock.move'
    
    partner_group_id = fields.Many2one('res.partner', compute='_compute_partner')
    
    @api.depends('group_id')
    def _compute_partner(self):
        for r in self:
            sale = self.env['sale.order'].search([('name', '=', r.group_id.name)])
            if sale:
                r.partner_group_id.id = sale.partner_id.id
    

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    partner_group_id = fields.Many2one('res.partner', compute='_compute_partner')
    
    @api.depends('group_id')
    def _compute_partner(self):
        for r in self:
            sale = self.env['sale.order'].search([('name', '=', r.group_id.name)])
            if sale:
                r.partner_group_id.id = sale.partner_id.id