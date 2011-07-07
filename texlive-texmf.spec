# This spec file is based on texjive project created by Michael A. Peters.
# Adopted and modified for Fedora users by Jindrich Novy.

%{!?_texmf_main: %global _texmf_main %{_datadir}/texmf}
%{!?_texmf_vendor: %global _texmf_vendor %{_datadir}/texmf}
%{!?_texmf_var: %global _texmf_var  %{_var}/lib/texmf}
%{!?_texmf_conf: %global _texmf_conf %{_sysconfdir}/texmf}
%{!?_texmf_local: %global _texmf_local %{_usr}/local/share/texmf}

%define	ptex_texmf_ver 2.5

# do not provide any perl deps (#516350)
%define __perl_provides %{nil}

Name:		texlive-texmf
Version:	2007
Release:	35%{?dist}
Summary:	Architecture independent parts of the TeX formatting system

Group:		Applications/Publishing
License:	Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:		http://tug.org/texlive/

# Source0 comes as a result from scripts that look for files in teTeX and assigns appropriate
# TeXLive styles to it so that no style present in teTeX will be missing in TeXLive.
# it contains expanded packages from ftp://tug.org/texlive/Contents/inst/archive/
# Scripts that are used for that are available at http://people.redhat.com/jnovy/files/texlive/scripts/
Source0:	texlive.texmf-%{version}.tar.lzma
# Source1 is http://www.tug.org/texlive/Contents/inst/archive/texmf-var.zip
Source1:	texlive.texmf-var-%{version}.zip

# pregenerated kpathsea ls-R files in case no binary TeXLive is present to regenerate them
Source10:	texlive.%{version}.ls-R
Source11:	texlive.var.%{version}.ls-R

# missing files (note - Fedora installs this with a patch)
Source50:	dvips-config.generic

# TeXLive package list included in Source0
Source91:	texlive.%{version}.zip.list

# filter perl requires
Source99: texlive-filter-requires.sh
%define __perl_requires %{SOURCE99}

# updates of the basic TeX Live 2007 texmf tree
Source100:	ftp://dante.ctan.org/tex-archive/macros/latex/contrib/envlab.zip
Source101:	ftp://dante.ctan.org/tex-archive/macros/latex/contrib/perltex.zip
Source102:	ftp://dante.ctan.org/tex-archive/macros/latex/contrib/achemso.zip
Source103:	ftp://dante.ctan.org/tex-archive/macros/latex/contrib/IEEEconf.zip

# speed up build, run only brp-compress, nothing else is needed
%define __os_install_post /usr/lib/rpm/brp-compress %{nil}

# Source1000-: Japanese pTeX
Source1000: ftp://ftp.ascii.co.jp/pub/TeX/ascii-ptex/tetex/ptex-texmf-%{ptex_texmf_ver}.tar.gz
Source1001: ftp://ftp.ascii.co.jp/pub/TeX/ascii-ptex/platex/platex209.tar.gz
Source1002: dvipsk-jfontimage.tar.bz2
Source1003: fmtutil-ptex.cnf

# patches
Patch0:		texlive-2007-badenv.patch
Patch1:		texlive-2007-tkdefaults.patch
Patch2:		texlive-2007-updmap.patch
Patch3:		texlive-2007-texmfconf.patch
Patch4:		texlive-2007-romanian.patch
Patch5:		texlive-2007-euro.patch
Patch6:		texlive-2007-beamerblocks.patch
Patch7:		texlive-2007-latin.patch

# Patch1000-: Japanese pTeX
Patch1001: texlive-2007-texmf.cnf-ptex.patch

BuildRequires:  sed >= 3.95 ghostscript lzma tex(latex)

Requires:	texlive-texmf-errata = %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

Obsoletes:	tetex-eurofont
Obsoletes:	tetex-unicode
Obsoletes:	tetex-lineno = 4.41
Provides:	tetex-lineno = 4.42

%description
texlive-texmf is a texmf distribution based upon TeX Live. All of the files
contained in these packages are from the TeX Live zip files. The intent is to
provide a packaging similar in style and layout to teTeX.

%package afm
Group:		Applications/Publishing
Summary:	Texmf files needed for texlive-afm
Requires:	texlive-texmf = %{version}-%{release}
Requires:	texlive-texmf-errata-afm = %{version}

%description afm
This package contains the components of the TEXMF tree needed for the
texlive-afm package.

%package doc
Group:		Applications/Publishing
Summary:	TeX documentation
Requires:	texlive-texmf-errata-doc = %{version}
Obsoletes:	tetex-doc < 3.0-99
Provides:	tetex-doc = 3.0-99
Obsoletes:	texlive-doc < 2007-7
Provides:	texlive-doc = %{version}-%{release}

%description doc
This package contains the documentation for packages installed as part of
texlive. You should install this package if you are new to TeX and LaTeX,
and familiarize yourself with the use of the texdoc command.

%package dvips
Group:		Applications/Publishing
Summary:	Texmf files needed for texlive-dvips
Requires:	texlive-texmf = %{version}-%{release}
Requires:	texlive-texmf-errata-dvips = %{version}

%description dvips
This package contains the components of the TEXMF tree needed for the
texlive-dvips package.

%package fonts
Group:		Applications/Publishing
Summary:	Font files needed for TeXLive
Requires:	texlive-texmf = %{version}-%{release}
Requires:	texlive-texmf-dvips = %{version}-%{release}
Requires:	texlive-texmf-errata-fonts = %{version}
Requires(post): coreutils

%description fonts
This package contains the components of the TEXMF tree needed for the
texlive-fonts package.

%package latex
Group:		Applications/Publishing
Summary:	Texmf files needed for texlive-latex
Requires:	texlive-texmf = %{version}-%{release}
Requires:	texlive-texmf-errata-latex = %{version}
Requires:	tex-preview
Obsoletes:	tetex-bytefield < 1.2a-7
Provides:	tetex-bytefield = 1.2a-7
Obsoletes:	tetex-prosper < 1.5-7
Provides:	tetex-prosper = 1.5-7
Obsoletes:	tetex-perltex < 2.0
Provides:	tetex-perltex = 2.0

