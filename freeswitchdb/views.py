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

from django.views import View
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend


from pbx.restpermissions import (
    AdminApiAccessPermission
)
from .models import (
    Agents, Aliases, Calls, Channels, Complete, DbData, FifoBridge, FifoCallers,
    FifoOutbound, GroupData, Interfaces, LimitData, Members, Nat, Recovery,
    Registrations, SipAuthentication, SipDialogs, SipPresence, SipRegistrations,
    SipSharedAppearanceDialogs, SipSharedAppearanceSubscriptions,
    SipSubscriptions, Tasks, Tiers, VoicemailMsgs, VoicemailPrefs
)
from .serializers import (
    AgentsSerializer, AliasesSerializer, CallsSerializer, ChannelsSerializer,
    CompleteSerializer, DbDataSerializer, FifoBridgeSerializer, FifoCallersSerializer,
    FifoOutboundSerializer, GroupDataSerializer, InterfacesSerializer,
    LimitDataSerializer, MembersSerializer, NatSerializer, RecoverySerializer,
    RegistrationsSerializer, SipAuthenticationSerializer, SipDialogsSerializer,
    SipPresenceSerializer, SipRegistrationsSerializer,
    SipSharedAppearanceDialogsSerializer, SipSharedAppearanceSubscriptionsSerializer,
    SipSubscriptionsSerializer, TasksSerializer, TiersSerializer,
    VoicemailMsgsSerializer, VoicemailPrefsSerializer
)


class AgentsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows to be viewed.
    """
    queryset = Agents.objects.all().order_by('name').using('freeswitch')
    serializer_class = AgentsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['state', 'status']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class AliasesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Aliases to be viewed.
    """
    queryset = Aliases.objects.all().order_by('alias_uuid', 'alias').using('freeswitch')
    serializer_class = AliasesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hostname']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class CallsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Calls to be viewed.
    """
    queryset = Calls.objects.all().order_by('call_created_epoch').using('freeswitch')
    serializer_class = CallsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hostname']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class ChannelsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Channels to be viewed.
    """
    queryset = Channels.objects.all().order_by('channel_uuid').using('freeswitch')
    serializer_class = ChannelsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['direction', 'state', 'hostname', 'secure']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class CompleteViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Complete to be viewed.
    """
    queryset = Complete.objects.all().order_by('complete_uuid').using('freeswitch')
    serializer_class = CompleteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hostname']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class DbDataViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows DbData to be viewed.
    """
    queryset = DbData.objects.all().order_by('db_data_uuid').using('freeswitch')
    serializer_class = DbDataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hostname', 'realm']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class FifoBridgeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows FifoBridge to be viewed.
    """
    queryset = FifoBridge.objects.all().order_by('fifo_name').using('freeswitch')
    serializer_class = FifoBridgeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['caller_uuid']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class FifoCallersViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows FifoCallers to be viewed.
    """
    queryset = FifoCallers.objects.all().order_by('fifo_name').using('freeswitch')
    serializer_class = FifoCallersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['uuid']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class FifoOutboundViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows FifoOutbound to be viewed.
    """
    queryset = FifoOutbound.objects.all().order_by('fifo_outbound_uuid').using('freeswitch')
    serializer_class = FifoOutboundSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hostname']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class GroupDataViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows GroupData to be viewed.
    """
    queryset = GroupData.objects.all().order_by('group_data_uuid').using('freeswitch')
    serializer_class = GroupDataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hostname']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class InterfacesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Interfaces to be viewed.
    """
    queryset = Interfaces.objects.all().order_by('interface_uuid').using('freeswitch')
    serializer_class = InterfacesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hostname']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class LimitDataViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Limit to be viewed.
    """
    queryset = LimitData.objects.all().order_by('limit_data_uuid').using('freeswitch')
    serializer_class = LimitDataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hostname', 'realm']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class MembersViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Members to be viewed.
    """
    queryset = Members.objects.all().order_by('member_uuid').using('freeswitch')
    serializer_class = MembersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['queue', 'state', 'base_score']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class NatViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Nat to be viewed.
    """
    queryset = Nat.objects.all().order_by('nat_uuid').using('freeswitch')
    serializer_class = NatSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hostname', 'proto']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class RecoveryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Recovery to be viewed.
    """
    queryset = Recovery.objects.all().order_by('uuid').using('freeswitch')
    serializer_class = RecoverySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hostname', 'profile_name']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class RegistrationsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Registrations to be viewed.
    """
    queryset = Registrations.objects.all().order_by('registration_uuid').using('freeswitch')
    serializer_class = RegistrationsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hostname', 'realm', 'network_proto']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class SipAuthenticationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows SipAuthentication to be viewed.
    """
    queryset = SipAuthentication.objects.all().order_by('sip_authentication_uuid').using('freeswitch')
    serializer_class = SipAuthenticationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hostname', 'profile_name']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class SipDialogsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows SipDialogs to be viewed.
    """
    queryset = SipDialogs.objects.all().order_by('sip_dialog_uuid').using('freeswitch')
    serializer_class = SipDialogsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hostname', 'profile_name', 'state', 'direction']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class SipPresenceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows SipPresence to be viewed.
    """
    queryset = SipPresence.objects.all().order_by('sip_presence_uuid').using('freeswitch')
    serializer_class = SipPresenceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hostname', 'profile_name', 'status']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class SipRegistrationsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows SipRegistrations to be viewed.
    """
    queryset = SipRegistrations.objects.all().order_by('sip_registration_uuid').using('freeswitch')
    serializer_class = SipRegistrationsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hostname', 'profile_name', 'status', 'sip_realm']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class SipSharedAppearanceDialogsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows SipSharedAppearanceDialogs to be viewed.
    """
    queryset = SipSharedAppearanceDialogs.objects.all().order_by('sip_shared_appearance_dialog_uuid').using('freeswitch')
    serializer_class = SipSharedAppearanceDialogsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hostname', 'profile_name']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class SipSharedAppearanceSubscriptionsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows SipSharedAppearanceSubscriptions to be viewed.
    """
    queryset = SipSharedAppearanceSubscriptions.objects.all().order_by('sip_shared_appearance_subscription_uuid').using('freeswitch')
    serializer_class = SipSharedAppearanceSubscriptionsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hostname', 'profile_name']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class SipSubscriptionsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows SipSubscriptions to be viewed.
    """
    queryset = SipSubscriptions.objects.all().order_by('sip_subscription_uuid').using('freeswitch')
    serializer_class = SipSubscriptionsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hostname', 'profile_name']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class TasksViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Tasks to be viewed.
    """
    queryset = Tasks.objects.all().order_by('task_uuid').using('freeswitch')
    serializer_class = TasksSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hostname']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class TiersViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Tiers to be viewed.
    """
    queryset = Tiers.objects.all().order_by('tier_uuid').using('freeswitch')
    serializer_class = TiersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['state', 'level', 'position']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class VoicemailMsgsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows VoicemailMsgs to be viewed.
    """
    queryset = VoicemailMsgs.objects.all().order_by('voicemail_msgs_uuid').using('freeswitch')
    serializer_class = VoicemailMsgsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['domain', 'flags']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]


class VoicemailPrefsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows VoicemailPrefs to be viewed.
    """
    queryset = VoicemailPrefs.objects.all().order_by('voicemail_prefs_uuid').using('freeswitch')
    serializer_class = VoicemailPrefsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['domain']
    permission_classes = [
        permissions.IsAuthenticated,
        AdminApiAccessPermission,
    ]
