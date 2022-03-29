# from django.contrib import admin
# from django.conf.urls import url
# from django.urls import include
# from django.conf import settings

# from manage import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.views.static import serve

from django.contrib import admin
from django.urls import path
from django.conf.urls import  include
from django.urls import re_path, include
# from infox_site import views
# from manage import views
from mapp import views
#from softwareapp import re_path
# from trainingapp import urls

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    # url(r'^mapp/', include('mapp.urls')),
    # url(r'^$', views.toapp),
    # re_path(r'^softwareapp/', include('softwareapp.urls')),    

    re_path(r'^$', views.home),
    re_path(r'^enquiry', views.enquiry),
    re_path(r'^Sector_SoftwareIndustries', views.software),
    re_path(r'^Sector_Training', views.training),
    re_path(r'^Sector_Autodealers', views.autodealers),
    re_path(r'^Sector_Banks', views.bank),
    re_path(r'^Sector_Consultancies', views.consultancies),
    re_path(r'^Sector_EmploymentAgency', views.employement),
    re_path(r'^Sector_Malls&Shopping', views.malls),
    re_path(r'^Sector_Motorshowroom', views.motor_showroom),
    re_path(r'^Sector_Rental&Leashing', views.rentals),
    re_path(r'^Sector_ServiceStations', views.service_stations),
    re_path(r'^Sector_GroceryStores', views.grocery),
    re_path(r'^Sector_Supermarket', views.supermarkets),
    re_path(r'^Sector_Restaurants&Hotels', views.restaurant),
    re_path(r'^Sector_FinancialInstitutions', views.financialinstitution),
    re_path(r'^Sector_Telecommunications&Media', views.telecommunication),
    re_path(r'^Sector_ArchitecturalCompany', views.architecture),
    re_path(r'^Sector_CateringSupply', views.catering),
    re_path(r'^Sector_EducationalInstitutions', views.educational),
    re_path(r'^Sector_ConstructionCompany', views.construction),
    re_path(r'^Sector_ElectricalProductCompany', views.electrical),
    re_path(r'^Sector_EntertainmentSections', views.entertainment),
    re_path(r'^Sector_EventPlanning', views.event),
    re_path(r'^Sector_Hospitals', views.hospital),
    re_path(r'^Sector_Jewelleries', views.jewel),
    re_path(r'^Sector_ManufacturingCompanies', views.manufacturing),
    re_path(r'^Sector_MarketingAgency', views.marketing),
    re_path(r'^Sector_Realestate', views.realestate),
    re_path(r'^Sector_Storage', views.storage),
    re_path(r'^Sector_TransportationCompany', views.transportation),
    re_path(r'^Sector_Travel&TourismPlanning', views.travel),
    re_path(r'^Addcon', views.Addcon),
    re_path(r'^Addenq', views.Addenq),
    re_path(r'^msearch', views.msearch),
    re_path(r'^esearch', views.esearch),
    re_path(r'^admin', views.admin),
    re_path(r'^registration', views.registration),
    re_path(r'^register', views.register),
    re_path(r'^login', views.login),
    re_path(r'^logout', views.logout),
    re_path(r'^dash', views.dash),
    re_path(r'^mdash', views.mdash),
    re_path(r'^edash', views.edash),
    re_path(r'^Erp', views.erp),
    re_path(r'^Accounting&Financial', views.accounting),
    re_path(r'^TreasuryManagement', views.treasury),
    re_path(r'^ARB&RManagement', views.receivable),
    re_path(r'^Supply-Manufacturing', views.supply),
    re_path(r'^Enterprise_AssetManagement', views.asset),
    re_path(r'^PLC_Management', views.plc),
    re_path(r'^CustomerData', views.customer),
    re_path(r'^Supply-Marketing', views.shop),
    re_path(r'^Supply-Commerce', views.commerce),
    re_path(r'^Supply-Sales', views.sales),
    re_path(r'^Supply-Serve', views.serve),
    re_path(r'^EmployeeExperienceManagement', views.exp1),
    re_path(r'^CoreHR&Payroll', views.core),
    re_path(r'^TalentManagement', views.talent),
    re_path(r'^Analytics&Workforce', views.workforce),
    re_path(r'^Finance_banking', views.finbank),
    re_path(r'^Insurance', views.insurance),
    re_path(r'^AgriBussiness', views.agri),
    re_path(r'^Customer_Product', views.cpro),
    re_path(r'Fashion', views.fashion),
    re_path(r'LifeScience', views.life),
    re_path(r'Retail', views.retail),
    re_path(r'WholesaleDistribution', views.wholesale),
    re_path(r'Media', views.media),
    re_path(r'Engineering,Construction&Operation', views.engineering),
    re_path(r'Sports&Entertainment', views.sports),
    re_path(r'ServiceTelecommunication', views.tele2),
    
    re_path(r'^softwareapp/', include('softwareapp.urls')),
    # url(r'^trainingapp/', include('trainingapp.urls')),    
    
    
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)