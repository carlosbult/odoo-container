
from odoo import models, fields, api, _


class PosSession(models.Model):
    _inherit = "pos.session"


    def _loader_params_res_company(self):
        res = super(PosSession, self)._loader_params_res_company()
        fields = res.get('search_params').get('fields')
        fields.extend(['street','street2','city','state_id','vat'])
        res['search_params']['fields'] = fields
        return res


class PosConfig(models.Model):
    _inherit = "pos.config"


    cstm_field_header = fields.Char("Custom Field Header",readonly=False)
    cstm_field_footer = fields.Char("Custom Field Footer",readonly=False)
   

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    cstm_field_header = fields.Char(related='pos_config_id.cstm_field_header',readonly=False)
    cstm_field_footer = fields.Char(related='pos_config_id.cstm_field_footer',readonly=False)