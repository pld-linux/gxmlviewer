Summary:	GTK+ XML Viewer
Summary(pl):	Przegl±darka plików XML w GTK+
Name:		gxmlviewer
Version:	1.2.0
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://prdownloads.sourceforge.net/gxmlviewer/%{name}-%{version}.tar.gz
URL:		http://gxmlviewer.sourceforge.net/
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	imlib-devel
BuildRequires:	libxml-devel
BuildRequires:	oaf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package -n mozilla-plugin-%{name}
Summary:	Mozilla XML plugin
Summary(pl):	Wtyczka XML do Mozilli
Group:		X11/Applications
Requires:	%{name} = %{version}
PreReq:		mozilla-embedded

%description -n mozilla-plugin-%{name}
XML plugin for Mozilla.

%description -n mozilla-plugin-%{name} -l pl
Wtyczka z obs³ug± XML dla Mozilli.

%prep
%setup -q

%build
rm -f missing
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
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

%files control
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmlview-control
%{_datadir}/oaf/GNOME_XMLView.oaf

%files -n mozilla-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mozilla/plugins/npgxmlviewer.so
