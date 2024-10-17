Name:		texlive-biblatex-true-citepages-omit
Version:	44653
Release:	2
Summary:	Correction of some limitation of the citepages=omit option of biblatex styles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-true-citepages-omit
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-true-citepages-omit.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-true-citepages-omit.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package corrects a limitation of the citepages=omit option
of the verbose family of biblatex citestyles. The option works
when you \cite[xx]{key}, but not when you \cite[\pno~xx, some
text]{key}. The package correct this problem.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-true-citepages-omit
%doc %{_texmfdistdir}/doc/latex/biblatex-true-citepages-omit

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
