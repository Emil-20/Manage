from django. contrib import messages
from unicodedata import name
from django.shortcuts import render
from django.shortcuts import render, redirect
from trainingapp.models import *
from datetime import datetime,date
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from io import BytesIO
from django.core.files import File
from django.conf import settings
import qrcode
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate , login , logout

# Create your views here.

def Tlogin(request):
    
    des = designation.objects.get(designation_name='manager')
    des1 = designation.objects.get(designation_name='trainer')
    des2 = designation.objects.get(designation_name='trainee')
    des3 = designation.objects.get(designation_name='accounts')

    if request.method == 'POST':
        
        email  = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
                request.session['SAdm_id'] = user.id
                return redirect( 'Admin_Dashboard')
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation_id=des.id).exists():
                member = user_registration.objects.get(
                email=request.POST['email'], password=request.POST['password'])
                request.session['m_designation_id'] = member.designation_id
                request.session['m_fullname'] = member.fullname
                request.session['m_id'] = member.id
                return render(request, 'dashsec.html', {'member': member})
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation_id=des1.id).exists():
                member = user_registration.objects.get(
                email=request.POST['email'], password=request.POST['password'])
                request.session['tr_designation_id'] = member.designation_id
                request.session['tr_fullname'] = member.fullname
                request.session['tr_team_id'] = member.team_id
                request.session['tr_id'] = member.id
                return render(request, 'tr_sec.html', {'member': member})
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation_id=des2.id).exists():
                member = user_registration.objects.get(
                email=request.POST['email'], password=request.POST['password'])
                request.session['te_designation_id'] = member.designation_id
                request.session['te_fullname'] = member.fullname
                request.session['te_id'] = member.id
                request.session['te_team_id'] = member.team_id
                return render(request, 'traineesec.html', {'member': member})
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation_id=des3.id).exists():
                member = user_registration.objects.get(
                email=request.POST['email'], password=request.POST['password'])
                request.session['acc_designation_id'] = member.designation_id
                request.session['acc_fullname'] = member.fullname
                request.session['acc_id'] = member.id
                return render(request, 'accountsec.html', {'member': member})
        elif request.method == 'POST':
            username = request.POST.get('email', None)
            password = request.POST.get('password', None)                    
            user = authenticate(username=username, password=password)
            if user:
                  login(request, user)
                  return redirect('Admin_Dashboard')
        else:
                context = {'msg': 'Invalid username or password'}
                return render(request, 'Tlogin.html', context)
    return render(request,'Tlogin.html')       



    
        # if request.method == 'POST':
        #     username = request.POST.get('email', None)
        #     password = request.POST.get('password', None)
        #     user = authenticate(email=username, password=password)
        #     if user:
        #         login(request, user)
        #         return redirect('Admin_Dashboard')
        #     else:
        #           context = {'msg': 'Invalid username or password'}
        #           return render(request, 'login.html',context)
        # if request.method == 'POST':
        #     email  = request.POST['email']
        #     password = request.POST['password']
        #     user = authenticate(email=email, password=password)
        #     if user is not None:
        #             request.session['SAdm_id'] = user.id
        #             return redirect('Admin_Dashboard')

        #     else:
        #         context = {'msg': 'Invalid username or password'}
        #         return render(request, 'login.html', context)
    

def manager_logout(request):
    if 'm_id' in request.session:  
        request.session.flush()
        return redirect('Tlogin')
    else:
        return redirect('Tlogin') 

def Admin_logout(request):
    auth.logout(request)
    return redirect('Tlogin')

def index(request):
    return render(request,'software_training/training/index.html')
    
def Trainings(request):
    return render(request,'software_training/training/training.html')

#******************Manager*****************************

def Manager_Dashboard(request):
    if 'm_id' in request.session:
        
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
       
        mem = user_registration.objects.filter(id=m_id)
        
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=m_id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'software_training/training/manager/manager_Dashboard.html', {'mem': mem ,'labels': labels,'data': data,})
    else:
        return redirect('/')
    
def Manager_trainer(request):
    return render(request,'software_training/training/manager/manager_trainer.html')

def manager_team(request):
    return render(request,'software_training/training/manager/manager_team.html')

def manager_current_team(request):
    return render(request,'software_training/training/manager/manager_current_team.html')

def Manager_current_task(request):
    return render(request,'software_training/training/manager/manager_current_task.html')

def manager_current_assigned(request):
    return render(request,'software_training/training/manager/manager_current_assigned.html')

def manager_current_trainees(request):
    return render(request,'software_training/training/manager/manager_current_trainees.html')

def manager_current_empdetails(request):
    return render(request,'software_training/training/manager/manager_current_empdetails.html')

def manager_current_attendance(request):
    return render(request,'software_training/training/manager/manager_current_attendance.html')

def manager_current_attendance_list(request):
    return render(request,'software_training/training/manager/manager_current_attendance_list.html')

