import MySQLdb
import serial
import sqlite3
import datetime
import time

d=datetime.datetime.date(datetime.datetime.now())# in main
se=2#se-1 no.of nodes
db = MySQLdb.connect(host="localhost", user="root", passwd="raspberry", db="Sensor_Statistics") #change the database
cur = db.cursor()

ser = serial.Serial('/dev/ttyAMA0', 9600)
string = 'Hello from Raspberry Pi'
sp = ';'
print 'Sending "%s"' % string
ser.write('%s\n' % string)
o=0
f=0
n1=0
c1=0
t1=0
l1=0
m1=0
p1=0
w1=0
s=0
n=[]
c=[]
t=[]
l=[]
m=[]
p=[]
w=[]
a=[0]


def light():
 global n,t,l,m,p,w,d,se
 conn = sqlite3.connect('test.db')
#print "Opened database successfully";
 i=1#node no. counter
 j=0#
 n_d=[]
 global s
 cusor = conn.execute("SELECT Id,Node_no,Temp,light_Intensity,moisture,pH,lime_req from Dlogs")
 conn.commit()
 e=datetime.datetime.date(datetime.datetime.now())
 if d!=e:
  while i<=se:
   for row in cusor:
     if i==int(row[1]):
       print "node no. = ", i, "\n"
       j=j+1
       print "j:",j
       if int(row[3])>=120:
         s=s+1
         print 'inner',i,'   '
   if j==0:
          coma=str(i)+','
          n_d.append(coma)
          n_d+=[]
   j=0
   if s<=18:
         sun= j*20
         sui=str(sun)+'mins'
         print 'hrs',sui
	 cur.execute("INSERT INTO Sensors1(Node_no,light_Intensity) VALUES ('%s','%s')" % (i,sui))
	 db.commit()
         s=0
   cusor = conn.execute("SELECT Id,Node_no,Temp,light_Intensity,moisture,pH,lime_req from Dlogs")
   conn.commit()
   i=i+1#while se ;
  if n_d:
   n_d=''.join(n_d)
   print 'nodes:',n_d,'down  '
   n_down= "INSERT INTO Sensors1(nodes_down) VALUES('%s')" % (n_d) 
   cur.execute(n_down)
   db.commit()
   del n_d

 # conn.execute("PRAGMA busy_timeout =15000")
 # conn.commit()
  conn.close()
  conn = sqlite3.connect('test.db')
  conn.execute("DROP TABLE Dlogs")
  conn.commit()
  conn.close()
  time.sleep(1/1000)
  conn = sqlite3.connect('test.db')
  conn.execute('''CREATE TABLE Dlogs
       (Id            INTEGER   PRIMARY KEY  AUTOINCREMENT,
        Node_no       VARCHAR(10)    NOT NULL,
        Temp           VARCHAR(10)     NOT NULL,
        light_Intensity  VARCHAR(10)     NOT NULL,
        moisture       VARCHAR(10)     NOT NULL,
        pH             VARCHAR(10)     NOT NULL,
        lime_req      VARCHAR(10)     NOT NULL);''')

  conn.commit()
#  conn.close()
  d=e#ife d ;
 elif e==d:
 # conn = sqlite3.connect('test.db')
  conn.execute("INSERT INTO Dlogs (Node_no,Temp,light_Intensity,moisture,pH,lime_req) VALUES('%s','%s','%s','%s','%s','%s')" % (n,t,l,m,p,w))
  conn.commit()
 # conn.close()
 return

def sq():
	global n,c,t,l,m,p,w
	sql= "INSERT INTO Sensors1(Node_no,Crop,Temp,light_Intensity, moisture, pH, lime_req) VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (n,c,t,l,m,p,w)
	cur.execute(sql)
        db.commit()	
	return

