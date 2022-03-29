from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'software_training/index.html')

def software(request):
    return render(request,'software_training/software.html')

def employees(request):
    return render(request,'software_training/employees.html')

#***********************developer**************************************************
def developer_Dashboard(request):
    return render(request,'software_training/software/developer/developer_Dashboard.html')

def developer_task(request):
    return render(request,'software_training/software/developer/developer_task.html')

def developer_task_form(request):
    return render(request,'software_training/software/developer/developer_task_form.html')

def developer_project_table(request):
    return render(request,'software_training/software/developer/developer_project_table.html')

def developer_attendance(request):
    return render(request,'software_training/software/developer/developer_attendance.html')

def developer_attendance_list(request):
    return render(request,'software_training/software/developer/developer_attendance_list.html')

def developer_reportedissue(request):
    return render(request,'software_training/software/developer/developer_reportedissue.html')

def developer_reportedissues(request):
    return render(request,'software_training/software/developer/developer_reportedissues.html')

def developer_reportissue(request):
    return render(request,'software_training/software/developer/developer_reportissue.html')

def developer_applyleave(request):
    return render(request,'software_training/software/developer/developer_applyleave.html')

def developer_apply_leave(request):
    return render(request,'software_training/software/developer/developer_apply_leave.html')  

def developer_apply_leave_list(request):
    return render(request,'software_training/software/developer/developer_apply_leave_list.html')

def developer_account_settings(request):
    return render(request,'software_training/software/developer/developer_account_settings.html')

def developer_change_password(request):
    return render(request,'software_training/software/developer/developer_change_password.html')

#****************** Project Manager ******************************************
    
def pm_Dashboard(request):
    return render(request, 'software_training/software/pm/pm_Dashboard.html')

def pm_projects(request):
    return render(request, 'software_training/software/pm/pm_projects.html')

def pm_upcomingProject(request):
    return render(request, 'software_training/software/pm/pm_upcomingProject.html')

def pm_currentProject(request):
    return render(request, 'software_training/software/pm/pm_currentProject.html')

def pm_completedProject(request):
    return render(request, 'software_training/software/pm/pm_completedProject.html')

def pm_createProject(request):
    return render(request, 'software_training/software/pm/pm_createProject.html')

def pm_newProj_status(request):
    return render(request, 'software_training/software/pm/pm_newProj_status.html')

def pm_assignProject(request):
    return render(request, 'software_training/software/pm/pm_assignProject.html')

def pm_newProject(request):
    return render(request, 'software_training/software/pm/pm_newProject.html')

def pm_acceptedProject(request):
    return render(request, 'software_training/software/pm/pm_acceptedProject.html')

def pm_rejectedProject(request):
    return render(request, 'software_training/software/pm/pm_rejectedProject.html')

def pm_currentProjectFirst(request):
    return render(request, 'software_training/software/pm/pm_currentProjectFirst.html')

def pm_currentprojectTeam(request):
    return render(request, 'software_training/software/pm/pm_currentprojectTeam.html')

def pm_currentprojectTeamList(request):
    return render(request, 'software_training/software/pm/pm_currentprojectTeamList.html')

def pm_completedFirst(request):
    return render(request, 'software_training/software/pm/pm_completedFirst.html')

def pm_completeProj_Team(request):
    return render(request, 'software_training/software/pm/pm_completeProj_Team.html')

def pm_completeProj_Teamlist(request):
    return render(request, 'software_training/software/pm/pm_completeProj_Teamlist.html')

def pm_employee(request):
    return render(request, 'software_training/software/pm/pm_employee.html')

def pm_employee_TL(request):
    return render(request, 'software_training/software/pm/pm_employee_TL.html')

def pm_TL_Team(request):
    return render(request, 'software_training/software/pm/pm_TL_Team.html')

def pm_TL_Team_profile(request):
    return render(request, 'software_training/software/pm/pm_TL_Team_profile.html')

def pm_TL_Team_involved(request):
    return render(request, 'software_training/software/pm/pm_TL_Team_involved.html')

def pm_TL_Team_attendence(request):
    return render(request, 'software_training/software/pm/pm_TL_Team_attendence.html')

def pm_TL_Team_viewAttendence(request):
    return render(request, 'software_training/software/pm/pm_TL_Team_viewAttendence.html')

