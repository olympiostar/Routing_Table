# -*- coding: utf-8 -*-
"""
Created on Wed Oct 7 13:37:00 2020
@author: Jayden
    
"""
# import os
import os

# import DB
import pymysql

### Header for TimeStamp ###
import datetime

### Header for IP Validation ###
import ipaddress

### Window Console Font ###
from colorama import init, Fore
init(autoreset=True)

### Global Var
global selected_date
global query_date

### list
vrf_prefix=[]
prefix_list=[]

### Class 정의
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

            
def print_menu() :
    global selected_date
    os.system('cls')
    print(Fore.LIGHTYELLOW_EX + "==================================================================================")
    print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
    print(Fore.LIGHTYELLOW_EX + "날짜 재선택 ('c' 또는 'C' 입력) : ")
    print(Fore.LIGHTYELLOW_EX + "==================================================================================")        
    print(Fore.LIGHTRED_EX + "1. 사업자 코드 검색")
    print(Fore.LIGHTGREEN_EX + "2. Advertised-Route : ASN 검색")
    print(Fore.LIGHTBLUE_EX + "3. Advertised-Route : IP 검색")
    print(Fore.LIGHTMAGENTA_EX + "4. Received-Route : ASN 검색")
    print(Fore.LIGHTCYAN_EX + "5. Received-Route : IP 검색")    
    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")        

def select_menu() :
    while (True):
        pre_key = input(">>메뉴 선택(1/2/3/4/5(c 또는 C)) : ")
        print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")        
        if(pre_key.isdigit()):
            menu_key = int(pre_key)
            if((menu_key == 1) |(menu_key == 2) | (menu_key == 3) | (menu_key == 4) | (menu_key == 5)):
                break;
            else :
                print_menu()
                print("※숫자 /1/2/3/4/5만 입력해주세요※")              
                print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")              
                continue;
        elif(pre_key =='c' or pre_key=='C'):
            menu_key = pre_key
            return menu_key;
        else: 
            print_menu()
            print("※'c' 또는 'C' 이외 문자 입력 금지 (Only 숫자 1/2/3/4/5(c 또는 C))※")              
            print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                          
            continue;
    return menu_key;


