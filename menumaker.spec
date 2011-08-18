Summary:	Menu generation utility
Name:		menumaker
Version:	0.99.7
Release:	0.1
License:	BSD
Group:		X11/Window Managers/Tools
Source0:	http://downloads.sourceforge.net/project/menumaker/MenuMaker/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a54cb7ec32db1bc8e04218e0be727b1e
URL:		http://menumaker.sourceforge.net/
BuildRequires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MenuMaker is a menu generation utility. It is capable of finding lots
of installed programs and generating a root menu consistent across all
supported X window managers, so one will get (almost) the same menu no
matter what window manager is selected. It is pure Python application
hence it runs on every relevant system. Supported X window managers
(As of 0.99.6)

BlackBox Deskmenu FluxBox IceWM OpenBox, version 3 PekWM WindowMaker
XFCE, version 4

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/mmaker
%dir %{_libdir}/menumaker
%{_libdir}/menumaker/*
%{_infodir}/mmaker.info*
