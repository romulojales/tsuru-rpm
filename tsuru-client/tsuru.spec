%global go_import_path     github.com/tsuru/tsuru-client

Name:	tsuru-tsuru-client		
Version:	1.0.0	
Release:	1%{?dist}
Summary:	tsuru-client is a tsuru command line tool for application developers.

License: BSD	
URL:	https://tsuru.io	
Source0:	https://github.com/tsuru/tsuru-client/archive/%{version}.zip

BuildRequires:	compiler(go-compilers)

%description
tsuru is the command line interface for the tsuru server
 Tsuru is an open source platform as a service software. This package installs
 the client used by application developers to communicate with tsuru server.

%prep
%setup -q %{name}-%{version}


%build
mkdir -p ./_build/src/github.com/tsuru/tsuru-client
ln -s $(pwd) ./_build/src/github.com/tsuru/tsuru-client

export GOPATH=$(pwd)/_build:%{gopath}
go build -o tsuru .


%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 ./tsuru %{buildroot}%{_bindir}/tsuru


%files
%doc



%changelog
* Tue 7 Apr 2016 Romulo Jales <romulo@romulojales.com> - 1.0.0
- first version

