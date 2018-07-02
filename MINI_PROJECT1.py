import sqlite3
import psycopg2
import datetime
try :
	
	password_verify = 0
	
#this is the initial step for creating a table for registrations

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	try :
		conn = psycopg2.connect("dbname=miniproject1 user=postgres password=011256 host=localhost port=5432")
		cur = conn.cursor()
		cur.execute("create table registration(id int,user_name char(30),phone_no char(15),password char(20),e_mail char(40),date_created_time char(30),date_time_last_seen char(30))")
		print "registration form was created"
		conn.commit()
		conn.close()

	except Exception as err :
		print err
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#-------------------sign in and registration formate---------------------------------------------------------------------------------------------------------------------------------------
	print "1.registration\n2.signin\n3.forgot password\n4.exit\n"
	correct_input = 0
	while correct_input == 0 :
		input = raw_input("enter the choices given above ")
		try :
			input = int(input)
			correct_input = 1
		
			if (input >4 or input <1) :
				print("entered choice is not in range of displayed ones")
				correct_input = 0
		except :
			print("entered choice is not a digit ..... please enter a digit value")
			correct_input = 0
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
						
#--------------------connect to data base--------------------------------------------------------------------------

	conn = psycopg2.connect("dbname=miniproject1 user=postgres password=011256 host=localhost port=5432")
	cur = conn.cursor()		
#-----------------------------------------------------------------------------------------------------------

#-----------------this if  part is for registration ------------------------------------------------------------------------------
	if input == 1 :
		q="select * from registration"
		cur.execute(q)
		registration_data = cur.fetchall()
		length = len(registration_data)
		new_name = raw_input("enter user name : ")	
		for i in range(0,length) :
			
			while new_name==registration_data[i][1].split()[0]:
				print "user name already exited........."
				new_name = raw_input("enter user name : ")		#have to work more on it.........=================
		
		new_phone_no = raw_input("enter your phone number : ") 
		e_mail =  raw_input("enter your mail : ")
		
		password1 = "y"
		password2 = "x"
		while password1 != password2 :
			password1 = raw_input("enter password : ")
			password2 = raw_input("re-enter password : ")
			if password1 != password2 :
				print "enter the same for password properly"
		date_time = datetime.datetime.now()
		date_time = str(date_time)
	
		q="select * from registration"
		cur.execute(q)
		data=cur.fetchall()
		new_id=len(data)+1
		
		
		#coformaionion
		condition = 0 
		while condition ==0 :
			conformation = raw_input("conform to register [y/n] : ")
			if conformation == "y"or conformation  == "Y" :
				q = "insert into registration(id,user_name,phone_no,password,e_mail,date_created_time,date_time_last_seen) values(%s,'%s','%s','%s','%s','%s','%s')"%(new_id,new_name,new_phone_no,password1,e_mail,date_time,date_time)
				cur.execute(q)	
				s = "create table customer%s(product_name char(20),product_chat char(20),date int,month int,year int,cost int,product_id int)"%(new_id)
				cur.execute(s)
				print"your id is : ",new_id
				condition = 1
				password_verify = 1
				varified_id = new_id
				
				
			else :
				if conformation == 'n' or conformation  == 'N' :
					condition = 1
#--------------registration completed ------------------------------------------------------------------------------

#--------------	sign in formate---------------------------------------------------------------------------------------------------------------------------------------
	if input == 2 :
		conformation = 0
		while conformation==0 :
			user_name = raw_input("user name : ")
			password = raw_input("enter password : ")
		
			q="select * from registration where user_name='%s' and password='%s'"%(user_name,password)
		
			cur.execute(q)
			registration_data = cur.fetchall()
			conformation = len(registration_data)
			
			if conformation == 1 :
				print "your last seen : ",registration_data[0][6]
				date_time = datetime.datetime.now()
				date_time = str(date_time)
				q="update registration set date_time_last_seen='%s' where id=%s"%(date_time,registration_data[0][0])
				cur.execute(q)
				password_verify = 1
				varified_id = registration_data[0][0]
			else :
				print "entered user name or password is wrong............"
				print "1.enter user name and password once again\n2.exit........"
				correct_input = 0 
				while correct_input == 0 :
					input = raw_input("enter the choices given above : ")
					try :
						input = int(input)
						correct_input = 1
		
						if (input >2 or input <1) :
							print("entered choice is not in range of displayed ones")
							correct_input = 0
					except :
						print("entered choice is not a digit ..... please enter a digit value")
						correct_input = 0
				if input==1 :
					conformation = 0
				if input==2 :
					break
					