def pm_employee_developer(request):
    return render(request, 'software_training/software/pm/pm_employee_developer.html')

def pm_emp_developers_dashboard(request):
    return render(request, 'software_training/software/pm/pm_emp_developers_dashboard.html')

def pm_developer_team(request):
    return render(request, 'software_training/software/pm/pm_developer_team.html')

def pm_tl_dashboard(request):
    return render(request, 'software_training/software/pm/pm_tl_dashboard.html')

def pm_reportedIssues(request):
    return render(request, 'software_training/software/pm/pm_reportedIssues.html')

def pm_report_reportedIssue(request):
    return render(request, 'software_training/software/pm/pm_report_reportedIssue.html')

def pm_reportedIssue_action(request):
    return render(request, 'software_training/software/pm/pm_reportedIssue_action.html')

def pm_report_issue(request):
    return render(request, 'software_training/software/pm/pm_report_issue.html')

def pm_tl_reported_issues(request):
    return render(request, 'software_training/software/pm/pm_tl_reported_issues.html')

def pm_tl_issuesVerified(request):
    return render(request, 'software_training/software/pm/pm_tl_issuesVerified.html')

def pm_applyLeave(request):
    return render(request, 'software_training/software/pm/pm_applyLeave.html')

def pm_applyleave_Form(request):
    return render(request, 'software_training/software/pm/pm_applyleave_Form.html')

def pm_requested_leave(request):
    return render(request, 'software_training/software/pm/pm_requested_leave.html')

def pm_Attendence(request):
    return render(request, 'software_training/software/pm/pm_Attendence.html')

def pm_attendenceList(request):
    return render(request, 'software_training/software/pm/pm_attendenceList.html')

def pm_TL_attendence(request):
    return render(request, 'software_training/software/pm/pm_TL_attendence.html')

def pm_TL_attendencelist(request):
    return render(request, 'software_training/software/pm/pm_TL_attendencelist.html')

def pm_developer_attendence(request):
    return render(request, 'software_training/software/pm/pm_developer_attendence.html')

def pm_developer_attendencelist(request):
    return render(request, 'software_training/software/pm/pm_developer_attendencelist.html')

#***************************TESTER ***************************************

def tester_dashboard(request):
    return render(request,'software_training/software/tester/tester_dashboard.html') 

def tester_task(request):
    return render(request, 'software_training/software/tester/tester_task.html')

def tester_taskassigned(request):
    return render(request, 'software_training/software/tester/tester_taskassigned.html')

def tester_taskpending(request):
    return render(request, 'software_training/software/tester/tester_taskpending.html')

def tester_projects(request):
    return render(request, 'software_training/software/tester/tester_projects.html')

def tester_projectdetails(request):
    return render(request, 'software_training/software/tester/tester_projectdetails.html')
    
#****** **************** Manager *****************************

def manager_Dashboard(request):
    return render(request,'software_training/software/manager/manager_Dashboard.html')


def manager_dept(request):
    return render(request,'software_training/software/manager/manager_dept.html') 

def manager_emp_dept(request):
    return render(request,'software_training/software/manager/manager_emp_dept.html')   

def manager_projects(request):
    return render(request,'software_training/software/manager/manager_projects.html')

def manager_proj_list(request):
    return render(request,'software_training/software/manager/manager_proj_list.html')

def manager_proj_details(request):
    return render(request,'software_training/software/manager/manager_proj_details.html')

def manager_proj_manager(request):
    return render(request,'software_training/software/manager/manager_proj_manager.html')

def manager_proj_manager1(request):
    return render(request,'software_training/software/manager/manager_proj_manager1.html')

def manager_proj_manager2(request):
    return render(request,'software_training/software/manager/manager_proj_manager2.html')

def manager_completed_proj(request):
    return render(request,'software_training/software/manager/manager_completed_proj.html')

def manager_completed_proj_details(request):
    return render (request,'software_training/software/manager/manager_completed_proj_details.html')

def manager_completed_proj_manager(request):
    return render(request, 'software_training/software/manager/manager_completed_proj_manager.html')

def manager_completed_proj_manager_list(request):
    return render(request,'software_training/software/manager/manager_completed_proj_manager_list.html')