def manager_current_task_list(request):
    return render(request,'software_training/training/manager/manager_current_task_list.html')

def manager_current_task_details(request):
    return render(request,'software_training/training/manager/manager_current_task_details.html')
    
def manager_previous_team(request):
    return render(request,'software_training/training/manager/manager_previous_team.html')

def Manager_previous_task(request):
    return render(request,'software_training/training/manager/Manager_previous_task.html')

def manager_previous_assigned(request):
    return render(request,'software_training/training/manager/manager_previous_assigned.html')

def manager_previous_trainees(request):
    return render(request,'software_training/training/manager/manager_previous_trainees.html')

def manager_previous_empdetails(request):
    return render(request,'software_training/training/manager/manager_previous_empdetails.html')

def manager_previous_attendance(request):
    return render(request,'software_training/training/manager/manager_previous_attendance.html')

def manager_previous_attendance_list(request):
    return render(request,'software_training/training/manager/manager_previous_attendance_list.html')

def manager_previous_task_list(request):
    return render(request,'software_training/training/manager/manager_previous_task_list.html')

def manager_previous_task_details(request):
    return render(request,'software_training/training/manager/manager_previous_task_details.html')

def manager_trainee(request):
    return render(request,'software_training/training/manager/manager_trainee.html')

def Manager_trainees_details(request):
    return render(request,'software_training/training/manager/Manager_trainees_details.html')

def Manager_trainees_attendance(request):
    return render(request,'software_training/training/manager/Manager_trainees_attendance.html')

def Manager_reported_issues(request):
    return render(request,'software_training/training/manager/manager_reported_issues.html')

def manager_trainerreportissue(request):
    return render(request,'software_training/training/manager/manager_trainerreportissue.html')

def manager_trainer_unsolvedissue(request):
    return render(request,'software_training/training/manager/manager_trainer_unsolvedissue.html')

def manager_trainer_solvedissue(request):
    return render(request,'software_training/training/manager/manager_trainer_solvedissue.html')

def manager_traineereportissue(request):
    return render(request,'software_training/training/manager/manager_traineereportissue.html')

def manager_trainee_unsolvedissue(request):
    return render(request,'software_training/training/manager/manager_trainee_unsolvedissue.html')

def manager_trainee_solvedissue(request):
    return render(request,'software_training/training/manager/manager_trainee_solvedissue.html')

def manager_report_issue(request):
    return render(request,'software_training/training/manager/manager_report_issue.html')

def manager_reported_issue(request):
    return render(request,'software_training/training/manager/manager_reported_issue.html')

def manager_trainee_solvedissue(request):
    return render(request,'software_training/training/manager/manager_trainee_solvedissue.html')

