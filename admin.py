from flask import * 
from database import*



admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():

	return render_template('admin_home.html')


@admin.route('/admin_Viewcolleges')
def admin_Viewcolleges():
	data={}
	q="select * from college"
	res=select(q)
	data['colleges']=res


	return render_template('admin_Viewcolleges.html',data=data)


@admin.route('/admin_viewcourse')
def admin_viewcourse():
	data={}
	cid=request.args['cid']
	q="select * from course inner join college using (college_id) where college_id='%s'"%(cid)
	res=select(q)
	data['course']=res
	return render_template('admin_viewcourse.html',data=data)

@admin.route('/admin_viewseats')
def admin_viewseats():
	data={}
	cid=request.args['cid']

	q="select * from seats inner join course using(course_id) where course_id='%s' "%(cid)
	res=select(q)
	data['seat']=res
	return render_template('admin_viewseats.html',data=data)



@admin.route('/admin_viewadmission')
def admin_viewadmission():
	data={}
	cid=request.args['cid']
	q="select * from admission inner join student using (student_id) inner join course using (course_id) where course_id='%s'"%(cid)
	res=select(q)
	data['addm']=res
	return render_template('admin_viewadmission.html',data=data)


@admin.route('/admin_viewcomplaint')
def admin_viewcomplaint():
	data={}
	q="select * from complaint inner join parent using (parent_id)"
	res=select(q)
	data['comp']=res
	return render_template('admin_viewcomplaint.html',data=data)


@admin.route('/admin_sendreply',methods=['post','get'])
def admin_sendreply():
	if "sendreply" in request.form:
		cid=request.args['cid']
		reply=request.form['reply']
		q="update complaint set reply='%s' where complaint_id='%s'"%(reply,cid)
		update(q)
		return redirect(url_for('admin.admin_viewcomplaint'))
	return render_template('admin_sendreply.html')