def manager_completed_proj_manager_tl(request):
    return render(request,'software_training/software/manager/manager_completed_proj_manager_tl.html')

def manager_emp_dept_list(request):
    return render(request,'software_training/software/manager/manager_emp_dept_list.html')

def manager_emp_dept_details(request):
    return render(request,'software_training/software/manager/manager_emp_dept_details.html')

def manager_emp_profile(request):
    return render(request,'software_training/software/manager/manager_emp_profile.html')

def manager_emp_involved_projects(request):
    return render(request,'software_training/software/manager/manager_emp_involved_projects.html')
    
def manager_emp_attendance(request):
    return render(request,'software_training/software/manager/manager_emp_attendance.html')

def manager_emp_attendance_show(request):
    return render(request,'software_training/software/manager/manager_emp_attendance_show.html')

def manager_upcoming(request):
    return render(request,'software_training/software/manager/manager_upcoming.html')

def manager_createproject(request):
    return render(request,'software_training/software/manager/manager_createproject.html')

def manager_upcoming_project(request):
    return render(request,'software_training/software/manager/manager_upcoming_project.html')

def manager_give_project(request):
    return render(request,'software_training/software/manager/manager_give_project.html')

def manager_accepted_project(request):
    return render(request,'software_training/software/manager/manager_accepted_project.html')

def manager_rejected_project(request):
    return render(request,'software_training/software/manager/manager_rejected_project.html')

def manager_task(request):
    return render(request,'software_training/software/manager/manager_task.html')

def manager_givetask(request):
    return render(request,'software_training/software/manager/manager_givetask.html')

def manager_current_task(request):
    return render(request,'software_training/software/manager/manager_current_task.html')

def manager_previous_task(request):
    return render(request,'software_training/software/manager/manager_previous_task.html')

def manager_registration_details(request):
    return render(request,'software_training/software/manager/manager_registration_details.html')  

def manager_new_department(request):
    return render(request,'software_training/software/manager/manager_new_department.html') 

def manager_create_department(request):
    return render(request,'software_training/software/manager/manager_create_department.html')

def manager_attendance(request):
    return render(request,'software_training/software/manager/manager_attendance.html') 

def manager_attendance_show(request):
    return render(request,'software_training/software/manager/manager_attendance_show.html')

def manager_reported_issues(request):
    return render(request,'software_training/software/manager/manager_reported_issues.html') 

def manager_issues(request):
    return render(request,'software_training/software/manager/manager_issues.html')

def manager_issues_form(request):
    return render(request,'software_training/software/manager/manager_issues_form.html')

def manager_myissues(request):
    return render(request,'software_training/software/manager/manager_myissues.html')

def manager_reported_detail(request):
    return render(request,'software_training/software/manager/manager_reported_detail.html')

def manager_reported_issue_show(request):
    return render(request,'software_training/software/manager/manager_reported_issue_show.html')

#***************************Admin ***************************************

def admin_Dashboard(request):
    return render(request,'software_training/software/admin/Admin_Dashboard.html')

def admin_dept(request):
    return render(request,'software_training/software/admin/Admin_dept.html') 

def admin_emp_dept(request):
    return render(request,'software_training/software/admin/Admin_emp_dept.html')  

def admin_projects(request):
    return render(request,'software_training/software/admin/Admin_projects.html')

def admin_proj_list(request):
    return render(request,'software_training/software/admin/Admin_proj_list.html')

def admin_proj_details(request):
    return render(request,'software_training/software/admin/Admin_proj_details.html')

def admin_proj_manager(request):
    return render(request,'software_training/software/admin/Admin_proj_manager.html')

def admin_proj_manager1(request):
    return render(request,'software_training/software/admin/Admin_proj_manager1.html')

def admin_proj_manager2(request):
    return render(request,'software_training/software/admin/Admin_proj_manager2.html')

def admin_completed_proj(request):
    return render(request,'software_training/software/admin/Admin_completed_proj.html')

def admin_completed_proj_details(request):
    return render (request,'software_training/software/admin/Admin_completed_proj_details.html')


def admin_completed_proj_manager(request):
    return render(request, 'software_training/software/admin/Admin_completed_proj_manager.html')

def admin_completed_proj_manager_list(request):
    return render(request,'software_training/software/admin/Admin_completed_proj_manager_list.html')