def Manager_attendance(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            m_id = "dummy"
        mem = user_registration.objects.all()
        
        return render(request, 'software_training/training/manager/manager_attendance.html',{'mem':mem})
    else:
        return redirect('/')
    # return render(request,'software_training/training/manager/manager_attendance.html',{'mem':mem}) 

def manager_trainee_attendance(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']        
        else:
            m_id = "dummy"
        mem = user_registration.objects.all()
    
        des = designation.objects.get(designation_name='trainee')
        vars = user_registration.objects.filter(designation_id=des.id)
        
        return render(request, 'software_training/training/manager/manager_trainee_attendance.html',{'mem':mem, 'vars':vars})
    else:
        return redirect('/')
    

def manager_trainer_attendance(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']        
        else:
            m_id = "dummy"
        mem = user_registration.objects.all()
    
        des = designation.objects.get(designation_name='trainer')
        vars = user_registration.objects.filter(designation_id=des.id)
        
        return render(request, 'software_training/training/manager/manager_trainer_attendance.html',{'mem':mem, 'vars':vars})
    else:
        return redirect('/')
    

def manager_trainer_attendance_table(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']        
        else:
            m_id = "dummy"
        mem = user_registration.objects.all() 
        if request.method == 'POST':
            start=request.POST['startdate']
            end=request.POST['enddate']
            user = request.POST['trainer']
            attend=attendance.objects.filter(attendance_date__gte=start,attendance_date__lte=end,attendance_user_id=user)
        return render(request, 'software_training/training/manager/manager_trainer_attendance_table.html',{'mem':mem,'vars':attend})
    else:
        return redirect('/')
    

def manager_trainee_attendance_table(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']        
        else:
            m_id = "dummy"
        mem = user_registration.objects.all() 
        if request.method == 'POST':
            start=request.POST['startdate']
            end=request.POST['enddate']
            user = request.POST['trainee']
            attend=attendance.objects.filter(attendance_date__gte=start,attendance_date__lte=end,attendance_user_id=user)
        return render(request, 'software_training/training/manager/manager_trainee_attendance_table.html',{'mem':mem,'vars':attend})
    else:
        return redirect('/')
   
def manager_applyleave(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            m_id = "dummy"
        mem = user_registration.objects.all()
        
    
        return render(request, 'software_training/training/manager/manager_applyleave.html',{'mem':mem})
    else:
        return redirect('/')

    

def manager_applyleavsub(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id'] 
        if request.session.has_key('m_designation_id'):
            m_designation_id = request.session['m_designation_id']        
        else:
            m_id = "dummy"
        mem = user_registration.objects.all()
        # des = designation.objects.get(designation_name='admin')
        des1 = designation.objects.get(designation_name='manager')
        cut = user_registration.objects.get(id=m_id)
        # ree = user_registration.objects.get(designation_id=des.id)
        # ree1 = user_registration.objects.get(designation_id=m_designation_id)
        if request.method == 'POST':
            vars = leave()
            vars.leave_from_date = request.POST['from']
            vars.leave_to_date = request.POST['to']
            vars.leave_reason = request.POST['reason']
            vars.leave_status = request.POST['haful']
            vars.leave_leaveapproved_status = 0
            vars.leave_user = cut
            vars.leave_designation_id = des1.id
     
            vars.save()
            return redirect('manager_applyleave')
    
    
        return render(request,'software_training/training/manager/manager_applyleavsub.html', {'mem': mem})
    else:
        return redirect('/')
    # return render(request,'software_training/training/manager/manager_applyleavsub.html')

def manager_requestedleave(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            usernametm = request.session['m_id']
        if request.session.has_key('m_fullname'):
            usernametm1 = request.session['m_fullname']
        
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation_name='manager')
        print(des.id)
        cut = leave.objects.filter(leave_designation_id=des.id).order_by('-id')
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'software_training/training/manager/manager_requestedleave.html', context)

    else:
        return redirect('/')



def manager_trainer_leave(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            m_id = "dummy"
        mem = user_registration.objects.all()
        
    
        return render(request, 'software_training/training/manager/manager_trainer_leave.html',{'mem':mem})
    else:
        return redirect('/')


def manager_trainers_leavelist(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        if request.session.has_key('m_fullname'):
            m_fullname = request.session['m_fullname']
        
        else:
            usernametm1 = "dummy"
        
    
        mem = user_registration.objects.filter(designation_id=m_id) .filter(fullname=m_fullname)
        des = designation.objects.get(designation_name='trainer')
        cut = leave.objects.filter(leave_designation_id=des.id).filter(leave_leaveapproved_status=0).order_by('-id')
        
        
        
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'software_training/training/manager/manager_trainers_leavelist.html', context)
    else:
        return redirect('/')

def approvedstatus(request,id):
    a=leave.objects.get(id=id)
    a.leave_leaveapproved_status=1
    a.save()
    return redirect('manager_trainers_leavelist')

def Leave_rejected(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        if request.session.has_key('m_fullname'):
            m_fullname = request.session['m_fullname']
        
        else:
            m_fullname = "dummy"
    
        # mem = user_registration.objects.filter(
        #     designation_id=m_id) .filter(fullname=m_fullname)
        # id = request.GET.get(id=id)
        vars = leave.objects.get(id=id) 
        if request.method == 'POST':
                  
            
            vars.leave_rejected_reason = request.POST['review']
            
            vars.leave_leaveapproved_status = 2
           
            
            vars.save()
        return redirect('manager_trainers_leavelist')
    else:
        return redirect('/')
   
def manager_trainer_leavestatus(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        if request.session.has_key('m_fullname'):
            m_fullname = request.session['m_fullname']
        if request.session.has_key('m_designation_id'):
            m_designation_id = request.session['m_designation_id']
        mem = user_registration.objects.filter(
            designation_id=m_id) .filter(fullname=m_fullname)
    
        des = designation.objects.get(designation_name='trainer')
        n = leave.objects.filter(leave_designation_id=des.id).order_by('-id')
        
    
        return render(request, 'software_training/training/manager/manager_trainer_leavestatus.html', {'mem': mem ,'n': n})
    else:
        return redirect('/')

    

def manager_trainee_leave(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            m_id = "dummy"
        mem = user_registration.objects.all()
        
    
        return render(request, 'software_training/training/manager/manager_trainee_leave.html',{'mem':mem})
    else:
        return redirect('/')
    

def manager_trainee_leavelist(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        if request.session.has_key('m_fullname'):
            m_fullname = request.session['m_fullname']
        if request.session.has_key('m_designation_id'):
            m_designation_id = request.session['m_designation_id']
        else:
            m_fullname = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=m_id) .filter(fullname=m_fullname)
        # .objects.filter(reported_to_id=usernametm2)
        des = designation.objects.get(designation_name='trainee')
       
        cut = leave.objects.filter(leave_designation_id=des.id).filter(leave_leaveapproved_status=0).order_by('-id')
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'software_training/training/manager/manager_trainee_leavelist.html', context)

    else:
        return redirect('/')
    
def approvedstatus_trainee(request,id):
    a=leave.objects.get(id=id)
    a.leave_leaveapproved_status=1
    a.save()
    return redirect('manager_trainee_leavelist')

def Leave_rejected_trainee(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        if request.session.has_key('m_fullname'):
            m_fullname = request.session['m_fullname']
        
        else:
            m_fullname = "dummy"
    
        # mem = user_registration.objects.filter(
        #     designation_id=m_id) .filter(fullname=m_fullname)
        # id = request.GET.get(id=id)
        vars = leave.objects.get(id=id) 
        if request.method == 'POST':
                  
            
            vars.leave_rejected_reason = request.POST['review']
            
            vars.leave_leaveapproved_status = 2
           
            
            vars.save()
        return redirect('manager_trainee_leavelist')
    else:
        return redirect('/')
    

def manager_trainee_leavestatus(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        if request.session.has_key('m_fullname'):
            m_fullname = request.session['m_fullname']
        if request.session.has_key('m_designation_id'):
            m_designation_id = request.session['m_designation_id']
        mem = user_registration.objects.filter(
            designation_id=m_id) .filter(fullname=m_fullname)
    
        des = designation.objects.get(designation_name='trainer')
        n = leave.objects.filter(leave_designation_id=des.id).order_by('-id')
        
    
        return render(request, 'software_training/training/manager/manager_trainee_leavestatus.html', {'mem': mem ,'n': n})
    else:
        return redirect('/')


def manager_new_team(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        if request.session.has_key('m_fullname'):
            m_fullname = request.session['m_fullname']
        if request.session.has_key('m_designation_id'):
            m_designation_id = request.session['m_designation_id']
        else:
            m_id = "dummy"
        mem = user_registration.objects.filter(designation_id=m_designation_id) .filter(fullname=m_fullname)
        var = create_team.objects.all().order_by('-id')
        des = designation.objects.get(designation_name='trainer')
        var1 = user_registration.objects.filter(designation_id=des.id)
        return render(request, 'software_training/training/manager/manager_new_team.html', {'mem': mem, 'var': var, 'var1': var1})
    else:
        return redirect('/')
    
def manager_new_teamcreate(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_fullname'):
            m_fullname = request.session['m_fullname']
        if request.session.has_key('m_designation_id'):
            m_designation_id = request.session['m_designation_id']
        else:
            m_fullname = "dummy"
        mem = user_registration.objects.filter(designation_id=m_designation_id) .filter(fullname=m_fullname)
        des = designation.objects.get(designation_name='trainer')
        var = user_registration.objects.filter(designation_id=des.id)
        return render(request, 'software_training/training/manager/manager_new_teamcreate.html', {'mem': mem, 'var': var})
    else:
        return redirect('/')
def manager_newteamadd(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_fullname'):
            m_fullname = request.session['m_fullname']
        if request.session.has_key('m_designation_id'):
            m_designation_id = request.session['m_designation_id']
        else:
            m_fullname = "dummy"
    if request.method == 'POST':
        team = request.POST['team']
        trainer = request.POST.get('trainer')
        try:
            des = designation.objects.get(designation_name='trainer')
            var = user_registration.objects.filter(designation_id=des.id)
            user= create_team.objects.get(create_team_name=team)
            mem = user_registration.objects.filter(designation_id=m_designation_id) .filter(fullname=m_fullname)
            context = {'msg': 'Team already exists!!!....  Try another name','mem':mem,'var': var}
            return render(request, 'software_training/training/manager/manager_new_teamcreate.html',context)
        except :
            user= create_team(create_team_name=team, create_team_trainer=trainer, create_team_progress=0)
            user.save()
            return redirect('manager_new_team')

def manager_teamupdate(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_fullname'):
            m_fullname = request.session['m_fullname']
        if request.session.has_key('m_designation_id'):
            m_designation_id = request.session['m_designation_id']
        else:
            m_fullname = "dummy"
    if request.method == 'POST':
        # tid = request.GET.get('tid')
        abc = create_team.objects.get(id=id)
        abc.create_team_name = request.POST.get('teams')
        abc.create_team_trainer = request.POST.get('trainer')
        abc.save()
        return redirect('manager_new_team')
    else:
        pass


def manager_teamdelete(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_fullname'):
            m_fullname = request.session['m_fullname']
        if request.session.has_key('m_designation_id'):
            m_designation_id = request.session['m_designation_id']
        else:
            m_fullname = "dummy"

    # tid = request.GET.get('tid')
    var = create_team.objects.get(id=id)
    
    var.delete()
    return redirect("manager_new_team")



def manager_submit(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_fullname'):
            m_fullname = request.session['m_fullname']
        if request.session.has_key('m_designation_id'):
            m_designation_id = request.session['m_designation_id']
        else:
            m_fullname = "dummy"
   
    if request.method == 'POST':
        var1 = create_team.objects.get(id=id)
        var1.create_team_status = 1        
        var1.save()
    return redirect("manager_new_team")
    
def manager_newtrainees(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_fullname'):
            m_fullname = request.session['m_fullname']
        if request.session.has_key('m_designation_id'):
            m_designation_id = request.session['m_designation_id']
        else:
            m_fullname = "dummy"
        mem = user_registration.objects.filter(
            designation_id=m_designation_id).filter(fullname=m_fullname)
        des = course.objects.all()
        
        team = create_team.objects.all()
        mem1 = designation.objects.get(designation_name="trainee")
        memm = user_registration.objects.filter(designation_id=mem1).order_by('-id')
        return render(request, 'software_training/training/manager/manager_newtrainees.html', {'mem': mem, 'memm': memm, 'des': des,  'team': team})
    else:
        return redirect('/')

def manager_newtraineeesteam(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_fullname'):
            m_fullname = request.session['m_fullname']
        if request.session.has_key('m_designation_id'):
            m_designation_id = request.session['m_designation_id']
        else:
            m_fullname = "dummy"
        mem = user_registration.objects.filter(
            designation_id=m_designation_id).filter(fullname=m_fullname)
        # tid = request.GET.get('tid')
        register = user_registration()
        des = designation.objects.all()        
        team = create_team.objects.all()
        mem1 = designation.objects.get(designation_name="trainee")
        memm = user_registration.objects.filter(designation_id=mem1)
        
        if request.method == 'POST':
            register = user_registration.objects.get(id=id)
            
            register.team =create_team.objects.get(id=int(request.POST['team']))
            register.course =course.objects.get(id=int(request.POST['cou']))
            register.save()
            return redirect('manager_newtrainees')
        return render(request, 'software_training/training/manager/manager_newtrainees.html', {'memm': memm, 'des': des, 'team': team, })
    else:
        return redirect('/')

def manager_changepassword(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
       
        mem = user_registration.objects.filter(id=m_id)
    
        if request.method == 'POST':
            abc = user_registration.objects.get(id=m_id)
    
            oldps = request.POST['currentPassword']
            newps = request.POST['newPassword']
            cmps = request.POST.get('confirmPassword')
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'software_training/training/manager/manager_Dashboard.html', {'mem': mem})
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')
    
            return render(request, 'software_training/training/manager/manager_changepassword.html', {'mem': mem})
    
        return render(request, 'software_training/training/manager/manager_changepassword.html', {'mem': mem})

    else:
        return redirect('/')

def manager_accountedit(request):
    if 'm_id' in request.session:
        
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        
        mem = user_registration.objects.filter(id=m_id)
    
    
        return render(request, 'software_training/training/manager/manager_accountedit.html', {'mem': mem})
    else:
        return redirect('/')
def manager_imagechange(request,id):
  
    if request.method == 'POST':
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filename']
        
        abc.save()
        return redirect('manager_accountedit')
    return render(request, 'software_training/training/manager/manager_accountedit.html')

def manager_paymentlist(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        if request.session.has_key('m_fullname'):
            m_fullname = request.session['m_fullname']
        if request.session.has_key('m_designation_id'):
            m_designation_id = request.session['m_designation_id']
        else:
            m_id = "dummy"
        mem = user_registration.objects.filter(designation_id=m_designation_id).filter(fullname=m_fullname).filter(id=m_id)
        acc=acntspayslip.objects.filter(acntspayslip_user_id=m_id).all().order_by('-id')
        
        return render(request, 'software_training/training/manager/manager_paymentlist.html', {'acc': acc,'mem':mem})
    else:
        return redirect('/')

def manager_payment_viewslip(request,id,tid):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        if request.session.has_key('m_fullname'):
            m_fullname = request.session['m_fullname']
        if request.session.has_key('m_designation_id'):
            m_designation_id = request.session['m_designation_id']
        else:
            m_id = "dummy"
        # tid = request.GET.get('tid')
        # id = request.GET.get('id')
        mem= user_registration.objects.filter(designation_id=m_designation_id).filter(fullname=m_fullname).filter(id=m_id)
        user = user_registration.objects.get(id=tid)
        acc = acntspayslip.objects.get(id=id)
        names = acntspayslip.objects.all()
        
        
        return render(request, 'software_training/training/manager/manager_payment_viewslip.html', {'mem': mem,'user':user,'acc':acc})
    else:
        return redirect('/')

def manager_payment_print(request,id,tid):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        if request.session.has_key('m_fullname'):
            m_fullname = request.session['m_fullname']
        if request.session.has_key('m_designation_id'):
            m_designation_id = request.session['m_designation_id']
        else:
            m_id = "dummy"
        mem = user_registration.objects.filter(designation_id=m_designation_id).filter(fullname=m_fullname).filter(id=m_id)
        z = user_registration.objects.filter(id=m_id)   
        user = user_registration.objects.get(id=tid)
        acc = acntspayslip.objects.get(id=id)
        
        
        return render(request, 'software_training/training/manager/manager_payment_print.html', {'z': z,'user':user,'acc':acc,'mem': mem})
    else:
        return redirect('/')

    
#******************Trainer*****************************

def trainer_dashboard(request):
    return render(request,'software_training/training/trainer/trainer_dashboard.html')

def trainer_applyleave(request):
    return render(request, 'software_training/training/trainer/trainer_applyleave.html')

def trainer_applyleave_form(request):
    return render(request, 'software_training/training/trainer/trainer_applyleave_form.html')

def trainer_traineesleave_table(request):
    return render(request, 'software_training/training/trainer/trainer_traineesleave_table.html')

def trainer_reportissue(request):
    return render(request, 'software_training/training/trainer/trainer_reportissue.html')

def trainer_reportissue_form(request):
    return render(request, 'software_training/training/trainer/trainer_reportissue_form.html')

def trainer_reportedissue_table(request):
    return render(request, 'software_training/training/trainer/trainer_reportedissue_table.html')

def trainer_topic(request):
    return render(request,'software_training/training/trainer/trainer_topic.html')

def trainer_addtopic(request):
    return render(request,'software_training/training/trainer/trainer_addtopic.html')

def trainer_viewtopic(request):
    return render(request,'software_training/training/trainer/trainer_viewtopic.html')

def trainer_attendance(request):
    return render(request,'software_training/training/trainer/trainer_attendance.html')

def trainer_attendance_trainees(request):
    return render(request,'software_training/training/trainer/trainer_attendance_trainees.html')

def trainer_attendance_trainer(request):
    return render(request, 'software_training/training/trainer/trainer_attendance_trainer.html')

def trainer_attendance_trainer_viewattendance(request):
    return render(request,'software_training/training/trainer/trainer_attendance_trainer_viewattendance.html')

def trainer_attendance_trainer_viewattendancelist(request):
    return render(request,'software_training/training/trainer/trainer_attendance_trainer_viewattendancelist.html')

def trainer_team(request):
    return render(request,'software_training/training/trainer/trainer_team.html')

def trainer_currentteam(request):
    return render(request,'software_training/training/trainer/trainer_current_team_list.html')

def trainer_currenttrainees(request):
    return render(request, 'software_training/training/trainer/trainer_current_trainees_list.html')

def trainer_currenttraineesdetails(request):
    return render(request,'software_training/training/trainer/trainer_current_tainees_details.html')

def trainer_currentattentable(request):
    return render(request,'software_training/training/trainer/trainer_current_atten_table.html')

def trainer_currentperform(request):
    return render(request,'software_training/training/trainer/trainer_current_perform.html')

def trainer_currentattenadd(request):
    return render(request,'software_training/training/trainer/trainer_current_atten_add.html')

def trainer_previousteam(request):
    return render(request,'software_training/training/trainer/trainer_previous_team_list.html')

def trainer_previoustrainees(request):
    return render(request,'software_training/training/trainer/trainer_previous_trainess_list.html')

def trainer_previoustraineesdetails(request):
    return render(request, 'software_training/training/trainer/trainer_previous_trainees_details.html')

def trainer_previousattentable(request):
    return render(request,'software_training/training/trainer/trainer_previous_atten_table.html')

def trainer_previousperfomtable(request):
    return render(request,'software_training/training/trainer/trainer_previous_performtable.html')

def trainer_current_attendance(request):
    return render(request,'software_training/training/trainer/trainer_current_attendance.html')

def trainer_Task(request) :
    return render(request,'software_training/training/trainer/trainer_task.html')
    
def trainer_teamlistpage(request) :
    return render(request,'software_training/training/trainer/trainer_teamlist.html')
    
def trainer_taskpage(request) :
    return render(request, 'software_training/training/trainer/trainer_taskfor.html')
    
def trainer_givetask(request) :
    return render(request, 'software_training/training/trainer/trainer_givetask.html')
    
def trainer_taskgivenpage(request) :
    return render(request,'software_training/training/trainer/trainer_taskgiven.html')
    
def trainer_taska(request):
    return render(request, 'software_training/training/trainer/trainer_taska.html')

def trainer_task_completed_teamlist(request):
    return render(request, 'software_training/training/trainer/trainer_task_completed_teamlist.html')

def trainer_task_completed_team_tasklist(request):
    return render(request, 'software_training/training/trainer/trainer_task_completed_team_tasklist.html')

def trainer_task_previous_teamlist(request):
    return render(request, 'software_training/training/trainer/trainer_task_previous_teamlist.html')

def trainer_task_previous_team_tasklist(request):
    return render(request, 'software_training/training/trainer/trainer_task_previous_team_tasklist.html')

def trainer_trainees(request):
    return render(request, 'software_training/training/trainer/trainer_trainees.html')

def trainer_previous_trainees(request):
    return render(request,'software_training/training/trainer/trainer_previous_trainees.html')

def trainer_current_trainees(request):
    return render(request,'software_training/training/trainer/trainer_current_trainees.html')

def trainer_myreportissue_table(request):
    return render(request, 'software_training/training/trainer/trainer_myreportissue_table.html')

def trainer_current_attendance_view(request):
    return render(request,'software_training/training/trainer/trainer_current_attendance_view.html')

def trainer_attendance_trainees_viewattendance(request):
    return render(request,'software_training/training/trainer/trainer_attendance_trainees_viewattendance.html')

def trainer_attendance_trainees_viewattendancelist(request):
    return render(request,'software_training/training/trainer/trainer_attendance_trainees_viewattendancelist.html')

def trainer_attendance_trainees_addattendance(request):
    return render(request,'software_training/training/trainer/trainer_attendance_trainees_addattendance.html')
    
#******************  Trainee  *****************************

def trainee_dashboard_trainee(request):
    return render(request,'software_training/training/trainee/trainee_dashboard_trainee.html')
    
def trainee_task(request):
   return render(request,'software_training/training/trainee/trainee_task.html')   

def trainee_task_list(request):
    return render(request,'software_training/training/trainee/trainee_task_list.html')

def trainee_task_details(request):
    return render(request,'software_training/training/trainee/trainee_task_details.html')

def trainee_completed_taskList(request):
   return render(request,'software_training/training/trainee/trainee_completed_taskList.html')

def trainee_completedTask(request):
    return render(request,'software_training/training/trainee/trainee_completedTask.html')

def trainee_completed_details(request):
    return render(request,'software_training/training/trainee/trainee_completed_details.html')

def trainee_topic(request):
    return render(request, 'software_training/training/trainee/trainee_topic.html')

def trainee_currentTopic(request):
    return render(request, 'software_training/training/trainee/trainee_currentTopic.html')
    
def trainee_previousTopic(request):
    return render(request, 'software_training/training/trainee/trainee_previousTopic.html')

def trainee_reported_issue(request):
    return render(request, 'software_training/training/trainee/trainee_reported_issue.html')
   
def trainee_report_reported(request):
    return render(request, 'software_training/training/trainee/trainee_report_reported.html')
  
def trainee_report_issue(request):
    return render(request, 'software_training/training/trainee/trainee_report_issue.html')

def trainee_applyleave_form(request):
    return render(request, 'software_training/training/trainee/trainee_applyleave_form.html')  

def trainee_applyleave_card(request):
     return render(request, 'software_training/training/trainee/trainee_applyleave_cards.html')
    
def trainee_appliedleave(request):
     return render(request, 'software_training/training/trainee/trainee_appliedleave.html')
    
def Attendance(request):
   return render(request,'software_training/training/trainee/trainees_attendance.html')
    
def trainees_attendance_viewattendance(request):
    return render(request,'software_training/training/trainee/trainees_attendance_viewattendance.html')
 
def trainees_attendance_viewattendancelist(request):
   return render(request,'software_training/training/trainee/trainees_attendance_viewattendancelist.html')
   
def trainee_payment(request):
   return render(request,'software_training/training/trainee/trainee_payment.html')
   
def trainee_payment_addpayment(request):
   return render(request,'software_training/training/trainee/trainee_payment_addpayment.html')
  
def trainee_payment_viewpayment(request):
     return render(request,'software_training/training/trainee/trainee_payment_viewpayment.html')

#****************************  Admin- view  ********************************

def Admin_Dashboard(request):
    mem = User.objects.all()
    z = designation.objects.get(designation_name='Admin')
    var = user_registration.objects.filter(designation_id=z.id)

    vars = user_registration.objects.all()
    return render(request, 'software_training/training/admin/admin_Dashboard.html', {'mem': mem, 'var':var, 'vars':vars, })

def Admin_categories(request):
    return render(request,'software_training/training/admin/admin_categories.html') 

def Admin_emp_categories(request):
    return render(request,'software_training/training/admin/admin_emp_categories.html')  

def Admin_courses(request):
    return render(request,'software_training/training/admin/admin_courses.html')

def Admin_emp_course_list(request):
    return render(request,'software_training/training/admin/admin_emp_course_list.html')

def Admin_emp_course_details(request):
    return render(request,'software_training/training/admin/admin_emp_course_details.html')

def Admin_emp_profile(request):
    return render(request,'software_training/training/admin/admin_emp_profile.html')

def Admin_emp_attendance(request):
    return render(request,'software_training/training/admin/admin_emp_attendance.html')

def Admin_emp_attendance_show(request):
    return render(request,'software_training/training/admin/admin_emp_attendance_show.html')

def Admin_task(request):
    return render(request,'software_training/training/admin/admin_task.html')

def Admin_givetask(request):
    return render(request,'software_training/training/admin/admin_givetask.html')

def Admin_current_task(request):
    return render(request,'software_training/training/admin/admin_current_task.html')

def Admin_previous_task(request):
    return render(request,'software_training/training/admin/admin_previous_task.html')

def Admin_registration_details(request):
    return render(request,'software_training/training/admin/admin_registration_details.html')  

def Admin_attendance(request):
    return render(request,'software_training/training/admin/admin_attendance.html') 

def Admin_attendance_show(request):
    return render(request,'software_training/training/admin/admin_attendance_show.html')

def Admin_reported_issues(request):
    return render(request,'software_training/training/admin/admin_reported_issues.html') 

def Admin_emp_reported_detail(request):
    return render(request,'software_training/training/admin/admin_emp_reported_detail.html')

def Admin_emp_reported_issue_show(request):
    return render(request,'software_training/training/admin/admin_emp_reported_issue_show.html')

def Admin_manager_reported_detail(request):
    return render(request,'software_training/training/admin/admin_manager_reported_detail.html')

def Admin_manager_reported_issue_show(request):
    return render(request,'software_training/training/admin/admin_manager_reported_issue_show.html')

def Admin_add(request):
    return render(request,'software_training/training/admin/admin_add.html') 

def Admin_addcategories(request):
    return render(request,'software_training/training/admin/admin_addcategories.html') 

def Admin_categorieslist(request):
    return render(request,'software_training/training/admin/admin_categorieslist.html') 

def Admin_addcourse(request):
    return render(request,'software_training/training/admin/admin_addcourse.html') 

def Admin_addnewcourse(request):
    return render(request,'software_training/training/admin/admin_addnewcourse.html') 

def Admin_addnewcategories(request):
    return render(request,'software_training/training/admin/admin_addnewcategories.html') 

def Admin_courselist(request):
    return render(request,'software_training/training/admin/admin_courselist.html') 

def Admin_coursedetails(request):
    return render(request,'software_training/training/admin/admin_coursedetails.html') 

#******************accounts****************

def accounts_Dashboard(request):
    return render(request, 'software_training/training/account/accounts_Dashboard.html')

def accounts_registration_details(request):
    return render(request, 'software_training/training/account/accounts_registration_details.html')

def accounts_payment_details(request):
    return render(request, 'software_training/training/account/account_payment_details.html')

def accounts_payment_salary(request):
    return render(request, 'software_training/training/account/account_payment_salary.html')

def accounts_payment_view(request):
    return render(request, 'software_training/training/account/account_payment_view.html')

def accounts_report_issue(request):
    return render(request, 'software_training/training/account/account_report_issue.html')

def accounts_report(request):
    return render(request, 'software_training/training/account/account_report.html')

def accounts_reported_issue(request):
    return render(request, 'software_training/training/account/account_reported_issue.html')

def accounts_acntpay(request):
    return render(request, 'software_training/training/account/accounts_acntpay.html')

def accounts_employee(request):
    return render(request, 'software_training/training/account/accounts_employee.html')

def accounts_emp_dep(request):
    return render(request, 'software_training/training/account/accounts_emp_dep.html')

def accounts_emp_list(request):
    return render(request, 'software_training/training/account/accounts_emp_list.html')

def accounts_emp_details(request):
    return render(request, 'software_training/training/account/accounts_emp_details.html')

def accounts_add_bank_acnt(request):
    return render(request, 'software_training/training/account/accounts_add_bank_acnt.html')

def accounts_bank_acnt_details(request):
    return render(request, 'software_training/training/account/accounts_bank_acnt_details.html')

def accounts_salary_details(request):
    return render(request, 'software_training/training/account/accounts_salary_details.html')

def accounts_expenses(request):
    return render(request, 'software_training/training/account/accounts_expenses.html')

def accounts_expenses_viewEdit(request):
    return render(request, 'software_training/training/account/accounts_expenses_viewEdit.html')

def accounts_expenses_viewEdit_Update(request):
    return render(request, 'software_training/training/account/accounts_expenses_viewEdit.html')

def accounts_expense_newTransaction(request):
    return render(request, 'software_training/training/account/accounts_expense_newTransaction.html')

def accounts_paydetails(request):
    return render(request, 'software_training/training/account/accounts_paydetails.html')

def accounts_print(request):
    return render(request, 'software_training/training/account/accounts_print.html')

def accounts_payment(request):
    return render(request,'software_training/training/account/accounts_payment.html')

def accounts_payment_dep(request):
    return render(request, 'software_training/training/account/accounts_payment_dep.html')

def accounts_payment_list(request):
    return render(request, 'software_training/training/account/accounts_payment_list.html')

def accounts_payment_details(request):
    return render(request, 'software_training/training/account/accounts_payment_details.html')

def accounts_payment_detail_list(request):
    return render(request, 'software_training/training/account/accounts_payment_detail_list.html')

def accounts_payslip(request):
    return render(request, 'software_training/training/account/accounts_payslip.html')