# http://github.com/garyburd/redigo

%global goipath         github.com/garyburd/redigo
%global commit          3e4727f0ef5938d3a846cdb57e560dba4419e854


%gometa -i

Name:           %{goname}
Version:        0
Release:        0.14%{?dist}
Summary:        Go client for Redis
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml
Patch0:         add-license.patch

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%patch0 -p1

%install
%goinstall glide.lock glide.yaml

%check
%gochecks -d redis

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license ASL-2.0.txt
%doc README.markdown

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.git3e4727f
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.20150520git3e4727f
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git3e4727f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git3e4727f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git3e4727f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git3e4727f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git3e4727f
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git3e4727f
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git3e4727f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git3e4727f
- Update to spec-2.1
  resolves: #1248994

* Fri Jul 31 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git3e4727f
- Update spec file to spec-2.0
  resolves: #1248994

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.git3e4727f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git3e4727f
- First package for Fedora
  resolves: #1228795