def search_CODE():
    global selected_date
    global query_date    
    os.system('cls')
    print(Fore.LIGHTYELLOW_EX + "==================================================================================")
    print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
    print(Fore.LIGHTYELLOW_EX + "==================================================================================")    
    print(Fore.LIGHTRED_EX + "1. 사업자 코드 검색")
    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")        
    
    while(True):
        pre_key = input(">>사업자 코드 검색 (처음 화면 복귀 'c' 또는 'C' 입력) : ")
        print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")            
        if ( (pre_key == 'c') | (pre_key == 'C') ):
            return 0;
        else:
            if( not ((pre_key.isalpha()) & (pre_key.isupper()) & (len(pre_key)==3)) ):
                os.system('cls')
                print(Fore.LIGHTYELLOW_EX + "==================================================================================")
                print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
                print(Fore.LIGHTYELLOW_EX + "==================================================================================")    
                print(Fore.LIGHTRED_EX + "1. 사업자 코드 검색 : "+pre_key)
                print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                print("※사업자 코드는 세자리 영문자 대문자로 구성되어 있습니다. 다시 확인해주세요!※")                       
                continue;
            else:                
                if( pre_key == "XXX" ):
                    os.system('cls')
                    print(Fore.LIGHTYELLOW_EX + "==================================================================================")
                    print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
                    print(Fore.LIGHTYELLOW_EX + "==================================================================================")    
                    print(Fore.LIGHTRED_EX + "1. 사업자 코드 검색 : "+pre_key)
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    print("사업자 코드 XXX는 DB 내 정보가 등록되지 않은 사업자를 의미합니다.")
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                                                               
                    continue;
                    
                # MySQL Connection
                conn = pymysql.connect((Skip. cause BY Security))                
                # Connection으로부터 Cursor 생성
                curs = conn.cursor()
                
                #SQL문 실행
                query = (Skip. cause BY Security)
                curs.execute(query)
                
                result_check = curs.fetchone()                                       
                curs.rownumber=0
                   
                #SQL Query 결과가 없다면
                if not result_check:
                    os.system('cls')
                    print(Fore.LIGHTYELLOW_EX + "==================================================================================")
                    print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
                    print(Fore.LIGHTYELLOW_EX + "==================================================================================")    
                    print(Fore.LIGHTRED_EX + "1. 사업자 코드 검색 : "+pre_key)
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    print("※DB에 없는 코드입니다. 코드 재확인 해주세요!※")                               
                    continue;                                                                        
                #SQL Query결과가 있다면                    
                else:
                    #SQL Query 결과 조회
                    asn_result = curs.fetchone()    
                    #SQL Query 결과 출력
                    if ( asn_result == "XXX"):
                        os.system('cls')
                        print(Fore.LIGHTYELLOW_EX + "==================================================================================")
                        print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
                        print(Fore.LIGHTYELLOW_EX + "==================================================================================")    
                        print(Fore.LIGHTRED_EX + "1. 사업자 코드 검색 : "+pre_key)
                        print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                        print("사업자 코드 XXX는 DB 내 정보가 등록되지 않은 사업자를 의미합니다.")
                        print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                                           
                    else :
                        os.system('cls')
                        print(Fore.LIGHTYELLOW_EX + "==================================================================================")
                        print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
                        print(Fore.LIGHTYELLOW_EX + "==================================================================================")    
                        print(Fore.LIGHTRED_EX + "1. 사업자 코드 검색 : "+pre_key)
                        print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                        print("사업자 코드 " + pre_key + "의 ASN은 [" + str(asn_result[0]) + "] 입니다. ASN 검색 메뉴에서 다시 검색해 주세요!")
                        print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                              
                    curs.close()   
                    continue;