%description latex
This package contains the components of the TEXMF tree needed for the
texlive-latex package.

%package xetex
Group:		Applications/Publishing
Summary:	Texmf files needed for texlive-xetex
Requires:	texlive-texmf = %{version}-%{release}
Requires:	texlive-texmf-errata-xetex = %{version}

%description xetex
This package contains the components of the TEXMF tree needed for the
texlive-xetex package.

%package east-asian
Group:		Applications/Publishing
Summary:	Texmf files needed for texlive-east-asian
Requires:	texlive-texmf = %{version}-%{release}
Obsoletes:	texlive-texmf-japanese < 2007-14
Provides:	texlive-texmf-japanese = %{version}-%{release}

%description east-asian
Architecture independent files for support of East Asian languages in TeXLive.

%package context
Group:		Applications/Publishing
Summary:	Texmf files needed for ConTeXt
Requires:	texlive-texmf = %{version}-%{release}
Requires:	texlive-texmf-errata-context = %{version}

%description context
This package contains the components of the TEXMF tree needed for the
texlive-context package.

%prep
%setup -q -c -T
lzma -dc %{SOURCE0} | tar x

# extract envlab
unzip %{SOURCE100}
# extract perltex
unzip %{SOURCE101}
# extract achemso
unzip %{SOURCE102}
# extract IEEEconf
unzip %{SOURCE103}

mkdir texmf-var
unzip -d texmf-var %{SOURCE1}
install -p -m644 %{SOURCE50} texmf-var/dvips/config/config.generic

%patch0  -p0
%patch1  -p0
%patch2  -p1
%patch3  -p1
%patch4  -p0
%patch5  -p0
%patch6  -p0
%patch7  -p1

cp -p %{SOURCE91} .

