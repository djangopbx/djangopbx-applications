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

from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _

#
# Django requies a Primany Key.
# Many of the models have a primary key fields that is not specidied, created or populated by FreeSWITCH
# But rely on a default value being available at the databse level.
# Some other fields also have default values specified.
# It is for this reason that the schems in the freeswitch database is creatd manually outside of Django
# and the models have the managed flag set to False.
#
# Since Django V5 it is possible to specify a field default that operates at the database level.  So if you
# are using Django 5.0 or newer, you can add "db_default='gen_random_uuid()'" to each of the Primary Key
# field definitions, also add any other field defaults and then
# remove managed = False, if you would like DjangoPBX to manage the freeswitch schema.
#
# Indexes are currently commented out because they add no value with managed = False
#


class Agents(models.Model):
    name                 = models.TextField(blank=True, null=True, verbose_name=_('Name'))         # noqa: E501, E221
    instance_id          = models.TextField(blank=True, null=True, verbose_name=_('Instance Id'))  # noqa: E501, E221
    uuid                 = models.TextField(blank=True, null=True, verbose_name=_('UUId'))         # noqa: E501, E221
    type                 = models.TextField(blank=True, null=True, verbose_name=_('Type'))         # noqa: E501, E221
    contact              = models.TextField(blank=True, null=True, verbose_name=_('Contact'))      # noqa: E501, E221
    status               = models.TextField(blank=True, null=True, verbose_name=_('Status'))       # noqa: E501, E221
    state                = models.TextField(blank=True, null=True, verbose_name=_('State'))        # noqa: E501, E221
    max_no_answer        = models.IntegerField(default=0, verbose_name=_('Max No Answer'))         # noqa: E501, E221
    wrap_up_time         = models.IntegerField(default=0, verbose_name=_('Wrap Up Time'))          # noqa: E501, E221
    reject_delay_time    = models.IntegerField(default=0, verbose_name=_('Reject elay Time'))      # noqa: E501, E221
    busy_delay_time      = models.IntegerField(default=0, verbose_name=_('Bust Delay Time'))       # noqa: E501, E221
    no_answer_delay_time = models.IntegerField(default=0, verbose_name=_('No Answer Delay Time'))  # noqa: E501, E221
    last_bridge_start    = models.IntegerField(default=0, verbose_name=_('Last Bridge Start'))     # noqa: E501, E221
    last_bridge_end      = models.IntegerField(default=0, verbose_name=_('Last Bridge End'))       # noqa: E501, E221
    last_offered_call    = models.IntegerField(default=0, verbose_name=_('Last Offered Call'))     # noqa: E501, E221
    last_status_change   = models.IntegerField(default=0, verbose_name=_('Last Status Change'))    # noqa: E501, E221
    no_answer_count      = models.IntegerField(default=0, verbose_name=_('No Answer Count'))       # noqa: E501, E221
    calls_answered       = models.IntegerField(default=0, verbose_name=_('Calls Answered'))        # noqa: E501, E221
    talk_time            = models.IntegerField(default=0, verbose_name=_('Talk Time'))             # noqa: E501, E221
    ready_time           = models.IntegerField(default=0, verbose_name=_('Ready Time'))            # noqa: E501, E221
    external_calls_count = models.IntegerField(default=0, verbose_name=_('External Calls Count'))  # noqa: E501, E221
    agent_uuid           = models.UUIDField(db_column='agent_uuid', primary_key=True, editable=False, verbose_name=_('Agent Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'Agents'
        db_table = 'agents'

    def __str__(self):
        return str(self.name)


class Aliases(models.Model):
    sticky     = models.IntegerField(blank=True, null=True, verbose_name=_('Sticky')) # noqa: E501, E221
    alias      = models.TextField(blank=True, null=True, verbose_name=_('Alias'))     # noqa: E501, E221
    command    = models.TextField(blank=True, null=True, verbose_name=_('Command'))   # noqa: E501, E221
    hostname   = models.TextField(blank=True, null=True, verbose_name=_('Hostname'))  # noqa: E501, E221
    alias_uuid = models.UUIDField(db_column='alias_uuid', primary_key=True, editable=False, verbose_name=_('Alias Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'Aliases'
        db_table = 'aliases'

    def __str__(self):
        return str(self.alias_id)


class Calls(models.Model):
    call_uuid          = models.UUIDField(db_column='call_uuid', primary_key=True, editable=False, verbose_name=_('Call Id')) # noqa: E501, E221
    call_created       = models.TextField(blank=True, null=True, verbose_name=_('Call Created'))           # noqa: E501, E221
    call_created_epoch = models.IntegerField(blank=True, null=True, verbose_name=_('Call Created Epoch'))  # noqa: E501, E221
    caller_uuid        = models.TextField(blank=True, null=True, verbose_name=_('Caller UUId'))            # noqa: E501, E221
    callee_uuid        = models.TextField(blank=True, null=True, verbose_name=_('Callee UUId'))            # noqa: E501, E221
    hostname           = models.TextField(blank=True, null=True, verbose_name=_('Hostname'))               # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'Calls'
        db_table = 'calls'
        """
        indexes = [
            models.Index(fields=['hostname'], name='callsidx1'),
            models.Index(fields=['callee_uuid'], name='eeuuindex'),
            models.Index(fields=['call_uuid'], name='eeuuindex2'),
            models.Index(fields=['caller_uuid', 'hostname'], name='eruuindex'),
        ]
        """

    def __str__(self):
        return str(self.call_uuid)



class Channels(models.Model):
    channel_uuid     = models.UUIDField(db_column='channel_uuid', primary_key=True, editable=False, verbose_name=_('Channel Id')) # noqa: E501, E221
    uuid             = models.TextField(blank=True, null=True, verbose_name=_('UUId'))                 # noqa: E501, E221
    direction        = models.TextField(blank=True, null=True, verbose_name=_('Direction'))            # noqa: E501, E221
    created          = models.TextField(blank=True, null=True, verbose_name=_('Created'))              # noqa: E501, E221
    created_epoch    = models.IntegerField(blank=True, null=True, verbose_name=_('Created Epoch'))     # noqa: E501, E221
    name             = models.TextField(blank=True, null=True, verbose_name=_('name'))                 # noqa: E501, E221
    state            = models.TextField(blank=True, null=True, verbose_name=_('state'))                # noqa: E501, E221
    cid_name         = models.TextField(blank=True, null=True, verbose_name=_('CID Name'))             # noqa: E501, E221
    cid_num          = models.TextField(blank=True, null=True, verbose_name=_('CID Number'))           # noqa: E501, E221
    ip_addr          = models.TextField(blank=True, null=True, verbose_name=_('IP Address'))           # noqa: E501, E221
    dest             = models.TextField(blank=True, null=True, verbose_name=_('Destination'))          # noqa: E501, E221
    application      = models.TextField(blank=True, null=True, verbose_name=_('Application'))          # noqa: E501, E221
    application_data = models.TextField(blank=True, null=True, verbose_name=_('Application Data'))     # noqa: E501, E221
    dialplan         = models.TextField(blank=True, null=True, verbose_name=_('Dialplan'))             # noqa: E501, E221
    context          = models.TextField(blank=True, null=True, verbose_name=_('Context'))              # noqa: E501, E221
    read_codec       = models.TextField(blank=True, null=True, verbose_name=_('Read Codec'))           # noqa: E501, E221
    read_rate        = models.TextField(blank=True, null=True, verbose_name=_('Read Rate'))            # noqa: E501, E221
    read_bit_rate    = models.TextField(blank=True, null=True, verbose_name=_('Read Bit Rate'))        # noqa: E501, E221
    write_codec      = models.TextField(blank=True, null=True, verbose_name=_('Write Codec'))          # noqa: E501, E221
    write_rate       = models.TextField(blank=True, null=True, verbose_name=_('Write Rate'))           # noqa: E501, E221
    write_bit_rate   = models.TextField(blank=True, null=True, verbose_name=_('Write Bit Rate'))       # noqa: E501, E221
    secure           = models.TextField(blank=True, null=True, verbose_name=_('Secure'))               # noqa: E501, E221
    hostname         = models.TextField(blank=True, null=True, verbose_name=_('Hostname'))             # noqa: E501, E221
    presence_id      = models.TextField(blank=True, null=True, verbose_name=_('Presence Id'))          # noqa: E501, E221
    presence_data    = models.TextField(blank=True, null=True, verbose_name=_('Presence Data'))        # noqa: E501, E221
    accountcode      = models.TextField(blank=True, null=True, verbose_name=_('Account Code'))         # noqa: E501, E221
    callstate        = models.TextField(blank=True, null=True, verbose_name=_('Call State'))           # noqa: E501, E221
    callee_name      = models.TextField(blank=True, null=True, verbose_name=_('Callee Name'))          # noqa: E501, E221
    callee_num       = models.TextField(blank=True, null=True, verbose_name=_('Callee Number'))        # noqa: E501, E221
    callee_direction = models.TextField(blank=True, null=True, verbose_name=_('Callee Direction'))     # noqa: E501, E221
    call_uuid        = models.TextField(blank=True, null=True, verbose_name=_('Call UUId'))            # noqa: E501, E221
    sent_callee_name = models.TextField(blank=True, null=True, verbose_name=_('Sent Callee_Name'))     # noqa: E501, E221
    sent_callee_num  = models.TextField(blank=True, null=True, verbose_name=_('Sent Callee Number'))   # noqa: E501, E221
    initial_cid_name = models.TextField(blank=True, null=True, verbose_name=_('Intial CID Name'))      # noqa: E501, E221
    initial_cid_num  = models.TextField(blank=True, null=True, verbose_name=_('Initial CID Number'))   # noqa: E501, E221
    initial_ip_addr  = models.TextField(blank=True, null=True, verbose_name=_('Initial IP Address'))   # noqa: E501, E221
    initial_dest     = models.TextField(blank=True, null=True, verbose_name=_('Initial Destination'))  # noqa: E501, E221
    initial_dialplan = models.TextField(blank=True, null=True, verbose_name=_('Initial Dialplan'))     # noqa: E501, E221
    initial_context  = models.TextField(blank=True, null=True, verbose_name=_('Initial Context'))      # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'Channels'
        db_table = 'channels'
        """
        indexes = [
            models.Index(fields=['hostname'], name='chidx1'),
            models.Index(fields=['uuid', 'hostname'], name='uuindex'),
            models.Index(fields=['call_uuid'], name='uuindex2'),
        ]
        """

    def __str__(self):
        return str(self.uuid)



class Complete(models.Model):
    sticky        = models.IntegerField(blank=True, null=True, verbose_name=_('Sticky'))   # noqa: E501, E221
    a1            = models.TextField(blank=True, null=True, verbose_name=_('a1'))          # noqa: E501, E221
    a2            = models.TextField(blank=True, null=True, verbose_name=_('a2'))          # noqa: E501, E221
    a3            = models.TextField(blank=True, null=True, verbose_name=_('a3'))          # noqa: E501, E221
    a4            = models.TextField(blank=True, null=True, verbose_name=_('a4'))          # noqa: E501, E221
    a5            = models.TextField(blank=True, null=True, verbose_name=_('a5'))          # noqa: E501, E221
    a6            = models.TextField(blank=True, null=True, verbose_name=_('a6'))          # noqa: E501, E221
    a7            = models.TextField(blank=True, null=True, verbose_name=_('a7'))          # noqa: E501, E221
    a8            = models.TextField(blank=True, null=True, verbose_name=_('a8'))          # noqa: E501, E221
    a9            = models.TextField(blank=True, null=True, verbose_name=_('a9'))          # noqa: E501, E221
    a10           = models.TextField(blank=True, null=True, verbose_name=_('a10'))         # noqa: E501, E221
    hostname      = models.TextField(blank=True, null=True, verbose_name=_('hostname'))    # noqa: E501, E221
    complete_uuid = models.UUIDField(db_column='complete_uuid', primary_key=True, editable=False, verbose_name=_('Complete Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'Complete'
        db_table = 'complete'
        """
        indexes = [
            models.Index(fields=['a1', 'hostname'], name='complete1'),
            models.Index(fields=['a2', 'hostname'], name='complete2'),
            models.Index(fields=['a3', 'hostname'], name='complete3'),
            models.Index(fields=['a4', 'hostname'], name='complete4'),
            models.Index(fields=['a5', 'hostname'], name='complete5'),
            models.Index(fields=['a6', 'hostname'], name='complete6'),
            models.Index(fields=['a7', 'hostname'], name='complete7'),
            models.Index(fields=['a8', 'hostname'], name='complete8'),
            models.Index(fields=['a9', 'hostname'], name='complete9'),
            models.Index(fields=['a10', 'hostname'], name='complete10'),
            models.Index(fields=['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'hostname'], name='complete11'),
        ]
        """

    def __str__(self):
        return str(self.complete_uuid)



class DbData(models.Model):
    hostname     = models.TextField(blank=True, null=True, verbose_name=_('Hostanme'))      # noqa: E501, E221
    realm        = models.TextField(blank=True, null=True, verbose_name=_('Realm'))         # noqa: E501, E221
    data_key     = models.TextField(blank=True, null=True, verbose_name=_('Data Key'))      # noqa: E501, E221
    data         = models.TextField(blank=True, null=True, verbose_name=_('Data'))          # noqa: E501, E221
    db_data_uuid = models.UUIDField(db_column='db_data_uuid', primary_key=True, editable=False, verbose_name=_('DB Data Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'DB Data'
        db_table = 'db_data'
        """
        indexes = [
            models.Index(fields=['realm'], name='dd_realm'),
        ]
        constraints = [
            models.UniqueConstraint(fields=['data_key', 'realm'], name='dd_data_key_realm')
        ]
        """

    def __str__(self):
        return str(self.dd_data_uuid)



class FifoBridge(models.Model):
    fifo_name               = models.TextField( verbose_name=_('FIFO Name'))                                    # noqa: E501, E221
    caller_uuid             = models.TextField( verbose_name=_('Caller UUId'))                                  # noqa: E501, E221
    caller_caller_id_name   = models.TextField(blank=True, null=True, verbose_name=_('CID Name'))               # noqa: E501, E221
    caller_caller_id_number = models.TextField(blank=True, null=True, verbose_name=_('CID Number'))             # noqa: E501, E221
    consumer_uuid           = models.TextField( verbose_name=_('Consumer UUId'))                                # noqa: E501, E221
    consumer_outgoing_uuid  = models.TextField(blank=True, null=True, verbose_name=_('Consumer Outgoing UUId')) # noqa: E501, E221
    bridge_start            = models.IntegerField(blank=True, null=True, verbose_name=_('Bridge Start'))        # noqa: E501, E221
    fifo_bridge_uuid        = models.UUIDField(db_column='fifo_bridge_uuid', primary_key=True, editable=False, verbose_name=_('FIFO Bridge Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'FIFO Bridge'
        db_table = 'fifo_bridge'

    def __str__(self):
        return str(self.fifo_bridge_uuid)


class FifoCallers(models.Model):
    fifo_name               = models.TextField( verbose_name=_('FIFO Name'))                           # noqa: E501, E221
    uuid                    = models.TextField( verbose_name=_('UUId'))                                # noqa: E501, E221
    caller_caller_id_name   = models.TextField(blank=True, null=True, verbose_name=_('CID Name'))      # noqa: E501, E221
    caller_caller_id_number = models.TextField(blank=True, null=True, verbose_name=_('CID Number'))    # noqa: E501, E221
    timestamp               = models.IntegerField(blank=True, null=True, verbose_name=_('Time Stamp')) # noqa: E501, E221
    fifo_caller_uuid        = models.UUIDField(db_column='fifo_caller_uuid', primary_key=True, editable=False, verbose_name=_('FIFO Caller Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'FIFO Callers'
        db_table = 'fifo_callers'

    def __str__(self):
        return str(self.fifo_caller_uuid)


class FifoOutbound(models.Model):
    uuid                         = models.TextField(blank=True, null=True, verbose_name=_('UUId'))                # noqa: E501, E221
    fifo_name                    = models.TextField(blank=True, null=True, verbose_name=_('FIFO Name'))           # noqa: E501, E221
    originate_string             = models.TextField(blank=True, null=True, verbose_name=_('Originate String'))    # noqa: E501, E221
    simo_count                   = models.IntegerField(blank=True, null=True, verbose_name=_('SIMO Count'))       # noqa: E501, E221
    use_count                    = models.IntegerField(blank=True, null=True, verbose_name=_('Use Count'))        # noqa: E501, E221
    timeout                      = models.IntegerField(blank=True, null=True, verbose_name=_('Timeout'))          # noqa: E501, E221
    lag                          = models.IntegerField(blank=True, null=True, verbose_name=_('Lag'))              # noqa: E501, E221
    next_avail                   = models.IntegerField(default=0, verbose_name=_('Next Available'))               # noqa: E501, E221
    expires                      = models.IntegerField(default=0, verbose_name=_('Expires'))                      # noqa: E501, E221
    static                       = models.IntegerField(default=0, verbose_name=_('Static'))                       # noqa: E501, E221
    outbound_call_count          = models.IntegerField(default=0, verbose_name=_('Outbound Call Count'))          # noqa: E501, E221
    outbound_fail_count          = models.IntegerField(default=0, verbose_name=_('Outbound Fail Count'))          # noqa: E501, E221
    hostname                     = models.TextField(blank=True, null=True, verbose_name=_('Hostname'))            # noqa: E501, E221
    taking_calls                 = models.IntegerField(default=1, verbose_name=_('Taking Calls'))                 # noqa: E501, E221
    status                       = models.TextField(blank=True, null=True, verbose_name=_('Status'))              # noqa: E501, E221
    outbound_call_total_count    = models.IntegerField(default=0, verbose_name=_('Outbound Call total Count'))    # noqa: E501, E221
    outbound_fail_total_count    = models.IntegerField(default=0, verbose_name=_('Outbound Fail total Count'))    # noqa: E501, E221
    active_time                  = models.IntegerField(default=0, verbose_name=_('Active Time'))                  # noqa: E501, E221
    inactive_time                = models.IntegerField(default=0, verbose_name=_('Inactive Time'))                # noqa: E501, E221
    manual_calls_out_count       = models.IntegerField(default=0, verbose_name=_('Manual Calls Out Count'))       # noqa: E501, E221
    manual_calls_in_count        = models.IntegerField(default=0, verbose_name=_('Manual Calls In Count'))        # noqa: E501, E221
    manual_calls_out_total_count = models.IntegerField(default=0, verbose_name=_('Manual Calls Out Total Count')) # noqa: E501, E221
    manual_calls_in_total_count  = models.IntegerField(default=0, verbose_name=_('Manual Calls In Total Count'))  # noqa: E501, E221
    ring_count                   = models.IntegerField(default=0, verbose_name=_('Ring Count'))                   # noqa: E501, E221
    start_time                   = models.IntegerField(default=0, verbose_name=_('Start Time'))                   # noqa: E501, E221
    stop_time                    = models.IntegerField(default=0, verbose_name=_('Stop time'))                    # noqa: E501, E221
    fifo_outbound_uuid           = models.UUIDField(db_column='fifo_outbound_uuid', primary_key=True, editable=False, verbose_name=_('FIFO Outbound Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'FIFO Outbound'
        db_table = 'fifo_outbound'

    def __str__(self):
        return str(self.fifo_outbound_uuid)


class GroupData(models.Model):
    hostname        = models.TextField(blank=True, null=True, verbose_name=_('Hostname'))   # noqa: E501, E221
    groupname       = models.TextField(blank=True, null=True, verbose_name=_('Group Name')) # noqa: E501, E221
    url             = models.TextField(blank=True, null=True, verbose_name=_('URL'))        # noqa: E501, E221
    group_data_uuid = models.UUIDField(db_column='group_data_uuid', primary_key=True, editable=False, verbose_name=_('Group Data Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'Group Data'
        db_table = 'group_data'
        """
        indexes = [
            models.Index(fields=['groupname'], name='gd_groupname'),
            models.Index(fields=['url'], name='gd_url'),
        ]
        """

    def __str__(self):
        return str(self.group_data_uuid)


class Interfaces(models.Model):
    type           = models.TextField(blank=True, null=True, verbose_name=_('Type'))        # noqa: E501, E221
    name           = models.TextField(blank=True, null=True, verbose_name=_('Name'))        # noqa: E501, E221
    description    = models.TextField(blank=True, null=True, verbose_name=_('Description')) # noqa: E501, E221
    ikey           = models.TextField(blank=True, null=True, verbose_name=_('I Key'))       # noqa: E501, E221
    filename       = models.TextField(blank=True, null=True, verbose_name=_('Filename'))    # noqa: E501, E221
    syntax         = models.TextField(blank=True, null=True, verbose_name=_('Syntax'))      # noqa: E501, E221
    hostname       = models.TextField(blank=True, null=True, verbose_name=_('Hostname'))    # noqa: E501, E221
    interface_uuid = models.UUIDField(db_column='interface_uuid', primary_key=True, editable=False, verbose_name=_('Interface Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'Interfaces'
        db_table = 'interfaces'

    def __str__(self):
        return str(self.interface_uuid)


class LimitData(models.Model):
    hostname        = models.TextField(blank=True, null=True, verbose_name=_('Hostname')) # noqa: E501, E221
    realm           = models.TextField(blank=True, null=True, verbose_name=_('Realm'))    # noqa: E501, E221
    id              = models.TextField(blank=True, null=True, verbose_name=_('Id'))       # noqa: E501, E221
    limit_data_uuid = models.UUIDField(db_column='limit_data_uuid', primary_key=True, editable=False, verbose_name=_('Limit Data Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'Limit data'
        db_table = 'limit_data'
        """
        indexes = [
            models.Index(fields=['hostname'], name='ld_hostname'),
            models.Index(fields=['id'], name='ld_id'),
            models.Index(fields=['realm'], name='ld_realm'),
            models.Index(fields=['uuid'], name='ld_uuid'),
        ]
        """

    def __str__(self):
        return str(self.limit_data_uuid)


class Members(models.Model):
    queue           = models.TextField(blank=True, null=True, verbose_name=_('Queue'))          # noqa: E501, E221
    instance_id     = models.TextField(blank=True, null=True, verbose_name=_('Instance Id'))    # noqa: E501, E221
    uuid            = models.TextField( default='', verbose_name=_('UUId'))                     # noqa: E501, E221
    session_uuid    = models.TextField( default='', verbose_name=_('Session UUId'))             # noqa: E501, E221
    cid_number      = models.TextField(blank=True, null=True, verbose_name=_('CID Number'))     # noqa: E501, E221
    cid_name        = models.TextField(blank=True, null=True, verbose_name=_('CID Name'))       # noqa: E501, E221
    system_epoch    = models.IntegerField(default=0, verbose_name=_('System Epoch'))            # noqa: E501, E221
    joined_epoch    = models.IntegerField(default=0, verbose_name=_('Joined Epoch'))            # noqa: E501, E221
    rejoined_epoch  = models.IntegerField(default=0, verbose_name=_('Re-Joined Epoch'))         # noqa: E501, E221
    bridge_epoch    = models.IntegerField(default=0, verbose_name=_('Bridge Epoch'))            # noqa: E501, E221
    abandoned_epoch = models.IntegerField(default=0, verbose_name=_('Abandoned Epoch'))         # noqa: E501, E221
    base_score      = models.IntegerField(default=0, verbose_name=_('Base Score'))              # noqa: E501, E221
    skill_score     = models.IntegerField(default=0, verbose_name=_('Skill Score'))             # noqa: E501, E221
    serving_agent   = models.TextField(blank=True, null=True, verbose_name=_('Serving Agent'))  # noqa: E501, E221
    serving_system  = models.TextField(blank=True, null=True, verbose_name=_('Serving System')) # noqa: E501, E221
    state           = models.TextField(blank=True, null=True, verbose_name=_('State'))          # noqa: E501, E221
    member_uuid     = models.UUIDField(db_column='member_uuid', primary_key=True, editable=False, verbose_name=_('Member Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'Members'
        db_table = 'members'

    def __str__(self):
        return str(self.member_uuid)


class Nat(models.Model):
    sticky   = models.IntegerField(blank=True, null=True, verbose_name=_('Sticky')) # noqa: E501, E221
    port     = models.IntegerField(blank=True, null=True, verbose_name=_('Port'))   # noqa: E501, E221
    proto    = models.IntegerField(blank=True, null=True, verbose_name=_('Proto'))  # noqa: E501, E221
    hostname = models.TextField(blank=True, null=True, verbose_name=_('Hostname'))  # noqa: E501, E221
    nat_uuid = models.UUIDField(db_column='nat_uuid', primary_key=True, editable=False, verbose_name=_('NAT Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'NAT'
        db_table = 'nat'
        """
        indexes = [
            models.Index(fields=['port', 'proto', 'hostname'], name='nat_map_port_proto'),
        ]
        """

    def __str__(self):
        return str(self.nat_uuid)


class Recovery(models.Model):
    runtime_uuid  = models.TextField(blank=True, null=True, verbose_name=_('Runtime UUId')) # noqa: E501, E221
    technology    = models.TextField(blank=True, null=True, verbose_name=_('Technology'))   # noqa: E501, E221
    profile_name  = models.TextField(blank=True, null=True, verbose_name=_('Profile Name')) # noqa: E501, E221
    hostname      = models.TextField(blank=True, null=True, verbose_name=_('Hostname'))     # noqa: E501, E221
    metadata      = models.TextField(blank=True, null=True, verbose_name=_('Meta Data'))    # noqa: E501, E221
    uuid = models.UUIDField(db_column='uuid', primary_key=True, editable=False, verbose_name=_('Recovery Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'Recovery'
        db_table = 'recovery'
        """
        indexes = [
            models.Index(fields=['technology'], name='recovery1'),
            models.Index(fields=['profile_name'], name='recovery2'),
            models.Index(fields=['uuid'], name='recovery3'),
            models.Index(fields=['runtime_uuid'], name='recovery4'),
        ]
        """

    def __str__(self):
        return str(self.recovery_uuid)


class Registrations(models.Model):
    reg_user          = models.TextField(blank=True, null=True, verbose_name=_('Reg. User'))        # noqa: E501, E221
    realm             = models.TextField(blank=True, null=True, verbose_name=_('Realm'))            # noqa: E501, E221
    token             = models.TextField(blank=True, null=True, verbose_name=_('Token'))            # noqa: E501, E221
    url               = models.TextField(blank=True, null=True, verbose_name=_('URL'))              # noqa: E501, E221
    expires           = models.IntegerField(blank=True, null=True, verbose_name=_('Expires'))       # noqa: E501, E221
    network_ip        = models.TextField(blank=True, null=True, verbose_name=_('Network IP'))       # noqa: E501, E221
    network_port      = models.TextField(blank=True, null=True, verbose_name=_('Network Port'))     # noqa: E501, E221
    network_proto     = models.TextField(blank=True, null=True, verbose_name=_('Network Protocol')) # noqa: E501, E221
    hostname          = models.TextField(blank=True, null=True, verbose_name=_('Hostanme'))         # noqa: E501, E221
    metadata          = models.TextField(blank=True, null=True, verbose_name=_('Meta Data'))        # noqa: E501, E221
    registration_uuid = models.UUIDField(db_column='registration_uuid', primary_key=True, editable=False, verbose_name=_('Registration Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'Registrations'
        db_table = 'registrations'
        """
        indexes = [
            models.Index(fields=['reg_user', 'realm', 'hostname'], name='regindex1'),
        ]
        """

    def __str__(self):
        return str(self.registration_uuid)


class SipAuthentication(models.Model):
    nonce                   = models.TextField(blank=True, null=True, verbose_name=_('Nonce'))        # noqa: E501, E221
    expires                 = models.BigIntegerField(blank=True, null=True, verbose_name=_('Expires'))# noqa: E501, E221
    profile_name            = models.TextField(blank=True, null=True, verbose_name=_('Profile Name')) # noqa: E501, E221
    hostname                = models.TextField(blank=True, null=True, verbose_name=_('Host Name'))    # noqa: E501, E221
    last_nc                 = models.IntegerField(blank=True, null=True, verbose_name=_('Last NC'))   # noqa: E501, E221
    algorithm               = models.IntegerField(default=1, verbose_name=_('Algorithm'))             # noqa: E501, E221
    sip_authentication_uuid = models.UUIDField(db_column='sip_authentication_uuid', primary_key=True, editable=False, verbose_name=_('SIP Authentication Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'SIP Authentications'
        db_table = 'sip_authentication'
        """
        indexes = [
            models.Index(fields=['expires'], name='sa_expires'),
            models.Index(fields=['hostname'], name='sa_hostname'),
            models.Index(fields=['last_nc'], name='sa_last_nc'),
            models.Index(fields=['nonce'], name='sa_nonce'),
        ]
        """

    def __str__(self):
        return str(self.sip_authentication_uuid)


class SipDialogs(models.Model):
    call_id         = models.TextField(blank=True, null=True, verbose_name=_('Call Id'))                     # noqa: E501, E221
    uuid            = models.TextField(blank=True, null=True, verbose_name=_('UUId'))                        # noqa: E501, E221
    sip_to_user     = models.TextField(blank=True, null=True, verbose_name=_('SIP to User'))                 # noqa: E501, E221
    sip_to_host     = models.TextField(blank=True, null=True, verbose_name=_('SIP to Host'))                 # noqa: E501, E221
    sip_from_user   = models.TextField(blank=True, null=True, verbose_name=_('SIP from User'))               # noqa: E501, E221
    sip_from_host   = models.TextField(blank=True, null=True, verbose_name=_('SIP from Host'))               # noqa: E501, E221
    contact_user    = models.TextField(blank=True, null=True, verbose_name=_('Contact User'))                # noqa: E501, E221
    contact_host    = models.TextField(blank=True, null=True, verbose_name=_('Contact Host'))                # noqa: E501, E221
    state           = models.TextField(blank=True, null=True, verbose_name=_('State'))                       # noqa: E501, E221
    direction       = models.TextField(blank=True, null=True, verbose_name=_('Direction'))                   # noqa: E501, E221
    user_agent      = models.TextField(blank=True, null=True, verbose_name=_('User Agent'))                  # noqa: E501, E221
    profile_name    = models.TextField(blank=True, null=True, verbose_name=_('Profile Name'))                # noqa: E501, E221
    hostname        = models.TextField(blank=True, null=True, verbose_name=_('Host Name'))                   # noqa: E501, E221
    contact         = models.TextField(blank=True, null=True, verbose_name=_('Contact'))                     # noqa: E501, E221
    presence_id     = models.TextField(blank=True, null=True, verbose_name=_('Presence Id'))                 # noqa: E501, E221
    presence_data   = models.TextField(blank=True, null=True, verbose_name=_('Presence Data'))               # noqa: E501, E221
    call_info       = models.TextField(blank=True, null=True, verbose_name=_('Call Info'))                   # noqa: E501, E221
    call_info_state = models.TextField(blank=True, null=True, default='', verbose_name=_('Call Info State')) # noqa: E501, E221
    expires         = models.BigIntegerField(blank=True, null=True, verbose_name=_('Expires'))               # noqa: E501, E221
    status          = models.TextField(blank=True, null=True, verbose_name=_('Status'))                      # noqa: E501, E221
    rpid            = models.TextField(blank=True, null=True, verbose_name=_('RPID'))                        # noqa: E501, E221
    sip_to_tag      = models.TextField(blank=True, null=True, verbose_name=_('SIP to Tag'))                  # noqa: E501, E221
    sip_from_tag    = models.TextField(blank=True, null=True, verbose_name=_('SIP from Tag'))                # noqa: E501, E221
    rcd             = models.IntegerField(default=0, verbose_name=_('RCD'))                                  # noqa: E501, E221
    sip_dialog_uuid = models.UUIDField(db_column='sip_dialog_uuid', primary_key=True, editable=False, verbose_name=_('SIP Dialog Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'SIP Dialogs'
        db_table = 'sip_dialogs'
        """
        indexes = [
            models.Index(fields=['call_id'], name='sd_call_id'),
            models.Index(fields=['call_info'], name='sd_call_info'),
            models.Index(fields=['call_info_state'], name='sd_call_info_state'),
            models.Index(fields=['expires'], name='sd_expires'),
            models.Index(fields=['hostname'], name='sd_hostname'),
            models.Index(fields=['presence_data'], name='sd_presence_data'),
            models.Index(fields=['presence_id'], name='sd_presence_id'),
            models.Index(fields=['rcd'], name='sd_rcd'),
            models.Index(fields=['sip_from_host'], name='sd_sip_from_host'),
            models.Index(fields=['sip_from_tag'], name='sd_sip_from_tag'),
            models.Index(fields=['sip_from_user'], name='sd_sip_from_user'),
            models.Index(fields=['sip_to_host'], name='sd_sip_to_host'),
            models.Index(fields=['sip_to_tag'], name='sd_sip_to_tag'),
            models.Index(fields=['uuid'], name='sd_uuid'),
        ]
        """

    def __str__(self):
        return str(self.sip_dialog_uuid)


class SipPresence(models.Model):
    sip_user          = models.TextField(blank=True, null=True, verbose_name=_('SIP User'))     # noqa: E501, E221
    sip_host          = models.TextField(blank=True, null=True, verbose_name=_('SIP Host'))     # noqa: E501, E221
    status            = models.TextField(blank=True, null=True, verbose_name=_('Status'))       # noqa: E501, E221
    rpid              = models.TextField(blank=True, null=True, verbose_name=_('RPID'))         # noqa: E501, E221
    expires           = models.BigIntegerField(blank=True, null=True, verbose_name=_('Expires'))# noqa: E501, E221
    user_agent        = models.TextField(blank=True, null=True, verbose_name=_('User Agent'))   # noqa: E501, E221
    profile_name      = models.TextField(blank=True, null=True, verbose_name=_('Profile Name')) # noqa: E501, E221
    hostname          = models.TextField(blank=True, null=True, verbose_name=_('Host Name'))    # noqa: E501, E221
    network_ip        = models.TextField(blank=True, null=True, verbose_name=_('Network IP'))   # noqa: E501, E221
    network_port      = models.TextField(blank=True, null=True, verbose_name=_('Network Port')) # noqa: E501, E221
    open_closed       = models.TextField(blank=True, null=True, verbose_name=_('Open Closed'))  # noqa: E501, E221
    sip_presence_uuid = models.UUIDField(db_column='sip_presence_uuid', primary_key=True, editable=False, verbose_name=_('SIP Presence Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'SIP Presence'
        db_table = 'sip_presence'
        """
        indexes = [
            models.Index(fields=['expires'], name='sp_expires'),
            models.Index(fields=['hostname'], name='sp_hostname'),
            models.Index(fields=['open_closed'], name='sp_open_closed'),
            models.Index(fields=['profile_name'], name='sp_profile_name'),
            models.Index(fields=['sip_host'], name='sp_sip_host'),
            models.Index(fields=['sip_user'], name='sp_sip_user'),
        ]
        """

    def __str__(self):
        return str(self.sip_presence_uuid)


class SipRegistrations(models.Model):
    call_id               = models.TextField(blank=True, null=True, verbose_name=_('Call Id'))           # noqa: E501, E221
    sip_user              = models.TextField(blank=True, null=True, verbose_name=_('SIP User'))          # noqa: E501, E221
    sip_host              = models.TextField(blank=True, null=True, verbose_name=_('SIP Host'))          # noqa: E501, E221
    presence_hosts        = models.TextField(blank=True, null=True, verbose_name=_('Presence Hosts'))    # noqa: E501, E221
    contact               = models.TextField(blank=True, null=True, verbose_name=_('Contact'))           # noqa: E501, E221
    status                = models.TextField(blank=True, null=True, verbose_name=_('Status'))            # noqa: E501, E221
    ping_status           = models.TextField(blank=True, null=True, verbose_name=_('Ping Status'))       # noqa: E501, E221
    ping_count            = models.IntegerField(blank=True, null=True, verbose_name=_('Ping Count'))     # noqa: E501, E221
    ping_time             = models.BigIntegerField(blank=True, null=True, verbose_name=_('Ping time'))   # noqa: E501, E221
    force_ping            = models.IntegerField(blank=True, null=True, verbose_name=_('Force Ping'))     # noqa: E501, E221
    rpid                  = models.TextField(blank=True, null=True, verbose_name=_('RPID'))              # noqa: E501, E221
    expires               = models.BigIntegerField(blank=True, null=True, verbose_name=_('Expires'))     # noqa: E501, E221
    ping_expires          = models.IntegerField(default=0, verbose_name=_('Ping Expires'))               # noqa: E501, E221
    user_agent            = models.TextField(blank=True, null=True, verbose_name=_('User Agent'))        # noqa: E501, E221
    server_user           = models.TextField(blank=True, null=True, verbose_name=_('Server User'))       # noqa: E501, E221
    server_host           = models.TextField(blank=True, null=True, verbose_name=_('Server Host'))       # noqa: E501, E221
    profile_name          = models.TextField(blank=True, null=True, verbose_name=_('Profile Name'))      # noqa: E501, E221
    hostname              = models.TextField(blank=True, null=True, verbose_name=_('Host Name'))         # noqa: E501, E221
    network_ip            = models.TextField(blank=True, null=True, verbose_name=_('Network IP'))        # noqa: E501, E221
    network_port          = models.TextField(blank=True, null=True, verbose_name=_('Network Port'))      # noqa: E501, E221
    sip_username          = models.TextField(blank=True, null=True, verbose_name=_('SIP User Name'))     # noqa: E501, E221
    sip_realm             = models.TextField(blank=True, null=True, verbose_name=_('SIP Realm'))         # noqa: E501, E221
    mwi_user              = models.TextField(blank=True, null=True, verbose_name=_('MWI User'))          # noqa: E501, E221
    mwi_host              = models.TextField(blank=True, null=True, verbose_name=_('MWI Host'))          # noqa: E501, E221
    orig_server_host      = models.TextField(blank=True, null=True, verbose_name=_('Orig. Server Host')) # noqa: E501, E221
    orig_hostname         = models.TextField(blank=True, null=True, verbose_name=_('Orig. Host Name'))   # noqa: E501, E221
    sub_host              = models.TextField(blank=True, null=True, verbose_name=_('Sub Host'))          # noqa: E501, E221
    sip_registration_uuid = models.UUIDField(db_column='sip_registration_uuid', primary_key=True, editable=False, verbose_name=_('SIP Registration Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'SIP Registrations'
        db_table = 'sip_registrations'
        """
        indexes = [
            models.Index(fields=['call_id'], name='sr_call_id'),
            models.Index(fields=['contact'], name='sr_contact'),
            models.Index(fields=['expires'], name='sr_expires'),
            models.Index(fields=['hostname'], name='sr_hostname'),
            models.Index(fields=['mwi_host'], name='sr_mwi_host'),
            models.Index(fields=['mwi_user'], name='sr_mwi_host'),
            models.Index(fields=['network_ip'], name='sr_network_ip'),
            models.Index(fields=['network_port'], name='sr_network_port'),
            models.Index(fields=['orig_hostname'], name='sr_orig_hostname'),
            models.Index(fields=['orig_server_host'], name='sr_orig_server_host'),
            models.Index(fields=['ping_expires'], name='sr_ping_expires'),
            models.Index(fields=['ping_status'], name='sr_ping_status'),
            models.Index(fields=['presence_hosts'], name='sr_presence_hosts'),
            models.Index(fields=['profile_name'], name='sr_profile_name'),
            models.Index(fields=['sip_host'], name='sr_sip_host'),
            models.Index(fields=['sip_realm'], name='sr_sip_realm'),
            models.Index(fields=['sip_user'], name='sr_sip_user'),
            models.Index(fields=['sip_username'], name='sr_sip_username'),
            models.Index(fields=['status'], name='sr_status'),
            models.Index(fields=['sub_host'], name='sr_sub_host'),
        ]
        """
    def __str__(self):
        return str(self.sip_registration_uuid)


class SipSharedAppearanceDialogs(models.Model):
    profile_name                      = models.TextField(blank=True, null=True, verbose_name=_('Profile Name'))   # noqa: E501, E221
    hostname                          = models.TextField(blank=True, null=True, verbose_name=_('Host Name'))      # noqa: E501, E221
    contact_str                       = models.TextField(blank=True, null=True, verbose_name=_('Contact String')) # noqa: E501, E221
    call_id                           = models.TextField(blank=True, null=True, verbose_name=_('Call Id'))        # noqa: E501, E221
    network_ip                        = models.TextField(blank=True, null=True, verbose_name=_('Netweork IP'))    # noqa: E501, E221
    expires                           = models.BigIntegerField(blank=True, null=True, verbose_name=_('Expires'))  # noqa: E501, E221
    sip_shared_appearance_dialog_uuid = models.UUIDField(db_column='sip_shared_appearance_dialog_uuid', primary_key=True, editable=False, verbose_name=_('SIP Shared Appearance Dialog Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'SIP Shared Appearance Dialogs'
        db_table = 'sip_shared_appearance_dialogs'
        """
        indexes = [
            models.Index(fields=['call_id'], name='ssd_call_id'),
            models.Index(fields=['contact_str'], name='ssd_contact_str'),
            models.Index(fields=['expires'], name='ssd_expires'),
            models.Index(fields=['hostname'], name='ssd_hostname'),
            models.Index(fields=['profile_name'], name='ssd_profile_name'),
        ]
        """

    def __str__(self):
        return str(self.sip_shared_appearance_dialog_uuid)


class SipSharedAppearanceSubscriptions(models.Model):
    subscriber                              = models.TextField(blank=True, null=True, verbose_name=_('Subscriber'))     # noqa: E501, E221
    call_id                                 = models.TextField(blank=True, null=True, verbose_name=_('Call Id'))        # noqa: E501, E221
    aor                                     = models.TextField(blank=True, null=True, verbose_name=_('AOR'))            # noqa: E501, E221
    profile_name                            = models.TextField(blank=True, null=True, verbose_name=_('Profile Name'))   # noqa: E501, E221
    hostname                                = models.TextField(blank=True, null=True, verbose_name=_('Host Name'))      # noqa: E501, E221
    contact_str                             = models.TextField(blank=True, null=True, verbose_name=_('Contact String')) # noqa: E501, E221
    network_ip                              = models.TextField(blank=True, null=True, verbose_name=_('Network IP'))     # noqa: E501, E221
    sip_shared_appearance_subscription_uuid = models.UUIDField(db_column='sip_shared_appearance_subscription_uuid', primary_key=True, editable=False, verbose_name=_('SIP Shared Appearance Subscription Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'SIP Shared Appearance Subscriptions'
        db_table = 'sip_shared_appearance_subscriptions'
        """
        indexes = [
            models.Index(fields=['aor'], name='ssa_aor'),
            models.Index(fields=['hostname'], name='ssa_hostname'),
            models.Index(fields=['network_ip'], name='ssa_network_ip'),
            models.Index(fields=['profile_name'], name='ssa_profile_name'),
            models.Index(fields=['subscriber'], name='ssa_subscriber'),
        ]
        """

    def __str__(self):
        return str(self.sip_shared_appearance_subscription_uuid)


class SipSubscriptions(models.Model):
    proto                 = models.TextField(blank=True, null=True, verbose_name=_('Protocol'))       # noqa: E501, E221
    sip_user              = models.TextField(blank=True, null=True, verbose_name=_('SIP User'))       # noqa: E501, E221
    sip_host              = models.TextField(blank=True, null=True, verbose_name=_('SIP Host'))       # noqa: E501, E221
    sub_to_user           = models.TextField(blank=True, null=True, verbose_name=_('Sub. to User'))   # noqa: E501, E221
    sub_to_host           = models.TextField(blank=True, null=True, verbose_name=_('Sub. to Host'))   # noqa: E501, E221
    presence_hosts        = models.TextField(blank=True, null=True, verbose_name=_('Presence Hosts')) # noqa: E501, E221
    event                 = models.TextField(blank=True, null=True, verbose_name=_('Event'))          # noqa: E501, E221
    contact               = models.TextField(blank=True, null=True, verbose_name=_('Contact'))        # noqa: E501, E221
    call_id               = models.TextField(blank=True, null=True, verbose_name=_('Call Id'))        # noqa: E501, E221
    full_from             = models.TextField(blank=True, null=True, verbose_name=_('Full From'))      # noqa: E501, E221
    full_via              = models.TextField(blank=True, null=True, verbose_name=_('Full Via'))       # noqa: E501, E221
    expires               = models.BigIntegerField(blank=True, null=True, verbose_name=_('Expires'))  # noqa: E501, E221
    user_agent            = models.TextField(blank=True, null=True, verbose_name=_('User Agent'))     # noqa: E501, E221
    accept                = models.TextField(blank=True, null=True, verbose_name=_('Accept'))         # noqa: E501, E221
    profile_name          = models.TextField(blank=True, null=True, verbose_name=_('Profile Name'))   # noqa: E501, E221
    hostname              = models.TextField(blank=True, null=True, verbose_name=_('Host Name'))      # noqa: E501, E221
    network_port          = models.TextField(blank=True, null=True, verbose_name=_('Network Port'))   # noqa: E501, E221
    network_ip            = models.TextField(blank=True, null=True, verbose_name=_('Network IP'))     # noqa: E501, E221
    version               = models.IntegerField(default=0, verbose_name=_('Version'))                 # noqa: E501, E221
    orig_proto            = models.TextField(blank=True, null=True, verbose_name=_('Orig. Protocol')) # noqa: E501, E221
    full_to               = models.TextField(blank=True, null=True, verbose_name=_('Full To'))        # noqa: E501, E221
    sip_subscription_uuid = models.UUIDField(db_column='sip_subscription_uuid', primary_key=True, editable=False, verbose_name=_('SIP Subscription Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'SIP Subscriptions'
        db_table = 'sip_subscriptions'
        """
        indexes = [
            models.Index(fields=['call_id'], name='ss_call_id'),
            models.Index(fields=['contact'], name='ss_contact'),
            models.Index(fields=['event'], name='ss_event'),
            models.Index(fields=['expires'], name='ss_expires'),
            models.Index(fields=['full_from'], name='ss_full_from'),
            models.Index(fields=['hostname'], name='ss_hostname'),
            models.Index(fields=['call_id', 'profile_name', 'hostname'], name='ss_multi'),
            models.Index(fields=['network_ip'], name='ss_network_ip'),
            models.Index(fields=['network_port'], name='ss_network_port'),
            models.Index(fields=['orig_proto'], name='ss_orig_proto'),
            models.Index(fields=['presence_hosts'], name='ss_presence_hosts'),
            models.Index(fields=['profile_name'], name='ss_profile_name'),
            models.Index(fields=['proto'], name='ss_proto'),
            models.Index(fields=['sip_host'], name='ss_sip_host'),
            models.Index(fields=['sip_user'], name='ss_sip_user'),
            models.Index(fields=['sub_to_host'], name='ss_sub_to_host'),
            models.Index(fields=['sub_to_user'], name='ss_sub_to_user'),
            models.Index(fields=['version'], name='ss_version'),
        ]
        """

    def __str__(self):
        return str(self.sip_subscription_uuid)


class Tasks(models.Model):
    task_id          = models.IntegerField(blank=True, null=True, verbose_name=_('Task Id'))          # noqa: E501, E221
    task_desc        = models.TextField(blank=True, null=True, verbose_name=_('Task Description'))    # noqa: E501, E221
    task_group       = models.TextField(blank=True, null=True, verbose_name=_('Task Group'))          # noqa: E501, E221
    task_runtime     = models.BigIntegerField(blank=True, null=True, verbose_name=_('Task Runtime'))  # noqa: E501, E221
    task_sql_manager = models.IntegerField(blank=True, null=True, verbose_name=_('Task SQL Manager')) # noqa: E501, E221
    hostname         = models.TextField(blank=True, null=True, verbose_name=_('Host Name'))           # noqa: E501, E221
    task_uuid        = models.UUIDField(db_column='task_uuid', primary_key=True, editable=False, verbose_name=_('Task Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'Tasks'
        db_table = 'tasks'
        """
        indexes = [
            models.Index(fields=['task_id'], name='tasks1'),
        ]
        """

    def __str__(self):
        return str(self.task_uuid)


class Tiers(models.Model):
    queue     = models.TextField(blank=True, null=True, verbose_name=_('Queue')) # noqa: E501, E221
    agent     = models.TextField(blank=True, null=True, verbose_name=_('Agent')) # noqa: E501, E221
    state     = models.TextField(blank=True, null=True, verbose_name=_('State')) # noqa: E501, E221
    level     = models.IntegerField(default=1, verbose_name=_('Level'))          # noqa: E501, E221
    position  = models.IntegerField(default=1, verbose_name=_('Position'))       # noqa: E501, E221
    tier_uuid = models.UUIDField(db_column='tier_uuid', primary_key=True, editable=False, verbose_name=_('Tier Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'Tiers'
        db_table = 'tiers'

    def __str__(self):
        return str(self.tier_uuid)


class VoicemailMsgs(models.Model):
    created_epoch       = models.IntegerField(blank=True, null=True, verbose_name=_('Created Epoch'))  # noqa: E501, E221
    read_epoch          = models.IntegerField(blank=True, null=True, verbose_name=_('Read Epoch'))     # noqa: E501, E221
    username            = models.TextField(blank=True, null=True, verbose_name=_('User Name'))         # noqa: E501, E221
    domain              = models.TextField(blank=True, null=True, verbose_name=_('Domain'))            # noqa: E501, E221
    uuid                = models.TextField(blank=True, null=True, verbose_name=_('UUId'))              # noqa: E501, E221
    cid_name            = models.TextField(blank=True, null=True, verbose_name=_('CID Name'))          # noqa: E501, E221
    cid_number          = models.TextField(blank=True, null=True, verbose_name=_('CID Number'))        # noqa: E501, E221
    in_folder           = models.TextField(blank=True, null=True, verbose_name=_('In Folder'))         # noqa: E501, E221
    file_path           = models.TextField(blank=True, null=True, verbose_name=_('File Path'))         # noqa: E501, E221
    message_len         = models.IntegerField(blank=True, null=True, verbose_name=_('Message Length')) # noqa: E501, E221
    flags               = models.TextField(blank=True, null=True, verbose_name=_('Flags'))             # noqa: E501, E221
    read_flags          = models.TextField(blank=True, null=True, verbose_name=_('Read Flags'))        # noqa: E501, E221
    forwarded_by        = models.TextField(blank=True, null=True, verbose_name=_('Forwarded By'))      # noqa: E501, E221
    voicemail_msgs_uuid = models.UUIDField(db_column='voicemail_msgs_uuid', primary_key=True, editable=False, verbose_name=_('Voicemail Message Id')) # noqa: E501, E221

    class Meta:
        managed = False
        verbose_name_plural = 'Voicemail Messages'
        db_table = 'voicemail_msgs'
        """
        indexes = [
            models.Index(fields=['created_epoch'], name='voicemail_msgs_idx1'),
            models.Index(fields=['username'], name='voicemail_msgs_idx2'),
            models.Index(fields=['domain'], name='voicemail_msgs_idx3'),
            models.Index(fields=['uuid'], name='voicemail_msgs_idx4'),
            models.Index(fields=['in_folder'], name='voicemail_msgs_idx5'),
            models.Index(fields=['read_flags'], name='voicemail_msgs_idx6'),
            models.Index(fields=['forwarded_by'], name='voicemail_msgs_idx7'),
            models.Index(fields=['read_epoch'], name='voicemail_msgs_idx8'),
            models.Index(fields=['flags'], name='voicemail_msgs_idx9'),
        ]
        """

    def __str__(self):
        return str(self.voicemail_msgs_uuid)


class VoicemailPrefs(models.Model):
    username             = models.TextField(blank=True, null=True, verbose_name=_('User Name'))     # noqa: E501, E221
    domain               = models.TextField(blank=True, null=True, verbose_name=_('Domain'))        # noqa: E501, E221
    name_path            = models.TextField(blank=True, null=True, verbose_name=_('Name Path'))     # noqa: E501, E221
    greeting_path        = models.TextField(blank=True, null=True, verbose_name=_('Greeting Path')) # noqa: E501, E221
    password             = models.TextField(blank=True, null=True, verbose_name=_('Password'))      # noqa: E501, E221
    voicemail_prefs_uuid = models.UUIDField(db_column='voicemail_prefs_uuid', primary_key=True, editable=False, verbose_name=_('Voicemail Pref Id')) # noqa: E501, E221

    class Meta:
        managed = False
        db_table = 'voicemail_prefs'
        verbose_name_plural = 'Voicemail Prefs'
        """
        indexes = [
            models.Index(fields=['username'], name='voicemail_prefs_idx1'),
            models.Index(fields=['domain'], name='voicemail_prefs_idx2'),
        ]
        """

    def __str__(self):
        return str(self.voicemail_prefs_uuid)
