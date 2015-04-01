Name:           %{name}
Version:        %{ver}
Release:        %{rel}%{?dist}
Summary:        Kibana - UI for elasticsearch
BuildArch:      noarch
Group:          Application/Internet
License:        commercial
URL:            http://www.elasticsearch.org/overview/kibana/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:        https://download.elasticsearch.org/kibana/kibana/kibana-%{ver}-linux-x64.tar.gz
Source1:        kibana.service

%define appdir /opt/%{name}
%define systemd_dest /usr/lib/systemd/system/
%description
Kibana - UI for elasticsearch

%prep
%setup -q -n %{name}-%{version}-linux-x64
cp -p %SOURCE1 .

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/kibana/
mkdir -p $RPM_BUILD_ROOT/%{systemd_dest}
cp -r * $RPM_BUILD_ROOT/opt/kibana/
%{__install} -p -m 0755 %{SOURCE1} $RPM_BUILD_ROOT/%{systemd_dest}/kibana.service

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(0755,root,root) /opt/kibana/*
%attr(0755,root,root) %{systemd_dest}/kibana.service
%config /opt/kibana/config.js

%changelog
* Wed Apr 01 2015 Daniel Menet <daniel.menet@swisstxt.ch> - 4.0.1
Updated to Kibana 4.0.1

* Fri Jan 16 2015 Daniel Menet <daniel.menet@swisstxt.ch> - 3.1.2
Updated to Kibana 3.1.2

* Mon Sep 22 2014 Daniel Menet <daniel.menet@swisstxt.ch> - 1-1
Initial creation
