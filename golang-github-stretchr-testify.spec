# Run tests in check section
%bcond_without check

# https://github.com/stretchr/testify
%global goipath         github.com/stretchr/testify
Version:                1.2.2

%global common_description %{expand:
Golang set of packages that provide many tools for testifying 
that your code will behave as you intend.

Features include:

 - Easy assertions
 - Mocking
 - Testing suite interfaces and functions}

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        Tools for testifying that your code will behave as you intend
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}


%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/davecgh/go-spew/spew)
BuildRequires: golang(github.com/pmezard/go-difflib/difflib)
BuildRequires: golang(github.com/stretchr/objx)

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Oct 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.2-1
- Update to upstream v1.2.2

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.2.1-3
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.1-1
- Update to upstream v1.2.1
- Update to new guidelines for Go

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-0.2.git69483b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 12 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.1.4-0.1.git69483b4
- Update to upstream v1.1.4
  resolves: #1490397

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.11.git976c720
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.10.git976c720
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 16 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.0-0.9.git976c720
- Bump to upstream 976c720a22c8eb4eb6a0b4348ad85ad12491a506
  related: #1246684

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.8.git089c718
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 17 2016 Jan Chaloupka <jchaloup@redhat.com> - 1.0-0.7.git089c718
- Polish the spec file
  related: #1246684

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.git089c718
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.5.git089c718
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.4.git089c718
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 11 2015 jchaloup <jchaloup@redhat.com> - 1.0-0.3.git089c718
- Add missing license in unit-test, BR of devel can be uncommented out
  relates: #1246684

* Mon Aug 10 2015 Fridolin Pokorny <fpokorny@redhat.com> - 1.0-0.2.git089c718
- Update spec file to spec-2.0
  relates: #1246684

* Fri Jul 24 2015 jchaloup <jchaloup@redhat.com> - 1.0-0.1.git089c718
- Bump to upstream 089c7181b8c728499929ff09b62d3fdd8df8adff
  resolves: #1246684

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.gite4ec815
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 06 2015 jchaloup <jchaloup@redhat.com> - 0-0.7.gite4ec815
- update URL to point to github repository
  related: #1141872

* Thu Mar 05 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.gite4ec815
- Bump to upstream e4ec8152c15fc46bd5056ce65997a07c7d415325
  related: #1141872

* Thu Oct 23 2014 jchaloup <jchaloup@redhat.com> - 0-0.5.gitd6577e0
- Bump to upstream d6577e08ec30538639ac0ea38b562b6f250e9055
- Spec file polishing to follow go draft
  related: #1141872

* Mon Sep 15 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.3.gitda775f0
- preserve timestamps of copied files

* Wed Aug 06 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.2.gitda775f0
- Fix up devel package listing

* Wed Aug 06 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.1.gitda775f0
- First package for Fedora.