def phr():
	global p,w
	if int(p)>=23 and int(p)<=30: 
		p=4.5
  	elif int(p)>18 and int(p)<23:
		p=5
  	elif int(p)<=18 and int(p)>=14: 
		p=5.5
  	elif int(p)>=9 and int(p)<=13: 
		p=6
  	elif int(p)<=8 and int(p)>=5:
		p=6.5
  	elif int(p)==4 or int(p)==3:
		p=7
	elif int(p)==2 or int(p)==1:
		p=7.5
  	elif int(p)==0: 
		p=8
  	else:   p=0
	
	if float(p)==4.5:
		w=4
	elif float(p)==5:
		w=3.5
  	elif float(p)==5.5:
		w=3
  	elif float(p)==6:
		w=2
  	elif float(p)==6.5:
		w=1
  	elif float(p)==7 or float(p)==7.5:
		w=0
  	else: 
		w='R'

	if float(p)!=6.5 and int(p)!=7 and int(p)!=7.5:
		sq()
	return

def rice():
	global t,l,m
	phr()
	light()
	if int(t)< 24 or int(t)> 36:
		sq()									
	
	if int(m)>500:
		pac=';N'+n+';W500;'
		ser.write(pac)
		sq()
	else:
		ser.write(';W0')
	if int(m)<210:
		m="Remove_water"
		sq()
	return

def crop():
	global c
	if c=='Rice':
		rice()
	return	



while True:
    incoming = ser.read().strip()
    print '%s' % incoming
    if incoming!=sp:
        a+=[]
	if a[0]==0:
		a[0]=incoming
	else:
		a.append(incoming)
	print 'a= %s' %a
	o+=1
    else:
	print '%s' % a
	if a[0]=='N':
	   if n1>0:
           	print 'yo'
		del n
           	n=[]
		n1=0
	   for i in range(1,o):
	       n.append(a[i])
	       n+=[]
	   del a
	   a=[0]
	   o=0
	   n1+=1
	   n=''.join(n)
	   print 'Node_no:%s ' % n
	   #sql= "INSERT INTO Sensors1(Node_no) VALUES ('%s')" % n 
	elif a[0]=='C':
	   if c1>0:
                del c
                c=[]
		c1=0
	   for i in range(1,o):
	       c.append(a[i])
	       c+=[]
	   del a
	   a=[0]
	   o=0
	   c1+=1
	   c =''.join(c)
	   print 'crop:%s ' % c#sql= "INSERT INTO Sensors1(Temp) VALUES ('%s')" % t 
	elif a[0]=='T':
	   if t1>0:
                del t
                t=[]
		t1=0
	   for i in range(1,o):
	       t.append(a[i])
	       t+=[]
	   del a
	   a=[0]
	   o=0
	   t1+=1
	   t =''.join(t)
	   print 'Temperature:%s ' % t#sql= "INSERT INTO Sensors(Temp) VALUES ('%s')" % t 
	elif a[0]=='L':
           if l1>0:
                del l
                l=[]
                l1=0
	   for i in range(1,o):
	       l.append(a[i])
	       l+=[]
	   del a
	   a=[0]
	   o=0
	   l1+=1
	   l=''.join(l)
	   print 'Light_intensity:%s' %l#sql= "INSERT INTO Sensors(light_Intensity) VALUES ('%s')" % l 
	elif a[0]=='M':
	   if m1>0:
                del m
                m=[]
                m1=0
	   for i in range(1,o):
	       m.append(a[i])
	       m+=[]
	   del a
	   a=[0]
	   o=0
	   m1+=1
	   m=''.join(m)
	   print 'Moisture:%s' %m#sql= "INSERT INTO Sensors(moisture) VALUES ('%s')" % m 
	elif a[0]=='P':
           if p1!=0:
                del p
                p=[]
                p1=0
	   for i in range(1,o):
	       p.append(a[i])
	   p1+=1
	   del a
	   a=[0]
	   o=0
	   p=''.join(p)
	   print 'pH:%s' %p# sql= "INSERT INTO Sensors(pH) VALUES ('%s')" % p 
	else:
	   print 'error:%s' % a
	   del a
	   a=[0]
	   o=0
	f=n1+c1+t1+l1+m1+p1
	if f==6:
	   crop()
	   del n,c,t,l,m,p,w
	   n=[]
	   c=[]
	   t=[]
	   l=[]
	   m=[]
	   p=[]
	   w=[]
	   o=0
	   f=0
	   n1=0
	   c1=0
	   t1=0
	   l1=0
	   m1=0
	   p1=0
	  

#