# we use web2c/fmutil.cnf for defaults
rm -f texmf/fmtutil/*

# these we do not want
# - they are owned by main package in /usr/bin
rm -rf texmf/scripts/tetex
rm -rf texmf/scripts/thumbpdf
rm -rf texmf/scripts/pdfcrop

# Japanese pTeX
# set platex to Japanese pLaTeX. original one is moved to platex-pl
cd texmf-dist/tex/platex/config
for i in *.ini ; do
  mv ${i} `basename ${i} .ini`-pl.ini
done
cd -
sed -e s/^platex/platex-pl/g \
    -e s/^pdfplatex/pdfplatex-pl/g \
    -e s/platex\.ini/platex\-pl\.ini/g \
     -i texmf/web2c/fmtutil.cnf
# add japanese ptex fmtutil configuration
cat texmf/web2c/fmtutil.cnf %{SOURCE1003} > texmf/web2c/fmtutil.cnf-ptex
mv texmf/web2c/fmtutil.cnf-ptex texmf/web2c/fmtutil.cnf

tar xfz %{SOURCE1000}
for i in doc fonts jbibtex ptex ; do
  cp -a ptex-texmf/${i} texmf/
done
mkdir -p texmf/doc/ptex/ptex-texmf
# Convert Japanese documents to UTF-8
for i in COPYRIGHT COPYRIGHT.jis Changes.txt README.txt ; do
  iconv -f ISO-2022-JP -t UTF-8 ptex-texmf/${i} \
        -o texmf/doc/ptex/ptex-texmf/${i}
done
rm -rf ptex-texmf
# Prepare platex209
tar xfz %{SOURCE1001} -C texmf/ptex
cat > texmf/ptex/platex209/plplain.ini << EOF
\input plplain.tex \dump
EOF
# Prepare pdvips fonts
mkdir pdvipsk-font
tar xfj %{SOURCE1002} -C pdvipsk-font
cp -a pdvipsk-font/usr/share/texmf/fonts/* texmf/fonts
rm -rf pdvipsk-font
# Prepare texmf.cnf
%patch1001 -p0

%build
# not compiling anything, but this stuff isn't really %%prep or %%install

# setup texmf.cnf properly
pushd texmf/web2c
%{__sed} -i 's?^TEXMFMAIN =.*?TEXMFMAIN = %{_texmf_main}?' texmf.cnf
%{__sed} -i 's?^TEXMFDIST =.*?TEXMFDIST = %{_texmf_main}?' texmf.cnf
%{__sed} -i 's?^TEXMFSYSVAR =.*?TEXMFSYSVAR = %{_texmf_var}?' texmf.cnf
%{__sed} -i 's?^TEXMFSYSCONFIG =.*?TEXMFSYSCONFIG = %{_texmf_conf}?' texmf.cnf
%{__sed} -i 's?^TEXMFVENDOR =.*?TEXMFVENDOR = %{_texmf_vendor}?' texmf.cnf
%{__sed} -i 's?^TEXMF =.*?TEXMF = {$TEXMFCONFIG,$TEXMFVAR,$TEXMFHOME,$TEXMFSYSCONFIG,!!$TEXMFSYSVAR,!!$TEXMFLOCAL,!!$TEXMFMAIN,!!$TEXMFDIST}?' texmf.cnf
%{__sed} -i 's?^TEXMFLOCAL =.*?TEXMFLOCAL = %{_texmf_local}?' texmf.cnf

%{__sed} -i 's?^TEXMFMAIN .*?TEXMFMAIN     = %{_texmf_main}?' context.cnf
%{__sed} -i 's?^VARTEXMF .*?VARTEXMF      = %{_texmf_var}?' context.cnf
%{__sed} -i 's?^TEXMFVENDOR .*?TEXMFVENDOR   = %{_texmf_vendor}?' context.cnf
popd

# nuke these
rm -f texmf/web2c/texmf.cnf-4WIN
rm -f texmf/web2c/texmf.cnf.orig
rm -f texmf/texdoctk/texdocrc-win32.defaults
rm -f texmf/ptex/platex/base/.cvsignore
rm -f texmf-dist/doc/latex/newlfm/*.bat
rm -f texmf-dist/doc/generic/t2/etc/rumkidx/*.bat
rm -f texmf-dist/tex/plain/cyrplain/makefmts.bat

install -d -m755 texmf-var/fonts/map/{dvipdfm,dvips,pdftex}/updmap

# for ghosting
touch texmf-var/fonts/map/dvipdfm/updmap/{dvipdfm_dl14.map,dvipdfm.map,dvipdfm_ndl14.map}
touch texmf-var/fonts/map/dvips/updmap/{builtin35.map,ps2pk.map,psfonts_pk.map,download35.map,psfonts.map,psfonts_t1.map}
touch texmf-var/fonts/map/pdftex/updmap/{pdftex_dl14.map,pdftex.map,pdftex_ndl14.map}

# We really don't want these imho
rm -rf texmf-dist/fonts/pk && mkdir texmf-dist/fonts/pk
rm -rf texmf/doc/man
rm -rf texmf-dist/doc/man
rm -rf texmf-dist/scripts/context/stubs/mswin

# We want these but in the right place
mv texmf/doc/info/tds.info .

# now nuke the info dir
rm -rf texmf/doc/info
rm -rf texmf-dist/doc/info

# Create symlinks for Euler fonts (RH #9782)
pushd texmf-dist/tex/latex/amsfonts
for i in ex f r s ; do
  ln -sf ueu${i}.fd Ueu${i}.fd
done
popd

# fix the bloody permissions - Grrrr
chmod 644 \
  texmf-dist/scripts/oberdiek/pdfatfi.pl texmf-dist/doc/generic/enctex/unimap.py \
  texmf-dist/doc/latex/minitoc/{emk,fmk,imk,pmk,rmk,tmk,xmk} texmf-dist/doc/latex/multibib/bibtexall \
  texmf-dist/doc/generic/pstricks-add/examples/{dataI.dat,dataII.dat}
chmod 755 texmf-var/{tex,dvipdfm,dvipdfm/config,dvips,dvips/config} texmf-var/tex \
  texmf-var/tex/{plain,plain/config,context,context/config,generic,generic/config}

# fix the ConTeXt ruby scripts
for ruby in `find texmf-dist/scripts/context/ruby/ -name *.rb` \
	    texmf-dist/scripts/context/stubs/unix/* \
	    ; do
  if [ `head -1 ${ruby} | grep -c "^#!"` -eq 1 ]; then
    chmod 755 ${ruby}
  else
    chmod 644 ${ruby}
  fi
done

# fix references to nonexistent cm-super fonts
for i in `find . -name *.map` ; do
  if [ `grep -c cm-super ${i}` != 0 ]; then
    mv ${i} ${i}.old
    grep -v cm-super ${i}.old > ${i} || :
    rm -f ${i}.old
  fi
done

# fix empty documentation files
echo "%%%" >> texmf-dist/doc/latex/mathpazo/mapppl.tex
echo "%%%" >> texmf-dist/doc/latex/mathpazo/mapzplm.tex

# these should be in scripts with symlink to current location
mkdir -p texmf/scripts/hyphen/sh
pushd texmf/tex/generic/hyphen/
install -p -m755 bahyph.sh ../../../scripts/hyphen/sh/
rm -f bahyph.sh
ln -s ../../../scripts/hyphen/sh/bahyph.sh .
popd

# these files owned by binary texlive package
rm -f texmf/web2c/pdfetex-pl.pool
rm -f texmf/web2c/pdfetex.pool

# these files owned by binary texlive-fonts package
rm -f texmf/web2c/{mktex.opt,mktexdir,mktexdir.opt,mktexnam,mktexnam.opt,mktexupd}

# these files owned by binary texlive-dvips package
rm -rf texmf/dvips/base

# remove ttf2pk stuff from bin-ttfutils
rm -f texmf/doc/man/man1/ttf2pk.1
rm -rf texmf/doc/ttf2pk/
rm -rf texmf/fonts/enc/ttf2pk/
rm -rf texmf/fonts/map/ttf2pk/
rm -rf texmf/fonts/sfd/
rm -rf texmf/ttf2pk/

#remove ubbold.fd (#458150)
rm -f texmf/tex/latex/jknapltx/ubbold.fd

# build envlab
rm -f texmf-dist/tex/latex/envlab/*
rm -f texmf-dist/doc/latex/envlab/*
pushd envlab
latex envlab.ins
install -p -m 644 *.sty ../texmf-dist/tex/latex/envlab/
install -p -m 644 *.pdf ../texmf-dist/doc/latex/envlab/
install -p -m 644 README ../texmf-dist/doc/latex/envlab/
popd

# build perltex
rm -f texmf-dist/tex/latex/perltex/*
rm -f texmf-dist/doc/latex/perltex/*
pushd perltex
latex perltex.ins
%{__sed} -i 's,^#! /usr/bin/env perl$,#!%{__perl},' perltex.pl
install -p -m 644 *.sty ../texmf-dist/tex/latex/perltex/
install -p -m 644 *.pdf ../texmf-dist/doc/latex/perltex/
install -p -m 644 README ../texmf-dist/doc/latex/perltex/
popd

# build achemso
rm -f texmf-dist/tex/latex/achemso/*
rm -f texmf-dist/doc/latex/achemso/*
pushd achemso
latex achemso.ins
install -p -m 644 *.sty ../texmf-dist/tex/latex/achemso/
install -p -m 644 *.cls ../texmf-dist/tex/latex/achemso/
install -p -m 644 *.bst ../texmf-dist/tex/latex/achemso/
install -p -m 644 *.cfg ../texmf-dist/tex/latex/achemso/
install -p -m 644 *.pdf ../texmf-dist/doc/latex/achemso/
install -p -m 644 README ../texmf-dist/doc/latex/achemso/
popd

# build IEEEconf
mkdir -p texmf-dist/tex/latex/IEEEconf
mkdir -p texmf-dist/doc/latex/IEEEconf
pushd IEEEconf
latex IEEEconf.ins
install -p -m 644 *.cls ../texmf-dist/tex/latex/IEEEconf/
install -p -m 644 *.pdf ../texmf-dist/doc/latex/IEEEconf/
install -p -m 644 README ../texmf-dist/doc/latex/IEEEconf/
popd


%install
rm -rf %{buildroot} && mkdir -p %{buildroot}

install -d -m755 %{buildroot}%{_infodir}
install -p -m644 tds.info %{buildroot}%{_infodir}/

# install the texmf
mkdir -p %{buildroot}%{_texmf_main}
mkdir -p %{buildroot}%{_texmf_var}
mkdir -p %{buildroot}%{_texmf_vendor}

cp -a %{SOURCE10} %{buildroot}%{_texmf_main}/default.ls-R
cp -a %{SOURCE11} %{buildroot}%{_texmf_var}/default.ls-R

# ghostscript cmap required for dvipdfmx
if [ -d "%{_datadir}/ghostscript/`gs --version| cut -d . -f 1-2`/Resource/CMap" ] ; then
  cmap_dir="%{_datadir}/ghostscript/"`gs --version| cut -d . -f 1-2`"/Resource/CMap/"
elif [ -d "%{_datadir}/ghostscript/Resource/CMap" ] ; then
  cmap_dir="%{_datadir}/ghostscript/Resource/CMap/"
fi
if [ z"$cmap_dir" != 'z' ]; then
  %{__sed} -i 's?^CMAPFONTS = .*?CMAPFONTS = .;$TEXMF/fonts/cmap//;'"$cmap_dir"'?' texmf/web2c/texmf.cnf
fi

cp -a texmf/* %{buildroot}%{_texmf_main}
cp -a texmf-var/* %{buildroot}%{_texmf_var}
cp -a texmf-dist/* %{buildroot}%{_texmf_vendor}

install -d -m755 %{buildroot}%{_texmf_main}/fonts/{cmap,sfd,type3,type42}

# move the configuration files and symlink them
install -d -m755 %{buildroot}%{_texmf_conf}/web2c
mv %{buildroot}%{_texmf_main}/web2c/mktex.cnf %{buildroot}%{_texmf_conf}/web2c/
for file in `ls %{buildroot}%{_texmf_conf}/web2c/ | egrep 'c(nf|fg)$'`; do
  filename="`basename ${file}`"
  ln -sf %{_texmf_conf}/web2c/${filename} %{buildroot}%{_texmf_main}/web2c/
done

if [ -x %{_bindir}/texhash ]; then
  texhash %{buildroot}%{_texmf_main}
  mv %{buildroot}%{_texmf_main}/ls-R %{buildroot}%{_texmf_main}/default.ls-R
  texhash %{buildroot}%{_texmf_var}
  mv %{buildroot}%{_texmf_var}/ls-R %{buildroot}%{_texmf_var}/default.ls-R
else
  install -p -m644 %{SOURCE10} %{buildroot}%{_texmf_main}/default.ls-R
  install -p -m644 %{SOURCE11} %{buildroot}%{_texmf_var}/default.ls-R
fi
touch %{buildroot}%{_texmf_main}/ls-R
touch %{buildroot}%{_texmf_var}/ls-R
install -d -m755 %{buildroot}%{_texmf_vendor}/{doc,tex}/{generic,latex}
install -d -m755 %{buildroot}%{_texmf_vendor}/fonts
touch %{buildroot}%{_texmf_vendor}/ls-R
touch %{buildroot}%{_texmf_conf}/ls-R

# remove xdvi files, now packaged separately
rm -rf %{buildroot}%{_texmf_var}/xdvi

# remove dvipdfmx files
rm %{buildroot}%{_texmf_main}/dvipdfm/{dvipdfmx.cfg,EUC-UCS2,README,UniKSCms-UCS2-H,UniKSCms-UCS2-V}

# remove win32 dvipdfm file
rm %{buildroot}%{_texmf_main}/dvipdfm/config/config-win32

# remove preview, it's now packaged separately (#425805)
rm -rf %{buildroot}%{_texmf_main}/tex/latex/preview/
rm -rf %{buildroot}%{_texmf_main}/doc/latex/preview/

# remove binaries from splitindex (#476636)
rm -rf %{buildroot}%{_texmf_main}/doc/latex/splitindex/*i386* \
%{buildroot}%{_texmf_main}/doc/latex/splitindex/*.exe \
%{buildroot}%{_texmf_main}/doc/latex/splitindex/*.class

# remove $TEXMFMAIN/tex/texinfo to not to clash with texinfo (#226488)
rm -rf %{buildroot}%{_texmf_main}/tex/texinfo/

# remove dvipdfm configuration file
rm -rf %{buildroot}%{_texmf_main}/dvipdfm

# install perltex
install -d -m755 %{buildroot}%{_bindir}
install -p -m755 perltex/perltex.pl %{buildroot}%{_bindir}/perltex

# fix permissions of /var/lib/texmf/web2c
chmod 755 %{buildroot}%{_texmf_var}/web2c

# create macro file for building texlive
mkdir -p %{buildroot}%{_sysconfdir}/rpm
cat <<EOF > %{buildroot}%{_sysconfdir}/rpm/macros.texlive
# macros to keep trees in texlive consistent
%%_texmf_main     %{_texmf_main}
%%_texmf_vendor   %{_texmf_vendor}
%%_texmf_var      %{_texmf_var}
%%_texmf_conf     %{_texmf_conf}
EOF

%clean
rm -rf %{buildroot}

%post
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
[ -x /sbin/install-info ] && /sbin/install-info %{_infodir}/tds.info.gz %{_infodir}/dir
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%post afm
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%post dvips
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%post fonts
# done in fonts because fonts package owns texhash
#  this is really only needed for build system
if [ ! -x %{_bindir}/texhash ]; then
  cat %{_texmf_main}/default.ls-R > %{_texmf_main}/ls-R
  cat %{_texmf_var}/default.ls-R  > %{_texmf_var}/ls-R
else
  [ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
fi
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%post latex
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%post xetex
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%post doc
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
:

%post east-asian
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%post context
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%preun
if [ "$1" = 0 ]; then
  [ -x /sbin/install-info ] && /sbin/install-info --delete %{_infodir}/tds.info.gz %{_infodir}/dir || :
fi
:


%postun
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%postun afm
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%postun dvips
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%postun fonts
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%postun latex
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%postun xetex
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%postun doc
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%postun east-asian
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%postun context
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/rpm/macros.texlive
%doc texlive.%{version}.zip.list
%dir %{_texmf_main}/bibtex
%{_texmf_main}/bibtex/bib/
%{_texmf_main}/bibtex/csf/
%dir %{_texmf_main}/bibtex/bst
%{_texmf_main}/bibtex/bst/[a-b]*/
%{_texmf_main}/bibtex/bst/camel/
%{_texmf_main}/bibtex/bst/[d-x]*/
%dir %{_texmf_main}/fmtutil
%{_texmf_main}/makeindex/
%{_texmf_main}/metafont/
%dir %{_texmf_main}/metapost
%{_texmf_main}/metapost/base/
%{_texmf_main}/metapost/config/
%{_texmf_main}/metapost/mfpic/
%{_texmf_main}/metapost/misc/
%{_texmf_main}/metapost/makecirc/
%{_texmf_main}/metapost/mpattern/
%{_texmf_main}/metapost/support/
%{_texmf_main}/metapost/texpower/
%{_texmf_main}/omega/
%dir %{_texmf_main}/scripts
%{_texmf_main}/scripts/hyphen/
%{_texmf_main}/scripts/oberdiek/
%{_texmf_main}/scripts/pkfix/
%{_texmf_main}/scripts/ppower4/
%{_texmf_main}/scripts/ps2eps/
%{_texmf_main}/texconfig/
%dir %{_texmf_main}/tex
%{_texmf_main}/tex/amstex/
%{_texmf_main}/tex/csplain/
%{_texmf_main}/tex/eplain/
%{_texmf_main}/tex/fontinst/
%dir %{_texmf_main}/tex/lambda
%dir %{_texmf_main}/tex/lambda/base
%{_texmf_main}/tex/lambda/config/
%{_texmf_main}/tex/lambda/base/*.tex
%{_texmf_main}/tex/lambda/base/*.bgd
%{_texmf_main}/tex/lambda/base/*.lay
%{_texmf_main}/tex/lambda/base/*.hpn
%{_texmf_main}/tex/lambda/base/*.fd
%{_texmf_main}/tex/lambda/base/*.def
%{_texmf_main}/tex/lambda/base/*.sty
%{_texmf_main}/tex/lambda/oinuit/
%{_texmf_main}/tex/mex/
%{_texmf_main}/tex/mltex/
%{_texmf_main}/tex/plain/
%{_texmf_main}/texdoctk/
%{_texmf_main}/vtex/
# will result in a couple files being owned by texmf and texmf-fonts
#  texmf/tex/generic/babel/{frenchb.cfg,hyphen.cfg}
#  Not really worth worrying about.
%dir %{_texmf_main}/tex/generic
%{_texmf_main}/tex/generic/[a-h]*/
%{_texmf_main}/tex/generic/[j-o]*/
%{_texmf_main}/tex/generic/p[a-f]*/
%dir %{_texmf_main}/tex/generic/pgf
%{_texmf_main}/tex/generic/pgf/basiclayer/
%{_texmf_main}/tex/generic/pgf/frontendlayer/
%{_texmf_main}/tex/generic/pgf/libraries/
%{_texmf_main}/tex/generic/pgf/systemlayer/
%dir %{_texmf_main}/tex/generic/pgf/utilities
%{_texmf_main}/tex/generic/pgf/utilities/*.tex
%{_texmf_main}/tex/generic/pgf/utilities/pgfutil-latex.def
%{_texmf_main}/tex/generic/pgf/utilities/pgfutil-plain.def
%{_texmf_main}/tex/generic/p[i-x]*/
%{_texmf_main}/tex/generic/[q-w]*/
%{_texmf_main}/tex/generic/xu-hyphen/
%{_texmf_main}/tex/generic/xypic/
# configs
%dir %{_texmf_main}/web2c
%{_texmf_main}/web2c/*.tcx
%{_texmf_main}/web2c/fmtutil.cnf
%{_texmf_main}/web2c/mktex.cnf
%{_texmf_main}/web2c/texmf.cnf
%{_texmf_main}/web2c/*.cfg
%config(noreplace) %{_texmf_conf}/web2c/*.cnf
%{_texmf_main}/web2c/aleph.pool
%{_texmf_main}/web2c/mf.pool
%{_texmf_main}/web2c/omega.pool
%{_texmf_main}/web2c/pdftex.pool
%{_texmf_main}/web2c/tex.pool
# var
%config(noreplace) %{_texmf_var}/web2c/mktex.cnf
%dir %{_texmf_var}/tex/
%{_texmf_var}/tex/generic
%{_texmf_var}/tex/plain
%dir %{_texmf_var}/fonts
%dir %{_texmf_var}/fonts/map
%dir %{_texmf_var}/fonts/map/dvipdfm
%dir %{_texmf_var}/fonts/map/dvipdfm/updmap
%dir %{_texmf_var}/fonts/map/dvips
%dir %{_texmf_var}/fonts/map/pdftex
%ghost %{_texmf_var}/fonts/map/dvipdfm/updmap/*
%dir %{_texmf_var}/fonts/map/dvips/updmap
%ghost %{_texmf_var}/fonts/map/dvips/updmap/*
%dir %{_texmf_var}/fonts/map/pdftex/updmap
%ghost %{_texmf_var}/fonts/map/pdftex/updmap/*
%{_texmf_var}/dvipdfm
%{_texmf_var}/web2c
# info
%{_infodir}/tds.info.*
# ls-R
%ghost %{_texmf_main}/ls-R
#%ghost %{_texmf_vendor}/ls-R
%ghost %{_texmf_conf}/ls-R
%ghost %{_texmf_var}/ls-R
%{_texmf_main}/default.ls-R
# former common subpackage, should not own any installed files.
%dir %{_texmf_main}
# for addon packages that want to put stuff in these directories
#%dir %{_texmf_vendor}
%dir %{_texmf_vendor}/doc
%dir %{_texmf_vendor}/doc/generic
%dir %{_texmf_vendor}/doc/latex
# a few TDS directories (more need to be added)
#%dir %{_texmf_vendor}/tex
#%dir %{_texmf_vendor}/tex/generic
%dir %{_texmf_vendor}/tex/latex
%dir %{_texmf_vendor}/fonts
%dir %{_texmf_var}
# conf
%dir %{_texmf_conf}
%dir %{_texmf_conf}/web2c
# texmf-var
%{_texmf_var}/default.ls-R

%files east-asian
%defattr(-,root,root,-)
%dir %{_texmf_main}/ptex
%{_texmf_main}/jbibtex
%{_texmf_main}/ptex/plain
%{_texmf_main}/ptex/platex
%{_texmf_main}/ptex/platex209

%files context
%defattr(-,root,root,-)
%dir %{_texmf_main}/context
%dir %{_texmf_main}/context/data
%{_texmf_main}/context/config/
%{_texmf_main}/context/data/*.gui
%{_texmf_main}/context/data/*.ini
%{_texmf_main}/context/data/*.xml
%{_texmf_main}/context/data/*.rme
%{_texmf_main}/context/data/*.dat
%{_texmf_main}/context/data/*.vim
%{_texmf_main}/context/data/cont-*.properties
%{_texmf_main}/context/data/context.properties
%{_texmf_main}/context/data/contextnames.txt
%{_texmf_main}/context/data/latex-scite.properties
%{_texmf_main}/context/data/metafun-scite.properties
%{_texmf_main}/context/data/scite-ctx.properties
%{_texmf_main}/context/data/scite-ctx.readme
%{_texmf_main}/tex/context/
%{_texmf_main}/scripts/context/
%{_texmf_var}/tex/context/
%{_texmf_main}/web2c/context.cnf
%{_texmf_main}/metapost/context/
%{_texmf_main}/tex/generic/context/
%{_texmf_main}/bibtex/bst/context/
%{_texmf_main}/tex/generic/pgf/utilities/pgfutil-context.def
%{_texmf_main}/fonts/enc/dvips/context/
%{_texmf_main}/fonts/map/pdftex/context/
%{_texmf_main}/fonts/map/dvipdfm/context/

%files afm
%defattr(-,root,root,-)
%{_texmf_main}/fonts/afm/

%files dvips
%defattr(-,root,root,-)
%dir %{_texmf_main}/dvips
%{_texmf_main}/dvips/[a-b]*/
%{_texmf_main}/dvips/cm/
%dir %{_texmf_main}/dvips/config
%config(noreplace) %{_texmf_main}/dvips/config/*
%{_texmf_main}/dvips/courier/
%{_texmf_main}/dvips/cs/
%{_texmf_main}/dvips/[d-z]*/
%{_texmf_var}/dvips/
%dir %{_texmf_main}/fonts/enc/dvips
%{_texmf_main}/fonts/enc/dvips/[a-b]*/
%{_texmf_main}/fonts/enc/dvips/cb/
%{_texmf_main}/fonts/enc/dvips/cc-pl/
%{_texmf_main}/fonts/enc/dvips/cs/
%{_texmf_main}/fonts/enc/dvips/[d-z]*/
%{_texmf_main}/fonts/map/dvips/

