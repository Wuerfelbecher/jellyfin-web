%global         debug_package %{nil}
Name:           jellyfin-web
Version:        10.1.0
Release:        1%{?dist}
Summary:        Jellyfin Webinterface

License:        GPLv2
URL:            https://jellyfin.media
Source0:        %{name}-%{version}.tar.gz

%description
Jellyfin Webinterface

%prep
%autosetup -n %{name}-%{version}

%build

%install
%{__install} -d %{buildroot}%{_libdir}/jellyfin/%{name}
%{__cp} -r ./src -d %{buildroot}%{_libdir}/jellyfin/%{name}



%files
%{_libdir}/jellyfin/%{name}/*

%license LICENSE


%changelog
* Thu Jan 31 2019 Thomas Büttner <thomas@vergesslicher.tech>
- Add SPEC