def admin_completed_proj_manager_tl(request):
    return render(request,'software_training/software/admin/Admin_completed_proj_manager_tl.html')

def admin_emp_dept_list(request):
    return render(request,'software_training/software/admin/Admin_emp_dept_list.html')

def admin_emp_dept_details(request):
    return render(request,'software_training/software/admin/Admin_emp_dept_details.html')

def admin_emp_profile(request):
    return render(request,'software_training/software/admin/Admin_emp_profile.html')

def admin_emp_involved_projects(request):
    return render(request,'software_training/software/admin/Admin_emp_involved_projects.html')

def admin_emp_attendance(request):
    return render(request,'software_training/software/admin/Admin_emp_attendance.html')

def admin_emp_attendance_show(request):
    return render(request,'software_training/software/admin/Admin_emp_attendance_show.html')

def admin_upcoming(request):
    return render(request,'software_training/software/admin/Admin_upcoming.html')

def admin_createproject(request):
    return render(request,'software_training/software/admin/Admin_createproject.html')

def admin_upcoming_project(request):
    return render(request,'software_training/software/admin/Admin_upcoming_project.html')

def admin_give_project(request):
    return render(request,'software_training/software/admin/Admin_give_project.html')

def admin_accepted_project(request):
    return render(request,'software_training/software/admin/Admin_accepted_project.html')

def admin_rejected_project(request):
    return render(request,'software_training/software/admin/Admin_rejected_project.html')

def admin_task(request):
    return render(request,'software_training/software/admin/Admin_task.html')

def admin_givetask(request):
    return render(request,'software_training/software/admin/Admin_givetask.html')

def admin_current_task(request):
    return render(request,'software_training/software/admin/Admin_current_task.html')

def admin_previous_task(request):
    return render(request,'software_training/software/admin/Admin_previous_task.html')

def admin_registration_details(request):
    return render(request,'software_training/software/admin/Admin_registration_details.html')  

def admin_new_department(request):
    return render(request,'software_training/software/admin/Admin_new_department.html') 

def admin_create_department(request):
    return render(request,'software_training/software/admin/Admin_create_department.html')

def admin_attendance(request):
    return render(request,'software_training/software/admin/Admin_attendance.html') 

def admin_attendance_show(request):
    return render(request,'software_training/software/admin/Admin_attendance_show.html')

def admin_reported_issues(request):
    return render(request,'software_training/software/admin/Admin_reported_issues.html') 

def admin_emp_reported_detail(request):
    return render(request,'software_training/software/admin/Admin_emp_reported_detail.html')

def admin_emp_reported_issue_show(request):
    return render(request,'software_training/software/admin/Admin_emp_reported_issue_show.html')

def admin_manager_reported_detail(request):
    return render(request,'software_training/software/admin/Admin_manager_reported_detail.html')

def admin_manager_reported_issue_show(request):
    return render(request,'software_training/software/admin/Admin_manager_reported_issue_show.html')
    #*******************************TL********************************


def index_tl(request):
    return render(request,'software_training/software/tl/tlHomepage.html')
    
def tlproject(request):
    return render(request,'software_training/software/tl/tlProject.html')

def tlproject_task(request):
    return render(request,'software_training/software/tl/tlproject_tasks.html')

def tl_project_table(request):
    return render(request,'software_training/software/tl/tlProject_table.html')

def tl_project_splittask(request):
    return render(request,'software_training/software/tl/tl_project_splittask.html')

def tl_projecttask_status(request):
    return render(request,'software_training/software/tl/tl_projecttask_status.html')

def tl_addtask(request):
    return render(request,'software_training/software/tl/tl_addtask.html')

def tl_attendance_sort(request):
    return render(request,'software_training/software/tl/tl_attendance_sort.html')

def attendance_tl(request):
    return render(request,'software_training/software/tl/tlattendance.html')

def tl_reportissue(request):
    return render(request,'software_training/software/tl/tl_reportissue.html')

def tl_reportissue_table(request):
    return render(request,'software_training/software/tl/tl_reportissue_table.html')

def tl_reportissue_submit(request):
    return render(request,'software_training/software/tl/tl_reportedissue_submit.html')

def tl_reportissue_register(request):
    return render(request,'software_training/software/tl/tl_reportissue_reg.html')

