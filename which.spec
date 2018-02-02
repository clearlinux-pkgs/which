#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : which
Version  : 2.21
Release  : 12
URL      : http://pkgs.fedoraproject.org/repo/pkgs/which/which-2.21.tar.gz/097ff1a324ae02e0a3b0369f07a7544a/which-2.21.tar.gz
Source0  : http://pkgs.fedoraproject.org/repo/pkgs/which/which-2.21.tar.gz/097ff1a324ae02e0a3b0369f07a7544a/which-2.21.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: which-bin
Requires: which-doc
BuildRequires : binutils-dev

%description
Install
=======
You will need an ANSI C compiler (like gcc) to compile this package.

%package bin
Summary: bin components for the which package.
Group: Binaries

%description bin
bin components for the which package.


%package doc
Summary: doc components for the which package.
Group: Documentation

%description doc
doc components for the which package.


%prep
%setup -q -n which-2.21

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/which

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
