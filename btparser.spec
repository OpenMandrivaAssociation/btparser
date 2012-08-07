%define major 2
%define libname %mklibname btparser %{major}

Name:		btparser
Version:	0.18
Release:	1
Summary:	Parser and analyzer for backtraces produced by GDB
Group:		Development/Other
License:	GPLv2+
URL:		http://fedorahosted.org/btparser
Source0:	https://fedorahosted.org/released/btparser/%{name}-%{version}.tar.xz
Patch0:		btparser-0.18-automake1.12.patch
BuildRequires:	python-devel
BuildRequires:	pkgconfig(glib-2.0)
Conflicts:	%{libname} < 0.18

%description
Btparser is a backtrace parser and analyzer, which works with
backtraces produced by the GNU Project Debugger. It can parse a text
file with a backtrace to a tree of C structures, allowing to analyze
the threads and frames of the backtrace and work with them.

Btparser also contains some backtrace manipulation and extraction
routines:
- it can find a frame in the crash-time backtrace where the program
  most likely crashed (a chance is that the function described in that
  frame is buggy)
- it can produce a duplication hash of the backtrace, which helps to
  discover that two crash-time backtraces are duplicates, triggered by
  the same flaw of the code
- it can "rate" the backtrace quality, which depends on the number of
  frames with and without the function name known (missing function
  name is caused by missing debugging symbols)

%files
%doc README NEWS COPYING TODO ChangeLog
%{_bindir}/btparser
%{_mandir}/man1/%{name}.1.*
%{py_platsitedir}/%{name}/*

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	Libraries for reporting crashes to different targets
Group:		System/Libraries

%description -n %{libname}
Btparser is a backtrace parser and analyzer, which works with
backtraces produced by the GNU Project Debugger. It can parse a text
file with a backtrace to a tree of C structures, allowing to analyze
the threads and frames of the backtrace and work with them.

Btparser also contains some backtrace manipulation and extraction
routines:
- it can find a frame in the crash-time backtrace where the program
  most likely crashed (a chance is that the function described in that
  frame is buggy)
- it can produce a duplication hash of the backtrace, which helps to
  discover that two crash-time backtraces are duplicates, triggered by
  the same flaw of the code
- it can "rate" the backtrace quality, which depends on the number of
  frames with and without the function name known (missing function
  name is caused by missing debugging symbols)

%files -n %{libname}
%{_libdir}/libbtparser.so.%{major}*

#--------------------------------------------------------------------

%define devname %mklibname %{name} -d

%package -n %{devname}
Summary:	Development libraries for %{name}
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development libraries and headers for %{name}.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

#--------------------------------------------------------------------
%prep
%setup -q
%patch0 -p1
autoreconf -fi

%build
%configure --disable-static
%make

%install
%makeinstall_std

%check
make check


%changelog
* Mon Mar 12 2012 Oden Eriksson <oeriksson@mandriva.com> 0.16-2
+ Revision: 784344
- rebuild (so that it ends up in main, hopefully)

* Wed Mar 07 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.16-1
+ Revision: 782778
- BR: python-devel
- imported package btparser

