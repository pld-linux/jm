#
# Conditional build:
# _without_gnome   		- without gnome support
#
Summary:	Jungle Monkey - distributed file sharing
Summary(pl):	Jungle Monkey - program do dzielenia zasobów
Name:		jm
Version:	0.1.10
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.junglemonkey.net/src/%{name}-%{version}.tar.gz
URL:		http://www.junglemonkey.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	gnet-devel >= 1.1.0
BuildRequires:	gtk+-devel >= 1.2.7
BuildRequires:	libglade-devel
BuildRequires:	libxml-devel
%{!?_without_gnome:BuildRequires:	gnome-libs-devel}
Obsoletes:	jm-gnome
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

%description -l pl
Jungle Monkey (JM) to program do rozproszonego dzielenia zasobów.
Mo¿esz do³±czyæ siê do kana³u gdzie ludzie oferuj± pliki do
¶ci±gniêcia, mo¿esz zaoferowaæ swoje pliki, a tak¿e tworzyæ w³asne
kana³y. Kiedy ¶ci±gniêsz plik, inni mog± po³±czyæ siê do ciebie ¿eby
¶ci±gn±æ ten plik. Mo¿esz tak¿e szukaæ plików. To jest wersja BETA.

%prep
%setup -q

%build
%ifarch alpha
   CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" ./configure --host=alpha-redhat-linux\
	%{!?_without_gnome:	--enable-gnome=yes} \
	%{?_without_gnome:	--enable-gnome=no} \
	--prefix=%{_prefix} \
	--enable-debug=yes \
	--with-gnu-ld
%else
   CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" ./configure \
	%{!?_without_gnome:--enable-gnome=yes} \
	%{?_without_gnome:--enable-gnome=no} \
	--prefix=%{_prefix} \
	--enable-debug=yes \
	--with-gnu-ld
%endif
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

gzip -9nf README ChangeLog NEWS TODO AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ChangeLog,NEWS,TODO,AUTHORS}.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/*
%{_mandir}/man1/*
