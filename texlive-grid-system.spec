Name:		texlive-grid-system
Version:	32981
Release:	2
Summary:	Page organisation, modelled on CSS facilities
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/grid-system
License:	APACHE2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grid-system.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grid-system.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means for LaTeX to implement a grid
system as known from CSS grid systems. The facility is useful
for creating box layouts as used in brochures.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/grid-system/grid-system.sty
%doc %{_texmfdistdir}/doc/latex/grid-system/LICENSE
%doc %{_texmfdistdir}/doc/latex/grid-system/README
%doc %{_texmfdistdir}/doc/latex/grid-system/grid-system.pdf
%doc %{_texmfdistdir}/doc/latex/grid-system/grid-system.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
