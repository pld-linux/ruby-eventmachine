#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	eventmachine
Summary:	Ruby event-processing library
Summary(pl.UTF-8):	Biblioteka przetwarzania zdarzeń dla języka Ruby
Name:		ruby-%{pkgname}
Version:	1.0.3
Release:	1
License:	GPL v2
Group:		Development/Libraries
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	579e4829c279995da1af5ac87713e1d0
URL:		http://rubyeventmachine.com/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	ruby-devel
%if %{with tests}
BuildRequires:	ruby-bluecloth
BuildRequires:	ruby-rake-compiler < 0.9
BuildRequires:	ruby-rake-compiler >= 0.8.3
BuildRequires:	ruby-yard >= 0.8.5.2
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby/EventMachine is a fast, simple event-processing library for Ruby
programs. It lets you write network clients and servers without
handling sockets - all you do is send and receive data.
Single-threaded socket engine - scalable and FAST!

%description -l pl.UTF-8
Ruby/EventMachine to szybka, prosta biblioteka przetwarzania zdarzeń
dla programów w języku Ruby. Pozwala pisać klientów i serwery sieciowe
bez obsługi gniazd sieciowych - wystarczy wysyłać i odbierać dane.
Jednowątkowy silnik gniazd - skalowalny i szybki.

%prep
%setup -q -n %{pkgname}-%{version}

%build
cd ext
%{__ruby} extconf.rb
%{__make} \
	CC="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_vendorarchdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
install -p ext/rubyeventmachine.so $RPM_BUILD_ROOT%{ruby_vendorarchdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md LICENSE
%{ruby_vendorlibdir}/em
%{ruby_vendorlibdir}/eventmachine.rb
%{ruby_vendorlibdir}/jeventmachine.rb
%attr(755,root,root) %{ruby_vendorarchdir}/rubyeventmachine.so
