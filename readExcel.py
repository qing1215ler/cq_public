#coding:utf-8
'''
   作者：    chenqing
'''
import xdrlib,sys
import xlrd
from datetime import date
def open_excel(file='file.xls'):
    try:
        data=xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

def excel_table_byindex(file='0329.xlsx',colnameindex=0,by_index=0):
    data=open_excel(file)
    table=data.sheets()[by_index]
    nrows=table.nrows #行数 
    ncols=table.ncols #列数
    colnames=table.row_values(colnameindex)#某一行数据
    list=[]
    for rownum in range(1,nrows):
        row=table.row_values(rownum)
        if row:
            app={}
           # for i in range(len(colnames)):
            
            app['jancode']=int(row[3])
           # app['price']=row[11]
            time=xlrd.xldate.xldate_as_tuple(row[8],0)
            app[date(*time[:3]).strftime('%Y/%m/%d')]=row[11]
            list.append(app)
    return list

def main():
    list=excel_table_byindex()
    list1=[]
#    print list
    
    for item in list:
        searched=False
        for dict in list1:
            if dict['jancode'] == item['jancode']:
                for key,value in item.items():
                    dict[key]=value
                searched=True
                break
        if not searched:
            list1.append(item)
   # print list1        

    list2=[]
    for item in list1:
        price=0
        dict={}
        dict['jancode']=item['jancode']
        keys = sorted(item.keys())
        values = sorted(item.values())
       # print values
        if len(values)>2:

            if (values[-2]-values[0])/values[0] > 0.3 :
                if len(values)==3:
                    dict['tips']='=2 price ,max price='+str(values[-2])+' min price='+str(values[0])   
                else:
                    dict['tips']='>2 price ,max price='+str(values[-2])+' min price='+str(values[0])
                for value in values[0:-2]:
                    price = price+value
                dict['avg_price'] = price/(len(values[0:-2]))
                
                #print values[0],values[-2],dict['tips']
            else:

                for value in values[:-1]:
                    price = price+value
                dict['avg_price'] = price/(len(values[:-1]))
        else:
            dict['avg_price'] = values[0]

        list2.append(dict)
   # print list2
    file=open('jancode0329.txt','w')
    for item in list2:
        content = sorted(item.values())
        file.write(str(content))
        file.write('\n')
    file.close()    

main()
