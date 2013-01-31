%define	use_ccache	1
%define	ccachedir	~/.ccache-OOo%{mdvsuffix}%{?_with_ccache: %global use_ccache 1}%{?_without_ccache: %global use_ccache 0}
%define			_enable_debug_packages	%{nil}
%define			debug_package		%{nil}
%define			distsuffix		mib

Name:		kmetronome
Version:	0.10.1
Release:	%mkrel 69.1
License:	GPLv2+
Summary:	KDE MIDI Metronome using ALSA Sequencer
Group:		Sound
URL:		http://kmetronome.sourceforge.net
Source:		http://sourceforge.net/projects/kmetronome/files/kmetronome/0.10.0/%{name}-%{version}.tar.bz2
BuildRequires:	gettext
BuildRequires:	qt4-devel
BuildRequires:	kdesdk4-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	libalsa-devel >= 1.0.0
BuildRequires:	drumstick-devel >= 0.5.0
#Requires:	kdebase4-runtime
Requires:	drumstick >= 0.5.0


%description
KMetronome is a MIDI metronome with KDE interface, based on the ALSA
sequencer. The intended audience is musicians and music students. Like solid,
real metronomes it is a tool to keep the rhythm while playing musical
instruments. It uses MIDI for sound generation instead of digital audio,
allowing low CPU usage, and very accurate timing thanks to the ALSA
sequencer.


%prep
%setup -q %{name}-%{version}-%{release}
# make sure bundled drumstick isn't used
rm -rf drumstick


%build
%cmake_kde4
%make


%install
%makeinstall_std -C build
%find_lang %{name}


%files -f %{name}.lang
%doc README ChangeLog AUTHORS TODO
%doc %{_mandir}/man1/*
%dir %{_datadir}/apps/%{name}
%dir %{_datadir}/icons/hicolor/24x24
%dir %{_datadir}/icons/hicolor/24x24/apps
%dir %{_datadir}/locale/*/*
%{_bindir}/%{name}
#{_datadir}/locale/*
%{_datadir}/doc/HTML/en/%{name}/*
%{_datadir}/applications/*/%{name}.desktop
%{_datadir}/dbus-1/*/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/apps/*/*


%changelog
* Sun Dec 30 2012 Giovanni Mariani <mc2374@mclink.it> 0.10.1-69.1
- Rebuilt for Rosa 2012.1 by the MIB

* Wed May 30 2012 Giovanni Mariani <mc2374@mclink.it> 0.10.1-69.1mib2010.2
- New release 0.10.1

* Mon Aug 2 2010 Giovanni Mariani <mc2374@mclink.it> 0.10.0-69.1mib2010.1
- Rebuilding for Mdv 2010.1
- Made some cosmetic changes to spec file
- Made Description text lines < than 76 chars long (according Wiki specs)
- Made the License tag rpmlint-compliant
- Killed some redundant defines (name, version...)
- Removed hardcoded Packager tag (to satisfy rpmlint)
- Made BuildRoot tag compliant with Wiki specs
- Changed Group tag to a standard one (to satisfy rpmlint)
- Added version to cmake BuildRequires (see INSTALL file in the sources)
- Added some needed BuilRequires and Requires (see README file in the sources)
- Added version info for alsa and drumstick libraries (according configure output)
- Removed BuilRequires and Requires for webkitkde (not listed in README/INSTALL)
- Made use of correct alias in BuildRequires to assure building on both 32 & 64 bit
- Removed the bundled drumstick source to make use of the system one
- Silenced some more rpmlint warning (files-not-in-lang and empty-post[un])

* Mon Jun 7 2010 Calogero Scarnà <specialworld83@gmail.com> 0.10.0-69mib2010.0
- new package Mandriva Italia Backport
