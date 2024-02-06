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

if [ ! -d "%{buildroot}%{_sysconfdir}" ]; then
mkdir -p %{buildroot}%{_sysconfdir}
fi

# Handle os-diff.cfg config file and move it to sysconfdir
if [ -f "%{buildroot}/os-diff.cfg" ]; then
mv %{buildroot}/os-diff.cfg %{buildroot}%{_sysconfdir}/os-diff.cfg
fi

# Handle config.yaml config file and move it to sysconfdir
if [ -f "%{buildroot}/config.yaml" ]; then
mv %{buildroot}/config.yaml %{buildroot}%{_sysconfdir}/config.yaml
fi

%clean

%files
%license LICENSE.txt
%doc README.md
%doc CHANGES.md
%{_bindir}/*

%changelog
