Summary:	Simple DVB-T/C tuner scan tool
Summary(pl.UTF-8):	Niewielkie narzędzie do strojenia tunerów DVB-T/C
Name:		w_scan
Version:	20141122
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://wirbel.htpc-forum.de/w_scan/%{name}-%{version}.tar.bz2
# Source0-md5:	da0f190bee696a02bf030fc01c0706e8
URL:		http://wirbel.htpc-forum.de/w_scan/index2.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small channel scan tool which generates DVB-T and DVB-C channels.conf
files. It's based on old "scan" from linuxtv-dvb-apps version 1.1.0,
with some differences:
- no initial tuning data needed,
- it works *only* for cable and terrestrial DVB/ATSC,
- it detects automatically which DVB/ATSC card to use.

%description -l pl.UTF-8
Małe narzędzie do wyszukiwania kanałów i generujące plik channels.conf
dla telewizji cyfrowej DVB-T oraz DVB-C. Program jest oparty na
narzędziu "scan" z pakietu linuxtv-dvb-apps w wersji 1.1.0, z pewnymi
różnicami:
- nie są potrzebne wartości inicjujące strojenie,
- działa *tylko* dla kablowej i naziemnej telewizji DVB/ATSC,
- automatycznie wykrywa, które urządzenie DVB/ATSC użyć.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/README* doc/rotor.conf
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
