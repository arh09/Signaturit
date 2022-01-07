# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
from signaturit_sdk.signaturit_client import SignaturitClient

client = SignaturitClient('YkgEPFZskZTLjOzRqWxSkPCiWtZwdGScslDXYDMeTxLshCCyIiorqeFwhpMGRCKszKmUDRpnWcXTloMDOHRpFM')


class SignaturitDocument(models.Model):
    _name = "signaturit.document"

    name = fields.Char()
    state = fields.Char()
