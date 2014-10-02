Summary:        Evolution plugin to minimize in tray
Name:           evolution-on
Version:        0.0.9
Release:        0.1.git1fa33facea1%{?dist}

License:        GPLv2
Group:          Applications/Productivity
Url:            https://github.com/KostadinAtanasov/evolution-on/
Source0:        evolution-on-0.0.9-1fa33facea1.tar.xz

BuildRequires:  gnome-common
BuildRequires:  intltool
%if 0%{?fedora} <= 20
BuildRequires:  pkgconfig(evolution-plugin-3.0)
%endif
BuildRequires:  pkgconfig(evolution-shell-3.0)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)

Requires:       evolution

%description
This plugin is useful when you want to put evolution in the "tray"
(notification area). While in the tray, evolution is minimized and
is not visible in the pager. Evolution can then be restored on any
workspace.

%prep
%setup -q -n %{name}

%build
# needed for patch1 and patch3
NOCONFIGURE=1 gnome-autogen.sh
%configure
make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%postun
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files
%{_datadir}/GConf/gsettings/%{name}.convert
%{_datadir}/glib-2.0/schemas/*.xml
%{_libdir}/evolution/*/plugins/*

%changelog
* Thu Oct  2 2014 Arkady L. Shane <ashejn@russianfedora.ru> - 0.0.9-0.1.git1fa33facea1.R
- initial build
