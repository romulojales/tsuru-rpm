%global go_import_path     github.com/tsuru/tsuru-client/tsuru

Name:	tsuru-client		
Version:	1.0.0	
Release:	1%{?dist}
Summary:	tsuru-client is a tsuru command line tool for application developers.

License: BSD	
URL:	https://tsuru.io	
Source0:	https://%{go_import_path}/archive/%{version}.zip

BuildRequires:	golang

%description
tsuru is the command line interface for the tsuru server
 Tsuru is an open source platform as a service software. This package installs
 the client used by application developers to communicate with tsuru server.

%prep
export GOPATH=$(pwd)/_source
go get %{go_import_path}


%build
mkdir -p ./_build/src/%{go_import_path}
ln -s $(pwd) ./_build/src/%{go_import_path}

export GOPATH=$(pwd)/_build/src
go build -o tsuru .


%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 ./tsuru %{buildroot}%{_bindir}/tsuru


%files
%doc



%changelog
* Thu Apr 7 2016 - Romulo Jales <romulo@romulojales.com> - 1.0.0
- first version