def search_AD():
    global selected_date
    global query_date    
    os.system('cls')

    print(Fore.LIGHTYELLOW_EX + "==================================================================================")
    print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
    print(Fore.LIGHTYELLOW_EX + "==================================================================================")    
    print(Fore.LIGHTGREEN_EX + "2. Advertised-Route : ASN 검색")
    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")        

    while(True):
        pre_key = input(">>검색 ASN (처음 화면 복귀 'c' 또는 'C' 입력) : ")
        print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")        
        if ( (pre_key == 'c') | (pre_key == 'C') ):
            return 0;
        else:
            if ( pre_key.isdigit() == False ) :
                os.system('cls')
                print(Fore.LIGHTYELLOW_EX + "==================================================================================")
                print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
                print(Fore.LIGHTYELLOW_EX + "==================================================================================")    
                print(Fore.LIGHTGREEN_EX + "2. Advertised-Route : ASN 검색 : "+pre_key)
                print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                print("※ASN은 숫자로 구성되어 있습니다. 다시 확인해주세요!※")              
                continue;        
            else:
                # MySQL Connection
                conn = pymysql.connect((Skip. cause BY Security))                
                # Connection으로부터 Cursor 생성
                curs = conn.cursor()
                
                #SQL문 실행
                query = (Skip. cause BY Security)
                curs.execute(query)
                
                result_check = curs.fetchone()                                       
                curs.rownumber=0
                                
                #SQL Query 결과가 없다면
                if not result_check:
                    os.system('cls')
                    print(Fore.LIGHTYELLOW_EX + "==================================================================================")
                    print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
                    print(Fore.LIGHTYELLOW_EX + "==================================================================================")    
                    print(Fore.LIGHTGREEN_EX + "2. Advertised-Route : ASN 검색 : "+pre_key)
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    print("※DB에 없는 미조회 ASN입니다. ASN 재확인 및 사업자 코드로 검색해보세요!※")                               
                    continue;                                                                        
                #SQL Query결과가 있다면                    
                else:
                    #SQL Query 결과 조회
                    for row in curs:   
                        p = Prefix(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7], row[8], row[9], row[10], row[11], row[12], row[13])                        
                        prefix_list.append(p)
                    
                    curs.close()
                    
                    #SQL Query 결과 출력
                    os.system('cls')
                    print(Fore.LIGHTYELLOW_EX + "==================================================================================")
                    print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
                    print(Fore.LIGHTYELLOW_EX + "==================================================================================")    
                    print(Fore.LIGHTGREEN_EX + "2. Advertised-Route : ASN 검색 : "+pre_key)
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    print(Fore.LIGHTGREEN_EX + "2-1. 사업자 정보")
                    print(Fore.LIGHTGREEN_EX + "----------------------------------------------------------------------------------")                        
                    print("2-1-A. 국가 : " + prefix_list[0].mno_country)
                    print("2-1-B. 사업자 명 : " +prefix_list[0].mno_name)
                    print("2-1-C. 사업자 코드 : " +prefix_list[0].mno_code)
                    print("2-1-D. 계약 중계사업자 : " +prefix_list[0].contract_ipx)                                     
                    
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    print(Fore.LIGHTGREEN_EX + "2-2. 중계 사업자 / 광고 송신 Router / LP" )
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    
                    k=0
                    temp_list=[]
                    for i in prefix_list:
                        temp = i.ipx_name + " / " + i.next_hop + " / " + str(i.lp)
                        if (temp in temp_list):
                            continue;
                        else:                            
                            print(Fore.LIGHTGREEN_EX + "[" + str(k+1) + "] : "+Fore.LIGHTWHITE_EX+temp)
                            k=k+1
                            temp_list.append(temp)
                                            
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    print(Fore.LIGHTGREEN_EX + "2-3. 광고 송신 Prefix-List")
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                                            
                    
                    temp_ipx_prefix=[]
                    total_ipx_prefix=[]
                    
                    for k in temp_list:
                        for i in prefix_list:
                            temp = i.ipx_name + " / " + i.next_hop + " / " + str(i.lp)
                            if (temp == k) :
                                temp_ipx_prefix.append(Fore.WHITE + i.ip_prefix + " : " + i.path)
                            else:
                                continue;
                        total_ipx_prefix.append(temp_ipx_prefix[:])
                        temp_ipx_prefix.clear()                      
                    
                    j=0
                    for k in temp_list:                        
                        print(Fore.LIGHTGREEN_EX + "[" + str(j+1) + "] : "+k)
                        print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                                                                
                        print(Fore.LIGHTGREEN_EX +"총 Prefix 갯수 : " + str(len(total_ipx_prefix[j])) + "개")
                        print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                                                                                        
                        for x in total_ipx_prefix[j]:
                            print(x)
                        j=j+1                
                        print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                                                                                        
                        
                        
                    i=0
                    j=0
                    k=0
                    temp_list.clear()
                    temp_ipx_prefix.clear()
                    total_ipx_prefix.clear()
                    vrf_prefix.clear()
                    prefix_list.clear()
                    continue;

