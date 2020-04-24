# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Visita(models.Model):

    _name = 'hospital.visita'

    data = fields.Date()


    # MANY TO ONE
    historial_id = fields.Many2one('hospital.hospital', ondelete='cascade', string='Hospital', required=True)


    # ONE TO ONE: MALALTIA
    malaltia_id = fields.Many2one('hospital.malaltia', compute='compute_malaltia', inverse='malaltia_inverse')
    malaltia_ids = fields.One2many('hospital.malaltia', 'visita_id')

    @api.one
    @api.depends('malaltia_ids')
    def compute_malaltia(self):
        if len(self.malaltia_ids) > 0:
            self.malaltia_id = self.malaltia_ids[0]

    @api.one
    def malaltia_inverse(self):
        if len(self.malaltia_ids) > 0:
            # delete previous reference
            malaltia = self.env['hospital.malaltia'].browse(self.malaltia_ids[0].id)
            malaltia.visita_id = False
        # set new reference
        self.malaltia_id.visita_id = self.malaltia_ids[0]


    # ONE TO ONE: METGE
    metge_id = fields.Many2one('hospital.metge', compute='compute_metge', inverse='metge_inverse')
    metge_ids = fields.One2many('hospital.metge', 'visita_id')

    @api.one
    @api.depends('metge_ids')
    def compute_metge(self):
        if len(self.metge_ids) > 0:
            self.metge_id = self.metge_ids[0]

    @api.one
    def metge_inverse(self):
        if len(self.metge_ids) > 0:
            # delete previous reference
            metge = self.env['hospital.metge'].browse(self.metge_ids[0].id)
            metge.visita_id = False
        # set new reference
        self.metge_id.visita_id = self.metge_ids[0]