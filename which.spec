#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : which
Version  : 2.20
Release  : 6
URL      : http://pkgs.fedoraproject.org/repo/pkgs/which/which-2.20.tar.gz/95be0501a466e515422cde4af46b2744/which-2.20.tar.gz
Source0  : http://pkgs.fedoraproject.org/repo/pkgs/which/which-2.20.tar.gz/95be0501a466e515422cde4af46b2744/which-2.20.tar.gz
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
%setup -q -n which-2.20

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make V=1 %{?_smp_mflags} check

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
