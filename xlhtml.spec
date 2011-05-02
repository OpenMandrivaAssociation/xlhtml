Name:         xlhtml
Version:      0.5
Release:      %mkrel 12
License:      GPL
Group:        Text tools
Requires:     xlhtml-cole
Summary:      Excel 95 and later file converter
URL:          http://chicago.sourceforge.net/xlhtml/
Source:       %{name}-%{version}.tar.bz2
Patch:        %{name}-%{version}.diff
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Buildrequires: automake

%description
xlHtml is an Excel 95 and later file converter. Its html output can be
used as a Netscape Plug-in to let you view xls e-mail attachments. It
can also extract regions of a spreadsheet and convert the spreadsheet
to pure text rather than html.


%package -n xlhtml-cole
Summary:      Free C OLE library
Group:        Development/C++

%description -n xlhtml-cole
Using cole, you can access Microsoft "Structured Storage" files. The
most popular Microsoft programs generate "Structured Storage" files,
including the Microsoft suite for offices. StarDivision's suite
(StarOffice) generates "Structured Storage" files, too. FlashPix file
format is "Structured Storage", too.


%prep
%setup -q
%patch -p0

mv ppthtml/README README-ppthtml

%build
autoreconf -fi
%configure2_5x
%make
%make -C cole/utils

%install
rm -fr %buildroot
%makeinstall_std
# xlhtml-cole
install -m 755 cole/cole-config $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/cole
install cole/cole.h  $RPM_BUILD_ROOT/%{_includedir}/cole
install cole/utils/cole_extract $RPM_BUILD_ROOT/%{_bindir}
install cole/utils/cole_isfs $RPM_BUILD_ROOT/%{_bindir}
install cole/utils/cole_isfs_fast $RPM_BUILD_ROOT/%{_bindir}
install cole/utils/cole_tree $RPM_BUILD_ROOT/%{_bindir}

%multiarch_binaries %{buildroot}%{_bindir}/cole-config

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(-,root,root)
%doc xlhtml/TODO xlhtml/README README-ppthtml
#%doc xlhtml/contrib/*.html
#%doc xlhtml/contrib/*.txt
%{_bindir}/nsopen
%{_bindir}/nspptview
%{_bindir}/nsxlview
%{_bindir}/ppthtml
%{_bindir}/xlhtml
%{_mandir}/*/*

%if %mdkversion < 200900
%post -n xlhtml-cole -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n xlhtml-cole -p /sbin/ldconfig
%endif

%files -n xlhtml-cole
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL ChangeLog NEWS cole/TODO README
%{_bindir}/cole-config
%{multiarch_bindir}/cole-config
%{_bindir}/cole_extract
%{_bindir}/cole_isfs
%{_bindir}/cole_isfs_fast
%{_bindir}/cole_tree
%{_includedir}/cole
%{_libdir}/libcole.*
#/usr/share/aclocal/cole.m4


