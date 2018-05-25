# -*- coding: utf-8 -*-
##############################################################################
#    公司下加说明性字段
#    author: hsx
#    Copyright (C) 2018 mycompayinfo.com
#
##############################################################################


from odoo import fields,osv,models
from datetime import datetime
import odoo.addons.decimal_precision as dp
from odoo.tools.translate import _



# 合同签订包含的字段
class sigining_contract(models.Model):
    _name = 'sigining.contract'
    _description ='he tong qianding'


     # 新加地方,要记录结算单条数,通过合同号来找到
    # def _get_jiesuan_order_count(self, cr, uid, ids, field_name, arg, context=None):
    #     res = dict.fromkeys(ids, 0)
    #
    #     try:
    #         contract_origin=self.browse(cr,uid,ids[0],context=context).contract_origin
    #         obj=self.pool('settle.account')
    #         sigining_contract_ids=obj.search(cr,uid,[('contract_origin','=',contract_origin)])
    #         res[ids[0]]=len(sigining_contract_ids)
    #     except:
    #         print u"err！"
    #     finally:
    #         return res
    contract_type=fields.Many2one('pay.type', string=u'合同类别', select=True, required=True, )
    name=fields.Char(u'合同编号')
    lx_origin=fields.Char(u'立项编号')
    contract_name=fields.Char(u'合同名称')
    df_util=fields.Many2one('res.partner', string=u'对方单位', select=True, )
    display_name=fields.Many2one('res.partner', string=u'公司', select=True, required=True, )
    # 'display_name=fields.related('id','display_name',relation='res.partner',string=u'公司',select=True,),
    contract_done=fields.Date(u'合同订立')
    start_contract=fields.Date(u'合同生效')
    end_contract=fields.Date(u'合同到期')
    contract_amount=fields.Float(u'合同金额')
    accumulated_amount=fields.Float(u' 累计结算')
    accumulated_pay=fields.Float(u'累计支付')
    zbjin=fields.Float(u'质保金')
    zbdate=fields.Integer(u'质保期限')
    name_related=fields.Many2one('hr.employee', string=u'经办人', select=True, )
    year=fields.Date(u'年度')
    remind=fields.Char(u'提醒天数')
    note=fields.Text(u'备注')
    discount=fields.Float(u'未结算')
    # 'jiesuan_order_count=fields.function(_get_jiesuan_order_count,string='结算清单'),
    state=fields.Selection([
        ('draft', u'草稿'),
        ('confirm', u'确认订单'),
        ('cancel', u'取消订单'), ]
        , u'状态', readonly=True, copy=False, select=True)
    company_id=fields.Many2one('res.company', string=u'公司', select=True, )

    # 新加的地方
    # def create(self, cr, uid, vals, context=None):
    #     context = context or {}
    #
    #     partner_id = vals.get('display_name')
    #     ht_type = vals.get('contract_type')
    #
    #     # 根据公司来生成不同的编号,不同类别从1开始
    #     if partner_id and ht_type:
    #             vals['contract_origin'] = self.get_ht_sequence(cr,uid,partner_id,ht_type)
    #
    #     else:
    #             raise osv.except_osv(u'请先选择公司或类别!')
    #
    #     new_id=super(sigining_contract, self).create(cr, uid, vals, context)
    #     return new_id
    #
    #
    # def create_ht_sequence(self,cr,uid,code,partner_id,ht_type):
    #     #创建编码原则
    #     ir_sequence_type_obj=self.pool.get('ir.sequence.type')
    #     ir_sequence_type_obj.create(cr,uid,{'name=code,'code=code})
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
    # #
    # def get_ht_sequence(self,cr,uid,partner_id,ht_type,context=None):
    #
    #     code="sigining_contract_no_%d_%d" %(partner_id,ht_type)
    #     no=self.pool.get('ir.sequence').get(cr, uid, code, context=context)
    #
    #
    #
    #     if no==False:
    #         self.create_ht_sequence(cr,uid,code,partner_id,ht_type)
    #         no=self.pool.get('ir.sequence').get(cr, uid, code, context=context)
    #
    #     partner_ids=self.pool.get('res.partner').search(cr,uid,[('id','=',partner_id)])
    #     ht_types=self.pool.get('pay.type').search(cr,uid,[('id','=',ht_type)])
    #
    #     partner_obj=self.pool.get('res.partner').browse(cr,uid,partner_ids)
    #     ht_types_obj=self.pool.get('pay.type').browse(cr,uid,ht_types)
    #
    #     print ht_types_obj.spay_type_jc
    #     no = "%s%s%s" %(partner_obj.code,no,ht_types_obj.spay_type_jc)
    #     return no
    #
    #
    #    # 新加地方,执行动作找到对应页面,结算单据
    # def action_jiesuan_order(self, cr, uid, ids, context=None):
    #     if not context:
    #        context = {}
    #     selfobj=self.browse(cr,uid,ids[0],context=context)
    #     pickobj=self.pool('settle.account')
    #     ctx={'default_contract_origin=selfobj.contract_origin,'default_contract_type=selfobj.contract_type.id,'default_contract_name_qd=selfobj.contract_name,'default_df_util=selfobj.df_util.id,'default_contract_amount=selfobj.contract_amount,'default_display_name=selfobj.display_name.id}
    #     mod_obj = self.pool.get('ir.model.data')
    #     form_res = mod_obj.get_object_reference(cr, uid, 'demo_contract', 'view_settle_account_form')
    #     form_id = form_res and form_res[1] or False
    #
    #
    #     return {
    #         'name=u'结算单页面',
    #         'type= 'ir.actions.act_window',
    #         'view_type= 'form,tree' ,
    #         'view_mode= 'form,tree',
    #         'res_model= 'settle.account',
    #         'views= [(form_id, 'form')],
    #         'view_id=form_id ,
    #         'context=ctx,
    #     }
    #
    #    ###############链接到结算单
    # def action_open_jiesuan_order(self, cr, uid, ids, context=None):
    #     try:
    #         act_obj = self.pool.get('ir.actions.act_window')
    #         mod_obj = self.pool.get('ir.model.data')
    #         obj=self.browse(cr,uid,ids[0],context=context)
    #         contract_origin=obj.contract_origin
    #         result = mod_obj.xmlid_to_res_id(cr, uid, 'demo_contract.action_settle_account',raise_if_not_found=True) #查找出动作的ID
    #         result = act_obj.read(cr, uid, [result], context=context)[0]
    #
    #         result['domain'] = "[('contract_origin','=','" + contract_origin + "')]"
    #     except:
    #         print u"err！"
    #     finally:
    #         return result
    #
    #
    #
    #       # 取消按钮
    # def action_cancel_order_ht(self,cr,uid,ids,context=None):
    #     assert len(ids)==1
    #     # 获取这张单据，用browse方法，删除条件为cancel的单据
    #     sigining_contract_obj=self.browse(cr,uid,ids,context)
    #     sigining_contract_obj.state='cancel'
    #     name=sigining_contract_obj.contract_origin
    #     sql2=" UPDATE settle_account SET state='cancel' where contract_origin='%s'"%(str(name))
    #     cr.execute(sql2)
    #
    #
    #
    #
    # #确认按钮  反写回合同页面
    # def action_split_order_ht(self,cr,uid,ids,context=None):
    #     assert len(ids)==1
    #     sigining_contract_obj=self.browse(cr,uid,ids,context)
    #     sigining_contract_obj.state='confirm'
    #     # name=sigining_contract_obj.contract_origin
    #     # sql="select sum(total_pay) as paytotal,sum(total_jies)  as jiestotal from  settle_account  where contract_origin='%s' GROUP BY contract_origin "%(str(name))
    #     # cr.execute(sql)
    #     # dict1=cr.dictfetchall()[0]
    #     # sigining_contract_obj.accumulated_amount= dict1['jiestotal']
    #     # sigining_contract_obj.accumulated_pay= dict1['paytotal']
    #
    #
    # # 重写删除方法，删除合同单，连结算单一起删除，可用sql语句，ids表示这个单子的id
    # def unlink(self, cr, uid, ids, context=None):
    #
    #     # sigining_contract查出状态信息
    #     sigining_contract = self.read(cr, uid, ids, ['state'], context=context)
    #     sigining_contract_obj=self.browse(cr,uid,ids,context)
    #     name=sigining_contract_obj.contract_origin
    #     # 根据合同号删除结算单号
    #     sql="DELETE from settle_account where contract_origin='%s'"%(str(name))
    #     cr.execute(sql)
    #     unlink_ids = []
    #     for s in sigining_contract:
    #          if s['state'] in ['draft','cancel','confirm']:
    #             unlink_ids.append(s['id'])
    #          else:
    #             raise osv.except_osv((u'警告!'), (u'已确认订单不可删除'))
    #
    #     return osv.osv.unlink(self, cr, uid, unlink_ids, context=context)
    #
    #

