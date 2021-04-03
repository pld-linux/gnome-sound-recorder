Summary:	GNOME Sound Recorder - a simple, modern sound recorder
Summary(pl.UTF-8):	GNOME Sound Recorder - prosty, nowoczesny program do nagrywania dźwięku
Name:		gnome-sound-recorder
Version:	40.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	https://download.gnome.org/sources/gnome-sound-recorder/40/%{name}-%{version}.tar.xz
# Source0-md5:	238c952ac95cf6019c1ef135b9a98211
URL:		https://wiki.gnome.org/Apps/SoundRecorder
BuildRequires:	gettext-tools
BuildRequires:	gjs-devel >= 1.54.0
BuildRequires:	glib2-devel >= 1:2.46
BuildRequires:	gobject-introspection-devel >= 1.32
# pkgconfig(gstreamer-player-1.0)
BuildRequires:	gstreamer-plugins-bad-devel >= 1.12
BuildRequires:	gtk+3-devel >= 3.13.2
BuildRequires:	libhandy1-devel >= 1.1.90
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.46
Requires(post,postun):	gtk-update-icon-cache
Requires:	gdk-pixbuf2 >= 2.0
Requires:	gjs >= 1.54.0
Requires:	glib2 >= 1:2.46
# base + elements: filesink
Requires:	gstreamer >= 1.12
# elements: volume
Requires:	gstreamer-audio-effects-base >= 1.12
# elements: level
Requires:	gstreamer-audio-effects-good >= 1.12
# libgstplayer, application/x-id3
Requires:	gstreamer-plugins-bad >= 1.12
# elements: audioconvert encodebin playbin
Requires:	gstreamer-plugins-base >= 1.12
# elements: pulsesink pulsesrc
Requires:	gstreamer-pulseaudio >= 1.12
Requires:	gtk+3 >= 3.13.2
Requires:	hicolor-icon-theme
Requires:	libhandy1 >= 1.1.90
# audio/x-flac
Suggests:	gstreamer-flac >= 1.12
# audio/mpeg,mpegversion=(int)1,layer=(int)3
Suggests:	gstreamer-mpg123 >= 1.12
# audio/x-opus
Suggests:	gstreamer-opus >= 1.12
# video/quicktime,variant=(string)iso, audio/mpeg,mpegversion=(int)4
Suggests:	gstreamer-plugins-good >= 1.12
# application/ogg, application/ogg;audio/ogg;video/ogg, audio/x-vorbis
Suggests:	gstreamer-vorbis >= 1.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Sound Recorder is a simple, modern sound recorder.

%description -l pl.UTF-8
GNOME Sound Recorder to prosty, nowoczesny program do nagrywania
dźwięku.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang org.gnome.SoundRecorder

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f org.gnome.SoundRecorder.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-sound-recorder
%{_datadir}/glib-2.0/schemas/org.gnome.SoundRecorder.gschema.xml
%{_datadir}/metainfo/org.gnome.SoundRecorder.metainfo.xml
%dir %{_datadir}/org.gnome.SoundRecorder
%attr(755,root,root) %{_datadir}/org.gnome.SoundRecorder/org.gnome.SoundRecorder
%{_datadir}/org.gnome.SoundRecorder/org.gnome.SoundRecorder.*.gresource
%{_desktopdir}/org.gnome.SoundRecorder.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.SoundRecorder.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.SoundRecorder-symbolic.svg
