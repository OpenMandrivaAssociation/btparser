%define major	2
%define libname %mklibname btparser %{major}
%define devname %mklibname %{name} -d
%define _disable_ld_no_undefined 1

Name:		btparser
Version:	0.26
Release:	7
Summary:	Parser and analyzer for backtraces produced by GDB
Group:		Development/Other
License:	GPLv2+
Url:		http://fedorahosted.org/btparser
Source0:	https://fedorahosted.org/released/btparser/%{name}-%{version}.tar.xz
Patch0:		btparser-0.18-automake1.12.patch
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(python2)

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

%package -n %{libname}
Summary:	Libraries for reporting crashes to different targets
Group:		System/Libraries

%description -n %{libname}
Shared library for %{name}.

%package -n %{devname}
Summary:	Development libraries for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development libraries and headers for %{name}.

%prep
%setup -q
%autopatch -p1

%build
export PYTHON=%{_bindir}/python2
export PYTHON_CONFIG=%{_bindir}/python2-config
%configure \
	--disable-static
%make

%install
%makeinstall_std

%check
make check

%files
%doc README NEWS COPYING TODO ChangeLog
%{_bindir}/btparser
%{_mandir}/man1/%{name}.1.*
%{py_platsitedir}/%{name}/*

%files -n %{libname}
%{_libdir}/libbtparser.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*


