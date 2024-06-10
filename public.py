from flask import *
from database import*


public=Blueprint('public',__name__)

@public.route('/')
def home():
	return render_template('home.html')



@public.route('/registration',methods=['post','get'])	
def registration():
	if "cusreg" in request.form:
		f=request.form['fname']
		a=request.form['address']
		p=request.form['place']
		
		ph=request.form['phone']
		e=request.form['email']
		u=request.form['uname']
		pa=request.form['pwd']
		types=request.form['types']

		q="select * from login where username='%s' and password='%s'"%(u,pa)
		res=select(q)
		if res:

			flash('already exist')

		else:
			if types=="college":
				q="insert into login values(null,'%s','%s','college')"%(u,pa)
				id=insert(q)
				q="insert into college values(null,'%s','%s','%s','%s','%s','%s')"%(id,f,a,p,ph,e)
				insert(q)
				flash("successfully")
			elif types=="parent":
				q="insert into login values(null,'%s','%s','parent')"%(u,pa)
				id=insert(q)
				q="insert into parent values(null,'%s','%s','%s','%s','%s','%s')"%(id,f,a,p,ph,e)
				insert(q)
				flash('successfully')
				return redirect(url_for('public.registration'))

	return render_template('registration.html')


@public.route('/login',methods=['post','get'])	
def login():
	if "login" in request.form:
		u=request.form['uname']
		pa=request.form['pwd']
		q="select * from login where username='%s' and password='%s'"%(u,pa)
		res=select(q)
		if res:
			session['login_id']=res[0]['login_id']
			lid=session['login_id']
			if res[0]['usertype']=="admin":
				return redirect(url_for('admin.admin_home'))

			elif res[0]['usertype']=="college":
				q="select * from college where login_id='%s'"%(lid)
				res=select(q)
				if res:
					session['college_id']=res[0]['college_id']
					cid=session['college_id']
				return redirect(url_for('college.college_home'))

			elif res[0]['usertype']=="parent":
				q="select * from parent where login_id='%s'"%(lid)
				res=select(q)
				if res:
					session['parent_id']=res[0]['parent_id']
					pid=session['parent_id']



				return redirect(url_for('parent.parent_home'))


			elif res[0]['usertype']=="staff":
				q="select * from staff where login_id='%s'"%(lid)
				res=select(q)
				if res:
					session['staff_id']=res[0]['staff_id']
					pid=session['staff_id']



				return redirect(url_for('staff.staffhome'))


		else:
			flash('invalid username and password')

	return render_template('login.html')