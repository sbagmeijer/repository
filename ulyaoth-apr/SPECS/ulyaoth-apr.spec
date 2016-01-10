%define debug_package %{nil}
%define aprver 1

# end of distribution specific definitions

Summary:    Apache Portable Runtime (APR)
Name:       ulyaoth-apr
Version:    1.5.2
Release:    1%{?dist}
BuildArch: x86_64
License:    Apache License version 2
Group:      System Environment/Libraries
URL:        https://apr.apache.org/
Vendor:     Elasticsearch BV
Packager:   Sjir Bagmeijer <sbagmeijer@ulyaoth.net>
Source0:    http://apache.mirrors.spacedump.net//apr/apr-1.5.2.tar.gz
BuildRoot:  %{_tmppath}/apr-%{version}-%{release}-root-%(%{__id_u} -n)

Provides: apr
Provides: ulyaoth-apr

%description
The mission of the Apache Portable Runtime (APR) project is to create and maintain software libraries that provide a predictable and consistent interface to underlying platform-specific implementations. The primary goal is to provide an API to which software developers may code and be assured of predictable if not identical behaviour regardless of the platform on which their software is built, relieving them of the need to code special-case conditions to work around or take advantage of platform-specific deficiencies or features.

%package devel
Group: Development/Libraries
Summary: APR library development kit
Requires: ulyaoth-apr = %{version}-%{release}, pkgconfig

%description devel
This package provides the support files which can be used to build applications using the APR library.  The mission of the Apache Portable Runtime (APR) is to provide a free library of C data structures and routines.

%prep
%setup -q -n apr-%{version}

%build
./buildconf

%configure \
        --includedir=%{_includedir}/apr-%{aprver} \
        --with-installbuilddir=%{_libdir}/apr-%{aprver}/build \
        --with-devrandom=/dev/urandom
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%pre

%files

%post
cat <<BANNER
----------------------------------------------------------------------

Thanks for using ulyaoth-apr!

Please find the official documentation for apr here:
* https://apr.apache.org/

For any additional help please visit my forum at:
* https://www.ulyaoth.net

----------------------------------------------------------------------
BANNER
fi

%preun

%postun

%changelog
* Sun Jan 10 2016 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 1.5.2-1
- Initial release with apr 1.5.2.
- Based on Fedora 23 spec file.