def search_AD_IP():
    global selected_date
    global query_date    
    os.system('cls')
    print(Fore.LIGHTYELLOW_EX + "==================================================================================")
    print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
    print(Fore.LIGHTYELLOW_EX + "==================================================================================")    
    print(Fore.LIGHTBLUE_EX + "3. Advertised-Route : IP 검색")
    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")        
    
    while(True):
        pre_key = input(">>IP 검색 (처음 화면 복귀 'c' 또는 'C' 입력) : ")
        print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")            
        if ( (pre_key == 'c') | (pre_key == 'C') ):
            return 0;
        else:
            if( not valid_ip(pre_key)):
                os.system('cls')
                print(Fore.LIGHTYELLOW_EX + "==================================================================================")
                print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
                print(Fore.LIGHTYELLOW_EX + "==================================================================================")    
                print(Fore.LIGHTBLUE_EX + "3. Advertised-Route : IP 검색: "+pre_key)
                print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                                        
                print("※IPv4 형식(A.B.C.D)으로만 검색 가능합니다.※") #서브넷 포함 검색 추가 예정
                continue;
            else:
                # MySQL Connection
                conn = pymysql.connect((Skip. cause BY Security))                
                # Connection으로부터 Cursor 생성
                curs = conn.cursor()
                
                #SQL문 실행
                query = (Skip. cause BY Security)
                curs.execute(query)
                
                result_check = curs.fetchone()                                       
                curs.rownumber=0
                   
                #SQL Query 결과가 없다면
                if not result_check:
                    os.system('cls')
                    print(Fore.LIGHTYELLOW_EX + "==================================================================================")
                    print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
                    print(Fore.LIGHTYELLOW_EX + "==================================================================================")    
                    print(Fore.LIGHTBLUE_EX + "3. Advertised-Route : IP 검색: "+pre_key)
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    print("※DB에 없는 미조회 IP 주소 입니다. 서브넷 마스크 확인 후 재검색해보세요!※")                                      
                    continue;                                                                        
                #SQL Query결과가 있다면                    
                else:
                    #SQL Query 결과 조회
                    i=0
                    for row in curs:   
                        p = Prefix(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7], row[8], row[9], row[10], row[11], row[12], row[13])                        
                        prefix_list.append(p)
                    curs.close()
                    
                    mno_asn_list=[]
                    i=0
                    for i in range (len(prefix_list)):
                        if (prefix_list[i].mno_asn) not in mno_asn_list:
                            mno_asn_list.append(prefix_list[i].mno_asn)
                    mno_asn_list_str= ""
                    i=0
                    for i in range(len(mno_asn_list)):
                        mno_asn_list_str = mno_asn_list_str + "/" + mno_asn_list[i]
                    
                    
                    #SQL Query 결과 출력
                    os.system('cls')
                    print(Fore.LIGHTYELLOW_EX + "==================================================================================")
                    print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
                    print(Fore.LIGHTYELLOW_EX + "==================================================================================")    
                    print(Fore.LIGHTBLUE_EX + "3. Advertised-Route : IP 검색: "+pre_key)
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    print(Fore.LIGHTBLUE_EX + "3-1. 관련 MNO 사업자 정보")
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    print("3-1-A. 관련 ASN : " + mno_asn_list_str)                                       
                    
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    print(Fore.LIGHTBLUE_EX + "3-2. 중계 사업자 / 광고 송신 Router / LP")
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                                            
                    k=0
                    temp_list=[]
                    for i in prefix_list:
                        temp = i.ipx_name + " / " + i.next_hop + " / " + str(i.lp)
                        if (temp in temp_list):
                            continue;
                        else:                            
                            print(Fore.LIGHTBLUE_EX + "[" + str(k+1) + "] : " + Fore.LIGHTWHITE_EX + temp)
                            k=k+1
                            temp_list.append(temp)
                            
                    i=0
                    k=0
                    temp_list.clear()
                    vrf_prefix.clear()
                    prefix_list.clear()
                    continue;



