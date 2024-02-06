%global debug_package %{nil}

# https://github.com/openstack-k8s-operators/os-diff
%global goipath         os-diff

# the macro %%gometa messes up with DLRN as it overwrites Version and Source
#%%gometa

Name:                   golang-github-openstack-k8s-operators-os-diff
Version:                XXX
Release:                XXX
Summary:                Diff tool for Openstack and Openshift services configuration.
License:                ASL 2.0
URL:                    https://github.com/openstack-k8s-operators/os-diff
Source:                 %{gosource}
# Remove patch once https://github.com/openstack-k8s-operators/os-diff/pull/42 is merged
Patch001:               0001-Add-vendor-directory-for-rpm-packaging.patch

BuildRequires:          go-rpm-macros
# ./vendor2provides.py os-diff-%%{version}/vendor/modules.txt
Provides:               bundled(golang(github.com/fsnotify/fsnotify)) = 1.6.0
Provides:               bundled(golang(github.com/go-ini/ini)) = 1.67.0
Provides:               bundled(golang(github.com/hashicorp/hcl)) = 1.0.0
Provides:               bundled(golang(github.com/inconshreveable/mousetrap)) = 1.1.0
Provides:               bundled(golang(github.com/magiconair/properties)) = 1.8.7
Provides:               bundled(golang(github.com/mitchellh/mapstructure)) = 1.5.0
Provides:               bundled(golang(github.com/pelletier/go-toml/v2)) = 2.1.0
Provides:               bundled(golang(github.com/sagikazarmark/locafero)) = 0.3.0
Provides:               bundled(golang(github.com/sagikazarmark/slog-shim)) = 0.1.0
Provides:               bundled(golang(github.com/sirupsen/logrus)) = 1.9.0
Provides:               bundled(golang(github.com/sourcegraph/conc)) = 0.3.0
Provides:               bundled(golang(github.com/spf13/afero)) = 1.10.0
Provides:               bundled(golang(github.com/spf13/cast)) = 1.5.1
Provides:               bundled(golang(github.com/spf13/cobra)) = 1.7.0
Provides:               bundled(golang(github.com/spf13/pflag)) = 1.0.5
Provides:               bundled(golang(github.com/spf13/viper)) = 1.17.0
Provides:               bundled(golang(github.com/stretchr/testify)) = 1.8.4
Provides:               bundled(golang(github.com/subosito/gotenv)) = 1.6.0
Provides:               bundled(golang(go.uber.org/atomic)) = 1.9.0
Provides:               bundled(golang(go.uber.org/multierr)) = 1.9.0
Provides:               bundled(golang(golang.org/x/exp)) = 9212866
Provides:               bundled(golang(golang.org/x/sys)) = 0.12.0
Provides:               bundled(golang(golang.org/x/text)) = 0.13.0
Provides:               bundled(golang(gopkg.in/ini.v1)) = 1.67.0
Provides:               bundled(golang(gopkg.in/yaml.v3)) = 3.0.1


%description
Diff tool for Openstack and Openshift services configuration.

%prep
# To be able to use groprep macro we would need to change the project name to
# golang-github-openstack-k8s-operators-os-diff in order to follow standardization.
# goprep does not provide '-n' option like autosetup
# i.e: https://github.com/softwarefactory-project/DLRN/blob/295d5ab098ddbf136b191ff4f10f714dba2b7c8e/scripts/build_srpm.sh#L60
#%%goprep -k
%autosetup -p1 -n os-diff-%{version}

%build
export GO111MODULE=off
export GOPATH="$PWD:/usr/share/gocode/"
mkdir src
ln -s $PWD src/%{goipath}
%gobuild -o bin/os-diff %{goipath}

%install
install -m 0755 -vd %{buildroot}%{_bindir}
install -m 0755 -vp bin/os-diff %{buildroot}%{_bindir}

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

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%changelog
