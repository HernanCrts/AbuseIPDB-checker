import mechanize
from bs4 import BeautifulSoup
import sys
import datetime
import requests
import time

br= mechanize.Browser()
#br.set_all_readonly(False)
br.set_handle_robots(False)
br.set_handle_refresh(False)
count=0
#set randomly user-agent..
def agent(p):
    desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                         'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                         'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                         'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                         'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11']
    
        

    br.addheaders=[('User-Agent',desktop_agents[p]),('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),('Accept-Charset','ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding','none'),('Accept-Language','en-US,en;q=0.8'),('Connection','keep-alive')] 
            
    
    
    return br.addheaders

def checkDomain_abuseipdb(urlist):
    global p
    p=0
    for blacklist in urlist:
        agent(p)
        time.sleep(2)
        #print br.addheaders
        br.open("https://www.abuseipdb.com/")
        time.sleep(1)
        br.form = list(br.forms())[0]  
        br.form["query"]=blacklist
        response=br.submit()
        
        #print response.read()
        time.sleep(3)
        soup = BeautifulSoup(response.read(),'html5lib')

        time.sleep(2)
        localhost=soup.findAll('i')[0]
        p+=1
        if p==6:
            p=0
            
        if localhost.text=='127.0.0.1':
            print (20*"-"+"\n\n {dom} is Local Host Ip: 127.0.0.1\n".format(dom=blacklist)+"\n"+20*"-"+"\n")
        
        tek=soup.findAll('b')[1]
        #tekx=soup.findAll('b')[0]
        
        if tek.text!='We can\'t resolve the domain {dom}!'.format(dom=blacklist) and localhost.text!='127.0.0.1':
            
            resulth3=soup.findAll('h3')[0]
            ##print ">>>> "+resulth3.text
                
            resultP = soup.findAll('p')[1] #total 14 p 
            #print resultP.text +"\n\n\n\n"
            
            
            #resultPx = soup.findAll('p')[3]
            #print len(resultPx.text)

            resultPx = soup.findAll('p')[2]
            #print resultPx.text
            #if len(resultPx.text)!=60:
            
            if "not" not in resultPx.text:
                resultTable=soup.findAll('table')[1]
                #print len(resultTable)
                print (20*"-"+"\n"+resultP.text +"\n"+20*"-"+"\n")
                i=0
                n=1
                list_of_rows=[]
                today=datetime.datetime.now()
                v4=today.strftime('%Y-%m-%d %H:%M:%S')
                
                with open(r'aidb.html','a+') as output:
                    output.writelines( """<html><font color="white"><b> Report [ {domain} ]: </b></font></html>""".format(domain=blacklist))
                output.close()
            
        
                while i<3:
                    
                    for row in resultTable.findAll('tr')[1:]:
                        list_of_cells = []
                        for cell in row.findAll('td'):
                            text = cell.text
                            list_of_cells.append(text)
                        list_of_rows.append(list_of_cells)
                    print (list_of_rows[i][0]+"   |   "+list_of_rows[i][1]+"   |   "+list_of_rows[i][3])
                    
                    time.sleep(3)
                    with open(r'aidb.html','a+') as output:
                            output.writelines("""<html>
                    <body style=" background-position: center;
                         background-repeat: no-repeat;
                         background-size: cover; background-image:url('logo_aidb.png');">
                         <table cellpadding="3" cellspacing="1" border="1" width="600px" style="margin-top: 0px; " align="center">
                            <tbody>
                            <tr>
                                <th align="left" valign="middle" width="200px" bgcolor="#33adff">
                                    <b>IP</b>
                                <th align="left" valign="middle" width="200px" bgcolor="#33adff">
                                    <b>Reporter</b>
                                </th>
                                <th align="left" valign="middle" width="100px" bgcolor="#33adff">
                                    <b>Fecha</b>
                                </th>
                                <th align="left" valign="middle" width="300px" bgcolor="#33adff">
                                    <b>Categorías</b>
                                </th>
                                
                            </tr>
                            
                            
                            
                            <tr bgcolor="#ffffff">
                                <td align="left" valign="top" nowrap="nowrap" width="200px " >{value_name5} </td>
                                <td align="left" valign="top" nowrap="nowrap" width="200px " >{value_name1}</td>
                                <td align="left" valign="top" nowrap="nowrap" width="100px " >{value_name2}</td>
                                <td align="left" valign="top" nowrap="nowrap" width="300px " >{value_name3}<br></td>
                            </tr>   
                            </tbody>
                        </table>
                            
                            
                    </body>
                </html>""".format(value_name1=list_of_rows[i][0],value_name2=list_of_rows[i][1],value_name3=list_of_rows[i][3],value_name4=v4,value_name5=blacklist))
                
                    i+=1
                print (20*"-")
                    
                output.close()
            

            else:
                print ("\n"+"!!!!! "+resulth3.text +"\n")
            
        

        if tek.text=='We can\'t resolve the domain {dom}!'.format(dom=blacklist):
            print ('We can\'t resolve the domain {dom}!'.format(dom=blacklist))

def main():
    try:
            singleUrl = input('Introduce una IP/URL: ')
            urlist = singleUrl.split()
            print ("""\n\n La IP/URL se esta verificando en Abuse IP DB..Mantenga en espera..\n\n\n\n """)
            #checkDomain_VT(urlist) 
            checkDomain_abuseipdb(urlist)            
    except:
            pass
def logo():
        print("""    

     _   ___                ___ _           _             _ 
    | | | _ \___ _ __ _  _ / __| |_  ___ __| |_____ _ _  | |
    | | |   / -_) '_ \ || | (__| ' \/ -_) _| / / -_) '_| | |
    | | |_|_\___| .__/\_,_|\___|_||_\___\__|_\_\___|_|   | |
    |_|         |_|                                      |_|
        
        The Reputation Checker on AbuseIpDB [ 2023 ]

              
100% Developed by @FerdiGul - https://github.com/FerdiGul
     Modified  by @HernanCortes00

""")
if "__name__=__main__":
    logo()
    main()