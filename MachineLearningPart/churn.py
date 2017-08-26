import datetime
#contains user_id and last date of visit
#if a customer doesn't turn up for 90 days then we mark that as churned
customer_data={'aakash':{'date':datetime.date(2017,3,24)},'anubhav':{'date':datetime.date(2017,7,6)},'yash':{'date':datetime.date(2017,5,24)},'arya':{'date':datetime.date(2017,8,15)}} #dummy data

#today's date
curr_date=datetime.date.today()

churn=0

for key in customer_data:
	last_visit_date=customer_data[key]['date']
	if (curr_date-last_visit_date).days>90:
		churn=churn+1

print str(float(churn)/len(customer_data)*100)+"%"		

