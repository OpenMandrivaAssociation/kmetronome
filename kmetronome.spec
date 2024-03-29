
#define _enable_debug_packages %{nil}
#define debug_package %{nil}
%define _empty_manifest_terminate_build 0

Name:		kmetronome
Version:	1.4.0
Release:	1
License:	GPLv2+
Summary:	KDE MIDI Metronome using ALSA Sequencer
Group:		Sound
Url:		https://kmetronome.sourceforge.io/
Source0:	https://download.sourceforge.net/kmetronome/%{name}-%{version}.tar.bz2

BuildRequires:	cmake
BuildRequires:  cmake(Qt6)
BuildRequires:  qmake-qt6
BuildRequires:	gettext
BuildRequires:  qt6-qtbase-theme-gtk3
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(drumstick-alsa)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Help)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:	cmake(Qt6Widgets)


%description
KMetronome is a MIDI metronome with KDE interface, based on the ALSA
sequencer. The intended audience is musicians and music students. Like solid,
real metronomes it is a tool to keep the rhythm while playing musical
instruments. It uses MIDI for sound generation instead of digital audio,
allowing low CPU usage, and very accurate timing thanks to the ALSA
sequencer.


%prep
%autosetup -p1

%build
%cmake -DBUILD_DOCS=OFF
%make_build

%install
%make_install -C build

%files
%doc ChangeLog AUTHORS NEWS
%doc %{_datadir}/doc/kmetronome/kmetronome/*/index.html
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/net.sourceforge.kmetronome.desktop
%{_datadir}/dbus-1/*/net.sourceforge.%{name}*
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1*
%{_datadir}/metainfo/net.sourceforge.kmetronome.metainfo.xml
