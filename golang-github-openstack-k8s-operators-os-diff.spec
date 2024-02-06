%global debug_package %{nil}

# https://github.com/openstack-k8s-operators/os-diff
%global goipath         github.com/openstack-k8s-operators/os-diff

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

# Be verbose and print every spec variable the macro sets.
%gometa -v

Name:                   %{goname}
Version:                XXX
Release:                XXX
Summary:                Diff tool for Openstack and Openshift services configuration.
License:                ASL 2.0
URL:                    %{gourl}
Source:                 %{gosource}

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

%gopkg

%prep
%goprep -k

%build
%gobuild -o bin/os-diff %{goipath}

%install
install -m 0755 -vd             %{buildroot}%{_bindir}
install -m 0755 -vp bin/os-diff %{buildroot}%{_bindir}/

if [ ! -d "%{buildroot}%{_sysconfdir}" ]; then
mkdir -p %{buildroot}%{_sysconfdir}/os-diff
fi

# Move os-diff.cfg to sysconfdir
mv os-diff.cfg %{buildroot}%{_sysconfdir}/os-diff/os-diff.cfg

# Move config.yaml to sysconfdir
mv config.yaml %{buildroot}%{_sysconfdir}/os-diff/config.yaml

# Move ssh.config file to sysconfdir
mv ssh.config %{buildroot}%{_sysconfdir}/os-diff/ssh.config

%files
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/os-diff/os-diff.cfg
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/os-diff/ssh-config
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/os-diff/config.yaml
%license LICENSE
%doc README.md
%{_bindir}/*

%changelog
