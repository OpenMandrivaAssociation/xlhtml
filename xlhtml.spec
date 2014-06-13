Name:         xlhtml
Version:      0.5
Release:      18
License:      GPL
Group:        Text tools
Requires:     xlhtml-cole
Summary:      Excel 95 and later file converter
URL:          http://chicago.sourceforge.net/xlhtml/
Source:       %{name}-%{version}.tar.bz2
Source100:	%{name}.rpmlintrc
Patch:        %{name}-%{version}.diff
Patch1:       xlhtml-automake-1.13.patch
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
%patch1 -p1 -b .am13~

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




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5-12mdv2011.0
+ Revision: 661761
- multiarch fixes

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5-11mdv2011.0
+ Revision: 608217
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5-10mdv2010.1
+ Revision: 524449
- rebuilt for 2010.1

* Mon Apr 13 2009 Funda Wang <fwang@mandriva.org> 0.5-9mdv2009.1
+ Revision: 366688
- rediff 0.5 patch

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.5-9mdv2009.0
+ Revision: 226050
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.5-8mdv2008.1
+ Revision: 179499
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Aug 25 2007 GaÃ«tan Lehmann <glehmann@mandriva.org> 0.5-7mdv2008.0
+ Revision: 71336
- rebuild


* Wed Aug 09 2006 glehmann
+ 08/09/06 21:24:14 (55177)
rebuild

* Wed Aug 09 2006 glehmann
+ 08/09/06 21:23:08 (55176)
Import xlhtml

* Fri Sep 16 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.5-5mdk
- rebuild

* Wed Jul 06 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.5-4mdk
- really fix url :-/

* Wed Jul 06 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.5-3mdk
- fix url (bug #16708)
- use mkrel

* Sat Apr 16 2005 Giuseppe Ghibò <ghibo@mandriva.com> 0.5-2mdk
- %%multiarch.

* Tue Jan 18 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.5-1mdk
- initial contrib

* Sun Jan 11 2004 - adrian@suse.de
- add %%defattr and %%run_ldconfig

