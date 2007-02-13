#
# Conditional build:
# _without_gnome   		- without gnome support
#
Summary:	Jungle Monkey - distributed file sharing
Summary(pl.UTF-8):	Jungle Monkey - program do dzielenia zasobów
Name:		jm
Version:	0.1.11
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.junglemonkey.net/src/%{name}-%{version}.tar.gz
# Source0-md5:	0493d7bdbdaeda9c9a033edab4be56f6
URL:		http://www.junglemonkey.net/
BuildRequires:	gnet-devel >= 1.1.0
BuildRequires:	gnet-devel < 2
%{!?_without_gnome:BuildRequires:	gnome-libs-devel}
BuildRequires:	gtk+-devel >= 1.2.7
BuildRequires:	libglade-devel
%{!?_without_gnome:BuildRequires:	libglade-gnome-devel}
BuildRequires:	libxml-devel
BuildRequires:	openssl-devel >= 0.9.7d
Requires:	glib >= 1.2
Requires:	gnet >= 1.1.0
Obsoletes:	jm-gnome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jungle Monkey (JM) is a distributed file sharing program. You join
channels where people offer files for download. You can offer your own
files and create your own channels as well. Once you download a file,
others can connect to you to get that file. You can also search for
files.

THIS IS BETA SOFTWARE - JM IS MOSTLY STABLE, BUT THERE MAY STILL BE
LINGERING BUGS.

%description -l pl.UTF-8
Jungle Monkey (JM) to program do rozproszonego dzielenia zasobów.
Można dołączyć się do kanału gdzie ludzie oferują pliki do
ściągnięcia, można zaoferować swoje pliki, a także tworzyć własne
kanały. Kiedy ściągniemy plik, inni mogą połączyć się do nas, żeby
ściągnąć ten plik. Można także szukać plików.

To jest oprogramowanie w wersji BETA - przeważnie działa, ale może
zawierać błędy.

%prep
%setup -q

%build
%configure2_13 \
	%{!?_without_gnome:--enable-gnome} \
	%{!?debug:--disable-debug} \
	--enable-openssl

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Internetdir=%{_applnkdir}/Network \
	pixmapdir=%{_pixmapsdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog NEWS TODO AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/jm
%{_mandir}/man1/*
%{_pixmapsdir}/*.png
%{_applnkdir}/Network/*.desktop
