%define debug_package %{nil}

# end of distribution specific definitions

Summary:    The Reliable, High Performance TCP/HTTP Load Balancer
Name:       ulyaoth-haproxy1.6
Version:    1.6.9
Release:    1%{?dist}
BuildArch: x86_64
License:    GPL/LGPL
Group:      System Environment/Libraries
URL:        https://www.haproxy.org/
Vendor:     HAProxy
Packager:   Sjir Bagmeijer <sbagmeijer@ulyaoth.net>
Source0:    http://www.haproxy.org/download/1.6/src/haproxy-%{version}.tar.gz
Source1:    https://raw.githubusercontent.com/ulyaoth/repository/master/ulyaoth-haproxy/SOURCES/haproxy1.6.cfg
Source2:    https://raw.githubusercontent.com/ulyaoth/repository/master/ulyaoth-haproxy/SOURCES/haproxy1.6.init
Source3:    https://raw.githubusercontent.com/ulyaoth/repository/master/ulyaoth-haproxy/SOURCES/haproxy1.6.service
BuildRoot:  %{_tmppath}/haproxy-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: zlib-devel
BuildRequires: ulyaoth-openssl1.0.2

Requires: ulyaoth-openssl1.0.2

Provides: haproxy1.6

%description
HAProxy is a free, very fast and reliable solution offering high availability, load balancing, and proxying for TCP and HTTP-based applications. It is particularly suited for very high traffic web sites and powers quite a number of the world's most visited ones. Over the years it has become the de-facto standard opensource load balancer, is now shipped with most mainstream Linux distributions, and is often deployed by default in cloud platforms. Since it does not advertise itself, we only know it's used when the admins report it :-)

%prep
%setup -q -n haproxy-%{version}

%build

make PREFIX=/usr/local/ulyaoth/haproxy/haproxy1.6 TARGET=linux26 USE_LINUX_TPROXY=1 USE_ZLIB=1 USE_OPENSSL=1 SSL_INC=/usr/local/ulyaoth/ssl/openssl1.0.2/include SSL_LIB=/usr/local/ulyaoth/ssl/openssl1.0.2/lib ADDLIB=-ldl

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/local/ulyaoth/haproxy/haproxy1.6

make PREFIX=/usr/local/ulyaoth/haproxy/haproxy1.6 install

mv $RPM_BUILD_ROOT/usr/local/ulyaoth/haproxy/haproxy1.6/share/man $RPM_BUILD_ROOT/usr/local/ulyaoth/haproxy/haproxy1.6/
rm -rf $RPM_BUILD_ROOT/usr/local/ulyaoth/haproxy/haproxy1.6/share

%{__mkdir} -p $RPM_BUILD_ROOT%{_sysconfdir}/haproxy
%{__install} -m 644 -p %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/haproxy/haproxy1.6.cfg

%if %{use_systemd}
# install systemd-specific files
%{__mkdir} -p $RPM_BUILD_ROOT%{_unitdir}
%{__install} -m644 %SOURCE3 \
    $RPM_BUILD_ROOT%{_unitdir}/haproxy1.6.service
%else
# install SYSV init stuff
%{__mkdir} -p $RPM_BUILD_ROOT%{_initrddir}
%{__install} -m755 %SOURCE3 \
    $RPM_BUILD_ROOT%{_initrddir}/haproxy1.6
%endif

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%pre

%files
%defattr(-,root,root,-)
%dir /usr/local/ulyaoth
%dir /usr/local/ulyaoth/haproxy
%dir /usr/local/ulyaoth/haproxy/haproxy1.6

%dir %{_sysconfdir}/haproxy
%config(noreplace) %{_sysconfdir}/haproxy/haproxy1.6.cfg

%dir /usr/local/ulyaoth/haproxy/haproxy1.6/sbin
/usr/local/ulyaoth/haproxy/haproxy1.6/sbin/haproxy

%dir  /usr/local/ulyaoth/haproxy/haproxy1.6/man
%dir  /usr/local/ulyaoth/haproxy/haproxy1.6/man/man1
/usr/local/ulyaoth/haproxy/haproxy1.6/man/man1/haproxy.1

%dir /usr/local/ulyaoth/haproxy/haproxy1.6/doc
%dir /usr/local/ulyaoth/haproxy/haproxy1.6/doc/haproxy/
/usr/local/ulyaoth/haproxy/haproxy1.6/doc/haproxy/architecture.txt
/usr/local/ulyaoth/haproxy/haproxy1.6/doc/haproxy/close-options.txt
/usr/local/ulyaoth/haproxy/haproxy1.6/doc/haproxy/configuration.txt
/usr/local/ulyaoth/haproxy/haproxy1.6/doc/haproxy/cookie-options.txt
/usr/local/ulyaoth/haproxy/haproxy1.6/doc/haproxy/intro.txt
/usr/local/ulyaoth/haproxy/haproxy1.6/doc/haproxy/linux-syn-cookies.txt
/usr/local/ulyaoth/haproxy/haproxy1.6/doc/haproxy/lua.txt
/usr/local/ulyaoth/haproxy/haproxy1.6/doc/haproxy/management.txt
/usr/local/ulyaoth/haproxy/haproxy1.6/doc/haproxy/network-namespaces.txt
/usr/local/ulyaoth/haproxy/haproxy1.6/doc/haproxy/proxy-protocol.txt

%if %{use_systemd}
%{_unitdir}/haproxy1.6.service
%else
%{_initrddir}/haproxy1.6
%endif

%post
/sbin/ldconfig
cat <<BANNER
----------------------------------------------------------------------

Thank you for using ulyaoth-haproxy1.6!

Please find the official documentation for HAProxy here:
* https://www.haproxy.org/

For any additional help please visit my forum at:
* https://www.ulyaoth.net

----------------------------------------------------------------------
BANNER

%postun -p /sbin/ldconfig

%changelog
* Tue Oct 11 2016 Sjir Bagmeijer <sbagmeijer@ulyaoth.net> 1.6.9-1
- Initial release for HAProxy 1.6.