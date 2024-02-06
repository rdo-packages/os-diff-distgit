Name: os-diff
Version: XXX
Release: XXX
Summary: Diff tool for Openstack and Openshift services configuration.
License: ASL 2.0
URL: https://github.com/openstack-k8s-operators/os-diff
Source: https://github.com/openstack-k8s-operators/os-diff

BuildRequires: curl
BuildRequires: git
BuildRequires: golang
BuildRequires: make

%description
Diff tool for Openstack and Openshift services configuration.

%prep
%setup

%build

# Build the binary:
make build

%install
install -m 0755 -d %{buildroot}%{_bindir}
install -m 0755 os-diff %{buildroot}%{_bindir}

%clean

%files
%license LICENSE.txt
%doc README.md
%doc CHANGES.md
%{_bindir}/*

%changelog
