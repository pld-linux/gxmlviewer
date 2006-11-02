Summary:	GTK+ XML Viewer
Summary(pl):	Przegl±darka plików XML w GTK+
Name:		gxmlviewer
Version:	1.3.3
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gxmlviewer/%{name}-%{version}.tar.gz
# Source0-md5:	e1f159e003e2ca99482ac7cf8677365e
Patch0:		%{name}-libxml2.patch
Patch1:		%{name}-no-nsplugin.patch
URL:		http://gxmlviewer.sourceforge.net/
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-devel >= 1.0.4
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	imlib-devel
BuildRequires:	libxml2-devel >= 2.3.1
BuildRequires:	oaf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GTK+ based XML file viewer.

%description -l pl
Przegl±darka plików XML oparta o GTK+.

%package control
Summary:	XML Viewer Bonobo Control
Summary(pl):	Kontrola Bonobo do przegl±darki XML-a
Group:		X11/Applications
Obsoletes:	xmlview-control

%description control
A Bonobo control for viewing XML files.

%description control -l pl
Kontrola Bonobo do przegl±darki XML-a.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__gettextize}
%{__aclocal} -I macros -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gxmlviewer

%files control
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmlview-control
%{_datadir}/oaf/GNOME_XMLView.oaf
