# 
#  Copyright 2005  Red Hat, Inc.
# 
#  Permission to use, copy, modify, distribute, and sell this software and its
#  documentation for any purpose is hereby granted without fee, provided that
#  the above copyright notice appear in all copies and that both that
#  copyright notice and this permission notice appear in supporting
#  documentation, and that the name of Red Hat not be used in
#  advertising or publicity pertaining to distribution of the software without
#  specific, written prior permission.  Red Hat makes no
#  representations about the suitability of this software for any purpose.  It
#  is provided "as is" without express or implied warranty.
# 
#  RED HAT DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
#  INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO
#  EVENT SHALL RED HAT BE LIABLE FOR ANY SPECIAL, INDIRECT OR
#  CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
#  DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
#  TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
#  PERFORMANCE OF THIS SOFTWARE.

bin_PROGRAMS = xdpyinfo

AM_CFLAGS = \
	$(DEP_CFLAGS) \
	$(XEXT_CFLAGS) \
	$(XKB_CFLAGS) \
	$(XF86VIDMODE_CFLAGS) \
	$(XF86DGA_CFLAGS) \
	$(XF86MISC_CFLAGS) \
	$(XINPUT_CFLAGS) \
	$(XRENDER_CFLAGS) \
	$(XINERAMA_CFLAGS) \
	$(DMX_CFLAGS) \
	$(XPRINT_CFLAGS)
	
xdpyinfo_LDADD = \
	$(DEP_LIBS) \
	$(XEXT_LIBS) \
	$(XKB_LIBS) \
	$(XF86VIDMODE_LIBS) \
	$(XF86DGA_LIBS) \
	$(XF86MISC_LIBS) \
	$(XINPUT_LIBS) \
	$(XRENDER_LIBS) \
	$(XINERAMA_LIBS) \
	$(DMX_LIBS) \
	$(XPRINT_LIBS)

xdpyinfo_SOURCES =	\
        xdpyinfo.c

dist_man1_MANS = \
        xdpyinfo.man

