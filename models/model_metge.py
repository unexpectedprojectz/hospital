# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Metge(models.Model):

    _name = 'hospital.metge'

    _inherit = 'hospital.persona'

    numEmpleat = fields.Integer(string= 'Núm. empleat', required= False, size= 3)

    salariMensual = fields.Integer(string= 'Salari mensual', required= False, size= 5)

    codiCompteCorrent = fields.Char(string= 'Codi compte corrent', required= False, size= 20)


    # ONE TO MANY
    hospital_id = fields.Many2one('hospital.hospital', ondelete= 'cascade', string='Hospital', required=True)


    # ONE TO ONE: VISITA
    visita_id = fields.Many2one('hospital.visita', ondelete='cascade', string='Visita')


    # ONE TO ONE: ADRECA
    adreca_id = fields.Many2one('hospital.adreca', compute='compute_adreca', inverse='adreca_inverse')
    adreca_ids = fields.One2many('hospital.adreca', 'metge_id')

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
            adreca.metge_id = False
        # set new reference
        self.adreca_id.metge_id = self.adreca_ids[0]