def search_ASN():
    global selected_date
    global query_date    
    
    os.system('cls')
    print(Fore.LIGHTYELLOW_EX + "==================================================================================")
    print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
    print(Fore.LIGHTYELLOW_EX + "==================================================================================")    
    print(Fore.LIGHTMAGENTA_EX + "4. Received-Route : ASN 검색")
    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")        
    
    while(True):
        pre_key = input(">>검색 ASN (처음 화면 복귀 'c' 또는 'C' 입력) : ")
        print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")        
        if ( (pre_key == 'c') | (pre_key == 'C') ):
            return 0;
        else:
            if ( pre_key.isdigit() == False ) :
                os.system('cls')
                print(Fore.LIGHTYELLOW_EX + "==================================================================================")
                print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
                print(Fore.LIGHTYELLOW_EX + "==================================================================================")    
                print(Fore.LIGHTMAGENTA_EX + "4. Received-Route : ASN 검색 : "+pre_key)
                print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                print("※ASN은 숫자로 구성되어 있습니다. 다시 확인해주세요!※")              
                continue;        
            else:
                # MySQL Connection
                conn = pymysql.connect((Skip. cause BY Security))                
                # Connection으로부터 Cursor 생성
                curs = conn.cursor()
                
                #SQL문 실행
                query = (Skip. cause BY Security)
                curs.execute(query)
                
                result_check = curs.fetchone()                                       
                curs.rownumber=0
                                
                #SQL Query 결과가 없다면
                if not result_check:
                    os.system('cls')
                    print(Fore.LIGHTYELLOW_EX + "==================================================================================")
                    print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
                    print(Fore.LIGHTYELLOW_EX + "==================================================================================")    
                    print(Fore.LIGHTMAGENTA_EX + "4. Received-Route : ASN 검색 : "+pre_key)
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    print("※DB에 없는 미조회 ASN입니다. ASN 재확인 및 사업자 코드로 검색해보세요!※")                               
                    continue;                                                                        
                #SQL Query결과가 있다면                    
                else:
                    #SQL Query 결과 조회
                    i=0
                    for row in curs:   
                        p = Prefix(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7], row[8], row[9], row[10], row[11], row[12], row[13])                        
                        if ( (i==0) or (prefix_list[i-1].vrf == row[2]) ):
                            prefix_list.append(p)
                            i=i+1
                        else :
                            vrf_prefix.append(prefix_list[:])
                            prefix_list.clear()
                            prefix_list.append(p)
                            i=1
                    vrf_prefix.append(prefix_list)                            
                    
                    curs.close()
                    
                    #SQL Query 결과 출력
                    os.system('cls')
                    print(Fore.LIGHTYELLOW_EX + "==================================================================================")
                    print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
                    print(Fore.LIGHTYELLOW_EX + "==================================================================================")    
                    print(Fore.LIGHTMAGENTA_EX + "4. Received-Route : ASN 검색 : "+pre_key)
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    print(Fore.LIGHTMAGENTA_EX + "4-1. 사업자 정보")
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    print("4-1-A. 국가 : " + vrf_prefix[0][0].mno_country)
                    print("4-1-B. 사업자 명 : " +vrf_prefix[0][0].mno_name)
                    print("4-1-C. 사업자 코드 : " +vrf_prefix[0][0].mno_code)
                    print("4-1-D. 계약 중계사업자 : " +vrf_prefix[0][0].contract_ipx)
                             
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    print(Fore.LIGHTMAGENTA_EX + "4-2. 광고 수신 Router / VRF / BGP Neighbor IP Address")
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    i=0
                    for i in range(len(vrf_prefix)):
                        print(Fore.LIGHTMAGENTA_EX + "[" + str(i+1) + "] : " + Fore.LIGHTWHITE_EX + vrf_prefix[i][0].router + " / " + vrf_prefix[i][0].vrf + " / " + vrf_prefix[i][0].bgp_neighbor)
                        i=i+1
                    
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    print(Fore.LIGHTMAGENTA_EX + "4-3. 광고 수신 Prefix-List")
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                                            
                    i=0
                    for i in range(len(vrf_prefix)):
                        print(Fore.LIGHTMAGENTA_EX + "[" + str(i+1) + "] : " + Fore.LIGHTWHITE_EX + vrf_prefix[i][0].router + " / " + vrf_prefix[i][0].vrf + " / " + vrf_prefix[i][0].bgp_neighbor)
                        j=0
                        print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                                                                
                        print("총 Prefix 갯수 : " + str(len(vrf_prefix[i])) + "개")
                        for j in range(len(vrf_prefix[i])):
                            print(vrf_prefix[i][j].ip_prefix + " : " + vrf_prefix[i][j].path)
                            j=j+1
                        i=i+1          
                        print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                                                                
                    
                    i=0
                    j=0
                    vrf_prefix.clear()
                    prefix_list.clear()
                    continue;      
            
def valid_ip(address):
    try: 
        print(ipaddress.ip_address(address))
        return True
    except:
        return False
