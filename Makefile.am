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
	$(XDPYINFO_CFLAGS) \
	$(DPY_XEXT_CFLAGS) \
	$(DPY_XKB_CFLAGS) \
	$(DPY_XF86VIDMODE_CFLAGS) \
	$(DPY_XF86DGA_CFLAGS) \
	$(DPY_XF86MISC_CFLAGS) \
	$(DPY_XINPUT_CFLAGS) \
	$(DPY_XRENDER_CFLAGS) \
	$(DPY_XINERAMA_CFLAGS) \
	$(DPY_DMX_CFLAGS) \
	$(DPY_XPRINT_CFLAGS)
	
xdpyinfo_LDADD = \
	$(XDPYINFO_LIBS) \
	$(DPY_XEXT_LIBS) \
	$(DPY_XKB_LIBS) \
	$(DPY_XF86VIDMODE_LIBS) \
	$(DPY_XF86DGA_LIBS) \
	$(DPY_XF86MISC_LIBS) \
	$(DPY_XINPUT_LIBS) \
	$(DPY_XRENDER_LIBS) \
	$(DPY_XINERAMA_LIBS) \
	$(DPY_DMX_LIBS) \
	$(DPY_XPRINT_LIBS)

xdpyinfo_SOURCES =	\
        xdpyinfo.c

dist_man1_MANS = \
        xdpyinfo.man

