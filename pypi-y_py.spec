#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v2
# autospec commit: f032afc
#
Name     : pypi-y_py
Version  : 0.6.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/76/af/589ff550212e832e6079553069ef3d7bd3e69ec0cf65993f4a16a2bb1ab9/y_py-0.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/76/af/589ff550212e832e6079553069ef3d7bd3e69ec0cf65993f4a16a2bb1ab9/y_py-0.6.0.tar.gz
Source1  : http://localhost/cgit/vendor/pypi-y_py/snapshot/pypi-y_py-2023-03-24-20-49-44.tar.xz
Summary  : Python bindings for the Y-CRDT built from yrs (Rust)
Group    : Development/Tools
License  : Apache-2.0 MIT Unicode-DFS-2016
Requires: pypi-y_py-license = %{version}-%{release}
Requires: pypi-y_py-python = %{version}-%{release}
Requires: pypi-y_py-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(glfw)
BuildRequires : pypi(maturin)
BuildRequires : pypi(numpy)
BuildRequires : pypi(websockets)
BuildRequires : pypi-maturin
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![PyPI version](https://badge.fury.io/py/y-py.svg)](https://badge.fury.io/py/y-py)

%package license
Summary: license components for the pypi-y_py package.
Group: Default

%description license
license components for the pypi-y_py package.


%package python
Summary: python components for the pypi-y_py package.
Group: Default
Requires: pypi-y_py-python3 = %{version}-%{release}

%description python
python components for the pypi-y_py package.


%package python3
Summary: python3 components for the pypi-y_py package.
Group: Default
Requires: python3-core
Provides: pypi(y_py)
Requires: pypi(glfw)
Requires: pypi(numpy)
Requires: pypi(websockets)

%description python3
python3 components for the pypi-y_py package.


%prep
%setup -q -n y_py-0.6.0
cd %{_builddir}
tar xf %{_sourcedir}/pypi-y_py-2023-03-24-20-49-44.tar.xz
cd %{_builddir}/y_py-0.6.0
mkdir -p ./vendor
cp -r %{_builddir}/pypi-y_py-2023-03-24-20-49-44/* %{_builddir}/y_py-0.6.0/./vendor
mkdir -p .cargo
echo '[source.crates-io]' >> .cargo/config.toml
echo 'replace-with = "vendored-sources"' >> .cargo/config.toml
echo '[source.vendored-sources]' >> .cargo/config.toml
echo 'directory = "vendor"' >> .cargo/config.toml
pushd ..
cp -a y_py-0.6.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697507701
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-y_py
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/autocfg/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/autocfg/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/e6d32072ef5f584a805b429ecbd4eec428316dde || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/bitflags/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/bitflags/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/9f3c36d2b7d381d9cf382a00166f3fbd06783636 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/bumpalo/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/bumpalo/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/0a1e89ac22450cb0311baa2613bc21b7131b321f || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/cfg-if/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/cfg-if/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/getrandom/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/getrandom/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/d74ad13f1402c35008f22bc588a6b8199ed164d3 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/indoc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/indoc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/js-sys/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/js-sys/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/libc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/libc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/36d69bcb88153a640740000efe933b009420ce7e || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/lock_api/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/lock_api/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/log/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/aca374a3362a76702c50bd4e7d590a57f8834fc7 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/log/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/f9cc84dfc567fdc0979fddc3e6257191d8ebc9d8 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/once_cell/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/once_cell/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/parking_lot/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/parking_lot/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/parking_lot_core/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/parking_lot_core/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/ppv-lite86/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/088830dcb78eba1a2052df69bd5cba5445e8f2d7 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/ppv-lite86/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/e1c86f32641f01a5b85d6e9b20138e8470b883fc || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/proc-macro2/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/proc-macro2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/pyo3-build-config/LICENSE %{buildroot}/usr/share/package-licenses/pypi-y_py/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/pyo3-macros-backend/LICENSE %{buildroot}/usr/share/package-licenses/pypi-y_py/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/pyo3-macros/LICENSE %{buildroot}/usr/share/package-licenses/pypi-y_py/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/pyo3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-y_py/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/quote/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/quote/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/rand/COPYRIGHT %{buildroot}/usr/share/package-licenses/pypi-y_py/f14afa20edce530124d39cd56312c7781c19b267 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/rand/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/rand/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/d74ad13f1402c35008f22bc588a6b8199ed164d3 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/rand_chacha/COPYRIGHT %{buildroot}/usr/share/package-licenses/pypi-y_py/f14afa20edce530124d39cd56312c7781c19b267 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/rand_chacha/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/rand_chacha/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/d74ad13f1402c35008f22bc588a6b8199ed164d3 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/rand_core/COPYRIGHT %{buildroot}/usr/share/package-licenses/pypi-y_py/f14afa20edce530124d39cd56312c7781c19b267 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/rand_core/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/rand_core/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/d74ad13f1402c35008f22bc588a6b8199ed164d3 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/rand_hc/COPYRIGHT %{buildroot}/usr/share/package-licenses/pypi-y_py/f14afa20edce530124d39cd56312c7781c19b267 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/rand_hc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/rand_hc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/2e87f5a7544123079270e8178a5ab0bbd19d0e51 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/redox_syscall/LICENSE %{buildroot}/usr/share/package-licenses/pypi-y_py/a00165152c82ea55b9fc254890dc8860c25e3bb6 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/scopeguard/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/scopeguard/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/f498d95a48889a0b1432e420e6754881eff1d593 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/smallvec/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/smallvec/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/c61640f6c218caf86d1b8072e09668a8362dba04 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/syn/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/syn/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/target-lexicon/LICENSE %{buildroot}/usr/share/package-licenses/pypi-y_py/f137043e018f2024e0414a9153ea728c203ae8e5 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/thiserror-impl/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/thiserror-impl/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/thiserror/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/thiserror/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/unicode-ident/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/unicode-ident/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/unicode-ident/LICENSE-UNICODE %{buildroot}/usr/share/package-licenses/pypi-y_py/583a5eebcf6119730bd96922e8a0faecf7faf720 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/unindent/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/unindent/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/wasi/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/wasi/LICENSE-Apache-2.0_WITH_LLVM-exception %{buildroot}/usr/share/package-licenses/pypi-y_py/f137043e018f2024e0414a9153ea728c203ae8e5 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/wasi/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/wasm-bindgen-backend/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/wasm-bindgen-backend/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/wasm-bindgen-macro-support/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/wasm-bindgen-macro-support/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/wasm-bindgen-macro/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/wasm-bindgen-macro/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/wasm-bindgen-shared/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/wasm-bindgen-shared/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/wasm-bindgen/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/wasm-bindgen/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-y_py/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/windows-sys/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-y_py/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/windows-sys/license-mit %{buildroot}/usr/share/package-licenses/pypi-y_py/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/windows-targets/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-y_py/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/windows-targets/license-mit %{buildroot}/usr/share/package-licenses/pypi-y_py/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/windows_aarch64_gnullvm/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-y_py/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/windows_aarch64_gnullvm/license-mit %{buildroot}/usr/share/package-licenses/pypi-y_py/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/windows_aarch64_msvc/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-y_py/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/windows_aarch64_msvc/license-mit %{buildroot}/usr/share/package-licenses/pypi-y_py/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/windows_i686_gnu/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-y_py/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/windows_i686_gnu/license-mit %{buildroot}/usr/share/package-licenses/pypi-y_py/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/windows_i686_msvc/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-y_py/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/windows_i686_msvc/license-mit %{buildroot}/usr/share/package-licenses/pypi-y_py/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/windows_x86_64_gnu/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-y_py/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/windows_x86_64_gnu/license-mit %{buildroot}/usr/share/package-licenses/pypi-y_py/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/windows_x86_64_gnullvm/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-y_py/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/windows_x86_64_gnullvm/license-mit %{buildroot}/usr/share/package-licenses/pypi-y_py/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/windows_x86_64_msvc/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-y_py/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-y_py-2023-03-24-20-49-44/windows_x86_64_msvc/license-mit %{buildroot}/usr/share/package-licenses/pypi-y_py/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/y_py-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-y_py/7c4f76a3018cd180d7f2d84c7c4c20ae953354e4 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-y_py/088830dcb78eba1a2052df69bd5cba5445e8f2d7
/usr/share/package-licenses/pypi-y_py/0a1e89ac22450cb0311baa2613bc21b7131b321f
/usr/share/package-licenses/pypi-y_py/2e87f5a7544123079270e8178a5ab0bbd19d0e51
/usr/share/package-licenses/pypi-y_py/36d69bcb88153a640740000efe933b009420ce7e
/usr/share/package-licenses/pypi-y_py/3b042d3d971924ec0296687efd50dbe08b734976
/usr/share/package-licenses/pypi-y_py/5798832c31663cedc1618d18544d445da0295229
/usr/share/package-licenses/pypi-y_py/583a5eebcf6119730bd96922e8a0faecf7faf720
/usr/share/package-licenses/pypi-y_py/5bb5828e544f63bd76c1b7112981a1ad86ae77f9
/usr/share/package-licenses/pypi-y_py/689ec0681815ecc32bee639c68e7740add7bd301
/usr/share/package-licenses/pypi-y_py/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a
/usr/share/package-licenses/pypi-y_py/7c4f76a3018cd180d7f2d84c7c4c20ae953354e4
/usr/share/package-licenses/pypi-y_py/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7
/usr/share/package-licenses/pypi-y_py/9f3c36d2b7d381d9cf382a00166f3fbd06783636
/usr/share/package-licenses/pypi-y_py/a00165152c82ea55b9fc254890dc8860c25e3bb6
/usr/share/package-licenses/pypi-y_py/a3b3a65335e78bde163f84d599fa899776552994
/usr/share/package-licenses/pypi-y_py/aca374a3362a76702c50bd4e7d590a57f8834fc7
/usr/share/package-licenses/pypi-y_py/c61640f6c218caf86d1b8072e09668a8362dba04
/usr/share/package-licenses/pypi-y_py/ce3a2603094e799f42ce99c40941544dfcc5c4a5
/usr/share/package-licenses/pypi-y_py/d74ad13f1402c35008f22bc588a6b8199ed164d3
/usr/share/package-licenses/pypi-y_py/e1c86f32641f01a5b85d6e9b20138e8470b883fc
/usr/share/package-licenses/pypi-y_py/e6d32072ef5f584a805b429ecbd4eec428316dde
/usr/share/package-licenses/pypi-y_py/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e
/usr/share/package-licenses/pypi-y_py/f137043e018f2024e0414a9153ea728c203ae8e5
/usr/share/package-licenses/pypi-y_py/f14afa20edce530124d39cd56312c7781c19b267
/usr/share/package-licenses/pypi-y_py/f498d95a48889a0b1432e420e6754881eff1d593
/usr/share/package-licenses/pypi-y_py/f9cc84dfc567fdc0979fddc3e6257191d8ebc9d8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