%files fonts
%defattr(-,root,root,-)
%dir %{_texmf_main}/fonts
%dir %{_texmf_main}/fonts/enc
%dir %{_texmf_main}/fonts/map
%{_texmf_main}/fonts/map/fontname/
%{_texmf_main}/fonts/cmap/
%{_texmf_main}/fonts/ofm/
%{_texmf_main}/fonts/opentype/
%{_texmf_main}/fonts/ovf/
%{_texmf_main}/fonts/ovp/
%{_texmf_main}/fonts/pfm/
%{_texmf_main}/fonts/map/vtex/
%dir %{_texmf_main}/fonts/pk
%dir %{_texmf_main}/fonts/sfd
%{_texmf_main}/fonts/source/
%{_texmf_main}/fonts/tfm/
%{_texmf_main}/fonts/type1/
%{_texmf_main}/fonts/truetype/
%dir %{_texmf_main}/fonts/type3
%dir %{_texmf_main}/fonts/type42
%{_texmf_main}/fonts/vf/
%{_texmf_main}/tex/generic/babel/frenchb.cfg
%{_texmf_main}/tex/generic/babel/hyphen.cfg
%{_texmf_main}/tex/lambda/base/omarab.cfg
%{_texmf_main}/tex/lambda/base/omlgc.cfg
%{_texmf_main}/fonts/enc/pdftex/
%dir %{_texmf_main}/fonts/map/pdftex
%{_texmf_main}/fonts/map/pdftex/updmap/
%{_texmf_main}/fonts/map/pdftex/vntex/
%dir %{_texmf_main}/fonts/map/dvipdfm
%{_texmf_main}/fonts/map/dvipdfm/dvipdfmx/
%{_texmf_main}/fonts/map/dvipdfm/tetex/
%{_texmf_main}/fonts/map/dvipdfm/updmap/

