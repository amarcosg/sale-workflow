# Copyright 2014 Akretion Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp.osv import orm
from openerp import api


class AutomaticWorkflowJob(orm.Model):
    _inherit = 'automatic.workflow.job'

    @api.model
    def _get_domain_for_sale_validation(self):
        res = super(AutomaticWorkflowJob, self).\
            _get_domain_for_sale_validation()
        res.append(('exceptions_ids', '=', False))
        return res
