Summary:	GNOME Sound Recorder - a simple, modern sound recorder
Summary(pl.UTF-8):	GNOME Sound Recorder - prosty, nowoczesny program do nagrywania dźwięku
Name:		gnome-sound-recorder
Version:	3.34.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-sound-recorder/3.34/%{name}-%{version}.tar.xz
# Source0-md5:	8e067d3451e4c0494119b0e6ae56802c
URL:		https://wiki.gnome.org/Apps/SoundRecorder
BuildRequires:	gettext-tools
BuildRequires:	gjs-devel >= 1.48.0
BuildRequires:	glib2-devel >= 1:2.46
BuildRequires:	gobject-introspection-devel >= 1.32
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gtk+3-devel >= 3.13.2
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.46
Requires(post,postun):	gtk-update-icon-cache
Requires:	gdk-pixbuf2 >= 2.0
Requires:	gjs >= 1.48.0
Requires:	glib2 >= 1:2.46
# base + elements: filesink
Requires:	gstreamer >= 1.0
# elements: volume
Requires:	gstreamer-audio-effects-base >= 1.0
# elements: level
Requires:	gstreamer-audio-effects-good >= 1.0
# elements: audioconvert encodebin playbin
Requires:	gstreamer-plugins-base >= 1.0
# elements: pulsesink pulsesrc
Requires:	gstreamer-pulseaudio >= 1.0
Requires:	gtk+3 >= 3.13.2
Requires:	hicolor-icon-theme
# audio/x-flac
Suggests:	gstreamer-flac >= 1.0
# audio/mpeg,mpegversion=(int)1,layer=(int)3
Suggests:	gstreamer-mpg123 >= 1.0
# audio/x-opus
Suggests:	gstreamer-opus >= 1.0
# application/x-id3
Suggests:	gstreamer-plugins-bad >= 1.0
# video/quicktime,variant=(string)iso, audio/mpeg,mpegversion=(int)4
Suggests:	gstreamer-plugins-good >= 1.0
# application/ogg, application/ogg;audio/ogg;video/ogg, audio/x-vorbis
Suggests:	gstreamer-vorbis >= 1.0
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
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-sound-recorder
%{_datadir}/glib-2.0/schemas/org.gnome.SoundRecorder.gschema.xml
%{_datadir}/metainfo/org.gnome.SoundRecorder.appdata.xml
%dir %{_datadir}/org.gnome.SoundRecorder
%attr(755,root,root) %{_datadir}/org.gnome.SoundRecorder/org.gnome.SoundRecorder
%{_datadir}/org.gnome.SoundRecorder/org.gnome.SoundRecorder.*.gresource
%{_desktopdir}/org.gnome.SoundRecorder.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.SoundRecorder.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.SoundRecorder-symbolic.svg