#--------------	forgot password formate-----------------------------------------------------------------------------------------	
					
	if input == 3 :
		user_name = raw_input("enter user name : ")
		phone_no = raw_input("enter phone number : ")
		e_mail = raw_input("enter e-mail : ")
		id = raw_input("enter ID : ")
		try : 
			id = int(id)
			q="select * from registration where user_name='%s' and id=%s and phone_no='%s' and e_mail='%s'"%(user_name,id,phone_no,e_mail)
			cur.execute(q)
			registration_data = cur.fetchall()
			new_password = raw_input("enter the new password : ")
			q="update registration set password='%s' where id=%s"%(new_password,id)
			cur.execute(q)
			print "=========>>>>password updated<<<<========="
			password_verify = 0
		except :
			print "entered things are not identical...!"
#----------------------------------------------------------------------------------------------------------------------------------------
			
#--------------	sign completed ___ home-screen formate---------------------------------------------------------------------------------------------------------
	while password_verify == 1 :	
	
#---------------input for the options-----------------------------------------------------------------------------------------------------------------------
		correct_input = 0
		print("\n1.add purchase\n2.display purchase\n3.exit\n")
		while correct_input == 0 :
			input = raw_input("enter the choices given above ")
			try :
				input = int(input)
				correct_input = 1
		
				if (input >3 or input <1) :
					print("entered choice is not in range of displayed ones")
					correct_input = 0
			except :
				print("entered choice is not a digit ..... please enter a digit value")
				correct_input = 0
#--------- exit option => break --------------------------------------------------------------------------------------------------------------			

		if input == 3 :
			break
		
#---------- add product -----------------------------------------------------------------	
		while input == 1 :

			#entering the product name :
			product_name = raw_input("enter the product name : ")	
	
			#entering the cost of product
			product_cost="x"
			while product_cost.isdigit()==False :
				product_cost = raw_input("enter the cost of the product : ")
				if product_cost.isdigit()==False :
					print "enter cost in digit"
			product_cost = int(product_cost)
			print product_cost,type(product_cost)

	
			#entering the date of purchase	------------------- now ------------- in past ------------------------
			print "1.purchased now\n2.purchased in past\n"
			
			
			correct_input = 0
			while correct_input == 0 :
				when = raw_input("enter the choices given above ")
				try :
					when = int(when)
					correct_input = 1
		
					if (when >2 or when <1) :
						print("entered choice is not in range of displayed ones")
						correct_input = 0
				except :
					print("entered choice is not a digit ..... please enter a digit value")
					correct_input = 0
			
			
			date_time=datetime.datetime.now()
			date_time=str(date_time)
			date_time_list = date_time.split(' ')
			#print date_time_list
			x=date_time_list[0]
			date_need = x.split('-')
			if when==1 :
				date = date_need[2]
				month = date_need[1]
				year = date_need[0]
			
				
			else :
				date = "x"
				month = "x"
				year = "x"
			
			while date.isdigit()==False or month.isdigit() == False  or year.isdigit() == False  :
				product_name_date = raw_input("enter the date of purschase of product dd/mm/yyyy formate : ")
				date_list = product_name_date.split('/')
				date = date_list[0]
				month = date_list[1]
				year = date_list[2]
				if date.isdigit()==False or month.isdigit() == False  or year.isdigit() == False :
					print"enter value in proper formate"
				if date.isdigit()==True and month.isdigit() == True  and year.isdigit() == True  :
					if int(date)>31 or int(month)>12 or int(year) >int(date_need[0]) or int(year) < 2000 :
						print"enter valid date"
						date = "x"
					else :
						if int(year) == int(date_need[0]) and  int(month) > int(date_need[1]):
							print"enter valid date"
							date = "x"
						else :
							if int(year) == int(date_need[0]) and  int(month) == int(date_need[1]) and date > date_need[2] :
								print"enter valid date"
								date = "x"	
			date=int(date)
			month= int(month)
			year=int(year)
	
	
			q="select * from customer%s"%(varified_id)
			cur.execute(q)
			data=cur.fetchall()
			d=len(data)
			count=1
			types=[]
			for i in range(0,d) :
				check=0
				for j in range(i,d) :
					if data[j][1]== data[i][1] :
						check = check+1
				if check == 1 :
					print count,data[i][1]
					types.append(data[i][1])
					count = count+1	
			print count,"---NEW TYPE---"
		
			new_type_no="x"
			while new_type_no.isdigit()==False :
				new_type_no = raw_input("enter the choice : ")
				if new_type_no.isdigit()==False :
					print "enter a digit"
				else :
					if int(new_type_no)<0 or int(new_type_no)>count :
						print "enter the number in range"
						new_type_no="x"
		
			new_type_no = int(new_type_no)		
		
			if new_type_no<count and new_type_no>0 :
				product_type = types[count-2]
			elif new_type_no == count :
				product_type = raw_input("enter the new type name : ")
			if d==0 :
				product_new_id = 1
			else :
				product_new_id = data[d-1][6]+1
			q = "insert into customer%s(product_name,product_chat,date,month,year,cost,product_id) values('%s','%s','%s',%s,%s,%s,%s)"%(varified_id,product_name,product_type,date,month,year,product_cost,product_new_id)
			cur.execute(q)
			
			
			condition = 0			
			while condition ==0 :
				conformation = raw_input("want to add one more product....... [y/n] : ")
				if conformation == "y"or conformation  == "Y" :
					condition = 1
				else :
					if conformation == 'n' or conformation  == 'N' :
						condition = 1
			if conformation == 'n' or conformation == 'N' : 
				break
