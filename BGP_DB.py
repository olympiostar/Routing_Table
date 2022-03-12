# -*- coding: utf-8 -*-
"""
Created on Wed Oct 7 13:37:00 2020
@author: Jayden
    
"""
import paramiko
import pymysql
import schedule
### Header for TimeStamp ###
import time
import csv
from datetime import datetime

### Global ###
username = "xxxx"
password = "xxxx"
adver_prefix_list=[]
vrf_prefix=[]
prefix_list=[]
adver_cmd_result=[]
cmd_result=[]
as_list=[]

cmd_list = {"xxx.xxx.xxx.xxx" : ["show ip bgp vpnv4 vrf xx1 neighbor xxx.xxx.xxx.xx1 received-routes\n",
                            "show ip bgp vpnv4 vrf xx2 neighbor xxx.xxx.xxx.xx2 received-routes\n",
                            "show ip bgp vpnv4 vrf xx3 neighbor xxx.xxx.xxx.xx3 received-routes\n"],
            "yyy.yyy.yyy.yyy" : ["show ip bgp vpnv4 vrf yy1 neighbor yyy.yyy.yyy.yy1 received-routes\n"],
            "zzz.zzz.zzz.zzz" : ["show ip bgp vpnv4 vrf zz1 neighbor zzz.zzz.zzz.zz1 received-routes\n"]        
            }


### Class ###
class Prefix:
    ip_prefix = ""
    router = ""
    vrf = ""
    mno_asn = ""
    mno_country = ""
    mno_code = ""
    mno_name = ""
    contract_ipx = ""
    ipx_name = ""
    ipx_asn = 0
    bgp_neighbor = ""
    next_hop = ""
    lp = 0
    path = ""
    def __init__(self, ip_prefix, router, vrf, mno_asn, mno_country, mno_code, mno_name, contract_ipx, ipx_name, ipx_asn, bgp_neighbor, next_hop, lp, path):
        self.ip_prefix = ip_prefix
        self.router = router
        self.vrf = vrf
        self.mno_asn = mno_asn
        self.mno_country = mno_country
        self.mno_code = mno_code
        self.mno_name = mno_name
        self.contract_ipx = contract_ipx
        self.ipx_name = ipx_name
        self.ipx_asn = ipx_asn
        self.bgp_neighbor = bgp_neighbor
        self.next_hop = next_hop
        self.lp = lp
        self.path = path

class AS_Map:
    mno_asn=""
    mno_country=""
    mno_code=""
    mno_name=""
    contract_ipx=""
    def __init__(self, mno_asn, mno_country, mno_code, mno_name, contract_ipx):
        self.mno_asn = mno_asn
        self.mno_country = mno_country
        self.mno_code = mno_code
        self.mno_name = mno_name
        self.contract_ipx = contract_ipx    
    
def read_map():
    global as_list
    
    f = open('(Skip. cause BY Security)','r')
    rdr = csv.reader(f)
    for line in rdr:
        asn = AS_Map(line[0], line[1], line[2], line[3], line[4])
        as_list.append(asn)

