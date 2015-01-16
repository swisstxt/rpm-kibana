Name:           %{name}
Version:        %{ver}
Release:        %{rel}%{?dist}
Summary:        Kibana - UI for elasticsearch
BuildArch:      noarch
Group:          Application/Internet
License:        commercial
URL:            http://www.elasticsearch.org/overview/kibana/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:        https://download.elasticsearch.org/kibana/kibana/kibana-%{ver}.tar.gz

%description
Kibana - UI for elasticsearch

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/kibana/
cp -r * $RPM_BUILD_ROOT/opt/kibana/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(0755,root,root) /opt/kibana/*
%config /opt/kibana/config.js

%changelog
* Fri Jan 16 2015 Daniel Menet <daniel.menet@swisstxt.ch> - 3.1.2
Updated to Kibana 3.1.2

* Mon Sep 22 2014 Daniel Menet <daniel.menet@swisstxt.ch> - 1-1
Initial creation
