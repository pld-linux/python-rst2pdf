# NOTE: for versions >= 0.98 (for python 3.6+) see python3-rst2pdf.spec
#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-rst2pdf.spec)

Summary:	Convert reStructured Text to PDF via ReportLab
Summary(pl.UTF-8):	Konwersja formatu reStructured Text do PDF przy użyciu ReportLaba
Name:		python-rst2pdf
# keep 0.97 here for python2 support
Version:	0.97
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/rst2pdf/
Source0:	https://files.pythonhosted.org/packages/source/r/rst2pdf/rst2pdf-%{version}.tar.gz
# Source0-md5:	b63d59e1abc28b22fb2e699010754fdf
URL:		https://rst2pdf.org/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The usual way of creating PDF from reStructuredText is by going
through LaTeX. This tool provides an alternative by producing PDF
directly using the ReportLab library.

%description -l pl.UTF-8
Najczęstszym sposobem tworzenia dokumentów PDF z formatu
reStructuredText jest przejście przez LaTeX. To narzędzie udostępnia
alternatywną metodę, tworząc PDF bezpośrednio przy użyciu biblioteki
ReportLab.

%package -n python3-rst2pdf
Summary:	Convert reStructured Text to PDF via ReportLab
Summary(pl.UTF-8):	Konwersja formatu reStructured Text do PDF przy użyciu ReportLaba
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-rst2pdf
The usual way of creating PDF from reStructuredText is by going
through LaTeX. This tool provides an alternative by producing PDF
directly using the ReportLab library.

%description -n python3-rst2pdf -l pl.UTF-8
Najczęstszym sposobem tworzenia dokumentów PDF z formatu
reStructuredText jest przejście przez LaTeX. To narzędzie udostępnia
alternatywną metodę, tworząc PDF bezpośrednio przy użyciu biblioteki
ReportLab.

%prep
%setup -q -n rst2pdf-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__mv} $RPM_BUILD_ROOT%{_bindir}/rst2pdf{,-2}
%endif

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/rst2pdf{,-3}
ln -sf rst2pdf-3 $RPM_BUILD_ROOT%{_bindir}/rst2pdf
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/rst2pdf-2
%{py_sitescriptdir}/rst2pdf
%{py_sitescriptdir}/rst2pdf-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-rst2pdf
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/rst2pdf
%attr(755,root,root) %{_bindir}/rst2pdf-3
%{py3_sitescriptdir}/rst2pdf
%{py3_sitescriptdir}/rst2pdf-%{version}-py*.egg-info
%endif
