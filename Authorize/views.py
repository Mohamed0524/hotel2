from django.shortcuts import render
from django.http import HttpResponse
from Authorize.models import Role,UserRole
from django.core.urlresolvers import reverse,reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect
from HotelApp.models import Proposal
from Authorize.models import Partners


def displayDash(request):
    user = request.user
    if user.userrole.roleid == 3:
        link = reverse('HotelApp:userDash')
        return HttpResponseRedirect(link)
    elif user.userrole.roleid == 4:
            link = reverse('ManageHotels:home')
            return HttpResponseRedirect(link)
    elif user.userrole.roleid == 2:
        link = reverse('Authorize:admindash')
        return HttpResponseRedirect(link)

def displayAdminDash(request):
    return render(request,'Authorize/admindash.html')
def showProposals(request):
    proposal_list = Proposal.objects.all()
    context = {'proposals': proposal_list}
    return render(request, 'Authorize/proposals.html', context)

def acceptProposals(request,id):
    proposal = Proposal.objects.get(id = id)
    user = proposal.user
    newpartner = Partners()
    newpartner.userID = user
    newpartner.CompanyName = proposal.CompanyName
    newpartner.CompanyEmail = proposal.CompanyEmail
    newpartner.HQAddress = proposal.HQAddress
    newpartner.save()
    updaterole = UserRole.objects.get(user = user)
    updaterole.roleid = 4
    updaterole.save()
    proposal.delete()
    link = reverse('Authorize:showproposals')
    return HttpResponseRedirect(link)
