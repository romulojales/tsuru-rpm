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
#rm -rf $(pwd)/*
export GOPATH=$(pwd)
go get -d %{go_import_path}


%build
export GOPATH=$(pwd)
go build -o tsuru %{go_import_path}


%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 ./tsuru %{buildroot}%{_bindir}/tsuru


%files
%defattr(-,root,root,-)
%doc
%{_bindir}/tsuru


%changelog
* Fri Apr 8 2016 - Romulo Jales <romulo@romulojales.com> - 1.0.0
- first version

