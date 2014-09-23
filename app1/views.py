from django.contrib import messages
from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
# from jtweet.forms import SignInForm
# Create your views here.

def index(request):
    return render_to_response('index.html',
        {},
                              context_instance=RequestContext(request))


def followers(request):
    user = request.user
    return render_to_response('followers.html',
                              {'followers': user.followers.all()},
                              context_instance=RequestContext(request))


    # def sign_in(request):
    # data = None
    #     if request.method == 'POST':
    #         data = request.POST
    #     form = SignInForm(data=data)
    #     if form.is_valid():
    #         user = form.user
    #         login(request, user)
    #         messages.add_message(request, messages.INFO, _('Welcome %s' % user.username))
    #         return HttpResponseRedirect(reverse('index'))
    #     return render_to_response('jtweet/sign-in.html',
    #                               {'form': form},
    #                               context_instance=RequestContext(request))