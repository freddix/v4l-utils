Summary:	Userspace tools and conversion library for Video 4 Linux
Name:		v4l-utils
Version:	1.6.2
Release:	1
License:	GPL v2+ (utilities), LGPL v2.1+ (libraries)
Group:		Applications/System
Source0:	http://linuxtv.org/downloads/v4l-utils/%{name}-%{version}.tar.bz2
# Source0-md5:	9cb3c178f937954e65bf30920af433ef
URL:		http://freshmeat.net/projects/libv4l
BuildRequires:	QtGui-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	qt-build
BuildRequires:	xorg-libX11-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
v4l-utils is a collection of various video4linux (V4L) and DVB
utilities. libv4l is an accompanying collection of libraries that adds
a thin abstraction layer on top of video4linux2 (V4L2) devices.
The purpose of this layer is to make it easy for application writers
to support a wide variety of devices without having to write separate
code for different devices in the same class.
tools to test V4L devices.

%package libs
Summary:	Abstraction layer on top of video4linux2 devices
License:	LGPL v2.1+
Group:		Libraries

%description libs
This package consists of 3 different libraries. libv4lconvert offers
functions to convert from any (known) pixel format to
V4l2_PIX_FMT_BGR24 or V4l2_PIX_FMT_YUV420. libv4l1 offers the
(deprecated) v4l1 API on top of v4l2 devices, independent of the
drivers for those devices supporting v4l1 compatibility (which many
v4l2 drivers do not). libv4l2 offers the v4l2 API on top of v4l2
devices, while adding support for the application transparent
libv4lconvert conversion where necessary.

%package devel
Summary:	Header files for libv4l libraries
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for libv4l libraries.

%package gui
Summary:	GUI for v4l-utils
License:	GPL v2+
Group:		X11/Applications
Requires:	%{name}-libs = %{version}-%{release}
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme

%description gui
A Qt based frontend to v4l-utils.

%package ir-keytable
Summary:	Swiss-knife tool to handle Remote Controllers
License:	GPL v2+
Group:		Applications

%description ir-keytable
ir-keytable is a tool that lists the Remote Controller devices, allows
one to get/set IR keycode/scancode tables, test events generated by
IR and to adjust other Remote Controller options.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%post gui
%update_icon_cache hicolor

%postun gui
%update_icon_cache hicolor

%post   libs -p /usr/sbin/ldconfig
%postun libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO contrib
%attr(755,root,root) %{_bindir}/cx18-ctl
%attr(755,root,root) %{_bindir}/decode_tm6000
%attr(755,root,root) %{_bindir}/dvb-fe-tool
%attr(755,root,root) %{_bindir}/dvb-format-convert
%attr(755,root,root) %{_bindir}/dvbv5-scan
%attr(755,root,root) %{_bindir}/dvbv5-zap
%attr(755,root,root) %{_bindir}/ivtv-ctl
%attr(755,root,root) %{_bindir}/media-ctl
%attr(755,root,root) %{_bindir}/rds-ctl
%attr(755,root,root) %{_bindir}/v4l2-compliance
%attr(755,root,root) %{_bindir}/v4l2-ctl
%attr(755,root,root) %{_bindir}/v4l2-sysfs-path
%attr(755,root,root) %{_sbindir}/v4l2-dbg

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libv4l1.so.0
%attr(755,root,root) %ghost %{_libdir}/libv4l2.so.0
%attr(755,root,root) %ghost %{_libdir}/libv4l2rds.so.0
%attr(755,root,root) %ghost %{_libdir}/libv4lconvert.so.0
%attr(755,root,root) %{_libdir}/libv4l1.so.*.*.*
%attr(755,root,root) %{_libdir}/libv4l2.so.*.*.*
%attr(755,root,root) %{_libdir}/libv4l2rds.so.*.*.*
%attr(755,root,root) %{_libdir}/libv4lconvert.so.*.*.*

%attr(755,root,root) %{_libdir}/v4l1compat.so
%attr(755,root,root) %{_libdir}/v4l2convert.so

%dir %{_libdir}/libv4l
%attr(755,root,root) %{_libdir}/libv4l/ov511-decomp
%attr(755,root,root) %{_libdir}/libv4l/ov518-decomp
%attr(755,root,root) %{_libdir}/libv4l/v4l1compat.so
%attr(755,root,root) %{_libdir}/libv4l/v4l2convert.so

%dir %{_libdir}/libv4l/plugins
%attr(755,root,root) %{_libdir}/libv4l/plugins/libv4l-mplane.so

%files devel
%defattr(644,root,root,755)
%doc README.lib*
%attr(755,root,root) %{_libdir}/libv4l1.so
%attr(755,root,root) %{_libdir}/libv4l2.so
%attr(755,root,root) %{_libdir}/libv4l2rds.so
%attr(755,root,root) %{_libdir}/libv4lconvert.so
%{_includedir}/libv4l*.h
%{_pkgconfigdir}/*.pc

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qv4l2
%{_desktopdir}/qv4l2.desktop
%{_iconsdir}/hicolor/*/apps/qv4l2.*

%files ir-keytable
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ir-keytable
%dir %{_sysconfdir}/rc_keymaps
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rc_maps.cfg
%{_prefix}/lib/udev/rc_keymaps
%{_prefix}/lib/udev/rules.d/70-infrared.rules
%{_mandir}/man1/ir-keytable.1*

