# -*- coding: utf-8 -*-
# © 2017 Ainara Galdona - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import fields, models, api


class AccountReportGeneralLedger(models.TransientModel):

    _inherit = "account.report.general.ledger"

    not_show_counterpart = fields.Boolean(string="Not show Counterpart",
                                          default=True)

    @api.multi
    def _print_report(self, data):
        res = super(AccountReportGeneralLedger, self)._print_report(data=data)
        data = res.get('data', data)
        if ('landscape' in data['form'] and not data['form']['landscape']):
            data['form'].pop('landscape')
        if self.not_show_counterpart:
            res_ctx = res.get('context', self.env.context)
            recs = self
            if res_ctx.get('active_model') == 'account.account':
                recs = self.env['account.account'].browse(
                    res_ctx.get('active_ids'))
            return self.with_context(res_ctx).env['report'].get_action(
                recs, 'enco_general_ledger.report_enco_generalledger',
                data=data)
        return res
