%global debug_package %{nil}

# Run tests in check section
%bcond_with check

# https://github.com/stretchr/testify
%global goipath		github.com/stretchr/testify
%global forgeurl	https://github.com/stretchr/testify
Version:		1.10.0

%gometa

Summary:	Tools for testifying that your code will behave as you intend
Name:		golang-github-stretchr-testify

Release:	1
Source0:	https://github.com/stretchr/testify/archive/v%{version}/testify-%{version}.tar.gz
URL:		https://github.com/stretchr/testify
License:	MIT
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildRequires:	golang(github.com/davecgh/go-spew/spew)
BuildRequires:	golang(github.com/pmezard/go-difflib/difflib)
BuildRequires:	golang(github.com/stretchr/objx)
BuildArch:	noarch

%description
Go code (golang) set of packages that provide many tools
for testifying that your code will behave as you intend.

Features include:

 *  Easy assertions
 *  Mocking
 *  Testing suite interfaces and functions


#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n testify-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

