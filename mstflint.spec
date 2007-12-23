Summary: Mellanox firmware burning application
Name: mstflint
Version: 1.3
Release: 1
License: GPL/BSD
Url: http://openib.org/
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Source: mstflint-1.3.tar.gz
ExclusiveArch: i386 x86_64 ia64 ppc ppc64
BuildRequires: zlib-devel

%description
This package contains a tool for burning updated firmware on to
Mellanox manufactured InfiniBand adapters.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install
# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/mstmread
%{_bindir}/mstmwrite
%{_bindir}/mstflint
%{_bindir}/mstregdump
%{_bindir}/mstvpd
%{_bindir}/mstmcra
%{_includedir}/mtcr.h

%changelog
* Fri Dec 23 2007 Oren Kladnitsky <orenk@dev.mellanox.co.il>
   Added mtcr.h installation
   
* Fri Dec 07 2007 Ira Weiny <weiny2@llnl.gov> 1.0.0
   initial creation

