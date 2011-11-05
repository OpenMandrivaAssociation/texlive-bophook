# revision 17062
# category Package
# catalog-ctan /macros/latex/contrib/bophook
# catalog-date 2006-12-31 16:08:10 +0100
# catalog-license lppl
# catalog-version 0.02
Name:		texlive-bophook
Version:	0.02
Release:	1
Summary:	Provides an At-Begin-Page hook
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bophook
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bophook.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bophook.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bophook.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Using the \AtBeginPage hook, you can add material in the
background of a page. \PageLayout can be used to give page
makeup commands to be executed on every page (e.g., depend on
the page style).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bophook/bophook.sty
%doc %{_texmfdistdir}/doc/latex/bophook/bophook.pdf
#- source
%doc %{_texmfdistdir}/source/latex/bophook/bophook.dtx
%doc %{_texmfdistdir}/source/latex/bophook/bophook.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
