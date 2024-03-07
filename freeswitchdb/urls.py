#
#    DjangoPBX
#
#    MIT License
#
#    Copyright (c) 2016 - 2024 Adrian Fretwell <adrian@djangopbx.com>
#
#    Permission is hereby granted, free of charge, to any person obtaining a copy
#    of this software and associated documentation files (the "Software"), to deal
#    in the Software without restriction, including without limitation the rights
#    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#    copies of the Software, and to permit persons to whom the Software is
#    furnished to do so, subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be included in all
#    copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#    SOFTWARE.
#
#    Contributor(s):
#    Adrian Fretwell <adrian@djangopbx.com>
#

from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'fs_agents', views.AgentsViewSet)
router.register(r'fs_aliases', views.AliasesViewSet)
router.register(r'fs_calls', views.CallsViewSet)
router.register(r'fs_channels', views.ChannelsViewSet)
router.register(r'fs_complete', views.CompleteViewSet)
router.register(r'fs_dbdata', views.DbDataViewSet)
router.register(r'fs_fifobridge', views.FifoBridgeViewSet)
router.register(r'fs_fifocallers', views.FifoCallersViewSet)
router.register(r'fs_fifooutbound', views.FifoOutboundViewSet)
router.register(r'fs_groupdata', views.GroupDataViewSet)
router.register(r'fs_interfaces', views.InterfacesViewSet)
router.register(r'fs_limitdata', views.LimitDataViewSet)
router.register(r'fs_members', views.MembersViewSet)
router.register(r'fs_nat', views.NatViewSet)
router.register(r'fs_recovery', views.RecoveryViewSet)
router.register(r'fs_registrations', views.RegistrationsViewSet)
router.register(r'fs_sipautentication', views.SipAuthenticationViewSet)
router.register(r'fs_sipdialogs', views.SipDialogsViewSet)
router.register(r'fs_sippresence', views.SipPresenceViewSet)
router.register(r'fs_sipregistrations', views.SipRegistrationsViewSet)
router.register(r'fs_sipsharedappearancedialogs', views.SipSharedAppearanceDialogsViewSet)
router.register(r'fs_sipsharedappearancesubscriptions', views.SipSharedAppearanceSubscriptionsViewSet)
router.register(r'fs_sipsubscriptions', views.SipSubscriptionsViewSet)
router.register(r'fs_tasks', views.TasksViewSet)
router.register(r'fs_tiers', views.TiersViewSet)
router.register(r'fs_voicemailmsgs', views.VoicemailMsgsViewSet)
router.register(r'fs_voicemailprefs', views.VoicemailPrefsViewSet)

urlpatterns = [
]
