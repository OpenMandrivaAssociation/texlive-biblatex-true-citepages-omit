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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package deals with a limitation of the citepages=omit option of the
verbose family of BibLaTeX citestyles. The option works when you
\cite[xx]{key}, but not when you \cite[\pno~xx, some text]{key}. The
package corrects this problem.

