Summary:	GTK+ XML Viewer
Name:		gxmlviewer
Version:	1.2.0
Release:	2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://prdownloads.sourceforge.net/gxmlviewer/%{name}-%{version}.tar.gz
URL:		http://sourceforge.net/projects/gxmlviewer/
BuildRequires:	ORBit-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	imlib-devel
BuildRequires:	libxml-devel
BuildRequires:	oaf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
A GTK+ based XML file viewer.

%package control
Summary:	XML Viewer Bonobo Control
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Obsoletes:	xmlview-control

%description control
A Bonobo control for viewing XML files.

%prep
%setup -q

%build
rm -f missing
aclocal -I macros
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PLUGIN_DIR=%{_libdir}/mizilla/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gxmlviewer
%{_libdir}/mozilla/plugins/npgxmlviewer.so

%files control
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmlview-control
%{_datadir}/oaf/GNOME_XMLView.oaf
