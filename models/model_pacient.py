# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pacient(models.Model):

    _name = 'hospital.pacient'

    _inherit = 'hospital.persona'


    # MANY TO ONE
    hospital_id = fields.Many2one('hospital.hospital', ondelete='cascade', string='Hospital', required=True)


    # ONE TO ONE: ADRECA
    adreca_id = fields.Many2one('hospital.adreca', compute='compute_adreca', inverse='adreca_inverse')
    adreca_ids = fields.One2many('hospital.adreca', 'pacient_id')

    @api.one
    @api.depends('adreca_ids')
    def compute_adreca(self):
        if len(self.adreca_ids) > 0:
            self.adreca_id = self.adreca_ids[0]

    @api.one
    def adreca_inverse(self):
        if len(self.adreca_ids) > 0:
            # delete previous reference
            adreca = self.env['hospital.adreca'].browse(self.adreca_ids[0].id)
            adreca.pacient_id = False
        # set new reference
        self.adreca_id.pacient_id = self


    # ONE TO ONE: HISTORIAL
    historial_id = fields.Many2one('hospital.historial', compute='compute_historial', inverse='historial_inverse')
    historial_ids = fields.One2many('hospital.historial', 'pacient_id')

    @api.one
    @api.depends('historial_ids')
    def compute_historial(self):
        if len(self.historial_ids) > 0:
            self.historial_id = self.historial_ids[0]

    @api.one
    def historial_inverse(self):
        if len(self.historial_ids) > 0:
            # delete previous reference
            historial = self.env['hospital.historial'].browse(self.historial_ids[0].id)
            historial.pacient_id = False
        # set new reference
        self.historial_id.pacient_id = self