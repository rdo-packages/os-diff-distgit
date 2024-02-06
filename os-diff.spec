Name: os-diff
Version: XXX
Release: XXX
Summary: Diff tool for Openstack and Openshift services configuration.
License: ASL 2.0
URL: https://github.com/openstack-k8s-operators/os-diff
Source: https://github.com/openstack-k8s-operators/os-diff

# We need to download Go explicitly because in most of the platforms that we
# use the version available is too old.
%define go_tar https://go.dev/dl/go1.20.4.linux-amd64.tar.gz
%define go_sum 698ef3243972a51ddb4028e4a1ac63dc6d60821bf18e59a807e051fee0a385bd

BuildRequires: curl
BuildRequires: git
BuildRequires: make

%description
Diff tool for Openstack and Openshift services configuration.

%prep
%setup

%build

# Create the Go directories:
export GOROOT="${PWD}/.goroot"
export GOPATH="${PWD}/.gopath"
mkdir "${GOROOT}" "${GOPATH}"
PATH="${GOROOT}/bin:${PATH}"

# Download and install Go:
curl --location --output go.tar.gz %{go_tar}
echo %{go_sum} go.tar.gz | sha256sum --check
tar --directory "${GOROOT}" --extract --strip-components 1 --file go.tar.gz

# Build the binary:
make build

%install
install -m 0755 -d %{buildroot}%{_bindir}
install -m 0755 os-diff %{buildroot}%{_bindir}

%clean
# This is necessary because Go writes its cache files and directories without
# write permission, and that means that a rgular `rm` can't remove them.
find .gopath -exec chmod +w {} \;
rm -rf .gopath

%files
%license LICENSE.txt
%doc README.md
%doc CHANGES.md
%{_bindir}/*

%changelog
