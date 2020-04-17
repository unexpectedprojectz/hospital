# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pacient(models.Model):

    _name = 'hospital.pacient'

    _inherit = 'hospital.persona'

    hospital_id = fields.Many2one('hospital.hospital', ondelete=cascade, string='Hospital', required=False)