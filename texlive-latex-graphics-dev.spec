%global tl_name latex-graphics-dev
%global tl_revision 79242

Name:		texlive-%{tl_name}
Epoch:		1
Version:	pre~release.0
Release:	%{tl_revision}.1
Summary:	Development pre-release of the LaTeX graphics bundle
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex-dev/required/graphics
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-graphics-dev.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-graphics-dev.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-graphics-dev.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(graphics-cfg)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a pre-release version of the standard LaTeX graphics bundle. It
accompanies the pre-testing kernel code (latex-base-dev), and is
intended for testing by knowledgeable users.

