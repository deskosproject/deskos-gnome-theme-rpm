%global arc_theme_version 20160331

Name:           deskos-gnome-theme
Version:        0.1
Release:        1
Summary:        DeskOS default theme for GTK 3 and GNOME Shell

Group:          User Interface/Desktops
License:        GPLv3
URL:            https://github.com/deskosproject/deskos-gnome-theme-rpm
Source0:        https://github.com/horst3180/arc-theme/archive/%{arc_theme_version}.tar.gz
Patch0:         deskos-name.patch

BuildArch:      noarch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gtk3-devel
Requires:       gnome-themes-standard
Requires:       gtk-murrine-engine

%description
DeskOS default theme based on Arc, a flat theme with transparent
elements for GTK 3, GTK 2 and Gnome-Shell.

%prep
%setup -q -n arc-theme-%{arc_theme_version}
%patch0 -p1

%build
./autogen.sh --prefix=/usr \
             --disable-darker \
             --disable-dark \
             --disable-cinnamon \
             --disable-gnome-shell \
             --disable-unity \
             --disable-xfwm \
             --disable-xfce-notify \
             --with-gnome=3.14

%install
make install DESTDIR=$RPM_BUILD_ROOT

find ${RPM_BUILD_ROOT} -name "*.sh" -exec chmod -x {} \;

%files
%defattr(-,root,root)
%doc
%{_datadir}/themes/DeskOS/gtk-2.0/
%{_datadir}/themes/DeskOS/gtk-3.0/
%{_datadir}/themes/DeskOS/metacity-1/
%{_datadir}/themes/DeskOS/index.theme

%changelog
* Thu May 12 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.1-1
- Initial release
