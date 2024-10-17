Name:		texlive-latex-graphics-dev
Version:	64899
Release:	2
Summary:	Development pre-release of the LaTeX graphics bundle
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/latex-graphics-dev
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-graphics-dev.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-graphics-dev.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-graphics-dev.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a pre-release version of the standard LaTeX graphics
bundle. It accompanies the pre-testing kernel code
(latex-base-dev), and is intended for testing by knowledgeable
users.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/source
%doc %{_texmfdistdir}/source/latex-dev
%doc %{_texmfdistdir}/source/latex-dev/graphics
%doc %{_texmfdistdir}/source/latex-dev/graphics/trig.dtx
%doc %{_texmfdistdir}/source/latex-dev/graphics/rotating.dtx
%doc %{_texmfdistdir}/source/latex-dev/graphics/mathcolor.dtx
%doc %{_texmfdistdir}/source/latex-dev/graphics/lscape.dtx
%doc %{_texmfdistdir}/source/latex-dev/graphics/keyval.dtx
%doc %{_texmfdistdir}/source/latex-dev/graphics/graphicx.dtx
%doc %{_texmfdistdir}/source/latex-dev/graphics/graphics.ins
%doc %{_texmfdistdir}/source/latex-dev/graphics/graphics.dtx
%doc %{_texmfdistdir}/source/latex-dev/graphics/graphics-drivers.ins
%doc %{_texmfdistdir}/source/latex-dev/graphics/epsfig.dtx
%doc %{_texmfdistdir}/source/latex-dev/graphics/drivers.dtx
%doc %{_texmfdistdir}/source/latex-dev/graphics/color.dtx
%{_texmfdistdir}/tex
%{_texmfdistdir}/tex/latex-dev
%{_texmfdistdir}/tex/latex-dev/graphics
%{_texmfdistdir}/tex/latex-dev/graphics/truetex.def
%{_texmfdistdir}/tex/latex-dev/graphics/trig.sty
%{_texmfdistdir}/tex/latex-dev/graphics/tcidvi.def
%{_texmfdistdir}/tex/latex-dev/graphics/rotating.sty
%{_texmfdistdir}/tex/latex-dev/graphics/pctexwin.def
%{_texmfdistdir}/tex/latex-dev/graphics/pctexps.def
%{_texmfdistdir}/tex/latex-dev/graphics/pctexhp.def
%{_texmfdistdir}/tex/latex-dev/graphics/pctex32.def
%{_texmfdistdir}/tex/latex-dev/graphics/mathcolor.ltx
%{_texmfdistdir}/tex/latex-dev/graphics/lscape.sty
%{_texmfdistdir}/tex/latex-dev/graphics/keyval.sty
%{_texmfdistdir}/tex/latex-dev/graphics/graphicx.sty
%{_texmfdistdir}/tex/latex-dev/graphics/graphics.sty
%{_texmfdistdir}/tex/latex-dev/graphics/graphics-2017-06-25.sty
%{_texmfdistdir}/tex/latex-dev/graphics/epsfig.sty
%{_texmfdistdir}/tex/latex-dev/graphics/emtex.def
%{_texmfdistdir}/tex/latex-dev/graphics/dviwin.def
%{_texmfdistdir}/tex/latex-dev/graphics/dvipsone.def
%{_texmfdistdir}/tex/latex-dev/graphics/dvipsnam.def
%{_texmfdistdir}/tex/latex-dev/graphics/dvipdf.def
%{_texmfdistdir}/tex/latex-dev/graphics/color.sty
%{_texmfdistdir}/doc
%doc %{_texmfdistdir}/doc/latex-dev
%doc %{_texmfdistdir}/doc/latex-dev/graphics
%doc %{_texmfdistdir}/doc/latex-dev/graphics/trig.pdf
%doc %{_texmfdistdir}/doc/latex-dev/graphics/rotex.tex
%doc %{_texmfdistdir}/doc/latex-dev/graphics/rotex.pdf
%doc %{_texmfdistdir}/doc/latex-dev/graphics/rotating.pdf
%doc %{_texmfdistdir}/doc/latex-dev/graphics/mathcolor.pdf
%doc %{_texmfdistdir}/doc/latex-dev/graphics/lscape.pdf
%doc %{_texmfdistdir}/doc/latex-dev/graphics/keyval.pdf
%doc %{_texmfdistdir}/doc/latex-dev/graphics/grfguide.tex
%doc %{_texmfdistdir}/doc/latex-dev/graphics/grfguide.pdf
%doc %{_texmfdistdir}/doc/latex-dev/graphics/graphicx.pdf
%doc %{_texmfdistdir}/doc/latex-dev/graphics/graphics.pdf
%doc %{_texmfdistdir}/doc/latex-dev/graphics/epsfig.pdf
%doc %{_texmfdistdir}/doc/latex-dev/graphics/drivers.pdf
%doc %{_texmfdistdir}/doc/latex-dev/graphics/color.pdf
%doc %{_texmfdistdir}/doc/latex-dev/graphics/changes.txt
%doc %{_texmfdistdir}/doc/latex-dev/graphics/cat.eps
%doc %{_texmfdistdir}/doc/latex-dev/graphics/README.md

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
