# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GestioHospital(models.Model):

    _name = 'hospital.gestiohospital'


    # ONE TO ONE: HOSPITAL
    hospital_id = fields.Many2one('hospital.hospital', ondelete='cascade', string='Hospital')