Summary:	KDE MIDI Metronome using ALSA Sequencer
Name:		kmetronome
Version:	0.10.1
Release:	2
License:	GPLv2+
Group:		Sound
Url:		http://kmetronome.sourceforge.net
Source0:	http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(alsa) >= 1.0.0
BuildRequires:	pkgconfig(drumstick-alsa) >= 0.5.0
Requires:	drumstick

%description
KMetronome is a MIDI metronome with KDE interface, based on the ALSA
sequencer. The intended audience is musicians and music students. Like solid,
real metronomes it is a tool to keep the rhythm while playing musical
instruments. It uses MIDI for sound generation instead of digital audio,
allowing low CPU usage, and very accurate timing thanks to the ALSA sequencer.

%files -f %{name}.lang
%doc README ChangeLog AUTHORS TODO
%{_bindir}/%{name}
%{_datadir}/applications/*/%{name}.desktop
%{_datadir}/dbus-1/*/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/apps/*/*
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%prep
%setup -q
# make sure that the bundled drumstick isn't used
rm -rf drumstick

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html

