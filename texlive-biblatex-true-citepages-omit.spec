# revision 33305
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-true-citepages-omit
# catalog-date 2014-04-08 11:06:38 +0200
# catalog-license lppl
# catalog-version 1.0.0
Name:		texlive-biblatex-true-citepages-omit
Version:	1.0.0
Release:	1
Summary:	Correction of some limitation of the citepages=omit option of biblatex styles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-true-citepages-omit
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-true-citepages-omit.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-true-citepages-omit.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/biblatex-true-citepages-omit/biblatex-true-citepages-omit.sty
%doc %{_texmfdistdir}/doc/latex/biblatex-true-citepages-omit/README
%doc %{_texmfdistdir}/doc/latex/biblatex-true-citepages-omit/biblatex-true-citepages-omit.bib
%doc %{_texmfdistdir}/doc/latex/biblatex-true-citepages-omit/biblatex-true-citepages-omit.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-true-citepages-omit/biblatex-true-citepages-omit.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-true-citepages-omit/exemple.bib
%doc %{_texmfdistdir}/doc/latex/biblatex-true-citepages-omit/exemple.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-true-citepages-omit/exemple.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-true-citepages-omit/latexmkrc
%doc %{_texmfdistdir}/doc/latex/biblatex-true-citepages-omit/makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
