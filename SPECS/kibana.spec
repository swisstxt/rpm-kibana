%global service_name kibana

Name:           kibana
Version:        %{ver}
Release:        %{rel}1%{?dist}
Summary:        Kibana - UI for elasticsearch
BuildArch:      noarch
Group:          Application/Internet
License:        commercial
URL:            http://www.elasticsearch.org/overview/kibana/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Kibana - UI for elasticsearch

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/kibana/
cp * $RPM_BUILD_ROOT/opt/kibana/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(0755,root,root) /opt/kibana/*
%config /opt/kibana/config.js

%changelog
* Mon Sep 22 2014 Daniel Menet <daniel.menet@swisstxt.ch> - 1-1
Initial creation