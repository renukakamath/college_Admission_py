from flask import * 
from database import*



staff=Blueprint('staff',__name__)

@staff.route('/staffhome')
def staffhome():

	return render_template('staffhome.html')



@staff.route('/staff_viewcourse')
def staff_viewcourse():
	data={}
	q="select * from course inner join college using (college_id)"
	res=select(q)
	data['coursess']=res


	return render_template('staff_viewcourse.html',data=data)

@staff.route('/staff_viewseats')
def staff_viewseats():
	data={}
	cid=request.args['cid']
	q="select * from seats inner join course using (course_id) where course_id='%s'"%(cid)
	res=select(q)
	data['seee']=res
	return render_template('staff_viewseats.html',data=data)





@staff.route('/staff_viewadmission')
def staff_viewadmission():
	data={}
	cid=request.args['cid']
	q="select * from admission inner join course using (course_id) inner join student using (student_id) where course_id='%s'"%(cid)
	res=select(q)
	data['seee']=res
	return render_template('staff_viewadmission.html',data=data)

@staff.route('/staff_viewuploadeddetails')
def staff_viewuploadeddetails():
	data={}
	adid=request.args['adid']
	q="select * from uploaddetails inner join admission using (admission_id) where admission_id='%s'"%(adid)
	res=select(q)
	data['seee']=res
	return render_template('staff_viewuploadeddetails.html',data=data)

