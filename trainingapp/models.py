from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class create_team(models.Model):
    create_team_name = models.CharField(max_length=200)
    create_team_trainer = models.CharField(max_length=200, default='')
    create_team_progress = models.IntegerField()
    create_team_status = models.CharField(max_length=200, default='0')


    def __str__(self):
        return self.name


class designation(models.Model):
    designation_name = models.CharField(max_length=100)
    designation_status = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class category(models.Model):
    category_name=models.CharField(max_length=200)
    
    def _str_(self):
        return self.name

class course(models.Model):
    course_name=models.CharField(max_length=200)
    course_total_fee=models.IntegerField()
    course_file=models.FileField(upload_to = 'images/', null=True, blank=True)
    course_syllabus_file=models.FileField(upload_to = 'images/', null=True, blank=True)
    course_category=models.ForeignKey(category, on_delete=models.SET_NULL,
                             related_name='coursecategory', null=True, blank=True)
    course_duration=models.CharField(max_length=200)


    def _str_(self):
        return self.name


class user_registration(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.SET_NULL,
                                    related_name='userregistrationdesignation', null=True, blank=True)  
    team = models.ForeignKey(create_team, on_delete=models.SET_NULL,
                             related_name='userregistrationteam', null=True, blank=True)
    course = models.ForeignKey(course, on_delete=models.SET_NULL, related_name='coursename',null=True,blank=True)
    category=models.ForeignKey(category, on_delete=models.SET_NULL,
                             related_name='catgname', null=True, blank=True)
    fullname = models.CharField(max_length=240, null=True)
    fathername = models.CharField(max_length=240, null=True)
    mothername = models.CharField(max_length=240, null=True)
    dateofbirth = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    gender = models.CharField(max_length=240, null=True)
    presentaddress1 = models.CharField(max_length=240, null=True)
    presentaddress2 = models.CharField(max_length=240, null=True)
    presentaddress3 = models.CharField(max_length=240, null=True)
    pincode = models.CharField(max_length=240, null=True)
    district = models.CharField(max_length=240, null=True)
    state = models.CharField(max_length=240, null=True)
    country = models.CharField(max_length=240, null=True)
    permanentaddress1 = models.CharField(max_length=240, null=True)
    permanentaddress2 = models.CharField(max_length=240, null=True)
    permanentaddress3 = models.CharField(max_length=240, null=True)
    permanentpincode = models.CharField(max_length=240, null=True)
    permanentdistrict = models.CharField(max_length=240, null=True)
    permanentstate = models.CharField(max_length=240, null=True)
    permanentcountry = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=240, null=True)
    alternativeno = models.CharField(max_length=240, null=True)
    employee_id = models.CharField(max_length=240,null=True,default='')
    email = models.EmailField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    idproof = models.FileField(upload_to='images/', null=True, blank=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    attitude = models.IntegerField(default='0')
    creativity = models.IntegerField(default='0')
    workperformance = models.IntegerField(default='0')
    joiningdate = models.DateField(
        auto_now_add=True, auto_now=False,  null=True, blank=True)
    startdate = models.DateField(
        auto_now_add=True, auto_now=False,  null=True, blank=True)
    enddate = models.DateField(
        auto_now_add=True, auto_now=False,  null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default="active")
    tl_id = models.IntegerField(default='0',null=True, blank=True)
    
    total_pay=models.IntegerField(default='0')
    payment_balance = models.IntegerField( default='0')
    account_no = models.CharField(max_length=200, null=True,blank=True, default='')
    ifsc =  models.CharField(max_length=200, null=True, default='')
    bank_name = models.CharField(max_length=240, null=True,blank=True, default='')
    bank_branch = models.CharField(max_length=240, null=True, default='')
    payment_status = models.CharField(max_length=200, null=True, default='')


    appoinment_date=models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    offer_letter=models.FileField(upload_to = 'images/', null=True, blank=True)
    relive_letter=models.FileField(upload_to = 'images/', null=True, blank=True)
    experience_certificate=models.FileField(upload_to = 'images/', null=True, blank=True)


    def __str__(self):
        return self.fullname

    
    @property
    def avg(self):
        return (self.attitude+self.creativity+self.workperformance)/3

class attendance(models.Model):
    attendance_user = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                             related_name='attendanceuser', null=True, blank=True)
    attendance_date = models.DateField(null=True, blank=True)
    attendance_status = models.CharField(max_length=200)

   
    def __str__(self):
        return self.user

class trainer_task(models.Model):
    trainer_task_user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,
                             related_name='trainer_task_trainee', null=True, blank=True)
    trainer_task_team_name = models.ForeignKey(
        create_team, on_delete=models.SET_NULL, related_name='team_name', null=True, blank=True)
    trainer_task_category=models.ForeignKey(category, on_delete=models.SET_NULL,
                             related_name='taskcategory', null=True, blank=True)
    trainer_task_course=models.ForeignKey(course, on_delete=models.SET_NULL,
                             related_name='taskcourse', null=True, blank=True)
    #designation=models.ForeignKey(designation, on_delete=models.SET_NULL,
                             #related_name='taskdesignation', null=True, blank=True)
    trainer_task_taskname = models.CharField(max_length=240)
    trainer_task_startdate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    trainer_task_enddate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    trainer_task_submitteddate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    trainer_task_files = models.FileField(upload_to='images/', null=True, blank=True)
    trainer_task_description = models.TextField(max_length=240)
    trainer_task_user_description = models.TextField(max_length=240)
    trainer_task_user_files = models.FileField(upload_to='images/', null=True, blank=True)
    trainer_task_status = models.CharField(max_length=200)
    def __str__(self):
        return self.user

