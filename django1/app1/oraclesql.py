# -*- coding: utf-8 -*-
import paramiko ,re ,time ,sys ,subprocess ,chardet
def sftp_upload_file(local_path ,server_path):
   try:
       t = paramiko.Transport(('192.168.0.22', 22))
       t.connect(username='root', password='fgoods.com')
       sftp = paramiko.SFTPClient.from_transport(t)
       sftp.put(local_path ,server_path  )
       t.close()
   except Exception, e:
       print e

if __name__ == '__main__':
    #sftp_upload_file('D:\\test\\erp-server-new.war' ,'/tmp/auto/erp-server-new.war')\
    #s = paramiko.SSHClient()
    #s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #s.connect('192.168.0.22', 22, 'root', 'fgoods.com')
    #stdin, stdout, stderr = s.exec_command("find /etrade/fgoods_nerp/webapps -name  '*tar.gz' -amin -20")
    #t2 = str(stdout.read()).split('/')
    #print t2[-1]
    #s.close()
    #print time.strftime('%Y%m%d', time.localtime(time.time()))#
    ###########################################################################
    import cx_Oracle ,sys ,os
    reload(sys)
    sys.setdefaultencoding('utf-8')
    i = 0
    z = ''
    b = []
    tns = cx_Oracle.makedsn('192.168.0.21', 1521, 'testoracle')
    db = cx_Oracle.connect('devcrm', 'devcrm', tns)
    cr = db.cursor()
    sql = "select i.sguid as id,        i.sinordernum,        i.saddoperator,        ddeliverydate,        sDeliveryType,        (select sum(g.finvoiceweight)           from nejx_InInvoiceGoods g           left join nejx_InInvoice t             on g.sininvoiceid = t.sguid          where g.sinorderid = i.sguid            and t.bstate = 50            and t.sinvoicekind = 1) as finvoiceweight,        (select sum(g.finvoicemoney)           from nejx_InInvoiceGoods g           left join nejx_InInvoice t             on g.sininvoiceid = t.sguid          where g.sinorderid = i.sguid            and t.bstate = 50            and t.sinvoicekind = 1) as finvoicemoney,        (select sum(g.finvoicemoney)           from nejx_InInvoiceGoods g           left join nejx_InInvoice t             on g.sininvoiceid = t.sguid          where g.sinorderid = i.sguid            and t.bstate = 50            and t.sinvoicekind <> 1            and t.sbusinesstype = 0) as fotherinvoicemoney,        nvl((select sum(nvl(isg.finweight, 0))              from nerk_InStore instore              join Nerk_Instoregoods isg                on instore.sguid = isg.sinstoreid             where instore.bstate <> 100               and instore.sinorderid = i.sguid),            0) - nvl((select sum(nvl(og.foutweight, 0))                       from nerk_InStore instore                       join Nerk_Instoregoods isg                         on instore.sguid = isg.sinstoreid                       join neth_OutStoreGoods og                         on isg.sguid = og.sinstoregoodsid                       join neth_OutStore ot                         on og.soutstoreid = ot.sguid                      where instore.bstate <> 100                        and ot.bstate in (50, 80)                        and instore.sinorderid = i.sguid),                     0) as fsurplusweight,        (select to_char(wmsys.wm_concat(distinct s.ssettlenum))           from njs_settleinordergoods sg           join njs_settleinorder s             on sg.ssettleid = s.sguid          where sg.sinorderid = i.sguid            and s.bstate = 50) as settlenum,        (select to_char(wmsys.wm_concat(distinct o.soutordernum))           from nexs_outordergoods g           join nexs_outorder o             on o.sguid = g.soutorderid          where g.sinorderid = i.sguid            and o.bstate < 90) as soutordernum,        (select nvl(sum(pg.fcurrentpaymoney + pg.fpaybalance), 0)           from nsfk_paygoods pg           join nsfk_pay p             on pg.spayid = p.sguid          where pg.srelevanttype = '1'            and p.bstate = 50            and pg.srelevantid = i.sguid            and p.spaytype in (101, 102, 103)) as paygoodsmoney,        (select nvl(sum(pg.fcurrentpaymoney + pg.fpaybalance), 0)           from nsfk_paygoods pg           join nsfk_pay p             on pg.spayid = p.sguid          where pg.srelevanttype = '1'            and p.bstate = 50            and pg.srelevantid = i.sguid            and p.spaytype in (201, 202, 203)) as payothermoney,        (select sum(g.foutweight * nvl(og.fSalesPrice, 0))           from neth_outstoregoods g           left join neth_outstore ot             on g.soutstoreid = ot.sguid           left join nexs_outordergoods og             on g.soutordergoodsid = og.sguid           left join (select sg.*                       from njs_settleoutordergoods sg                       join njs_settleoutorder se                         on sg.ssettleid = se.sguid                      where se.bstate = 50) sg             on g.sguid = sg.soutstoregoodsid          where ot.bstate in (50, 80)            and g.sinorderid = i.sguid) as foutmoney,        case          when (select nvl(t.fbalancemoney, 0)                  from njs_SettleInOrder t                 where t.srelevantid = i.sguid                   and t.bstate = 50) < 0 then           (nvl((select sum(nvl(g.fcurrentpaymoney, 0) + nvl(g.fpaybalance, 0))                  from Nsfk_Paygoods g                  left join nsfk_pay p                    on g.spayid = p.sguid                  left join njs_SettleInOrder sio                    on g.srelevantid = sio.sguid                 where g.srelevanttype = '3'                   and p.bstate = 50                   and sio.srelevantid = i.sguid),                0) - nvl((select sum(nvl(g.fcurrentreceivemoney, 0) +                                     nvl(g.Freceiveprice, 0))                            from nsfk_receivegoods g                            left join nsfk_receive r                              on g.sreceiveid = r.sguid                            left join njs_SettleInOrder sio                              on g.srelevantid = sio.sguid                           where g.srelevanttype = '3'                             and r.bstate = 50                             and sio.srelevantid = i.sguid),                          0))          else           (nvl((select sum(nvl(g.fcurrentreceivemoney, 0) +                           nvl(g.Freceiveprice, 0))                  from nsfk_receivegoods g                  left join nsfk_receive r                    on g.sreceiveid = r.sguid                  left join njs_SettleInOrder sio                    on g.srelevantid = sio.sguid                 where g.srelevanttype = '3'                   and r.bstate = 50                   and sio.srelevantid = i.sguid),                0) -           nvl((select sum(nvl(g.fcurrentpaymoney, 0) + nvl(g.fpaybalance, 0))                  from Nsfk_Paygoods g                  left join nsfk_pay p                    on g.spayid = p.sguid                  left join njs_SettleInOrder sio                    on g.srelevantid = sio.sguid                 where g.srelevanttype = '3'                   and p.bstate = 50                   and sio.srelevantid = i.sguid),                0))        end as fsettled,        (select nvl(t.fbalancemoney, 0)           from njs_SettleInOrder t          where t.srelevantid = i.sguid            and t.bstate = 50) as fbalancemoney,        i.sinordertype,        i.scontractnum,        i.ddatesigncontract,        i.dadddate,        (select sname           from sys_parametergroupdetail          where sgroupid in (select sguid                               from sys_parametergroup                              where sgroupno = 'ERP20160615001')            and svalue = to_char(i.sinordertype)) as type,        (select sname           from sys_parametergroupdetail          where sgroupid in (select sguid                               from sys_parametergroup                              where sgroupno = 'ERP2016060609')            and svalue = to_char(i.bstate)) as state,        nvl((select sum(nvl(ri.fcurrentreceivemoney, 0))              from nsfk_ReceiveInOrder ri             where ri.sinorderid = i.sguid),            0) as freceivablesmoney,        (select io.dsettledate           from njs_SettleInOrderGoods g           join njs_SettleInOrder io             on g.ssettleid = io.sguid          where g.sinorderid = i.sguid            and io.bstate = 50            and rownum = 1) as dsettledate,        i.sbuyer,        i.sauditor,        i.sauditorid,        i.sauditorreason,        i.dauditortime,        (select nvl(sum(g.finweight), 0)           from nerk_instoregoods g           left join nerk_instore instore             on g.sinstoreid = instore.sguid          where instore.sinorderid = i.sguid            and instore.bstate = 10) as instoreweight,        i.sdeliverycustomerid,        (select sum(gk.dweight)           from necg_goodstrack gk          where gk.sinorderid = i.sguid) as deliverytotalweight,        (select m.scnname           from hy_member m          where m.sguid = i.sdeliverycustomerid) as deliverycustomername,        i.scustomerid,        (select m.scnname from hy_member m where m.sguid = i.scustomerid) as customername,        i.sbranchid,        (select d.sdepartmentname           from sys_Department d          where d.sguid = i.sbranchid) as branchname,        (SELECT sum(cg.fsayweight)           FROM necg_inordergoods cg          where cg.sinorderid = i.sguid) as totalweight,        (SELECT sum(cg.fTotalMoney)           FROM necg_inordergoods cg          where cg.sinorderid = i.sguid) as totalamount,        (select nvl(sum(p.fcurrentpaymoney + p.fpaybalance), 0)           from nsfk_paygoods p           left join nsfk_pay sp             on p.spayid = sp.sguid          where p.srelevantid = i.sguid            and sp.bstate = 50) as fpaymentmoney,        (select nvl(sum(p.fcurrentpaymoney + p.fpaybalance), 0)           from nsfk_paygoods p           left join nsfk_pay sp             on p.spayid = sp.sguid          where p.srelevantid = i.sguid            and sp.bstate = 50) as fpaymoney   from necg_inorder i  where 1 = 1    and dadddate >= to_date('2017-04-18', 'yyyy-MM-dd')    and dadddate <= to_date('2017-04-25', 'yyyy-MM-dd') + 1  order by i.dadddate desc"
    print sql
    for k in sql:
        if k == "cba":
            print "对不起你不能执行这项操作"
            exit()
        elif k == "drop":
            print "对不起你不能执行这项操作"
            exit()
        elif k == "update":
            print "对不起你不能执行这项操作"
            exit()
        elif k ==  "delete":
            print "对不起你不能执行这项操作"
            exit()
        elif k ==  "insert":
            print "对不起你不能执行这项操作"
            exit()
    cr.execute(sql)
    rs = cr.fetchall()
    c = len(rs)
    print rs
    for x in range(c):
        for t in rs[x]:
            if t is not None or type(t) == 'str':
            #    z = z + t.encode('GBK') + '  '*2\
                z = z + str(t) + '\t'*2
            else:
                z = z + str(t)  + '\t'*2
        z = z + '\n'
        b.append(z)
        z = " "
    for m in b:
        print m
    cr.close()
    db.close()
    #########################################################
    #popen = subprocess.Popen(['ping', '127.0.0.1'],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #p = popen.poll()
    #while p is None:
    #    line = popen.stdout.readline()
    #    p = popen.poll()
    #    line = line.strip()
    #    print line + 'ssssss'
