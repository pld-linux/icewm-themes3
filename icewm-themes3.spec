Summary:	Pack of themes for icewm
Summary(pl):	Zestaw tematów dla icewm
Name:		icewm-themes-pack3
Version:	1.0
Release:	2
BuildArch:      noarch
License:	GPL (?)
Group:		Themes
Group(de):	Themen
Group(pl):	Motywy
Source0:	%{name}.tar.gz

Requires:	icewm
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themesdir	/usr/X11R6/lib/X11/icewm/themes

%description 
This is a set of 25 themes for icewm.
Thane			Xerithane <xerithane@nerdfarm.org>
crud			<dwl@wolsi.com>
Getaway			Xerithane <xerithane@nerdfarm.org>
houseMoneyBlessing	?
iMac-lol		RB_____ from the Jim-mac theme of Jakub Steiner
lameh			artwiz
aQua			CW Zuckschwerdt <zany@triq.net>
mechasan		Pal Palocz <palocz.pal@mail.deltav.hu>
Strange Dreams (MJ-5)	RudeSka
stric			<johannes@defcom.se>
Tile			Daniel W. Lemon  <dwl@wolsi.com>
Timesteps		<dwl@wolsi.com>
transistor		kraftBoy <gthomson@targetnet.com
tubes			Sawsedge <sawsedge@yahoo.com>
UFO Sightings (MJ-6)	RudeSka
Unusual Scars		RudeSka
Whistling		<dwl@wolsi.com>
William3		William Wieboldt (Poke'mon Master) <waw@iname.com>
Windows 3.1		Toaster T. Toaster <toaster@kami.com>
WMgtk			enterfornone <efn@themes.org>
WM.T.O			Pal Palocz <palocz.pal@mail.deltav.hu>
WoodIT			Igor Truszkowski <igor@chaos.w.pl>
xshare			Josef 'Jupp' Schugt <jupp@gmx.de>
X.T.O			Pal Palocz <palocz.pal@mail.deltav.hu>
zrpg			Joel Rosenthal

%description -l pl
Jest to zestaw 25 tematów do uprzyjemnienia wygl±du twojego icewm'a.
Thane			Xerithane <xerithane@nerdfarm.org>
crud			<dwl@wolsi.com>
Getaway			Xerithane <xerithane@nerdfarm.org>
houseMoneyBlessing	?
iMac-lol		RB_____ from the Jim-mac theme of Jakub Steiner
lameh			artwiz
aQua			CW Zuckschwerdt <zany@triq.net>
mechasan		Pal Palocz <palocz.pal@mail.deltav.hu>
Strange Dreams (MJ-5)	RudeSka
stric			<johannes@defcom.se>
Tile			Daniel W. Lemon  <dwl@wolsi.com>
Timesteps		<dwl@wolsi.com>
transistor		kraftBoy <gthomson@targetnet.com
tubes			Sawsedge <sawsedge@yahoo.com>
UFO Sightings (MJ-6)	RudeSka
Unusual Scars		RudeSka
Whistling		<dwl@wolsi.com>
William3		William Wieboldt (Poke'mon Master) <waw@iname.com>
Windows 3.1		Toaster T. Toaster <toaster@kami.com>
WMgtk			enterfornone <efn@themes.org>
WM.T.O			Pal Palocz <palocz.pal@mail.deltav.hu>
WoodIT			Igor Truszkowski <igor@chaos.w.pl>
xshare			Josef 'Jupp' Schugt <jupp@gmx.de>
X.T.O			Pal Palocz <palocz.pal@mail.deltav.hu>
zrpg			Joel Rosenthal

%prep
%setup -q -n %{name}
%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_themesdir}
cp -R * $RPM_BUILD_ROOT%{_themesdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_themesdir}
%{_themesdir}/*
