Name:		kmetronome
Version:	0.10.1
Release:	%mkrel 1
License:	GPLv2+
Summary:	KDE MIDI Metronome using ALSA Sequencer
Group:		Sound
URL:		http://kmetronome.sourceforge.net
Source0:	http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	gettext
BuildRequires:	qt4-devel
BuildRequires:	kdesdk4-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(alsa) >= 1.0.0
BuildRequires:	pkgconfig(drumstick-alsa) >= 0.5.0
#Requires:	kdebase4-runtime
Requires:	drumstick >= 0.5.0


%description
KMetronome is a MIDI metronome with KDE interface, based on the ALSA
sequencer. The intended audience is musicians and music students. Like solid,
real metronomes it is a tool to keep the rhythm while playing musical
instruments. It uses MIDI for sound generation instead of digital audio,
allowing low CPU usage, and very accurate timing thanks to the ALSA sequencer.


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


%files -f %{name}.lang
%doc README ChangeLog AUTHORS TODO
%doc %{_mandir}/man1/*
%dir %{_datadir}/apps/%{name}
%dir %{_datadir}/icons/hicolor/24x24
%dir %{_datadir}/icons/hicolor/24x24/apps
%dir %{_datadir}/locale/*/*
%{_bindir}/%{name}
# Already provided by %%find_lang macro
#{_datadir}/locale/*
#{_datadir}/doc/HTML/en/%%{name}/*
%{_datadir}/applications/*/%{name}.desktop
%{_datadir}/dbus-1/*/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/apps/*/*


%changelog
* Fri Feb 01 2013 Giovanni Mariani <mc2374@mclink.it> 0.10.1-1
- Imported in Rosa 2012.1