def exec_command():
    
    global vrf_prefix, prefix_list, cmd_result, adver_cmd_result, as_list, adver_prefix_list


    ### 광고 송신 BGP 테이블 생성 ###   
    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())    
    remote_conn_pre.connect("xxx.xxx.xxx.xxx", username=username, password=password, look_for_keys=False, allow_agent=False)
    adver_cmd =(Skip. cause BY Security)
    print("SSH connection established to xxx.xxx.xxx.xxx \n   - Execute CMD : " + adver_cmd)
    stdin, stdout, stderr = remote_conn_pre.exec_command(adver_cmd,get_pty=True)
    adver_cmd_result = stdout.readlines()
    
    ### Trim ###
    i=0
    for i in range(len(adver_cmd_result)):     
        adver_cmd_result[i] = adver_cmd_result[i].strip()
    adver_cmd_result = list(filter(bool, adver_cmd_result))              
      
    i=0        
    for i in range(len(adver_cmd_result)):
        if (i+1) >= len(adver_cmd_result):
            break;
        if ( len(adver_cmd_result[i]) < 30 ):
            adver_cmd_result[i]=adver_cmd_result[i]+"    "+adver_cmd_result[i+1]
            del adver_cmd_result[i+1]

    i=0
    for i in range(len(adver_cmd_result)):     
        if adver_cmd_result[i][0] != '*':
            adver_cmd_result[i] = ''
    adver_cmd_result = list(filter(bool, adver_cmd_result))     
    
    i=0
    for i in range(len(adver_cmd_result)):                     
        adver_cmd_result[i] = adver_cmd_result[i].split()
        if adver_cmd_result[i][0] == '*>':
            adver_cmd_result[i] = ''
    adver_cmd_result = list(filter(bool, adver_cmd_result))                     

   ### Parsing ###
    i=0
    for i in range(len(adver_cmd_result)):                     
        if (adver_cmd_result[i][1]=='i'):
            adver_cmd_result[i][0] = "*i"
            del adver_cmd_result[i][1]
            
    i=0
    title_prefix=""            
    for i in range(len(adver_cmd_result)):                         
        if ("10.171" not in adver_cmd_result[i][1]):
            title_prefix = adver_cmd_result[i][1]
            continue;
        else:
           adver_cmd_result[i].insert(1,title_prefix)

    f=open("C:\Python Class\output.txt", mode='wt', encoding='utf-8')
    for i in range(len(adver_cmd_result)):                         
        f.write(str(adver_cmd_result[i])+"\n")
    f.close()



    ### 객체 생성 ###
    for i in range(len(adver_cmd_result)):       
        row = [0 for k in range(14)]    
        row[0] = adver_cmd_result[i][1]
        row[1] = "xxx"
        row[2] = "xxx"
        ### MNO_ASN ###
        if( (adver_cmd_result[i][len(adver_cmd_result[i])-2])[0] == '{' ) :
            (adver_cmd_result[i][len(adver_cmd_result[i])-2]) = (adver_cmd_result[i][len(adver_cmd_result[i])-2])[1:len((adver_cmd_result[i][len(adver_cmd_result[i])-2]))-1]
            row[3] = str(adver_cmd_result[i][len(adver_cmd_result[i])-2])
        else:
            row[3] = str(adver_cmd_result[i][len(adver_cmd_result[i])-2])

        ### (Skip. cause BY Security) ###                    
        ### 맵핑표 참조 ###
        t=0
        as_key=0
        for t in range(len(as_list)):
            if ((Skip. cause BY Security)
                break;
                
        if(as_key==0):
            row[4]="미등록"
            row[5]="XXX"
            row[6]="미등록"
            row[7]="미등록"

        ### BGP_Neighbor ###
        row[10] = ""
        ### Next_Hop ###
        row[11] = adver_cmd_result[i][2]
                
        ### Path ###
        temp_path = ''
        for k in range(len(adver_cmd_result[i])-1,0,-1):
            temp_path = temp_path + adver_cmd_result[i][k] + " "
            if (adver_cmd_result[i][k] == '0'):
                break;
        temp_path = temp_path.split()
        temp_path.reverse()
        str_path = " ".join(temp_path)
        row[13] = str_path.strip()        

        ### LP ###
        row[12] = 0
        for k in range(len(adver_cmd_result[i])-1,0,-1):                    
            del adver_cmd_result[i][k]
            if (adver_cmd_result[i][k-1] == '0'):
                del adver_cmd_result[i][k-1]    
                if len(adver_cmd_result[i][k-2]) < 5:
                    row[12] = int(adver_cmd_result[i][k-2])
                else:
                    row[12] = 0
                break;
        
        ### IPX_Name & ASN###
        row[9]=int(row[13].split()[1])  
        (Skip. cause BY Security)
    
        p = Prefix(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7], row[8], row[9], row[10], row[11], row[12], row[13])                        
        adver_prefix_list.append(p)        
    
    
    ### 광고 수신 BGP 테이블 생성 ###
    for key in cmd_list.keys():
        ### CMD & VRF Loop ###
        for value in cmd_list[key]:
            remote_conn_pre = paramiko.SSHClient()
            remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            host = key
            
            if (key!="10.171.15.1") :
                remote_conn_pre.connect(host, username=username, password=password, look_for_keys=False, allow_agent=False)
                print("SSH connection established to " + host + "\n   - Execute CMD : " + value)
                
                cmd = value
                stdin, stdout, stderr = remote_conn_pre.exec_command(cmd,get_pty=True)
                cmd_result = stdout.readlines()
            
                ### Trim ###
                i=0
                for i in range(len(cmd_result)):     
                    cmd_result[i] = cmd_result[i].strip()
                cmd_result = list(filter(bool, cmd_result))              
  
                i=0        
                for i in range(len(cmd_result)):
                    if (i+1) >= len(cmd_result):
                        break;
                    if ( len(cmd_result[i]) < 30 ):
                        cmd_result[i]=cmd_result[i]+"    "+cmd_result[i+1]
                        del cmd_result[i+1]

                i=0
                for i in range(len(cmd_result)):     
                    if cmd_result[i][0] != '*':
                        cmd_result[i] = ''
                cmd_result = list(filter(bool, cmd_result)) 

                ### 객체 생성 ###
                i=0
                cmd=cmd.split()
                
                ### Prefix Loop ###
                for i in range(len(cmd_result)):                     
                    cmd_result[i] = cmd_result[i].split()
                    row = [0 for i in range(14)]
                    
                    ### Prefix ###
                    row[0]= cmd_result[i][1]
                    ### Router ###
                    (Skip. cause BY Security)                   
                    ### VRF ###
                    row[2] = cmd[5]
                    ### MNO_ASN ###
                    if( (cmd_result[i][len(cmd_result[i])-2])[0] == '{' ) :
                        (cmd_result[i][len(cmd_result[i])-2]) = (cmd_result[i][len(cmd_result[i])-2])[1:len((cmd_result[i][len(cmd_result[i])-2]))-1]
                        row[3] = str(cmd_result[i][len(cmd_result[i])-2])
                    else:
                        row[3] = str(cmd_result[i][len(cmd_result[i])-2])
                    
                    
                    ### MNO_Country/MNO_Code/MNO_Name/Contract_IPX/ ###                    
                    ### 맵핑표 참조 ###
                    t=0
                    as_key=0
                    for t in range(len(as_list)):
                        if (row[3] == as_list[t].mno_asn):
                            row[4] = as_list[t].mno_country
                            row[5] = as_list[t].mno_code
                            row[6] = as_list[t].mno_name
                            row[7] = as_list[t].contract_ipx               
                            as_key=1
                            break;
                            
                    if(as_key==0):
                        row[4]="미등록"
                        row[5]="XXX"
                        row[6]="미등록"
                        row[7]="미등록"

                    ### IPX_Name & ASN ###
                    (Skip. cause BY Security)    
                    
                    ### BGP_Neighbor ###
                    row[10] = cmd[7]
                    ### Next_Hop ###
                    row[11] = cmd_result[i][2]

                    ### Path ###
                    temp_path = ''
                    for k in range(len(cmd_result[i])-1,0,-1):
                        temp_path = temp_path + cmd_result[i][k] + " "
                        if (cmd_result[i][k] == '0'):
                            break;
                    temp_path = temp_path.split()
                    temp_path.reverse()
                    str_path = " ".join(temp_path)
                    row[13] = str_path.strip()

                    ### LP ###
                    row[12] = 0
                    for k in range(len(cmd_result[i])-1,0,-1):                    
                        del cmd_result[i][k]
                        if (cmd_result[i][k-1] == '0'):
                            del cmd_result[i][k-1]    
                            if len(cmd_result[i][k-2]) < 5:
                                row[12] = int(cmd_result[i][k-2])
                            else:
                                row[12] = 0
                            break;


                    p = Prefix(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7], row[8], row[9], row[10], row[11], row[12], row[13])                        
                    prefix_list.append(p)
                    
                vrf_prefix.append(prefix_list[:])

                ### cmd_result 초기화 및 SSH Close ###  
                prefix_list.clear()
                cmd_result=[None]
                remote_conn_pre.close()                
                
            else :#Telnet 접속 필요
                break;
                #remote_conn_pre.connect(host, username=username, password=password, look_for_keys=False, allow_agent=False)


