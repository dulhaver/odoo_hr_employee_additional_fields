from openerp.osv import fields, osv


class hr_employee(osv.osv):
    _inherit = 'hr.employee'

    _columns = {
        'emp_number': fields.integer('Employee Number', size=16),
        'shebao_number': fields.char('She Bao #', size=64),
        'hukou': fields.char('Hu Kou', size=64),
        'join_company_date': fields.date('Join company Date', size=8),
    }

hr_employee()
