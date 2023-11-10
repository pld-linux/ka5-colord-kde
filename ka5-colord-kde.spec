#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.3
%define		kframever	5.103.0
%define		qtver		5.15.2
%define		kaname		colord-kde
Summary:	colord KDE
Name:		ka5-%{kaname}
Version:	23.08.3
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	878b82e511a65b53f0a8ac0ebbfa3fb0
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= 5.15.2
BuildRequires:	Qt5DBus-devel >= 5.15.2
BuildRequires:	Qt5Gui-devel >= 5.15.2
BuildRequires:	Qt5Widgets-devel >= 5.15.2
BuildRequires:	Qt5X11Extras-devel >= 5.15.2
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.91.0
BuildRequires:	kf5-kauth-devel >= 5.103.0
BuildRequires:	kf5-kcmutils-devel >= 5.91.0
BuildRequires:	kf5-kcodecs-devel >= 5.103.0
BuildRequires:	kf5-kcompletion-devel >= 5.103.0
BuildRequires:	kf5-kconfig-devel >= 5.103.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.103.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.103.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.91.0
BuildRequires:	kf5-ki18n-devel >= 5.91.0
BuildRequires:	kf5-kio-devel >= 5.91.0
BuildRequires:	kf5-kitemviews-devel >= 5.103.0
BuildRequires:	kf5-kjobwidgets-devel >= 5.103.0
BuildRequires:	kf5-kservice-devel >= 5.103.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.103.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.103.0
BuildRequires:	kf5-kxmlgui-devel >= 5.103.0
BuildRequires:	kf5-solid-devel >= 5.103.0
BuildRequires:	libxcb-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
colord KDE

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%doc MAINTAINERS TODO
%attr(755,root,root) %{_bindir}/colord-kde-icc-importer
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/colord.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_colord.so
%dir %{_datadir}/kpackage/kcms/kcm_colord
%dir %{_datadir}/kpackage/kcms/kcm_colord/contents
%dir %{_datadir}/kpackage/kcms/kcm_colord/contents/ui
%{_datadir}/kpackage/kcms/kcm_colord/contents/ui/ProfileMetaDataView.qml
%{_datadir}/kpackage/kcms/kcm_colord/contents/ui/main.qml
%{_desktopdir}/colordkdeiccimporter.desktop
