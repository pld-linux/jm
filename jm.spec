Summary:	Jungle Monkey (Gnome version)
Name:		jm-gnome
Version:	@VERSION@
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	%{name}-%{PACKAGE_VERSION}.tar.gz
URL:		http://www.eecs.umich.edu/~dhelder/misc/jm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	jm
Requires:	glib >= 1.2
Requires:	gnet >= 1.0.1

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Jungle Monkey (JM) is a distributed file sharing program. You join
channels where people offer files for download. You can offer your own
files and create your own channels as well. Once you download a file,
others can connect to you to get that file. You can also search for
files.

THIS IS BETA SOFTWARE - JM IS MOSTLY STABLE, BUT THERE MAY STILL BE
LINGERING BUGS. JM is for Unix and requires GTK/GLIB 1.2, GNet 1.0,
and some other libraries.

JM has been tested in Linux 2.2 with GTK/GLIB 1.2.7. It may work on
other systems, but may require some additional hacking.

Comments, questions, and bug reports should be sent to
jm@eecs.umich.edu. Please read the FAQ before asking questions.

The Jungle Monkey homepage is at
http://www.eecs.umich.edu/~dhelder/misc/jm or
http://jungle.monkey.usuck.com

You can join the Jungle Monkey mailing lists by sending an email to
<name>-request@eecs.umich.edu with "subscribe" as the subject where
<name> is the name of the mailing list. The mailing lists are:

jm-announce Announcements about Jungle Monkey jm Discussion of Jungle
Monkey for JM users jm-dev Discussion of Jungle Monkey for JM
developers

%prep
%setup -q

%build
%ifarch alpha
   CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" ./configure --enable-gnome --host=alpha-redhat-linux\
	--prefix=%{_prefix} \
	--enable-debug=yes \
	--with-gnu-ld
%else
   CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" ./configure --enable-gnome \
	--prefix=%{_prefix} \
	--enable-debug=yes \
	--with-gnu-ld 
%endif
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%post

%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING ChangeLog NEWS TODO AUTHORS INSTALL 
%attr(755,root,root) %{_bindir}/*
%{_datadir}/*
%{_mandir}/man1/*