def search_IP():    
    global selected_date
    global query_date    
    os.system('cls')
    print(Fore.LIGHTYELLOW_EX + "==================================================================================")
    print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
    print(Fore.LIGHTYELLOW_EX + "==================================================================================")    
    print(Fore.LIGHTCYAN_EX + "5. Received-Route : IP 검색")    
    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")        
    
    while(True):
        pre_key = input(">>IP 검색 (처음 화면 복귀 'c' 또는 'C' 입력) : ")
        print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")            
        if ( (pre_key == 'c') | (pre_key == 'C') ):
            return 0;
        else:
            if( not valid_ip(pre_key)):
                os.system('cls')
                print(Fore.LIGHTYELLOW_EX + "==================================================================================")
                print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
                print(Fore.LIGHTYELLOW_EX + "==================================================================================")    
                print(Fore.LIGHTCYAN_EX + "5. Received-Route : IP 검색 : "+pre_key)
                print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                                        
                print("※IPv4 형식(A.B.C.D)으로만 검색 가능합니다.※") #서브넷 포함 검색 추가 예정
                continue;
            else:
                # MySQL Connection
                conn = pymysql.connect((Skip. cause BY Security))                
                # Connection으로부터 Cursor 생성
                curs = conn.cursor()
                
                #SQL문 실행
                query = (Skip. cause BY Security)
                curs.execute(query)
                
                result_check = curs.fetchone()                                       
                curs.rownumber=0
                   
                #SQL Query 결과가 없다면
                if not result_check:
                    os.system('cls')
                    print(Fore.LIGHTYELLOW_EX + "==================================================================================")
                    print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
                    print(Fore.LIGHTYELLOW_EX + "==================================================================================")    
                    print(Fore.LIGHTCYAN_EX + "5. Received-Route : IP 검색 : "+pre_key)
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    print("※DB에 없는 미조회 IP 주소 입니다. 서브넷 마스크 확인 후 재검색해보세요!※")                                      
                    continue;                                                                        
                #SQL Query결과가 있다면                    
                else:
                    #SQL Query 결과 조회
                    i=0
                    for row in curs:   
                        p = Prefix(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7], row[8], row[9], row[10], row[11], row[12], row[13])                        
                        if ( (i==0) or (prefix_list[i-1].vrf == row[2]) ):
                            prefix_list.append(p)
                            i=i+1
                        else :
                            vrf_prefix.append(prefix_list[:])
                            prefix_list.clear()
                            prefix_list.append(p)
                            i=1
                    vrf_prefix.append(prefix_list)                            
                    curs.close()
                    
                    mno_asn_list=[]
                    i=0
                    for i in range (len(vrf_prefix)):
                        for k in range (len(vrf_prefix[i])):
                            if (vrf_prefix[i][k].mno_asn) not in mno_asn_list:
                                mno_asn_list.append(vrf_prefix[i][k].mno_asn)
                    
                    mno_asn_list_str= ""
                    i=0
                    for i in range(len(mno_asn_list)):
                        mno_asn_list_str = mno_asn_list_str + "/" + mno_asn_list[i]
                    
                    
                    #SQL Query 결과 출력
                    os.system('cls')
                    print(Fore.LIGHTYELLOW_EX + "==================================================================================")
                    print(Fore.LIGHTYELLOW_EX + "국제IPX 라우팅 테이블 검색 ("+ selected_date +")")
                    print(Fore.LIGHTYELLOW_EX + "==================================================================================")    
                    print(Fore.LIGHTCYAN_EX + "5. Received-Route : IP 검색 : "+pre_key)
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    print(Fore.LIGHTCYAN_EX + "5-1. 관련 MNO 사업자 정보")
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    print("5-1-A. 관련 ASN : " +mno_asn_list_str)
                                        
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    print(Fore.LIGHTCYAN_EX + "5-2. 광고 수신 Router / VRF / BGP Neighbor IP Address")
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    i=0
                    for i in range(len(vrf_prefix)):
                        print(Fore.LIGHTCYAN_EX + "[" + str(i+1) + "] : " + Fore.LIGHTWHITE_EX + vrf_prefix[i][0].router + " / " + vrf_prefix[i][0].vrf + " / " + vrf_prefix[i][0].bgp_neighbor)
                        i=i+1
                    
                    print(Fore.LIGHTYELLOW_EX + "----------------------------------------------------------------------------------")                        
                    vrf_prefix.clear()
                    prefix_list.clear()
                    continue;

