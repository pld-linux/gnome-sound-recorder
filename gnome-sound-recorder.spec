Summary:	GNOME Sound Recorder - a simple, modern sound recorder
Summary(pl.UTF-8):	GNOME Sound Recorder - prosty, nowoczesny program do nagrywania dźwięku
Name:		gnome-sound-recorder
Version:	3.28.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-sound-recorder/3.28/%{name}-%{version}.tar.xz
# Source0-md5:	b9d14e08fd93cfca5bbcdc1b16da10b2
Patch0:		%{name}-ac.patch
URL:		https://wiki.gnome.org/Design/Apps/SoundRecorder
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.46
BuildRequires:	gobject-introspection-devel >= 1.32
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gtk+3-devel >= 3.12
BuildRequires:	intltool >= 0.26
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.46
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.46
Requires:	gstreamer >= 1.0
# elements: flacenc flacparse
Requires:	gstreamer-flac >= 1.0
# elements: audioconvert playbin uridecodebin
Requires:	gstreamer-plugins-base >= 1.0
# elements: qtdemux qtmux
Requires:	gstreamer-plugins-good >= 1.0
# elements: oggdemux
Requires:	gstreamer-vorbis >= 1.0
Requires:	gtk+3 >= 3.12
Requires:	hicolor-icon-theme
# elements: id3mux
Suggests:	gstreamer-plugins-bad >= 1.0
Suggests:	gstreamer-pulseaudio >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Sound Recorder is a simple, modern sound recorder.

%description -l pl.UTF-8
GNOME Sound Recorder to prosty, nowoczesny program do nagrywania
dźwięku.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	GJS=/usr/bin/gjs \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gnome-sound-recorder
%{_datadir}/metainfo/org.gnome.SoundRecorder.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-sound-recorder.gschema.xml
%dir %{_datadir}/gnome-sound-recorder
%attr(755,root,root) %{_datadir}/gnome-sound-recorder/org.gnome.SoundRecorder
%{_datadir}/gnome-sound-recorder/org.gnome.SoundRecorder.src.gresource
%{_datadir}/gnome-sound-recorder/application.css
%{_desktopdir}/org.gnome.SoundRecorder.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.SoundRecorder.png
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.SoundRecorder-symbolic.svg