#-------------------------------------------------------------------------------------------------------------------------------------------------------


#------------------ 2.DISPLAY PURCHASE MODE --------------------------------------------------------------------------------------------------
			
			
		while input == 2 :
			modified_id = 0
			print("1.display all\n2.dispaly as per dates\n3.displaya as per cost\n4.dispaly as per type\n5.back\n")
			correct_input = 0
			while correct_input == 0 :
				input1 = raw_input("enter the choices given above ")
				try :
					input1 = int(input1)
					correct_input = 1
		
					if (input1 >5 or input1 <1) :
						print("entered choice is not in range of displayed ones")
						correct_input = 0
				except :
					print("entered choice is not a digit ..... please enter a digit value")
					correct_input = 0
				# ------------------------ exit => break --------------------------------------------------------------------------------------
			if input1 == 5 :
				break
				# ------------------------ dispaly all products----------------------------------------------------------------------------------
			if 	input1 == 1 :
				
				q="select * from customer%s"%(varified_id)
				cur.execute(q)
				data=cur.fetchall()
				length = len(data)
				count = 0
				total=0
				print"----------------------------------------------------------------------------------------------------------------"
				print  "s.no",'\t',"name",'\t\t\t',"type",'\t\t\t',"cost",'\t',"date of purchase"
				print"----------------------------------------------------------------------------------------------------------------"
				for i in range(0,length):
					count = count +1
					print  i+1,'\t',data[i][0],'\t',data[i][1],'\t',data[i][5],'\t',str(data[i][2])+'/'+str(data[i][3])+'/'+str(data[i][4])
					total = total + data[i][5]
				print"----------------------------------------------------------------------------------------------------------------"
				print '\t\t\t\t\t\t',"total = ",total
				print"----------------------------------------------------------------------------------------------------------------"
				
				#-------------------------------
				print"1.to modify\n2.to continue this\n"
				
				correct_input = 0
				while correct_input == 0 :
					input4 = raw_input("enter the choice : ")
					try :
						input4 = int(input4)
						correct_input = 1
	
						if (input4 >2 or input4 <1) :
							print("entered choice is not in range of displayed ones")
							correct_input = 0
					except :
						print("entered choice is not a digit ..... please enter a digit value")
						correct_input = 0
				if input4 == 1 :
					correct_input = 0
					while correct_input == 0 :
						input5 = raw_input("enter the number to modify : ")
						try :
							input5 = int(input5)
							correct_input = 1
		
							if (input5 >count or input5 <1) :
								print("entered choice is not in range of displayed ones")
								correct_input = 0
						except :
							print("entered choice is not a digit ..... please enter a digit value")
							correct_input = 0	
					
					q="select * from customer%s"%(varified_id)
					cur.execute(q)
					data=cur.fetchall()
					length = len(data)
				
					
					count = 0
					for i in range(0,length):
						count = count +1
						if count== input5 :
							modified_id = data[i][6]
					print modified_id
					
				#---------------dispaly by ranging dates ---------------------------------------------------------------------	
			if input1 == 2:
				date_time=datetime.datetime.now()
				date_time=str(date_time)
				date_time_list = date_time.split(' ')
				date_month_year = date_time_list[0].split('-')
				
				input_date1 ='x'
				input_month1='y'
				input_year1 ='z'
				
				input_date2 ='x'
				input_month2='y'
				input_year2 ='z'
							
				if 1==1 :
					while input_date1.isdigit() == False or input_month1.isdigit() == False or input_year1.isdigit() == False or input_date2.isdigit() == False or input_month2.isdigit() == False or input_year2.isdigit() == False :
						#if input1 == 2 :
						date_input = raw_input("enter the range in this formate dd/mm/yyyy-dd/mm/yyyy :  ")
						date_input = date_input.split('-')
						'''if len(date_input) == 2:
							year.append(year[0])'''
						try :
							date_input1 = date_input[0].split('/')
							date_input2 = date_input[1].split('/')
							
							input_date1 = date_input1[0]
							input_month1= date_input1[1]
							input_year1 = date_input1[2]
							
							input_date2 = date_input2[0]
							input_month2= date_input2[1]
							input_year2 = date_input2[2]
							
							
						except :
							print "enter the year in proper formate"
							input_date1 ='x'
							input_month1='y'
							input_year1 ='z'
							
							
							
						finally :
							if  input_year1>input_year2 :
								input_year1 = 'x'
								print "------------------>  enter the lowest first  <-------------------------"
							else :
								if input_year1 == input_year2 and input_month1>input_month2 :
									input_month1='y'
									print "------------------>  enter the lowest first  <-------------------------"
								else :
									if input_year1 == input_year2 and input_month1==input_month2 and input_year1>input_year2:
										input_year1 ='z'
										
									
								
							if input_year2 < int(date_month_year[0]) :
								input_year1 ='z'
								print "---------------->  entered date is invalid year  <------------------"
								
							#print input_date1,input_month1,input_year1,input_date2 ,input_month2,input_year2
					input_date1 = int(date_input1[0])
					input_month1= int(date_input1[1])
					input_year1 = int(date_input1[2])
							
					input_date2 = int(date_input2[0])+1
					input_month2= int(date_input2[1])
					input_year2 = int(date_input2[2])
					print"----------------------------------------------------------------------------------------------------------------"
					print  "s.no",'\t',"name",'\t\t\t',"type",'\t\t\t',"cost",'\t',"date of purchase"
					print"----------------------------------------------------------------------------------------------------------------"
					
				
					total=0
					count=0
					for j in range(input_year1,input_year2):
						for k in range(input_month1,13):
							for l in range(input_date1,32):
								q="select * from customer%s where date='%s' and month='%s' and year='%s'"%(varified_id,l,k,j)
								cur.execute(q)
								data=cur.fetchall()
								length = len(data)	
								for i in range(0,length) :
									count = count + 1
									print  count,'\t',data[i][0],'\t',data[i][1],'\t',data[i][5],'\t',str(data[i][2])+'/'+str(data[i][3])+'/'+str(data[i][4])
									total = total + data[i][5]
							input_date1 = 1
						input_month1 = 1
					for j in range(input_year2,input_year2+1):
						if input_year1==input_year2 :
							start_month=input_month1
						else :
							start_month=1
						for k in range(start_month,input_month2+1):
							if input_year1==input_year2 and input_month1==input_month2 :
								start_date=input_date1
							else :
								start_date=1
							if k != input_month2 :
								some = 32
							else :
								some = input_date2
							for l in range(start_date,some):
					
								q="select * from customer%s where date='%s' and month='%s' and year='%s'"%(varified_id,l,k,j)
								cur.execute(q)
								data=cur.fetchall()
								length = len(data)
								for i in range(0,length) :
									count = count + 1
									print  count,'\t',data[i][0],'\t',data[i][1],'\t',data[i][5],'\t',str(data[i][2])+'/'+str(data[i][3])+'/'+str(data[i][4])
									total = total + data[i][5]
						
						
						
					print"----------------------------------------------------------------------------------------------------------------"
					print '\t\t\t\t\t\t',"total = ",total
					print"----------------------------------------------------------------------------------------------------------------"
					print"1.to modify\n2.to continue this\n"
					correct_input = 0
					while correct_input == 0 :
						input2 = raw_input("enter the choices given above ")
						try :
							input2 = int(input2)
							correct_input = 1
	
							if (input2 >2 or input2 <1) :
								print("entered choice is not in range of displayed ones")
								correct_input = 0
						except :
							print("entered choice is not a digit ..... please enter a digit value")
							correct_input = 0
					if input2==1 :
						
						correct_input = 0
						while correct_input == 0 :
							input3 = raw_input("enter the number to modify : ")
							try :
								input3 = int(input3)
								correct_input = 1
		
								if (input3 >count or input3 <1) :
									print("entered choice is not in range of displayed ones")
									correct_input = 0
							except :
								print("entered choice is not a digit ..... please enter a digit value")
								correct_input = 0
					
						count=0
						for j in range(input_year1,input_year2):
							for k in range(input_month1,13):
								for l in range(input_date1,32):
									q="select * from customer%s where date='%s' and month='%s' and year='%s'"%(varified_id,l,k,j)
									cur.execute(q)
									data=cur.fetchall()
									length = len(data)	
									for i in range(0,length) :
										count = count + 1
										if count == input3 :
											modified_id = data[i][6]
								input_date1 = 1
							input_month1 = 1
						for j in range(input_year2,input_year2+1):
							if input_year1==input_year2 :
								start_month=input_month1
							else :
								start_month=1
							for k in range(start_month,input_month2+1):
								if input_year1==input_year2 and input_month1==input_month2 :
									start_date=input_date1
								else :
									start_date=1
								
								if k != input_month2 :
									some = 32
								else :
									some = input_date2
								for l in range(start_date,some):
					
									q="select * from customer%s where date='%s' and month='%s' and year='%s'"%(varified_id,l,k,j)
									cur.execute(q)
									data=cur.fetchall()
									length = len(data)
									for i in range(0,length) :
										count = count + 1
										if count == input3 :
											modified_id = data[i][6]
				
					print modified_id
			#--------------	dispaly as per cost -----------------------------------------------------------------------------------------
			
			if input1 == 3 :
				condition = 0
				while condition == 0 :
					range_cost = raw_input("enter the range of cost in this formate xxxx-xxxx : ")
					range_cost = range_cost.split('-')
					try : 
						range_cost[0] = int(range_cost[0])
						range_cost[1] = int(range_cost[1])
						condition = 1
						if int(range_cost[0])>int(range_cost[1]) :
							print "enter lowest first"
							condition = 0
					except :
						condition = 0
						print "enter in proper formate"
				print range_cost
				
				q="select * from customer%s"%(varified_id)
				cur.execute(q)
				data=cur.fetchall()
				length = len(data)
				count = 0
				total=0
				print"----------------------------------------------------------------------------------------------------------------"
				print  "s.no",'\t',"name",'\t\t\t',"type",'\t\t\t',"cost",'\t',"date of purchase"
				print"----------------------------------------------------------------------------------------------------------------"
				for i in range(0,length):
					if data[i][5]>range_cost[0] and data[i][5]<range_cost[1] :
						count = count +1
						print  count,'\t',data[i][0],'\t',data[i][1],'\t',data[i][5],'\t',str(data[i][2])+'/'+str(data[i][3])+'/'+str(data[i][4])
						total = total + data[i][5]
				print"----------------------------------------------------------------------------------------------------------------"
				print '\t\t\t\t\t\t',"total = ",total
				print"----------------------------------------------------------------------------------------------------------------"
				print"1.to modify\n2.to continue this\n"
				correct_input = 0
				while correct_input == 0 :
					input6 = raw_input("enter the choice : ")
					try :
						input6 = int(input6)
						correct_input = 1
	
						if (input6 >2 or input6 <1) :
							print("entered choice is not in range of displayed ones")
							correct_input = 0
					except :
						print("entered choice is not a digit ..... please enter a digit value")
						correct_input = 0
				if input6 == 1:
					correct_input = 0
					while correct_input == 0 :
						input5 = raw_input("enter the munber to modify : ")
						try :
							input5 = int(input5)
							correct_input = 1
	
							if (input5 >count or input5 <1) :
								print("entered choice is not in range of displayed ones")
								correct_input = 0
						except :
							print("entered choice is not a digit ..... please enter a digit value")
							correct_input = 0
					q="select * from customer%s"%(varified_id)
					cur.execute(q)
					data=cur.fetchall()
					length = len(data)
					count = 0
					modified_id = 0
				
					for i in range(0,length):
						if data[i][5]>range_cost[0] and data[i][5]<range_cost[1] :
							count = count +1
							if input5 == count :
								modified_id = data[i][6]
				#print modified_id
						
				
				
			#--------------	dispaly by type of product -----------------------------------------------------------------------------------------	
			if input1 == 4 :
				q="select * from customer%s"%(varified_id)
				cur.execute(q)
				data=cur.fetchall()
				d=len(data)
				count=1
				types=[]
				for i in range(0,d) :
					check=0
					for j in range(i,d) :
						if data[j][1]== data[i][1] :
							check = check+1
					if check == 1 :
						print count,data[i][1]
						types.append(data[i][1])
						count = count+1	
		
				type_no="x"
				while type_no.isdigit()==False :
					type_no = raw_input("enter the choice : ")
					if type_no.isdigit()==False :
						print "enter a digit"
					else :
						if int(type_no)< 1 or  int(type_no)>count-1 :
							print "enter the number in range"
							type_no="x"
		
				type_no = int(type_no)		
				
				print type_no
				
				q="select * from customer%s where product_chat='%s'"%(varified_id,types[type_no-1])
				cur.execute(q)
				data=cur.fetchall()
				length = len(data)
				count = 0
				total=0
				print"----------------------------------------------------------------------------------------------------------------"
				print  "s.no",'\t',"name",'\t\t\t',"type",'\t\t\t',"cost",'\t',"date of purchase"
				print"----------------------------------------------------------------------------------------------------------------"
				for i in range(0,length):
					count = count +1
					print  i+1,'\t',data[i][0],'\t',data[i][1],'\t',data[i][5],'\t',str(data[i][2])+'/'+str(data[i][3])+'/'+str(data[i][4])
					total = total + data[i][5]
				print"----------------------------------------------------------------------------------------------------------------"
				print '\t\t\t\t\t\t',"total = ",total
				print"----------------------------------------------------------------------------------------------------------------"
				
				
				print"1.to modify\n2.to continue this\n"
				correct_input = 0
				while correct_input == 0 :
					input6 = raw_input("enter the choice : ")
					try :
						input6 = int(input6)
						correct_input = 1
	
						if (input6 >2 or input6 <1) :
							print("entered choice is not in range of displayed ones")
							correct_input = 0
					except :
						print("entered choice is not a digit ..... please enter a digit value")
						correct_input = 0
				if input6 == 1:
					correct_input = 0
					while correct_input == 0 :
						input5 = raw_input("enter the munber to modify : ")
						try :
							input5 = int(input5)
							correct_input = 1
	
							if (input5 >count or input5 <1) :
								print("entered choice is not in range of displayed ones")
								correct_input = 0
						except :
							print("entered choice is not a digit ..... please enter a digit value")
							correct_input = 0
					
					
					q="select * from customer%s where product_chat='%s'"%(varified_id,types[type_no-1])
					cur.execute(q)
					data=cur.fetchall()
					length = len(data)
					count = 0
					for i in range(0,length):
						count = count +1
						if count == input5 :
							modified_id = data[i][6]
				print modified_id
				
				#-------------------MODIFICATION PART ---------------------------------
				
			if modified_id != 0 :
				print "1.delete this product\n2.modify this product\n3.exit"
				correct_input = 0
				while correct_input == 0 :
					input7 = raw_input("enter the choice : ")
					try :
						input7 = int(input7)
						correct_input = 1
	
						if (input7 >3 or input7 <1) :
							print("entered choice is not in range of displayed ones")
							correct_input = 0
					except :
						print("entered choice is not a digit ..... please enter a digit value")
						correct_input = 0	
				if input7 == 1 :
					delete = raw_input("conformation ---- warning-------enter [y/n]")
					q="delete from customer%s where product_id='%s'"%(varified_id,modified_id)
					if delete == 'y' or delete == 'Y' :
						cur.execute(q)
				if input7 == 2 :
					q="select * from customer%s where product_id='%s'"%(varified_id,modified_id)
					cur.execute(q)
					data=cur.fetchall()
					p = "name : %s\t\t modify name : "%(data[0][0])
					modified_name = raw_input(p)
					p = "type : %s\t\t modify type : "%(data[0][1])
					modified_type = raw_input(p)
					p = "cost : %s\t\t\t\t modify cost : "%(data[0][5])
					modified_cost = raw_input(p)
					q="update customer%s set product_name= '%s' where product_id=%s"%(varified_id,modified_name,modified_id)
					cur.execute(q)
					q="update customer%s set product_chat= '%s' where product_id=%s"%(varified_id,modified_type,modified_id)
					cur.execute(q)
					q="update customer%s set cost= %s where product_id=%s"%(varified_id,modified_cost,modified_id)
					cur.execute(q)
					print "data updated ...."
				
			
#========================================================================================================================================================				
					
			
except Exception as err :
	print err
	print err
finally :
	conn.commit()
	conn.close()
#'input3'