def tl_reportissue_success(request):
    return render(request,'software_training/software/tl/tl_reportissue_success.html')

def tl_developreport(request):
    return render(request,'software_training/software/tl/tl_developreport.html')

def tl_developer_view(request):
    return render(request,'software_training/software/tl/tl_developer_view.html')

def tl_task(request):
    return render(request,'software_training/software/tl/tl_task.html')

def tl_taskpending(request):
    return render(request,'software_training/software/tl/tl_taskpending.html')

def tl_tasksubmit(request):
    return render(request,'software_training/software/tl/tl_tasksubmit.html')

def tl_leave(request):
    return render(request,'software_training/software/tl/tl_leave.html')

def tl_leaverequest(request):
    return render(request,'software_training/software/tl/tl_leave_request.html')

def tl_leaverequest_view(request):
    return render(request,'software_training/software/tl/tl_leavereq_view.html')


#**********************project*************************

def project_details(request):
    return render(request,'software_training/software/project/project_details.html')

#*************************client**************************8

def client_card(request):
    return render(request,'software_training/software/client/client_card.html')

def client_details(request):
    return render(request,'software_training/software/client/client_details.html')

#****************** hr module ******************************************

def hr_Dashboard(request):
    return render(request,'software_training/software/hr/hr_Dashboard.html')

def base_hr(request):
     return render(request,'software_training/software/hr/base_hr.html')

def hr_view_attendance(request):
     return render(request,'software_training/software/hr/hr_view_attendance.html')

def hr_view_attendance_list(request):
     return render(request,'software_training/software/hr/hr_view_attendance_list.html')

def hr_vacancy_list(request):
     return render(request,'software_training/software/hr/hr_vacancy_list.html')

def hr_vacancy_details(request):
     return render(request,'software_training/software/hr/hr_vacancy_details.html')

#****************** Digital Marketing *************************************


def digitalmarketing_card(request):
    return render(request,'software_training/software/digitalmarketing/digitalmarketing_card.html')

