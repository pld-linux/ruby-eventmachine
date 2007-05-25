Summary:	Ruby event-processing library
Summary(pl.UTF-8):	Biblioteka przetwarzania zdarzeń dla języka Ruby
Name:		ruby-eventmachine
Version:	0.7.0
Release:	1
License:	GPL v2
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/14933/eventmachine-%{version}.gem
# Source0-md5:	b22a7d79ba3beb6c38d1b44ddc39560f
URL:		http://rubyforge.org/projects/eventmachine/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	ruby-modules
BuildRequires:	setup.rb
%{?ruby_mod_ver_requires_eq}
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
%setup -q -c -T
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-

%build
cp %{_datadir}/setup.rb .
touch ext/MANIFEST
ruby setup.rb config --rbdir=%{ruby_rubylibdir} --sodir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README RELEASE_NOTES TODO
#%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/*.rb
%{ruby_rubylibdir}/evma
%{ruby_rubylibdir}/protocols
%{ruby_rubylibdir}/em
%attr(755,root,root) %{ruby_archdir}/*.so
