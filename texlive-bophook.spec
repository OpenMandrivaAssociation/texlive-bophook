Name:		texlive-bophook
Version:	17062
Release:	1
Summary:	Provides an At-Begin-Page hook
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bophook
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bophook.r17062.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bophook.doc.r17062.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bophook.source.r17062.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Using the \AtBeginPage hook, you can add material in the
background of a page. \PageLayout can be used to give page
makeup commands to be executed on every page (e.g., depend on
the page style).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bophook/bophook.sty
%doc %{_texmfdistdir}/doc/latex/bophook/bophook.pdf
#- source
%doc %{_texmfdistdir}/source/latex/bophook/bophook.dtx
%doc %{_texmfdistdir}/source/latex/bophook/bophook.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
