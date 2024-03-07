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

from django.contrib import admin
from django.db import models
from django.forms.widgets import TextInput
from import_export.admin import ExportMixin
from import_export import resources

from .models import (
    Agents, Aliases, Calls, Channels, Complete, DbData, FifoBridge, FifoCallers,
    FifoOutbound, GroupData, Interfaces, LimitData, Members, Nat, Recovery,
    Registrations, SipAuthentication, SipDialogs, SipPresence, SipRegistrations,
    SipSharedAppearanceDialogs, SipSharedAppearanceSubscriptions,
    SipSubscriptions, Tasks, Tiers, VoicemailMsgs, VoicemailPrefs,
)

class AgentsResource(resources.ModelResource):

    class Meta:
        model = Agents


class AliasesResource(resources.ModelResource):

    class Meta:
        model = Aliases


class CallsResource(resources.ModelResource):

    class Meta:
        model = Calls


class ChannelsResource(resources.ModelResource):

    class Meta:
        model = Channels


class CompleteResource(resources.ModelResource):

    class Meta:
        model = Complete


class DbDataResource(resources.ModelResource):

    class Meta:
        model = DbData


class FifoBridgeResource(resources.ModelResource):

    class Meta:
        model = FifoBridge


class FifoCallersResource(resources.ModelResource):

    class Meta:
        model = FifoCallers


class FifoOutboundResource(resources.ModelResource):

    class Meta:
        model = FifoOutbound


class GroupDataResource(resources.ModelResource):

    class Meta:
        model = GroupData


class InterfacesResource(resources.ModelResource):

    class Meta:
        model = Interfaces


class LimitDataResource(resources.ModelResource):

    class Meta:
        model = LimitData


class MembersResource(resources.ModelResource):

    class Meta:
        model = Members


class NatResource(resources.ModelResource):

    class Meta:
        model = Nat


class RecoveryResource(resources.ModelResource):

    class Meta:
        model = Recovery


class RegistrationsResource(resources.ModelResource):

    class Meta:
        model = Registrations


class SipAuthenticationResource(resources.ModelResource):

    class Meta:
        model = SipAuthentication


class SipDialogsResource(resources.ModelResource):

    class Meta:
        model = SipDialogs


class SipPresenceResource(resources.ModelResource):

    class Meta:
        model = SipPresence


class SipRegistrationsResource(resources.ModelResource):

    class Meta:
        model = SipRegistrations


class SipSharedAppearanceDialogsResource(resources.ModelResource):

    class Meta:
        model = SipSharedAppearanceDialogs


class SipSharedAppearanceSubscriptionsResource(resources.ModelResource):

    class Meta:
        model = SipSharedAppearanceSubscriptions


class SipSubscriptionsResource(resources.ModelResource):

    class Meta:
        model = SipSubscriptions


class TasksResource(resources.ModelResource):

    class Meta:
        model = Tasks


class TiersResource(resources.ModelResource):

    class Meta:
        model = Tiers


class VoicemailMsgsResource(resources.ModelResource):

    class Meta:
        model = VoicemailMsgs


class VoicemailPrefsResource(resources.ModelResource):

    class Meta:
        model = VoicemailPrefs


class AgentsAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = AgentsResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }
    list_display = ('contact', 'state', 'status')
    ordering = ['contact']

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class AliasesAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = AliasesResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class CallsAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = CallsResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ChannelsAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = ChannelsResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }
    list_display = ('context', 'cid_num', 'ip_addr', 'state', 'dest', 'application')
    list_filter= ('context', 'direction')
    ordering = ['context']

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class CompleteAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = CompleteResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }
    list_display = ('a1', 'a2', 'a3')
    list_filter= ('a1', )
    ordering = ['a1']

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class DbDataAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = DbDataResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class FifoBridgeAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = FifoBridgeResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class FifoCallersAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = FifoCallersResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class FifoOutboundAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = FifoOutboundResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class GroupDataAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = GroupDataResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class InterfacesAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = InterfacesResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class LimitDataAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = LimitDataResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class MembersAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = MembersResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class NatAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = NatResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class RecoveryAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = RecoveryResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class RegistrationsAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = RegistrationsResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }
    list_display = ('realm', 'reg_user', 'network_ip', 'network_port', 'network_proto')
    list_filter= ('realm', 'network_proto')
    ordering = ['realm', 'reg_user']

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class SipAuthenticationAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = SipAuthenticationResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }
    list_display = ('nonce', 'profile_name')

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class SipDialogsAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = SipDialogsResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }
    list_display = ('call_id', 'sip_from_host', 'sip_to_host', 'contact_user', 'direction')
    list_filter= ('sip_from_host', 'sip_to_host', 'direction')
    ordering = ['sip_from_host', 'sip_to_host', 'contact_user']

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class SipPresenceAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = SipPresenceResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class SipRegistrationsAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = SipRegistrationsResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }
    list_display = ('sip_host', 'sip_user', 'network_ip', 'network_port', 'status', 'ping_status')
    list_filter= ('sip_host', 'status', 'ping_status')
    ordering = ['sip_host', 'sip_user']

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class SipSharedAppearanceDialogsAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = SipSharedAppearanceDialogsResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class SipSharedAppearanceSubscriptionsAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = SipSharedAppearanceSubscriptionsResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class SipSubscriptionsAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = SipSubscriptionsResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }
    list_display = ('sip_host', 'sip_user', 'network_ip', 'sub_to_user', 'event')
    list_filter= ('sip_host', )
    ordering = ['sip_host', 'sip_user']

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class TasksAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = TasksResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }
    list_display = ('task_id', 'task_group', 'task_desc')
    ordering = ['task_group']

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class TiersAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = TiersResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }
    list_display = ('queue', 'agent', 'state')

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class VoicemailMsgsAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = VoicemailMsgsResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }
    list_display = ('domain', 'username', 'cid_number', 'in_folder', 'message_len', 'read_flags')
    list_filter= ('domain', 'read_flags')
    ordering = ['domain', 'username']

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class VoicemailPrefsAdmin(ExportMixin, admin.ModelAdmin):
    using = 'freeswitch'
    resource_class = VoicemailPrefsResource
    formfield_overrides = {
        models.TextField: {"widget": TextInput},
    }
    list_display = ('domain', 'username')
    list_filter= ('domain', )
    ordering = ['domain', 'username']

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Agents, AgentsAdmin)
admin.site.register(Aliases, AliasesAdmin)
admin.site.register(Calls, CallsAdmin)
admin.site.register(Channels, ChannelsAdmin)
admin.site.register(Complete, CompleteAdmin)
admin.site.register(DbData, DbDataAdmin)
admin.site.register(FifoBridge, FifoBridgeAdmin)
admin.site.register(FifoCallers, FifoCallersAdmin)
admin.site.register(FifoOutbound, FifoOutboundAdmin)
admin.site.register(GroupData, GroupDataAdmin)
admin.site.register(Interfaces, InterfacesAdmin)
admin.site.register(LimitData, LimitDataAdmin)
admin.site.register(Members, MembersAdmin)
admin.site.register(Nat, NatAdmin)
admin.site.register(Recovery, RecoveryAdmin)
admin.site.register(Registrations, RegistrationsAdmin)
admin.site.register(SipAuthentication, SipAuthenticationAdmin)
admin.site.register(SipDialogs, SipDialogsAdmin)
admin.site.register(SipPresence, SipPresenceAdmin)
admin.site.register(SipRegistrations, SipRegistrationsAdmin)
admin.site.register(SipSharedAppearanceDialogs, SipSharedAppearanceDialogsAdmin)
admin.site.register(SipSharedAppearanceSubscriptions, SipSharedAppearanceSubscriptionsAdmin)
admin.site.register(SipSubscriptions, SipSubscriptionsAdmin)
admin.site.register(Tasks, TasksAdmin)
admin.site.register(Tiers, TiersAdmin)
admin.site.register(VoicemailMsgs, VoicemailMsgsAdmin)
admin.site.register(VoicemailPrefs, VoicemailPrefsAdmin)
