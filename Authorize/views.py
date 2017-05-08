from django.shortcuts import render
from django.http import HttpResponse
from Authorize.models import Role,UserRole
from django.core.urlresolvers import reverse,reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect
from HotelApp.models import Proposal
from Authorize.models import Partners

# Displays the appropriate dashboard for each type of user.
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
#
def displayAdminDash(request):
    return render(request,'Authorize/admindash.html')
# Show partners , Accept proposals and remove partners.
def showProposals(request):
    proposal_list = Proposal.objects.all()
    context = {'proposals': proposal_list}
    return render(request, 'Authorize/proposals.html', context)
def showPartners(request):
    partner_list = Partners.objects.all()
    context = {'partners': partner_list}
    return render(request, 'Authorize/partners.html', context)
def removePartner(request,id):
    partner = Partners.objects.get(id = id)
    userid = partner.userID
    role = UserRole.objects.get(user = userid)
    role.roleid = 3
    role.save()
    partner.delete()

    link = reverse('Authorize:showpartners')
    return HttpResponseRedirect(link)
    #Accepts a partner and inputs them into the partners database aswell
    #as changing the role id to reflect this .
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
def declineProposals(request,id):
    proposal = Proposal.objects.get(id = id)
    proposal.delete()
    link = reverse('Authorize:showproposals')
    return HttpResponseRedirect(link)

#  A user can check the status of their application
def checkstatus(request):
    proposal_list = Proposal.objects.filter(user = request.user)
    context = {'proposal': proposal_list}
    return render(request, 'Authorize/checkstatus.html', context)
