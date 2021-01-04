
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Name:		kmetronome
Version:	1.2.1
Release:	1
License:	GPLv2+
Summary:	KDE MIDI Metronome using ALSA Sequencer
Group:		Sound
Url:		https://kmetronome.sourceforge.io/
Source0:	https://download.sourceforge.net/kmetronome/%{name}-%{version}.tar.bz2

BuildRequires:	cmake
BuildRequires:	gettext
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(drumstick-alsa)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Widgets)


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
%cmake_qt5
%make_build

%install
%make_install -C build

%files
%doc ChangeLog AUTHORS NEWS doc/%{name}.html doc/%{name}*.png
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/*/net.sourceforge.%{name}*
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1*

