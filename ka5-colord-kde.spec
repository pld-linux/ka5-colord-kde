#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.01.95
%define		kframever	5.103.0
%define		qtver		5.15.2
%define		kaname		colord-kde
Summary:	colord KDE
Name:		ka5-%{kaname}
Version:	24.01.95
Release:	0.1
License:	GPL v2+
Group:		X11/Libraries
Source0:	https://download.kde.org/unstable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	7089a63f77d15ebf0b4de1f8784abfd9
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= 5.15.2
BuildRequires:	Qt6DBus-devel >= 5.15.2
BuildRequires:	Qt6Gui-devel >= 5.15.2
BuildRequires:	Qt6Widgets-devel >= 5.15.2
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= 5.91.0
BuildRequires:	kf6-kauth-devel >= 5.103.0
BuildRequires:	kf6-kcmutils-devel >= 5.91.0
BuildRequires:	kf6-kcodecs-devel >= 5.103.0
BuildRequires:	kf6-kcompletion-devel >= 5.103.0
BuildRequires:	kf6-kconfig-devel >= 5.103.0
BuildRequires:	kf6-kconfigwidgets-devel >= 5.103.0
BuildRequires:	kf6-kcoreaddons-devel >= 5.103.0
BuildRequires:	kf6-kdbusaddons-devel >= 5.91.0
BuildRequires:	kf6-ki18n-devel >= 5.91.0
BuildRequires:	kf6-kio-devel >= 5.91.0
BuildRequires:	kf6-kitemviews-devel >= 5.103.0
BuildRequires:	kf6-kjobwidgets-devel >= 5.103.0
BuildRequires:	kf6-kservice-devel >= 5.103.0
BuildRequires:	kf6-kwidgetsaddons-devel >= 5.103.0
BuildRequires:	kf6-kwindowsystem-devel >= 5.103.0
BuildRequires:	kf6-kxmlgui-devel >= 5.103.0
BuildRequires:	kf6-solid-devel >= 5.103.0
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
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/colord.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_colord.so
%{_desktopdir}/colordkdeiccimporter.desktop
%{_desktopdir}/kcm_colord.desktop
