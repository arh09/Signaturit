# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from signaturit_sdk.signaturit_client import SignaturitClient

client = SignaturitClient('YkgEPFZskZTLjOzRqWxSkPCiWtZwdGScslDXYDMeTxLshCCyIiorqeFwhpMGRCKszKmUDRpnWcXTloMDOHRpFM')


class WizardSignaturit(models.TransientModel):
    _name = 'wizard.signaturit'
    _description = 'Wizard Signaturit'

    path_file = fields.Char('Path file', required=True)

    def signaturit_confirm(self):
        recipients = [{'name': self.env.user.name, 'email': self.env.user.email}]
        sign_params = {'subject': 'To sign', 'body': 'Please, can you sign this?'}
        file_path = self.path_file
        response = client.create_signature(file_path, recipients, sign_params)
        return response


class SignaturitWizard(models.TransientModel):
    _name = 'signaturit.wizard'
    _description = 'Signaturit Wizard'

    def confirm(self):
        response = client.get_signatures()
        for item in response:
            self.env['signaturit.document'].create({'name': item['documents'][0]['file']['name'],
                                                    'state': item['documents'][0]['status']})
        return response
