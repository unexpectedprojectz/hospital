# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Hospital(models.Model):

    _name = 'hospital.hospital'

    nom = fields.Char(string= 'Nom hospital', required= True, size= 20)


    # ONE TO MANY
    metge_ids = fields.One2many('hospital.metge', 'hospital_id', string='Metges')

    historial_ids = fields.One2many('hospital.historial', 'hospital_id', string='Historials')

    malaltia_ids = fields.One2many('hospital.malaltia', 'hospital_id', string='Malalties')

    pacient_ids = fields.One2many('hospital.pacient', 'hospital_id', string='Pacients')


    # ONE TO ONE: ADRECA
    adreca_id = fields.Many2one('hospital.adreca', compute='compute_adreca', inverse='adreca_inverse')
    adreca_ids = fields.One2many('hospital.adreca', 'hospital_id')

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
            adreca.hospital_id = False
        # set new reference
        self.adreca_id.hospital_id = self
