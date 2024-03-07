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

from rest_framework import serializers
from .models import (
    Agents, Aliases, Calls, Channels, Complete, DbData, FifoBridge, FifoCallers,
    FifoOutbound, GroupData, Interfaces, LimitData, Members, Nat, Recovery,
    Registrations, SipAuthentication, SipDialogs, SipPresence, SipRegistrations,
    SipSharedAppearanceDialogs, SipSharedAppearanceSubscriptions,
    SipSubscriptions, Tasks, Tiers, VoicemailMsgs, VoicemailPrefs,
)


class AgentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agents
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class AliasesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aliases
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class CallsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calls
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class ChannelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channels
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class CompleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Complete
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class DbDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = DbData
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class FifoBridgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FifoBridge
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class FifoCallersSerializer(serializers.ModelSerializer):

    class Meta:
        model = FifoCallers
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class FifoOutboundSerializer(serializers.ModelSerializer):

    class Meta:
        model = FifoOutbound
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class GroupDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupData
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class InterfacesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interfaces
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class LimitDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = LimitData
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class MembersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Members
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class NatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nat
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class RecoverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Recovery
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])



class RegistrationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registrations
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class SipAuthenticationSerializer(serializers.ModelSerializer):

    class Meta:
        model = SipAuthentication
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class SipDialogsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SipDialogs
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class SipPresenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = SipPresence
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class SipRegistrationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SipRegistrations
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class SipSharedAppearanceDialogsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SipSharedAppearanceDialogs
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class SipSharedAppearanceSubscriptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SipSharedAppearanceSubscriptions
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class SipSubscriptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SipSubscriptions
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class TasksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tasks
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class TiersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tiers
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class VoicemailMsgsSerializer(serializers.ModelSerializer):

    class Meta:
        model = VoicemailMsgs
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])


class VoicemailPrefsSerializer(serializers.ModelSerializer):

    class Meta:
        model = VoicemailPrefs
        fields = ['url']
        fields.extend([field.name for field in model._meta.fields])