%files latex
%defattr(-,root,root,-)
%{_bindir}/perltex
%{_texmf_main}/tex/cslatex/
%{_texmf_main}/tex/latex/
%{_texmf_main}/tex/platex/

%files xetex
%defattr(-,root,root,-)
%dir %{_texmf_main}/fonts/misc
%{_texmf_main}/tex/xelatex/
%{_texmf_main}/fonts/misc/xetex/
%{_texmf_main}/scripts/xetex/
%{_texmf_main}/web2c/xetex.pool
%{_texmf_main}/tex/generic/ifxetex/
%{_texmf_main}/tex/generic/xetexconfig/

%files doc
%defattr(-,root,root,-)
%doc %{_texmf_main}/doc/

%changelog
* Tue Jan 12 2010 Jindrich Novy <jnovy@redhat.com> 2007-35
- use tar.gz tarball instead of tar.bz2, it is no more present
  on upstream servers

* Fri Dec 04 2009 Jindrich Novy <jnovy@redhat.com> 2007-34
- fix permissions of /var/lib/texmf/web2c (#512459, #531894)
- add IEEEconf (#495877)
- update achemso (#521459)
- update perltex to 2.0 from CTAN
- obsolete tetex-perltex

* Thu Dec 03 2009 Jindrich Novy <jnovy@redhat.com> 2007-33
- drop tetex-perltex dependency

* Mon Oct 26 2009 Tom "spot" Callaway <tcallawa@redhat.com> 2007-32
- resolve conflict between texlive-texmf (and -doc) and tetex-perltex
- resolve conflict between texlive-texmf and tetex-prosper
- resolve conflict between texlive-texmf and tetex-perltex

* Tue Oct 20 2009 Jindrich Novy <jnovy@redhat.com> 2007-31
- do not conflict with dvipdfm
- update perl requires filter
- update latin.ldf (#469948)
- do not provide any perl dependencies (#516350)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2007-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2007-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 16 2008 Jindrich Novy <jnovy@redhat.com> - 2007-27
- remove binaries from splitindex (#476636)
- add unowned dirs into the filelist (#474027)
- fix patch to brp-compress script (#468179)
- remove F8 related chunks from spec

* Mon Oct 13 2008 Jindrich Novy <jnovy@redhat.com> - 2007-26
- increase limits in texmf.cnf so that PostgreSQL documentation build
  passes (#460982)
- update to texlive-2008 version of envlab

* Fri Aug 29 2008 Jindrich Novy <jnovy@redhat.com> - 2007-25
- get rid of the bogus perl require for -doc subpackage
- obsolete tetex-unicode (#459322)

* Wed Aug 27 2008 Jindrich Novy <jnovy@redhat.com> - 2007-24
- fix rendering of beamer slides (#457836)
- remove ubbold.fd (#458150), thanks to Jason Cross
- fix broken Euro sign (#459332) and Romanian accent (#460266),
  thanks to Vasile Gaburici

* Mon Jun 23 2008 Jindrich Novy <jnovy@redhat.com> - 2007-23
- do not directly depend on restorecon and run it only if
  selinux is enabled

* Thu Jun 19 2008 Jindrich Novy <jnovy@redhat.com> - 2007-22
- rebuild to have higher NVR than F9

* Mon May 05 2008 Jindrich Novy <jnovy@redhat.com> - 2007-21
- fix SELinux contexts everywhere possible, don't allow restorecon
  to fail (#444922)

* Mon Apr 07 2008 Jindrich Novy <jnovy@redhat.com> - 2007-20
- mark dvips config files %%config(noreplace) (#441171)

* Thu Apr 03 2008 Jindrich Novy <jnovy@redhat.com> - 2007-19
- texmf-afm and texmf-dvips requires the main texmf tree
- directory ownership fixes (#440359)

* Tue Apr 01 2008 Jindrich Novy <jnovy@redhat.com> - 2007-18
- run restorecon in fonts subpackage to fix bad SELinux contexts
- require coreutils for post (#437457)

* Mon Mar 10 2008 Jindrich Novy <jnovy@redhat.com> - 2007-17
- add styles from upstream collection-latexextra to have more
  complete LaTeX distribution (#436180)
- move tex-preview dependency to texlive-texmf-latex (#436699)
- remove tex4ht completely from lists
- regenerate ls-Rs

* Mon Mar 03 2008 Jindrich Novy <jnovy@redhat.com> - 2007-16
- update texlive package list to ship complete upstream XeTeX
  TeXLive distribution
- introduce new texlive-texmf-xetex subpackage
- move context bits to its subpackage, add missing styles from
  upstream collection-context

* Sat Mar 01 2008 Jindrich Novy <jnovy@redhat.com> - 2007-15
- require texlive-texmf in texlive-texmf-fonts (#431255)
- add missing post/postun scriptlets for texlive-texmf-latex
- require tex-preview

* Thu Feb 28 2008 Jindrich Novy <jnovy@redhat.com> - 2007-14
- rename texlive-texmf-japanese to texlive-texmf-east-asian
- use better approach in installation of cmap files for dvipdfmx
  (#418091), thanks to Patrice Dumas
- drop useless ghostscript Requires from texlive-texmf-fonts,
  drop xdg-utils Requires from texlive-texmf (#428489)

* Mon Feb 25 2008 Jindrich Novy <jnovy@redhat.com> - 2007-13
- ship config file for dvipdfm (#434165), thanks to Patrice Dumas
- obsolete/provide tetex-lineno (#426929)

* Sun Feb 17 2008 Jindrich Novy <jnovy@redhat.com> - 2007-12
- package bigfoot, erroneously missing from the original
  TeX Live 2007 (#426507)
- remove references to cm-super fonts from map files to make
  dvips work correctly (#431182)
- package ConTeXt separately to texlive-texmf-context to get
  rid of the ruby dependency
- move from bz2 to lzma to save space
- move font stuff out of the dvips subpackage

* Tue Feb 05 2008 Miroslav Lichvar <mlichvar@redhat.com> - 2007-11
- don't require texinfo-tex, tex-preview (#431516)

* Mon Jan 28 2008 Jindrich Novy <jnovy@redhat.com> - 2007-10
- BR: texinfo-tex
- package Japanese separately -> texlive-texmf-japanese
- prevent packaging patch backups
- correct directory/file permissions in less wasteful way to
  increase build speed
- run only brp-compress

* Fri Jan 25 2008 Jindrich Novy <jnovy@redhat.com> - 2007-9
- remove $TEXMFMAIN/tex/texinfo to not to clash with texinfo (#226488)

* Fri Jan 18 2008 Jindrich Novy <jnovy@redhat.com> - 2007-8
- update updmap.cfg so that pdftex map files are consistent
  with the current package set

* Mon Jan 14 2008 Jindrich Novy <jnovy@redhat.com> - 2007-7
- remove Requires: htmlview (#428506)
- texlive-doc -> texlive-texmf-doc

* Fri Jan 04 2008 Jindrich Novy <jnovy@redhat.com> - 2007-6
- require tex-preview (#425805)

* Wed Jan 02 2008 Jindrich Novy <jnovy@redhat.com> - 2007-5
- remove preview, it is to be packaged separately (#425805)
- add japanese ptex fmtutil configuration, thanks to Patrice Dumas
- update texlive-texmf-fonts package description to reflect
  texlive and texlive-fonts merge (related: #426388)

* Mon Dec 17 2007 Jindrich Novy <jnovy@redhat.com> - 2007-4
- fix cmap path sed substitution

* Mon Dec 10 2007 Jindrich Novy <jnovy@redhat.com> - 2007-3
- readd symlinks to gs maps (#418091)

* Thu Dec 06 2007 Jindrich Novy <jnovy@redhat.com> - 2007-2
- don't conflict with tetex-doc (#413141)
- remove tex4ht from texlive, it's packaged separately (#411501)

* Sun Dec 02 2007 Jindrich Novy <jnovy@redhat.com> - 2007-1
- drop Requires: texlive, since it's not yet built and
  texlive buildrequires texlive-texmf

* Fri Nov 30 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.15
- add .gz suffix to info pages so that they gets successfully
  removed in preun phase

* Thu Nov 29 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.14
- replace htmlview by xdg-open

* Wed Sep 12 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.13
- move configuration files to the main texlive package
- remove useless common subpackage and move its content to main package
- increase default texmf.cnf limits so that xmlto works
- don't call install-info in scriptlets if it doesn't exist
- fix some multiple file ownerships
- update ptex-texmf to 2.5
- use xdg-utils and htmlview in tkdefaults

* Thu Sep 06 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.12
- update comments related to sources

* Tue Aug 27 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.11
- XDvi config file is owned only by one subpackage (thanks to S.Umar)
- declare config files as config(noreplace)
- BR ghostscript
- ship separate ls-R when japanese is enabled

* Wed Aug 22 2007 MATSUURA Takanori <t.matsuu at gmail.com> - 2007-0.10.2
- add Japanese pTeX
- move Polish platex and pdfplatex are moved to platex-pl and
  pdfplatex respectively.
- add ghostscript dependency and symbolic links to the cmap
  files. required for dvipdfmx

* Sat Aug 18 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.10
- add bin-dvipsk, bin-bibtex, bin-amstex, bin-cyrillic, bin-cslatex,
  bin-cweb, bin-dvipdfmx, bin-dvicopy, bin-pstools, bin-texware,
  bin-thumbpdf, bin-web, bin-ttfutils (these contain man pages and
  config files for packaged binaries)
- legal cleanup: remove literat, latex-tipps-und-tricks, fancybox,
  URW fonts with bad licenses and pcatcode from amscls

* Tue Aug 14 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.9
- obsolete tetex-eurofont, it's a part of TeXLive
- properly obsolete teTeX
- update license tag (some styles/fonts need yet to be removed,
  licenses discussed upstream)
- sort the zip list

* Tue Aug 07 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.8
- add bin-tex, bin-xetex, bin-omega, bin-aleph, bin-metafont
- remove sources lists and tpms from the texmf tarball
- install texmf tree in a less hackish way, update texmf macro definitions
- update updmap default configuration, move updmap.cfg to sysconfdir

* Tue Jul 24 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.7
- add tetex-doc obsoletes/provides to fix upgrading from tetex

* Mon Jul 16 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.6
- remove obsolete make-texlive-texmf.sh
- remove external cstex

* Wed Jul 04 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.5
- generate new complete style list based on styles in teTeX
  exclusively, regardless the upstream scheme-tetex
  (srpm size reduced from 280M -> 180M for texmf tree)
- add new hyphenations that weren't present, add latex-fonts,
  latexconfig, etc. to regenerate all fmts successfully

* Tue Jun 30 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.4
- reintroduce the texlive-errata scheme
- remove old texjive lists and generate the texmf archive lists
  from scheme-tetex.tpm automatically
  (collection-xetex was added manually to scheme-tetex.tpm because
  the texmf tree is incomplete -> fmtutil --all complains)
- fix all filelists to reflect the change above
- fix empty document creation

* Mon Jun 04 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.3
- remove obsolete make-texlive-texmf.sh

* Sat Jun 02 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.2
- update to official TeXLive release
- don't use dates in upstream tarball names
- remove texlive-errata dependencies

* Mon Feb 12 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.1.20070212rc
- update to TeXLive 2007 release candidate as of 12th Feb
- don't package cslatex in separate tarballs
- fix backups for patches 0, 7
- unzip files quietly
- package cnf files in texmf/web2c correctly
- package new files for conTeXt
- forwardport TeXLive-2005 patches
- rpmlint fixes

* Tue May 30 2006 Michael A. Peters <mpeters@mac.com> - 2005-0.10
- couple more minor tweaks to file ownership.

* Tue May 30 2006 Michael A. Peters <mpeters@mac.com> - 2005-0.9
- some cleanup work on directory ownership
- added missing dstroke package
- added texmf tree for vendor bolt-on packages
-
- commented out perl script fix noted in 2005-0.5 changelog
-  until it can be investigated further (and fixed with patch instead)

* Mon May 29 2006 Michael A. Peters <mpeters@mac.com> - 2005-0.8
- Initial mock build attempt

* Sun May 28 2006 Michael A. Peters <mpeters@mac.com> - 2005-0.6
- Attempting to comply with FHS guidelines.
-  install a rpm macro file so that texjive binary package always uses
-  the same directories for texmf, texmf-config, texmf-var
- Filter out requires for perl(only) and perl(path_tre)

* Sun May 28 2006 Michael A. Peters <mpeters@mac.com> - 2005-0.5
- Fixed perl scripts in TEXMF/scripts that thought it would be cute
- to not use a proper shell bang
-
- Install an rpm macro file for building the binary package

* Sun May 28 2006 Michael A. Peters <mpeters@mac.com> - 2005-0.4
- install utopia, use updates cstex

* Sat May 27 2006 Michael A. Peters <mpeters@mac.com> - 2005-0.3
- fonts package should own the web2c/*.cnf files
- web2c/*.pool files owned by binary package

* Sat May 27 2006 Michael A. Peters <mpeters@mac.com> - 2005-0.2
- some rpmlint cleaning

* Sat May 27 2006 Michael A. Peters <mpeters@mac.com> - 2005-0.1
- Initial packaging
