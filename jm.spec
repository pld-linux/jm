# Note that this is NOT a relocatable package
%define ver      @VERSION@
%define rel      1
%define prefix   /usr

Summary: Jungle Monkey (Gnome version)
Name:      jm-gnome
Version:   %ver
Release:   %rel
Copyright: GPL
Group: X11/Application
Source0:   jm-gnome-%{PACKAGE_VERSION}.tar.gz
URL:       http://www.eecs.umich.edu/~dhelder/misc/jm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Docdir: %{prefix}/doc
Packager: Xavier Nicolovici <nicolovi@club-internet.fr>
Conflicts: jm
Requires: glib >= 1.2
Requires: gnet >= 1.0.1

%description
Jungle Monkey (JM) is a distributed file sharing program.  You join
channels where people offer files for download.  You can offer your
own files and create your own channels as well.  Once you download a
file, others can connect to you to get that file.  You can also search
for files.

THIS IS BETA SOFTWARE - JM IS MOSTLY STABLE, BUT THERE MAY STILL BE
LINGERING BUGS.  JM is for Unix and requires GTK/GLIB 1.2, GNet 1.0,
and some other libraries.

JM has been tested in Linux 2.2 with GTK/GLIB 1.2.7.  It may work on
other systems, but may require some additional hacking.

Comments, questions, and bug reports should be sent to
jm@eecs.umich.edu.  Please read the FAQ before asking questions.

The Jungle Monkey homepage is at
        http://www.eecs.umich.edu/~dhelder/misc/jm
                        or
        http://jungle.monkey.usuck.com

You can join the Jungle Monkey mailing lists by sending an email to
<name>-request@eecs.umich.edu with "subscribe" as the subject where
<name> is the name of the mailing list.  The mailing lists are:

        jm-announce     Announcements about Jungle Monkey
        jm              Discussion of Jungle Monkey for JM users
        jm-dev          Discussion of Jungle Monkey for JM developers

%prep
%setup

%build
%ifarch alpha
   CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" ./configure --enable-gnome --host=alpha-redhat-linux\
	--prefix=%{prefix} \
	--enable-debug=yes \
	--with-gnu-ld
%else
   CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" ./configure --enable-gnome \
	--prefix=%{prefix} \
	--enable-debug=yes \
	--with-gnu-ld 
%endif
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{prefix} install

%post

%postun

#%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc README COPYING ChangeLog NEWS TODO AUTHORS INSTALL 
%{prefix}/bin/*
%{prefix}/share/*
%{prefix}/man/man1/*

%changelog
* Thu Jan 13 2000 Xavier Nicolovici <nicolovi@club-internet.fr>
- First try at an RPM
