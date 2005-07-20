
dnl  Copyright 2005 Red Hat, Inc.
dnl 
dnl  Permission to use, copy, modify, distribute, and sell this software and its
dnl  documentation for any purpose is hereby granted without fee, provided that
dnl  the above copyright notice appear in all copies and that both that
dnl  copyright notice and this permission notice appear in supporting
dnl  documentation, and that the name of Red Hat not be used in
dnl  advertising or publicity pertaining to distribution of the software without
dnl  specific, written prior permission.  Red Hat makes no
dnl  representations about the suitability of this software for any purpose.  It
dnl  is provided "as is" without express or implied warranty.
dnl 
dnl  RED HAT DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
dnl  INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO
dnl  EVENT SHALL RED HAT BE LIABLE FOR ANY SPECIAL, INDIRECT OR
dnl  CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
dnl  DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
dnl  TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
dnl  PERFORMANCE OF THIS SOFTWARE.
dnl
dnl Process this file with autoconf to create configure.

AC_PREREQ([2.57])
AC_INIT(xdpyinfo,[7.0], [xorg@freedesktop.org],xdpyinfo)
AM_INIT_AUTOMAKE([dist-bzip2])
AM_MAINTAINER_MODE

AM_CONFIG_HEADER(config.h)

AC_PROG_CC
AC_PROG_INSTALL

# Checks for pkg-config packages
PKG_CHECK_MODULES(XDPYINFO, xext x11 xtst)
AC_SUBST(XDPYINFO_CFLAGS)
AC_SUBST(XDPYINFO_LIBS)

PKG_CHECK_MODULES(XEXT, xextproto xext,
	[SAVE_CPPFLAGS="$CPPFLAGS"
	CPPFLAGS="$CPPFLAGS $XEXTPROTO_CFLAGS"
	AC_CHECK_HEADERS([X11/extensions/multibuf.h X11/extensions/XShm.h],,,[#include <X11/Xlib.h>])
	CPPFLAGS="$SAVE_CPPFLAGS"],[echo "not found"])

PKG_CHECK_MODULES(XKB, kbproto x11, 
	[SAVE_CPPFLAGS="$CPPFLAGS"
	CPPFLAGS="$CPPFLAGS $XKB_CFLAGS"
	AC_CHECK_HEADERS([X11/extensions/XKB.h X11/XKBlib.h],,,[#include <X11/Xlib.h>])
	CPPFLAGS="$SAVE_CPPFLAGS"],[echo "not found"])

PKG_CHECK_MODULES(XF86VIDMODE, xf86vidmodeproto xxf86vm, 
	[SAVE_CPPFLAGS="$CPPFLAGS"
	CPPFLAGS="$CPPFLAGS $XF86VIDMODE_CFLAGS"
	AC_CHECK_HEADERS([X11/extensions/xf86vmode.h X11/extensions/xf86vmstr.h],,,[#include <X11/Xlib.h>])
	CPPFLAGS="$SAVE_CPPFLAGS"],[echo "not found"])

PKG_CHECK_MODULES(XF86DGA, xf86dgaproto xxf86dga, 
	[SAVE_CPPFLAGS="$CPPFLAGS"
	CPPFLAGS="$CPPFLAGS $XF86DGA_CFLAGS"
	AC_CHECK_HEADERS([X11/extensions/xf86dga.h X11/extensions/xf86dgastr.h],,,
			 [#include <X11/Xlib.h>
#include <X11/Xproto.h>])
	CPPFLAGS="$SAVE_CPPFLAGS"],[echo "not found"])

PKG_CHECK_MODULES(XF86MISC, xf86miscproto xxf86misc, 
	[SAVE_CPPFLAGS="$CPPFLAGS"
	CPPFLAGS="$CPPFLAGS $XF86MISC_CFLAGS"
	AC_CHECK_HEADERS([X11/extensions/xf86misc.h X11/extensions/xf86mscstr.h],,,
			  [#include <X11/Xlib.h>
#include <X11/Xproto.h>])
	CPPFLAGS="$SAVE_CPPFLAGS"],[echo "not found"])

PKG_CHECK_MODULES(XINPUT, inputproto xi, 
	[SAVE_CPPFLAGS="$CPPFLAGS"
	CPPFLAGS="$CPPFLAGS $XINPUT_CFLAGS"
	AC_CHECK_HEADERS([X11/extensions/XInput.h],,,[#include <X11/Xlib.h>])
	CPPFLAGS="$SAVE_CPPFLAGS"],[echo "not found"])

PKG_CHECK_MODULES(XRENDER, renderproto xrender, 
	[SAVE_CPPFLAGS="$CPPFLAGS"
	CPPFLAGS="$CPPFLAGS $XRENDER_CFLAGS"
	AC_CHECK_HEADERS([X11/extensions/Xrender.h],,,[#include <X11/Xlib.h>])
	CPPFLAGS="$SAVE_CPPFLAGS"],[echo "not found"])

PKG_CHECK_MODULES(XINERAMA, panoramixproto xinerama, 
	[SAVE_CPPFLAGS="$CPPFLAGS"
	CPPFLAGS="$CPPFLAGS $XINERAMA_CFLAGS"
	AC_CHECK_HEADERS([X11/extensions/Xinerama.h],,,[#include <X11/Xlib.h>])
	CPPFLAGS="$SAVE_CPPFLAGS"],[echo "not found"])

PKG_CHECK_MODULES(DMX, dmxproto dmx, 
	[SAVE_CPPFLAGS="$CPPFLAGS"
	CPPFLAGS="$CPPFLAGS $DMX_CFLAGS"
	AC_CHECK_HEADERS([X11/extensions/dmxext.h],,,[#include <X11/Xlib.h>])
	CPPFLAGS="$SAVE_CPPFLAGS"],[echo "not found"])

PKG_CHECK_MODULES(XPRINT, printproto xp, 
	[SAVE_CPPFLAGS="$CPPFLAGS"
	CPPFLAGS="$CPPFLAGS $XPRINT_CFLAGS"
	AC_CHECK_HEADERS([X11/extensions/Print.h],,,[#include <X11/Xlib.h>])
	CPPFLAGS="$SAVE_CPPFLAGS"],[echo "not found"])

AC_OUTPUT([Makefile])
