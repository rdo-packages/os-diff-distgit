%global debug_package %{nil}

# The macro %%gometa needs Version:, %{commit} or %{tag} to be defined
# before the macro invocation, but as we set XXX as Version for DLRN, it fails.
# So we add a dummy tag and remove the distprefix (i.e .git<tag>) which
# is added at the end of the RPM if a tag is defined.
# At the end, it's a noop operation and the macro does not fail anymore
%{?dlrn: %global tag        0}
%{?dlrn: %global distprefix %{nil}}
# By default extractdir = %{repo}-%{version} with repo = os-diff
# but DLRN generates tarball with <project_name>-<version> as tarball name.
# FTR goname = project_name
%{?dlrn: %global extractdir %{goname}-%{version}}

# https://github.com/openstack-k8s-operators/os-diff
%global goipath         github.com/openstack-k8s-operators/os-diff
# Version should be defined before %%gometa
Version:                XXX

# Be verbose and print every spec variable the macro sets.
%gometa -v
# by default ref=v%{version} but upstream project issue tag without 'v' prefix
%global ref %{version}

Name:                   %{goname}
Release:                XXX
Summary:                Retired empty package (os-diff removed).
License:                Apache-2.0
URL:                    %{gourl}
Source:                 %{gosource}

%description
Retired empty package. Previously shipped the os-diff CLI and configs;
this package installs no files so upgrades remove them.

%prep
%goprep -k

%build

%install

%check

%files

%changelog

