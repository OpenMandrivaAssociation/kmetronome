#define _enable_debug_packages %%{nil}
#define debug_package %%{nil}
#define _empty_manifest_terminate_build 0

Summary:		QT MIDI Metronome using ALSA Sequencer
Name:		kmetronome
Version:		1.4.1
Release:		1
License:		GPLv2+
Url:		https://kmetronome.sourceforge.io/
Group:		Sound
Source0:	https://download.sourceforge.net/kmetronome/%{name}-%{version}.tar.bz2
BuildRequires:		cmake >= 3.16
BuildRequires:		gettext
BuildRequires:		gzip-utils
BuildRequires:		qmake-qt6
BuildRequires:		qt6-qtbase-theme-gtk3
BuildRequires:		cmake(Qt6Core) >= 6.2
BuildRequires:		cmake(Qt6DBus)
BuildRequires:		cmake(Qt6Gui)
BuildRequires:		cmake(Qt6Help)
BuildRequires:		cmake(Qt6LinguistTools)
BuildRequires:		cmake(Qt6Svg)
BuildRequires:		cmake(Qt6SvgWidgets)
BuildRequires:		cmake(Qt6Widgets)
BuildRequires:		pkgconfig(alsa)
BuildRequires:		pkgconfig(drumstick-alsa) >= 2.10.0
BuildRequires:		pkgconfig(vulkan)
BuildRequires:		pkgconfig(xkbcommon-x11)
Requires:	drumstick >= 2.10.0

%description
A MIDI metronome with QT interface, based on the ALSA sequencer. The intended
audience is musicians and music students. Like solid, real metronomes it is
a tool to keep the rhythm while playing musical instruments. It uses MIDI for
sound generation instead of digital audio, allowing low CPU usage, and very
accurate timing thanks to the ALSA sequencer.

%files
%license COPYING
%doc ChangeLog AUTHORS NEWS
%doc %{_datadir}/doc/%{name}/%{name}/*/index.html
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/net.sourceforge.%{name}.desktop
%{_datadir}/dbus-1/*/net.sourceforge.%{name}*
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1*
%{_datadir}/metainfo/net.sourceforge.%{name}.metainfo.xml

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%cmake -DBUILD_DOCS=OFF -DUSE_QT5=NO
%make_build


%install
%make_install -C build

# Fix gzipped-svg-icon
(
cd %{buildroot}%{_iconsdir}/hicolor/scalable/apps/
zcat %{name}.svgz > %{name}.svg && rm -f %{name}.svgz
)
