from flask import * 
from database import*
import uuid



parent=Blueprint('parent',__name__)

@parent.route('/parent_home')
def parent_home():

	return render_template('parent_home.html')


@parent.route('/parent_addstudent',methods=['post','get'])
def parent_addstudent():
	data={}

	q="select * from student"
	res=select(q)
	data['customerview']=res


	if "addgallery" in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		email=request.form['email']
		place=request.form['place']
		num=request.form['phone']
		dob=request.form['dob']
		pid=session['parent_id']
		
		
		q="insert into student values(null,'%s','%s','%s','%s','%s','%s','%s')"%(pid,fname,lname,place,num,email,dob)

		insert(q)
		return redirect(url_for('parent.parent_addstudent'))

	return render_template('parent_addstudent.html',data=data)



@parent.route('/parent_Viewcollege',methods=['post','get'])
def parent_Viewcollege():
	data={}

	q="select * from college"
	res=select(q)
	data['annnoo']=res

	return render_template('parent_Viewcollege.html',data=data)


@parent.route('/parent_viewgallery',methods=['post','get'])
def parent_viewgallery():
	data={}
	cid=request.args['cid']

	q="select * from gallery inner join college using (college_id) where college_id='%s'"%(cid)
	res=select(q)
	data['annnoo']=res

	return render_template('parent_viewgallery.html',data=data)



@parent.route('/parent_viewannouncement',methods=['post','get'])
def parent_viewannouncement():
	data={}
	cid=request.args['cid']

	q="select * from announcement inner join college using (college_id) where college_id='%s'"%(cid)
	res=select(q)
	data['annnoo']=res

	return render_template('parent_viewannouncement.html',data=data)


@parent.route('/parent_viewevent',methods=['post','get'])
def parent_viewevent():
	data={}
	cid=request.args['cid']

	q="select * from events inner join college using (college_id) where college_id='%s'"%(cid)
	res=select(q)
	data['annnoo']=res

	return render_template('parent_viewevent.html',data=data)



@parent.route('/parent_viewcourse',methods=['post','get'])
def parent_viewcourse():
	data={}
	cid=request.args['cid']

	q="select * from course inner join college using (college_id) where college_id='%s'"%(cid)
	res=select(q)
	data['annnoo']=res

	return render_template('parent_viewcourse.html',data=data)



@parent.route('/parent_viewseat',methods=['post','get'])
def parent_viewseat():
	data={}
	cid=request.args['cid']

	q="select * from seats  where course_id='%s'"%(cid)
	res=select(q)
	data['annnoo']=res

	return render_template('parent_viewseat.html',data=data)


@parent.route('/parent_requestadmission',methods=['post','get'])
def parent_requestadmission():
	data={}
	cid=request.args['cid']

	q="select * from admission inner join student using (student_id) inner join course using (course_id) where course_id='%s' "%(cid)
	res=select(q)
	data['admisss']=res
	

	if "addgallery" in request.form:
		Details=request.form['Details']
		date=request.form['date']
		pid=session['parent_id']
		cid=request.args['cid']
		q="insert into admission values(null,'%s',(select student_id from student where parent_id='%s'),'%s','%s','Applied')"%(cid,pid,Details,date)
		insert(q)
		return redirect(url_for('parent.parent_requestadmission',cid=cid))


	return render_template('parent_requestadmission.html',data=data)


@parent.route('/parent_uploaddetails',methods=['post','get'])
def parent_uploaddetails():
	if "addgallery" in request.form:
		title=request.form['title']
		file=request.files['file']
		path="static/image"+str(uuid.uuid4())+file.filename
		file.save(path)
		date=request.form['date']
		aid=request.args['aid']
		q="insert into uploaddetails values(null,'%s','%s','%s','%s')"%(aid,title,path,date)
		insert(q)
		return redirect(url_for('parent.parent_Viewcollege'))
	return render_template('parent_uploaddetails.html')



@parent.route('/parent_addcomplaints',methods=['post','get'])
def parent_addcomplaints():
	data={}
	q="select * from complaint"
	res=select(q)
	data['comp']=res
	
	if "addgallery" in request.form:
		complaints=request.form['complaints']
		pid=session['parent_id']
		q="insert into complaint values(null,'%s','%s','pending',curdate())"%(pid,complaints)
		insert(q)
		return redirect(url_for('parent.parent_addcomplaints'))
	return render_template('parent_addcomplaints.html',data=data)













