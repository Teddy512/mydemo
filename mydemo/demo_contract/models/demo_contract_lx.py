# -*- coding: utf-8 -*-
##############################################################################
#    公司下加说明性字段
#    author: hsx
#    Copyright (C) 2017 myconpany.com
#
##############################################################################


from odoo import  models, fields
from datetime import datetime

# 立项包含的字段
class demo_contract_lx(models.Model):
    _name = 'demo.contract.lx'
    _description = 'li xiang '

    name = fields.Char(u'立项编号')
    sequence = fields.Integer(u'自动流水号')
    lx_type = fields.Many2one('pay.type', string=u'类别', select=True, )
    lx_datetime = fields.Datetime(u'立项时间')
    display_name = fields.Many2one('res.partner', string=u'公司', select=True, required=True)
    df_util = fields.Many2one('res.partner', string=u'对方单位', select=True, )
    pro_name = fields.Char('项目名称')
    payamount = fields.Float(u'立项金额')
    contact_person = fields.Char(u'联系人')
    by_hand = fields.Char(u'经手人')
    smeno = fields.Text('备注')
    state = fields.Selection([
        ('draft', u'草稿'),
        ('confirm', u'确认'),
        ('cancel', u'取消'), ]
        , u'状态', readonly=True, copy=False, select=True)
    company_id = fields.Many2one('res.company', string=u'公司', select=True, )





      # 新加地方,要记录立项的条数,通过合同号来找到
    # def _get_lx_order_count(self, cr, uid, ids, field_name, arg, context=None):
    #     res = dict.fromkeys(ids, 0)
    #
    #     try:
    #         lx_origin=self.browse(cr,uid,ids[0],context=context).lx_origin
    #         obj=self.pool('sigining.contract')
    #         sigining_contract_ids=obj.search(cr,uid,[('lx_origin','=',lx_origin)])
    #         res[ids[0]]=len(sigining_contract_ids)
    #     except:
    #         print u"err！"
    #     finally:
    #         return res




    # _columns = {
    #    'sequence':fields.Integer(u'自动流水号'),
    #     # 'name':fields.Char(u'立项编号'),
    #     'lx_type':fields.Many2one('pay.type',string=u'类别',select=True,),
    #     'datetime':fields.Date(u'立项时间'),
    #     'display_name':fields.Many2one('res.partner',string=u'公司',select=True,required=True),
    #     'df_util':fields.Many2one('res.partner',string=u'对方单位',select=True,),
    #     # 'df_unit':fields.char( string=u'对方单位'),
    #     'project_name':fields.Char(u'项目名称'),
    #     'amount':fields.Float(u'立项金额'),
    #     'contact_person':fields.Char(u'联系人'),
    #     'by_hand':fields.Char(u'经手人'),
    #     'meno':fields.Text(u'备注'),
    #     # 'lx_order_count':fields.function(_get_lx_order_count,string='立项单'),
    #     'state':fields.Selection([
    #         ('draft',u'草稿'),
    #         ('confirm',u'确认'),
    #         ('cancel',u'取消'),]
    #         ,u'状态', readonly=True, copy=False, select=True),
    #     'company_id':fields.Many2one('res.company',string=u'公司',select=True,),
    # }
    # # _defaults={
    # #     'sequence':1,
    # #     'datetime':fields.Datetime.now,
    # #     'state':'draft',
    # #     'lx_origin': lambda obj, cr, uid, context: '/',
    # # }


    # 新加的地方
    # def create(self, cr, uid, vals, context=None):
    #     context = context or {}
    #
    #     partner_id = vals.get('display_name')
    #     # 根据公司来生成不同的编号
    #     if partner_id:
    #             vals['lx_origin'] = self.get_lx_sequence(cr,uid,partner_id)
    #     else:
    #             raise osv.except_osv(u'请先选择公司!')
    #     new_id=super(demo_contract_lx, self).create(cr, uid, vals, context)
    #     return new_id


    # def create_new_sequence(self,cr,uid,code,partner_id):
    #     #创建编码原则
    #     ir_sequence_type_obj=self.pool.get('ir.sequence.type')
    #     ir_sequence_type_obj.create(cr,uid,{'name':code,'code':code})
    #     values={}
    #     values['name']=code
    #     values['code']=code
    #     values['implementation']='no_gap'
    #     values['active']=True
    #     values['prefix']="%(year)s-"
    #     values['number_next']=1
    #     values['number_next_actual']=1
    #     values['number_increment']=1
    #     values['padding']=3
    #     ir_sequence_obj=self.pool.get('ir.sequence')
    #     ir_sequence_obj.create(cr,uid,values)
    #
    # def get_lx_sequence(self,cr,uid,partner_id,context=None):
    #     code="demo_contract_lx_no_%d" %(partner_id)
    #     no=self.pool.get('ir.sequence').get(cr, uid, code, context=context)
    #     if no==False:
    #         self.create_new_sequence(cr,uid,code,partner_id)
    #         no=self.pool.get('ir.sequence').get(cr, uid, code, context=context)
    #     partner_ids=self.pool.get('res.partner').search(cr,uid,[('id','=',partner_id)])
    #     partner_obj=self.pool.get('res.partner').browse(cr,uid,partner_ids)
    #     NUM= partner_obj.code
    #     NU=str(NUM)+'LX'
    #     no="%s%s" %(str(NU),no)
    #     return no
    #
    # # 创建合同
    # def action_view_sigining_contract(self, cr, uid, ids, context=None):
    #     if not context:
    #        context = {}
    #     selfobj=self.browse(cr,uid,ids[0],context=context)
    #     pickobj=self.pool('sigining.contract')
    #     ctx={'default_contract_type':selfobj.lx_type.id,'default_df_util':selfobj.df_util.id,'default_display_name':selfobj.display_name.id,'default_contract_amount':selfobj.amount,'default_lx_origin':selfobj.lx_origin}
    #     mod_obj = self.pool.get('ir.model.data')
    #     form_res = mod_obj.get_object_reference(cr, uid, 'demo_contract', 'view_sigining_contract_form')
    #     form_id = form_res and form_res[1] or False
    #
    #     return {
    #         'name':u'创建合同',
    #         'type': 'ir.actions.act_window',
    #         'view_type': 'form,tree',
    #         'view_mode': 'form,tree',
    #         'res_model': 'sigining.contract',
    #         'views': [(form_id, 'form')],
    #         'view_id':form_id,
    #         'context':ctx,
    #     }
    #
    #
    #
    #   ###############链接到hetong页面tree视图
    # def action_open_lx_order(self, cr, uid, ids, context=None):
    #     try:
    #         act_obj = self.pool.get('ir.actions.act_window')
    #         mod_obj = self.pool.get('ir.model.data')
    #         obj=self.browse(cr,uid,ids[0],context=context)
    #         lx_origin=obj.lx_origin
    #         result = mod_obj.xmlid_to_res_id(cr, uid, 'demo_contract.action_sigining_contract',raise_if_not_found=True) #查找出动作的ID
    #         result = act_obj.read(cr, uid, [result], context=context)[0]
    #
    #         result['domain'] = "[('lx_origin','=','" + lx_origin + "')]"
    #     except:
    #         print u"err！"
    #     finally:
    #         return result
    #
    #
    # # 取消按钮
    # def action_cancel_order(self,cr,uid,ids,context=None):
    #     assert len(ids)==1
    #     contract_lx_obj=self.browse(cr,uid,ids,context)
    #     contract_lx_obj.state='cancel'
    #
    # #确认按钮
    # def action_split_order(self,cr,uid,ids,context=None):
    #     assert len(ids)==1
    #     contract_lx_obj=self.browse(cr,uid,ids,context)
    #     contract_lx_obj.state='confirm'