def marketingtl_Dashboard(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_Dashboard.html')

def datacollector_Dashboard(request):
    return render(request,'software_training/software/digitalmarketing/datacollector/datacollector_Dashboard.html')

def marketingexecutive_Dashboard(request):
    return render(request,'software_training/software/digitalmarketing/marketingexecutive/marketingexecutive_Dashboard.html')

def datacollector_attendance(request):
    return render(request,'software_training/software/digitalmarketing/datacollector/datacollector_attendance.html')

def datacollector_attendance_list(request):
    return render(request,'software_training/software/digitalmarketing/datacollector/datacollector_attendance_list.html')

def datacollector_reportedissue(request):
    return render(request,'software_training/software/digitalmarketing/datacollector/datacollector_reportedissue.html')

def datacollector_reportissue_form(request):
    return render(request,'software_training/software/digitalmarketing/datacollector/datacollector_reportissue_form.html')

def datacollector_reportedissue_table(request):
    return render(request,'software_training/software/digitalmarketing/datacollector/datacollector_reportedissue_table.html')

def marketingexecutive_attendance(request):
    return render(request,'software_training/software/digitalmarketing/marketingexecutive/marketingexecutive_attendance.html')

def marketingexecutive_attendance_list(request):
    return render(request,'software_training/software/digitalmarketing/marketingexecutive/marketingexecutive_attendance_list.html')

def marketingexecutive_reportedissue(request):
    return render(request,'software_training/software/digitalmarketing/marketingexecutive/marketingexecutive_reportedissue.html')

def marketingexecutive_reportissue_form(request):
    return render(request,'software_training/software/digitalmarketing/marketingexecutive/marketingexecutive_reportissue_form.html')

def marketingexecutive_reportedissue_table(request):
    return render(request,'software_training/software/digitalmarketing/marketingexecutive/marketingexecutive_reportedissue_table.html')

def marketingtl_reportedissue(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_reportedissue.html')

def marketingtl_reportissue_form(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_reportissue_form.html')

def marketingtl_reportedissue_table(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_reportedissue_table.html')

def marketingtl_attendance(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_attendance.html')

def marketingtl_attendance_datacollector(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_attendance_datacollector.html')

def marketingtl_attendance_executive(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_attendance_executive.html')

def marketingtl_attendance_executiveview(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_attendance_executiveview.html')

def marketingtl_attendance_datacollectorview(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_attendance_datacollectorview.html')

def marketingtl_attendance_executiveview_list(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_attendance_executiverview_list.html')

def marketingtl_attendance_datacollectorview_list(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_attendance_datacollectorview_list.html')

def marketingtl_attendance_datacollectoradd(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_attendance_datacollectoradd.html')

def marketingtl_attendance_executiveadd(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_attendance_executiveadd.html')

def marketingtl_attendance_view(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_attendance_view.html')

def marketingtl_attendance_view_list(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_attendance_view_list.html')

def marketingtl_mytask(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_mytask.html')

def marketingexecutive_mytask(request):
    return render(request,'software_training/software/digitalmarketing/marketingexecutive/marketingexecutive_mytask.html')

def marketingtl_sharedtask(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_sharedtask.html')

def datacollector_mytask(request):
    return render(request,'software_training/software/digitalmarketing/datacollector/datacollector_mytask.html')

def marketingtl_products_table(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_products_table.html')

def marketingtl_recruitments_table(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_recruitments_table.html')

def marketingtl_products_details(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_products_details.html')

def marketingtl_recruitments_details(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_recruitments_details.html')

def datacollector_products_table(request):
    return render(request,'software_training/software/digitalmarketing/datacollector/datacollector_products_table.html')

def datacollector_recruitments_table(request):
    return render(request,'software_training/software/digitalmarketing/datacollector/datacollector_recruitments_table.html')

def datacollector_products_details(request):
    return render(request,'software_training/software/digitalmarketing/datacollector/datacollector_products_details.html')

def datacollector_recruitments_details(request):
    return render(request,'software_training/software/digitalmarketing/datacollector/datacollector_recruitments_details.html')

def marketingexecutive_products_table(request):
    return render(request,'software_training/software/digitalmarketing/marketingexecutive/marketingexecutive_products_table.html')

def marketingexecutive_recruitments_table(request):
    return render(request,'software_training/software/digitalmarketing/marketingexecutive/marketingexecutive_recruitments_table.html')

def marketingexecutive_products_details(request):
    return render(request,'software_training/software/digitalmarketing/marketingexecutive/marketingexecutive_products_details.html')

def marketingexecutive_recruitments_details(request):
    return render(request,'software_training/software/digitalmarketing/marketingexecutive/marketingexecutive_recruitments_details.html')

def marketingexecutive_products_data(request):
    return render(request,'software_training/software/digitalmarketing/marketingexecutive/marketingexecutive_products_data.html')

def marketingexecutive_recruitments_data(request):
    return render(request,'software_training/software/digitalmarketing/marketingexecutive/marketingexecutive_recruitments_data.html')

def datacollector_products_collectdata(request):
    return render(request,'software_training/software/digitalmarketing/datacollector/datacollector_products_collectdata.html')

def datacollector_recruitments_collectdata(request):
    return render(request,'software_training/software/digitalmarketing/datacollector/datacollector_recruitments_collectdata.html')

def marketingtl_shtask_products_table(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_shtask_products_table.html')

def marketingtl_shtask_recruitments_table(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_shtask_recruitments_table.html')

def marketingtl_shtask_products_details(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_shtask_products_details.html')

def marketingtl_shtask_recruitments_details(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_shtask_recruitments_details.html')

def marketingtl_products_data(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_products_data.html')

def marketingtl_recruitments_data(request):
    return render(request,'software_training/software/digitalmarketing/marketingtl/marketingtl_recruitments_data.html')

 

######################### TESTER #################################

def tester_dashboard(request):
    return render(request,'software_training/software/tester/tester_dashboard.html')  
    

def tester_task(request):
    return render(request, 'software_training/software/tester/tester_task.html')


def tester_taskassigned(request):
    return render(request, 'software_training/software/tester/tester_taskassigned.html')


def tester_taskpending(request):
    return render(request, 'software_training/software/tester/tester_taskpending.html')
    

def tester_projects(request):
    return render(request, 'software_training/software/tester/tester_projects.html')
    

def tester_projectdetails(request):
    return render(request, 'software_training/software/tester/tester_projectdetails.html')

