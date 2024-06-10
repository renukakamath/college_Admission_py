from flask import * 
from database import*
import uuid



college=Blueprint('college',__name__)

@college.route('/college_home')
def college_home():

	return render_template('college_home.html')

@college.route('/college_updateprofile',methods=['post','get'])
def college_updateprofile():
	data={}
	cid=session['college_id']
	q="select * from college where college_id='%s'"%(cid)
	res=select(q)
	data['collegess']=res

	if "update" in request.form:
		fname=request.form['fname']
		email=request.form['email']
		address=request.form['address']
		place=request.form['place']
		num=request.form['num']
		q="update college set fname='%s',address='%s',place='%s',phone='%s',email='%s' where college_id='%s'"%(fname,address,place,num,email,cid)
		update(q)
		return redirect(url_for('college.college_updateprofile'))
	return render_template('college_updateprofile.html',data=data)


@college.route('/college_addgallery',methods=['post','get'])
def college_addgallery():
	data={}
	cid=session['college_id']
	q="select * from gallery inner join college using (college_id) where college_id='%s'"%(cid)
	res=select(q)
	data['adgrl']=res


	if "addgallery" in request.form:
		cid=session['college_id']
		file=request.files['gallery']
		path="static/image"+str(uuid.uuid4())+file.filename
		file.save(path)
		title=request.form['title']
		q="insert into gallery values(null,'%s','%s','%s')"%(cid,path,title)
		insert(q)
		return redirect(url_for('college.college_addgallery'))


	return render_template('college_addgallery.html',data=data)


@college.route('/college_addannouncement',methods=['post','get'])
def college_addannouncement():
	data={}
	cid=session['college_id']
	q="select * from announcement inner join college using (college_id) where college_id='%s'"%(cid)
	res=select(q)
	data['customerview']=res

	if "annoo" in request.form:
		title=request.form['title']
		details=request.form['details']
		q="insert into announcement values(null,'%s','%s','%s')"%(cid,title,details)
		insert(q)
		return redirect(url_for('college.college_addannouncement'))

	return render_template('college_addannouncement.html',data=data)


@college.route('/college_addevent',methods=['post','get'])
def college_addevent():
	data={}
	cid=session['college_id']
	q="select * from events inner join college using (college_id) where college_id='%s'"%(cid)
	res=select(q)
	data['annnoo']=res

	if "events" in request.form:
		event=request.form['event']
		
		q="insert into events values(null,'%s','%s')"%(cid,event)
		insert(q)
		return redirect(url_for('college.college_addevent'))

	return render_template('college_addevent.html',data=data)


@college.route('/college_managestaff',methods=['post','get'])
def college_managestaff():
	data={}
	cid=session['college_id']
	q="select * from staff  where college_id='%s'"%(cid)
	res=select(q)
	data['stafffview']=res



	if "action" in  request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None

	if action=='delete':
		q="delete from staff where staff_id='%s'"%(cid)
		delete(q)
		return redirect(url_for('college.college_managestaff'))


	if action=='update':
		q="select * from staff where staff_id='%s'"%(cid)
		res=select(q)
		data['stafff']=res

	if "update" in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		email=request.form['email']
		place=request.form['place']
		num=request.form['num']
		
		q="update staff set fname='%s',lname='%s',place='%s',phone='%s',email='%s' where staff_id='%s'"%(fname,lname,place,num,email,cid)
		update(q)
		return redirect(url_for('college.college_managestaff'))
		

	if "stafff" in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		email=request.form['email']
		place=request.form['place']
		num=request.form['num']
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="insert into login values (null,'%s','%s','staff')"%(uname,pwd)
		id=insert(q)
		
		q="insert into staff values(null,'%s','%s','%s','%s','%s','%s','%s')"%(id,cid,fname,lname,place,num,email)

		insert(q)
		return redirect(url_for('college.college_managestaff'))

	return render_template('college_managestaff.html',data=data)



@college.route('/college_managescourse',methods=['post','get'])
def college_managescourse():
	data={}
	cid=session['college_id']
	q="select * from course inner join college using (college_id) where college_id='%s'"%(cid)
	res=select(q)
	data['annnoo']=res



	if "action" in  request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None

	if action=='delete':
		q="delete from course where course_id='%s'"%(cid)
		delete(q)
		return redirect(url_for('college.college_managescourse'))


	if action=='update':
		q="select * from course where course_id='%s'"%(cid)
		res=select(q)
		data['stafff']=res

	if "update" in request.form:
		course=request.form['course']
		
		
		q="update course set course='%s' where course_id='%s'"%(course,cid)
		update(q)
		return redirect(url_for('college.college_managescourse'))
		

	if "addgallery" in request.form:
		course=request.form['course']
	
	
		q="insert into course values(null,'%s','%s')"%(cid,course)

		insert(q)
		return redirect(url_for('college.college_managescourse'))

	return render_template('college_managescourse.html',data=data)




@college.route('/college_addseat',methods=['post','get'])
def college_addseat():
	data={}
	coid=request.args['coid']
	q="select * from seats inner join course using (course_id) where course_id='%s'"%(coid)
	res=select(q)
	data['annnoo']=res

	if "addgallery" in request.form:
		course=request.form['seat']
		
		q="insert into seats values(null,'%s','%s')"%(coid,course)
		insert(q)
		return redirect(url_for('college.college_addseat',coid=coid))

	return render_template('college_addseat.html',data=data)


@college.route('/college_viewadmision',methods=['post','get'])
def college_viewadmision():
	data={}
	cid=session['college_id']
	q="select * from admission inner join course using (course_id) inner join student using (student_id) where college_id='%s' "%(cid)
	res=select(q)
	data['addm']=res
	return render_template('college_viewadmision.html',data=data)
@college.route('/college_viewstudent',methods=['post','get'])
def college_viewstudent():
	data={}
	sid=request.args['sid']
	q="select * from student where student_id='%s'"%(sid)
	res=select(q)
	data['stuuu']=res
	return render_template('college_viewstudent.html',data=data)
















