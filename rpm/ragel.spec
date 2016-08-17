Name:       ragel
Summary:    Finite state machine compiler
Version:    6.9
Release:    1
Group:      Development/Tools
License:    GPLv2
URL:        http://www.colm.net/open-source/ragel/
Source0:    http://www.colm.net/files/ragel/%{name}-%{version}.tar.gz


%description
Ragel compiles executable finite state machines from regular languages. Ragel targets C, C++ and ASM.


%prep
%setup -q -n %{name}-%{version}/ragel

%build

autoreconf -vfi
%configure

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install



%files
%defattr(-,root,root,-)
%{_bindir}/ragel
%exclude %{_datadir}/doc/ragel/*
%exclude %{_datadir}/man/man1/*