def validate(selected_date):
    try:
        datetime.datetime.strptime(selected_date, '%Y-%m-%d').date()
        return 0;
    except ValueError:
        return -1;
        
def select_date():
    os.system('cls')
    print(Fore.LIGHTYELLOW_EX + "==================================================================================")
    print(Fore.LIGHTYELLOW_EX + "최초 테이블 : 2020-11-30")
    print(Fore.LIGHTYELLOW_EX + "BGP 테이블 조회 날짜를 입력해주세요. (현재 날짜 : "+ datetime.datetime.today().strftime("%Y-%m-%d")+")")
    print(Fore.LIGHTYELLOW_EX + "==================================================================================")        
    while(True):
        selected_date = input(">>날짜 입력 (YYYY-MM-DD, ex)2020-01-01) : ")
        if ( validate(selected_date) == 0):
            first = datetime.datetime.strptime("2020-11-30","%Y-%m-%d")
            now = datetime.datetime.today().strftime("%Y-%m-%d")
            now = datetime.datetime.strptime(now,"%Y-%m-%d")
            sel = datetime.datetime.strptime(selected_date,"%Y-%m-%d")
            if(sel < first):
                os.system('cls')
                print(Fore.LIGHTYELLOW_EX + "==================================================================================")
                print(Fore.RED + ">>최초 DB는 2020-11-30 입니다.")
                print(Fore.LIGHTYELLOW_EX + "BGP 테이블 조회 날짜를 입력해주세요. (현재 날짜 : "+ datetime.datetime.today().strftime("%Y-%m-%d")+")")
                print(Fore.LIGHTYELLOW_EX + "==================================================================================")
                continue;
            elif( sel > now) :
                os.system('cls')
                print(Fore.LIGHTYELLOW_EX + "==================================================================================")
                print(Fore.RED + ">>금일 자정 기준 DB 업데이트입니다.")
                print(Fore.LIGHTYELLOW_EX + "BGP 테이블 조회 날짜를 입력해주세요. (현재 날짜 : "+ datetime.datetime.today().strftime("%Y-%m-%d")+")")
                print(Fore.LIGHTYELLOW_EX + "==================================================================================")
                continue;
            else:                
                return selected_date;
        else:
            os.system('cls')
            print(Fore.LIGHTYELLOW_EX + "==================================================================================")
            print(Fore.LIGHTYELLOW_EX + "최초 테이블 : 2020-11-30")
            print(Fore.LIGHTYELLOW_EX + "BGP 테이블 조회 날짜를 입력해주세요. (현재 날짜 : "+ datetime.datetime.today().strftime("%Y-%m-%d")+")")
            print(Fore.LIGHTYELLOW_EX + "==================================================================================")        
            print(Fore.RED + ">>날짜 형식을 다시 확인하여 입력해주세요. (YYYY-MM-DD, ex)2020-01-01)")    
            continue;
        

### Loop Start ###
while(True):
    selected_date=select_date()   
    query_date = selected_date[0:4]+"_"+selected_date[5:7]+"_"+selected_date[8:10]    
    print_menu()
    menu_key = select_menu()
    if (menu_key == 'c' or menu_key == 'C'):
        continue;
    elif (menu_key == 1) :
        result = search_CODE();
        if(result == 0):
            continue;        
    elif (menu_key == 2) :
        result = search_AD();
        if(result == 0):
            continue;        
    elif(menu_key == 3) :
        result = search_AD_IP();
        if(result == 0):
            continue;
    elif(menu_key == 4) :
        result = search_ASN();
        if(result == 0):
            continue;
    elif(menu_key == 5) :
        result = search_IP();        
        if(result == 0):
            continue;            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    