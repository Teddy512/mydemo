# -*- coding: utf-8 -*-
##############################################################################
#    公司下加说明性字段
#    author: hsx
#    Copyright (C) 2017 odooinfo.com
#
##############################################################################


from odoo import fields,models,osv
from datetime import datetime

# 结算清单包含的字段
class settle_account(models.Model):
    _name = 'settle.account'
    _description = 'jie suan qingdan'

    contract_origin=fields.Char(u'合同编号')
    display_name=fields.Many2one('res.partner', string=u'公司', select=True, )
    contract_name_qd=fields.Char(u'合同名称')
    name=fields.Char(u'结算单号')
    contract_type=fields.Many2one('pay.type', string=u'合同类别', select=True, )
    jies_date=fields.Date(u'结算日期')
    jies_account=fields.Float(u'结算金额')
    pay_account=fields.Float(u'支付金额')
    accumulated_amount=fields.Float(u'累计结算')
    big_accumulated_amount=fields.Char(u' 累计结算(大写)', )
    accumulated_pay=fields.Float(u'累计支付')
    big_accumulated_pay=fields.Char(u'累计支付(大写)', )
    note=fields.Char(u'备注')
    contract_amount=fields.Float(u'合同金额')
    big_contract_amount=fields.Char(u'合同金额(大写)', )
    df_util=fields.Many2one('res.partner', string=u'对方单位', select=True, )
    line_id=fields.One2many('settle.account.line', 'contract_origin_line', 'Order Line', copy=True)
    note1=fields.Char(u'备注')
    state=fields.Selection([
        ('draft', u'草稿'),
        ('confirm', u'确认订单'),
        ('cancel', u'取消订单'), ]
        , u'状态', readonly=True, copy=False, select=True)


    #
    #
    # #改动地方 总支付金额 求和:
    # def _get_subtotal(self, cr, uid, ids, field_name, arg,  context=None):
    #     res = {}
    #     for order in self.browse(cr, uid, ids, context=context):
    #         subtotal=0
    #         for line in order.line_id:
    #             subtotal += line.jies_account_line
    #         res[order.id] = subtotal
    #     return res
    #
    #
    # #改动地方 小计增加金额 求和:
    # def _get_sumzaccount(self, cr, uid, ids, field_name, arg,  context=None):
    #
    #     res={}
    #     for order in self.browse(cr, uid, ids, context=context):
    #         Q=0.0
    #         qq=order.zadd_money
    #         qq1=order.zadd_money2
    #         qq2=order.zadd_money3
    #         qq3=order.zadd_money4
    #         Q=qq+qq1+qq2+qq3
    #         res[order.id]=Q
    #
    #     return res
    #
    # #改动地方 小计减少金额 求和:
    # def _get_sumjaccount(self, cr, uid, ids, field_name, arg,  context=None):
    #
    #     res={}
    #     for order in self.browse(cr, uid, ids, context=context):
    #         P=0.0
    #         jj=order.jadd_money
    #         jj1=order.jadd_money2
    #         jj2=order.jadd_money3
    #         jj3=order.jadd_money4
    #         P=jj+jj1+jj2+jj3
    #         res[order.id]=P
    #
    #     return res
    #
    #
    #  #改动地方 总结算金额 求和:
    # def _get_subtotal2(self, cr, uid, ids, field_name, arg,  context=None):
    #     # 初始化
    #     print ids
    #     print 11
    #     res = {}
    #     # 获取本页面单据
    #     for order in self.browse(cr, uid, ids, context=context):
    #         subtotal2=0
    #         # 循环遍历明细表中的数据，汇总
    #         for line in order.line_id:
    #             # 明细表中数据，以次相加
    #             subtotal2 += line.pay_account_line
    #         res[order.id] = subtotal2
    #     return res

  
       
       # 'total_pay=fields.function(_get_subtotal2,string=u'总支付金额',type='float',store=True,),
       # 'total_jies=fields.function(_get_subtotal,string=u'总结算金额',type='float',store=True,),


    # def create(self,cr,uid,vals,context=None):
    #     if context is None:
    #         context ={}
    #     ct=vals.get('contract_amount')
    #     big = self.pool.get('global.function').numtoCny(ct)
    #     vals['big_contract_amount']=big
    #     if vals.get('jiesuan_number', '/') == '/=
    #         vals['jiesuan_number'] = self.pool.get('ir.sequence').get(cr, uid, 'settle.account', context=context) or '/'
    #     new_id=super(settle_account,self).create(cr,uid,vals,context=context)
    #     return new_id
    #
       # 取消按钮
    def action_cancel_order_js(self,cr,uid,ids,context=None):
        assert len(ids)==1
        settle_account_obj=self.browse(cr,uid,ids,context)
        settle_account_obj.state='cancel'


    #确认按钮
    def action_split_order_js(self,cr,uid,ids,context=None):
        assert len(ids)==1

        # 获取结算单，状态为完成的
        settle_account_obj=self.browse(cr,uid,ids,context)
        settle_account_obj.state='confirm'
    #
    #     name=settle_account_obj.contract_origin
    #
    #      # 获取合同编号，并查出总的支付和结算金额
    #     sql="select sum(total_pay) as paytotal,sum(total_jies)  as jiestotal from  settle_account  where contract_origin='%s' GROUP BY contract_origin "%(str(name))
    #     cr.execute(sql)
    #     dict1=cr.dictfetchall()[0]
    #     if dict1:
    #      PT=dict1['paytotal']
    #      JT=dict1['jiestotal']
    #
    #      # 当前页面的字段赋值重新
    #      settle_account_obj.accumulated_amount=dict1['jiestotal']
    #      settle_account_obj.accumulated_pay=dict1['paytotal']
    #      pt=settle_account_obj.accumulated_amount
    #
    #      # 将数据转化为大写
    #      big = self.pool.get('global.function').numtoCny(pt)
    #      settle_account_obj.big_accumulated_amount=big
    #
    #      # 自动更新合同页面上的累计结算和累计支付
    #      sql2=" UPDATE sigining_contract SET accumulated_amount='%d',accumulated_pay='%d' where contract_origin='%s'"%(JT,PT,str(name))
    #      cr.execute(sql2)
    #     else:
    #      return True
    #
    #
    # def on_change_diszcount(self,cr,uid,ids,zadd_money,zadd_money2,context=None):
    #     result={}
    #     if zadd_money>0.0 :
    #         result['zaccount']=zadd_money
    #     return {'value=result}




# 结算明细包含的字段
class settle_account_line(models.Model):
    _description = 'jie suan qingdan  mingxi'
    _name = 'settle.account.line'

    name=fields.Integer(u'流水号')
    contract_origin_line=fields.Many2one('settle.account', u'合同编号')
    jies_date_line=fields.Datetime(u'结算日期')
    jies_account_line=fields.Float(u'结算金额')
    pay_account_line=fields.Float(u'支付金额')
    contract_type=fields.Many2one('pay.type', string=u' 合同类别', select=True, )
    note=fields.Char(u'备注')

    