class leave(models.Model):
    leave_user = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                             related_name='leaveuser', null=True, blank=True)
    leave_from_date = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    leave_to_date = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    leave_reason = models.TextField()
    leave_status = models.CharField(max_length=200)
    leave_leaveapproved_status = models.CharField(max_length=200)
    leave_replay=models.TextField()
    leave_designation_id = models.CharField(max_length=200)
    leave_rejected_reason = models.CharField(max_length=300)

    
    def __str__(self):
        return self.user


class topic(models.Model):
    topic_trainee = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                                related_name='topictrainee', null=True, blank=True, default='')
    topic_trainer = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                                related_name='topictrainer', null=True, blank=True)
    topic_team = models.ForeignKey(create_team, on_delete=models.SET_NULL,
                             related_name='topicteam', null=True, blank=True)
    topic_topic = models.CharField(max_length=240)
    topic_startdate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    topic_enddate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    topic_files = models.FileField(upload_to='images/', null=True, blank=True)
    topic_description = models.TextField()
    topic_review = models.TextField()
    topic_status = models.CharField(max_length=200)

class paymentlist(models.Model):
    paymentlist_user_id = models.ForeignKey(user_registration, on_delete=models.SET_NULL, related_name='userpay',null=True,blank=True)
    paymentlist_amount_pay = models.IntegerField(default='0')
    paymentlist_amount_date =models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    paymentlist_current_date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    paymentlist_amount_status = models.CharField(max_length=200, null=True)
    paymentlist_amount_downlod = models.FileField(upload_to = 'images/', null=True, blank=True)
    paymentlist_balance_amt = models.IntegerField(default='0')
    paymentlist_course = models.ForeignKey(course, on_delete=models.SET_NULL, related_name='total',null=True,blank=True, default='')
    
    @property
    def balance(self):
        return (self.course.total_fee-self.amount_pay)

class reported_issue(models.Model):
    reported_issue_reporter = models.ForeignKey(user_registration, on_delete=models.SET_NULL,related_name='reported_issuereporter', null=True, blank=True)
    reported_issue_reported_to = models.ForeignKey(user_registration, on_delete=models.SET_NULL,related_name='reported_issuereported_to', null=True, blank=True)
    reported_issue_issue = models.TextField()
    reported_issue_reported_date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    reported_issue_reply = models.TextField()
    reported_issue_issuestatus = models.CharField(max_length=200)
    reported_issue_designation_id = models.ForeignKey(designation, on_delete=models.SET_NULL,related_name='reportissuedesignation', null=True, blank=True)

    def __str__(self):
        return self.reporter

class acntspayslip(models.Model):
    acntspayslip_basic_salary = models.IntegerField()
    acntspayslip_user_id = models.ForeignKey(user_registration, on_delete=models.SET_NULL, related_name='user',null=True,blank=True)
    acntspayslip_designation = models.ForeignKey(designation, on_delete=models.SET_NULL, related_name='desic',null=True,blank=True)
    acntspayslip_hra = models.IntegerField()
    acntspayslip_conveyns = models.CharField(max_length=100)
    acntspayslip_tax = models.IntegerField()
    acntspayslip_incentives = models.IntegerField()
    acntspayslip_fromdate = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    acntspayslip_todate = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    acntspayslip_taxengine = models.CharField(max_length=100) 
    acntspayslip_incometax = models.IntegerField() 
    acntspayslip_uan = models.CharField(max_length=100) 
    acntspayslip_pf = models.IntegerField() 
    acntspayslip_esi = models.CharField(max_length=100)  
    acntspayslip_pro = models.CharField(max_length=100) 
    acntspayslip_leavesno = models.IntegerField() 
    acntspayslip_pf_tax = models.IntegerField()
    acntspayslip_delay = models.IntegerField()
    acntspayslip_basictype =  models.CharField(max_length=255,default='')
    acntspayslip_hratype = models.CharField(max_length=255,default='')
    acntspayslip_contype = models.CharField(max_length=255,default='')
    acntspayslip_protype = models.CharField(max_length=255,default='')
    acntspayslip_instype = models.CharField(max_length=255,default='')
    acntspayslip_deltype = models.CharField(max_length=255,default='')
    acntspayslip_leatype = models.CharField(max_length=255,default='')
    acntspayslip_pftype = models.CharField(max_length=255,default='')
    acntspayslip_esitype = models.CharField(max_length=255,default='')
    
class acntexpensest (models.Model):
    acntexpensest_payee =models.CharField(max_length=100)
    acntexpensest_payacnt=models.CharField(max_length=200)
    acntexpensest_paymethod =models.CharField(max_length=100)
    acntexpensest_paydate=models.CharField(max_length=100)
    acntexpensest_refno=models.CharField(max_length=100)
    acntexpensest_amount =models.IntegerField()
    acntexpensest_tax=models.IntegerField()
    acntexpensest_total=models.IntegerField()
    acntexpensest_category=models.CharField(max_length=100)
    acntexpensest_description=models.CharField(max_length=100)


