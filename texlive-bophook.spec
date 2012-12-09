# revision 17062
# category Package
# catalog-ctan /macros/latex/contrib/bophook
# catalog-date 2006-12-31 16:08:10 +0100
# catalog-license lppl
# catalog-version 0.02
Name:		texlive-bophook
Version:	0.02
Release:	2
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.02-2
+ Revision: 749842
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.02-1
+ Revision: 717973
- texlive-bophook
- texlive-bophook
- texlive-bophook
- texlive-bophook
- texlive-bophook

