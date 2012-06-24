# Note that this is NOT a relocatable package
%define ver      1.2.0
%define rel      2

Summary:   GTK+ XML Viewer
Name:      gxmlviewer
Version:   %ver
Release:   %rel
Copyright: GPL
Group:     X11/Utilities
Source:    gxmlviewer-%{PACKAGE_VERSION}.tar.gz
URL:       http://sourceforge.net/projects/gxmlviewer/
BuildRoot: /var/tmp/gxmlviewer-%{PACKAGE_VERSION}-root

%description
A GTK+ based XML file viewer.

%package -n xmlview-control
Summary:   XML Viewer Bonobo Control
Requires:  bonobo >= 0.36
Group:     GNOME/Internet/Controls

%description -n xmlview-control
A Bonobo control for viewing XML files.

%prep
%setup

%build
%configure

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_prefix}/bin/gxmlviewer
%{_prefix}/lib/netscape/plugins/npgxmlviewer.so

%files -n xmlview-control
%{_prefix}/bin/xmlview-control
%{_prefix}/share/oaf/GNOME_XMLView.oaf

%changelog
