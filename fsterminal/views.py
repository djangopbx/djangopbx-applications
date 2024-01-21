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

import socket
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.views.decorators import staff_member_required
from pbx.commonfunctions import shcommand


@staff_member_required
def fsterminal(request):

    try:
        hostname = socket.gethostname()
    except:
        hostname = 'localhost'
    prompt = 'freeswitch@%s' % hostname
    promptlen = len(prompt) + 2

    return render(request, 'fsterminal/term.html', {'prompt': prompt, 'promptlen': promptlen})

@staff_member_required
def fsterminalcmd(request):
    cmdstr = request.GET.get('fscmd', '')
    if len(cmdstr) < 1:
        return HttpResponse(_('command not found.'), content_type='text/plain')
    if cmdstr.startswith('/event'):
        return HttpResponse(_('Cannot listen to events in this terminal.'), content_type='text/plain')
    if cmdstr.startswith('/quit'):
        return HttpResponse('\033[H\033[J%s' % _('Goodbye. Choose a new screen from the navigation bar.'), content_type='text/plain')
    if cmdstr == 'clear' or cmdstr == 'cls':
        return HttpResponse('\033[H\033[J', content_type='text/plain')

    cmdoutput = shcommand(
        ['/usr/local/bin/fscmd.sh', cmdstr]
        )
    return HttpResponse(cmdoutput, content_type='text/plain')