### MySQL Connection ###
def make_table():
    global vrf_prefix, prefix_list, cmd_result, adver_prefix_list
    
 
    ### BGP 송신 테이블 DB 생성 ###
    conn = pymysql.connect((Skip. cause BY Security)
    # Connection으로부터 Cursor 생성
    curs = conn.cursor()    
    #SQL문 실행
    table_name=(Skip. cause BY Security)+str(datetime.today().strftime("%Y_%m_%d"))
    #table_name= (Skip. cause BY Security)
    query = (Skip. cause BY Security)
    curs.execute(query)

    query=''
    i=0
    for i in adver_prefix_list :
        query = (Skip. cause BY Security)
        curs.execute(query)
        query=''
    
    conn.commit()
    curs.close()
    
    ### BGP 수신 테이블 DB 생성 ###
    conn = pymysql.connect(Skip. cause BY Security)
    # Connection으로부터 Cursor 생성
    curs = conn.cursor()    
    #SQL문 실행
   (Skip. cause BY Security)

    query=''
    for x in vrf_prefix :
        for y in x :
            query = (Skip. cause BY Security)
            curs.execute(query)
            query=''
    
    conn.commit()
    curs.close()

def job():
    global vrf_prefix, prefix_list, cmd_result, adver_prefix_list
    exec_command()
    make_table()    
    del vrf_prefix[:]
    del prefix_list[:]
    del cmd_result[:]    
    del adver_prefix_list[:]
    

read_map()
#exec_command()
#make_table()        
print("프로세스가 실행되는 동안 DB는 매일 자정 자동 업데이트 됩니다.")
schedule.every().day.at("00:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
