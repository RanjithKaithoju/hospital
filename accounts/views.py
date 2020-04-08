from django.shortcuts import render

from .models import PatientInfo
# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request,'index.html')
    else:

        p=PatientInfo(date=request.POST.get('date'),clinic=request.POST.get('clinic'),lname=request.POST.get('lname'),fname=request.POST.get('fname'),mname=request.POST.get('mname'),
                    address=request.POST.get('address'),city=request.POST.get('city'),state=request.POST.get('state'),zip=request.POST.get('zip'),phone=request.POST.get('phone'),ssecurity=request.POST.get('ssecurity'),
                    dob=request.POST.get('dob'),age=request.POST.get('age'),gender=request.POST.get('gender'),mstatus=request.POST.get('mstatus'),dlicense=request.POST.get('dlicense'),
                    wphone=request.POST.get('wphone'),ena=request.POST.get('ena'),email=request.POST.get('email'),eca=request.POST.get('eca'),ecd=request.POST.get('ecd'),heardby=request.POST.get('heardby'),
                    refferedby=request.POST.get('refferedby'))
        p=p.save()

        # g=GuanratorInfo(PatientInfo.objects.id,relationgtop=request.POST.get('optradio'),lname=request.POST.get('glname'),fname=request.POST.get('gfname'),mname=request.POST.get('gmname'),
        #                 address=request.POST.get('gaddress'),city=request.POST.get('gcity'),state=request.POST.get('gstate'),zip=request.POST.get('gzip'),phone=request.POST.get('gphone'),ssecurity=request.POST.get('gssecurity'),
        #                 dob=request.POST.get('gdob'), age=request.POST.get('gage'), gender=request.POST.get('ggender'),ena=request.POST.get('gena')
        #                 )
        # g.save()
        return render(request,'index.html')