%global tl_name biblatex-true-citepages-omit
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0.0
Release:	%{tl_revision}.1
Summary:	Correction of some limitation of the citepages=omit option of BibLaTeX styles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-true-citepages-omit
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-true-citepages-omit.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-true-citepages-omit.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package deals with a limitation of the citepages=omit option of the
verbose family of BibLaTeX citestyles. The option works when you
\cite[xx]{key}, but not when you \cite[\pno~xx, some text]{key}. The
package corrects this problem.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-true-citepages-omit
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-true-citepages-omit
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-true-citepages-omit/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-true-citepages-omit/biblatex-true-citepages-omit-example.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-true-citepages-omit/biblatex-true-citepages-omit-example.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-true-citepages-omit/biblatex-true-citepages-omit.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-true-citepages-omit/biblatex-true-citepages-omit.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-true-citepages-omit/biblatex-true-citepages-omit.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-true-citepages-omit/example.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-true-citepages-omit/latexmkrc
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-true-citepages-omit/makefile
%{_datadir}/texmf-dist/tex/latex/biblatex-true-citepages-omit/biblatex-true-citepages-omit.sty
