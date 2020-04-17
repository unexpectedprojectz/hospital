# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Persona(models.AbstractModel):

    _name = 'hospital.persona'

    nom = fields.Char(string= 'Nom', required= False, size= 15)

    cognom1 = fields.Char(string='Primer cognom', required= False, size= 20)

    cognom2 = fields.Char(string= 'Segon cognom', required= False, size= 20)

    numSegSocial = fields.Char(string= 'Núm. seguretat social', required= False, size= 30)

    nif = fields.Char(string= 'NIF', required= True, size= 9)

    telefon = fields.Char(string= 'Telèfon', required= False, size= 15)