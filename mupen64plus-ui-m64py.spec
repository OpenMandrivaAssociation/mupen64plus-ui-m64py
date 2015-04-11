# Could be noarch package but depends on arch library path
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define oname m64py

Summary:	M64Py - A frontend for Mupen64Plus
Name:		mupen64plus-ui-%{oname}
Version:	0.2.1
Release:	2
License:	GPLv3+
Group:		Emulators
Url:		http://m64py.sourceforge.net
Source0:	http://sourceforge.net/projects/m64py/files/%{oname}-%{version}/%{oname}-%{version}.tar.gz
BuildRequires:	python2-setuptools
BuildRequires:	python2-devel
BuildRequires:	python-qt4-devel
BuildRequires:	pkgconfig(icu-i18n)

Requires:	PyQt4
Requires:	mupen64plus >= 2.0

%description
M64Py is a Qt4 front-end (GUI) for Mupen64Plus 2.0, a cross-platform
plugin-based Nintendo 64 emulator. Front-end is written in Python and
it provides a user-friendly interface over Mupen64Plus shared library.

%files
%{_bindir}/%{oname}
%{_datadir}/applications/%{oname}.desktop
%{_iconsdir}/hicolor/96x96/mimetypes/application-x-%{oname}.png
%{_datadir}/mime/packages/application-x-%{oname}.xml
%{_datadir}/pixmaps/%{oname}.png
%{py2_puresitedir}/%{oname}
%{py2_puresitedir}/%{oname}-*.egg-info

%prep
%setup -q -n %{oname}-%{version}
sed s,"/usr/lib/mupen64plus","%{_libdir}/mupen64plus2",g -i src/m64py/platform.py

#----------------------------------------------------------------------------

%build
ln -s %{_bindir}/python2 python
export PATH=`pwd`:$PATH

python setup.py build

%install
python setup.py install --root %{buildroot}

# messged up in setup.py
rm -rf %{buildroot}%{_iconsdir}/hicolor/96x96/mimetypes/application-x-%{oname}.png
cp xdg/%{oname}.png %{buildroot}%{_iconsdir}/hicolor/96x96/mimetypes/application-x-%{oname}.png

