Summary:	GTK+ XML Viewer
Summary(pl):	Przegl±darka plików XML w GTK+
Name:		gxmlviewer
Version:	1.2.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://prdownloads.sourceforge.net/gxmlviewer/%{name}-%{version}.tar.gz
URL:		http://sourceforge.net/projects/gxmlviewer/
BuildRequires:	ORBit-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	imlib-devel
BuildRequires:	libxml-devel
BuildRequires:	oaf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
A GTK+ based XML file viewer.

%description -l pl
Przegl±darka plików XML oparta o GTK+.

%package control
Summary:	XML Viewer Bonobo Control
Summary(pl):	Kontrola Bonobo do przegl±darki XML
Group:		X11/Applications
Obsoletes:	xmlview-control

%description control
A Bonobo control for viewing XML files.

%description control -l pl
Kontrola Bonobo do przegl±darki XML.

%prep
%setup -q

%build
rm -f missing
aclocal -I macros
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PLUGIN_DIR=%{_libdir}/mozilla/plugins

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
