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
BuildRequires: golang-github-go-ini-ini
BuildRequires: golang-github-spf13-cobra
BuildRequires: golang-gopkg-yaml
BuildRequires: golang-gopkg-yaml-3
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

# Move os-diff.cfg to sysconfdir
if [ -f "%{buildroot}/os-diff.cfg" ]; then
mv %{buildroot}/os-diff.cfg %{buildroot}%{_sysconfdir}/os-diff.cfg
fi

# Move config.yaml to sysconfdir
if [ -f "%{buildroot}/config.yaml" ]; then
mv %{buildroot}/config.yaml %{buildroot}%{_sysconfdir}/config.yaml
fi

# Move ssh.config file to sysconfdir
if [ -f "%{buildroot}/ssh.config" ]; then
mv %{buildroot}/ssh.config %{buildroot}%{_sysconfdir}/ssh.config
fi

%clean

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%changelog
