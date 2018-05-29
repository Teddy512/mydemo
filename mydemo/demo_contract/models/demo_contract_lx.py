# -*- coding: utf-8 -*-
##############################################################################
#    公司下加说明性字段
#    author: hsxx
#    Copyright (C) 2017 myconpany.com
#
##############################################################################


from odoo import  models, fields,osv,api
from datetime import datetime
# from odoo.addons.demo_contract import models
from odoo.exceptions import UserError



# 立项包含的字段
class demo_contract_lx(models.Model):
    _description = 'li xiang '
    _name = 'demo.contract.lx'


    WORKFLOW_STATE_SELECTION = [
        ('draft', u'草稿'),
        ('confirm', u'确认'),
        ('cancel', u'取消')
    ]

    name = fields.Char(u'立项编号',default='/',)
    sequence = fields.Integer(u'自动流水号')
    lx_type = fields.Many2one('pay.type', string=u'类别', select=True, )
    lx_datetime = fields.Datetime(u'立项时间')
    date_start=fields.Datetime(u'开始日期')
    pro_name = fields.Char(u'项目名称')
    payamount = fields.Float(u'立项金额')
    smeno = fields.Text(u'备注')
    state = fields.Selection(WORKFLOW_STATE_SELECTION, default='draft', string=u'状态', readonly=True)
    company_id = fields.Many2one('res.company', string=u'公司', select=True, required=True, change_default=True, index=True, track_visibility='always' )
    partner_id = fields.Many2one('res.partner', string='对方单位',
                                 required=True, change_default=True, index=True, track_visibility='always')
    user_person=fields.Many2one('res.users',string='经手人',
                                 required=True, change_default=True, index=True, track_visibility='always')
    contact_person = fields.Many2one('hr.employee', string='联系人',
                                   required=True, change_default=True, index=True, track_visibility='always')
    lx_order_count=fields.Integer(complex='_get_lx_order_count',string=u'合同条数',store=True)




      # 新加地方,要记录立项的条数,通过合同号来找到
    def _get_lx_order_count(self, cr, uid, ids, field_name, arg, context=None):
        res = dict.fromkeys(ids, 0)
        try:
            name=self.browse(cr,uid,ids[0],context=context).name
            obj=self.pool('sigining.contract')
            sigining_contract_ids=obj.search(cr,uid,[('lx_origin','=',name)])
            res[ids[0]]=len(sigining_contract_ids)
        except:
            print u"err！"
        finally:
            return res






    # 新加的地方
    @api.model
    def create(self, vals):
        # 自动生成单号，单号统一由seq.xml里面来定义管理
        if vals.get('name', '/') == '/':
                vals['name'] = self.env['ir.sequence'].next_by_code('demo.contract.lx') or '/'
        new_id = super(demo_contract_lx, self).create(vals)
        return new_id

    # 跳转到合同页面，并带数据到合同页面
    @api.multi
    def action_view_sigining_contract(self):
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            form_id = ir_model_data.get_object_reference('demo_contract', 'view_sigining_contract_form')[1]
        except ValueError:
            form_id, = False
        ctx = dict()
        ctx.update({
            'default_model': 'sigining.contract',
            'default_res_id': self.ids[0],
            'default_contract_type': self.lx_type.id,
            'default_contract_amount': self.payamount,
            'default_lx_origin': self.name,
            'default_df_util':self.partner_id.id,
            'default_company_id':self.company_id.id,
        })
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sigining.contract',
            'views': [(form_id, 'form')],
            'view_id': form_id,
            'target': 'current',
            'context': ctx,
        }
    #
    #
    #
      ###############链接到hetong页面tree视图
    def action_open_lx_order(self, cr, uid, ids, context=None):
        try:
            act_obj = self.pool.get('ir.actions.act_window')
            mod_obj = self.pool.get('ir.model.data')
            obj=self.browse(cr,uid,ids[0],context=context)
            name=obj.name
            result = mod_obj.xmlid_to_res_id(cr, uid, 'demo_contract.action_sigining_contract',raise_if_not_found=True) #查找出动作的ID
            result = act_obj.read(cr, uid, [result], context=context)[0]

            result['domain'] = "[('lx_origin','=','" + name + "')]"
        except:
            print u"err！"
        finally:
            return result

    @api.multi
    def action_split_order(self):
        self.state = 'confirm'
        return True

    @api.multi
    def action_cancel_order(self):
        self.state = 'cancel'
        return True