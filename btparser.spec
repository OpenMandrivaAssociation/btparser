Name:    btparser
Version: 0.16
Release: 1
Summary: Parser and analyzer for backtraces produced by GDB
Group:   Development/Other
License: GPLv2+
URL:     http://fedorahosted.org/btparser
Source0: https://fedorahosted.org/released/btparser/%{name}-%{version}.tar.xz
BuildRequires: python-devel

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

#--------------------------------------------------------------------

%define lib_major 2
%define libname %mklibname btparser %{lib_major}

%package -n %libname
Summary: Libraries for reporting crashes to different targets
Group:   System/Libraries

%description -n %libname
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

%files -n %libname
%{_libdir}/libbtparser.so.%{lib_major}*
%{py_platsitedir}/%{name}/*


#--------------------------------------------------------------------

%define lib_name_devel %mklibname %{name} -d

%package -n %lib_name_devel
Summary: Development libraries for %{name}
Group: Development/Other
Provides: %{name}-devel = %{version}-%{release}
Provides: lib%{name}-devel = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n %lib_name_devel
Development libraries and headers for %{name}.

%files -n %lib_name_devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

#--------------------------------------------------------------------
%prep
%setup -q

autoreconf -fi

%build
%configure --disable-static
%make

%install
%makeinstall_std

# Remove all libtool archives (*.la) from modules directory.
find %{buildroot} -regex ".*\.la$" | xargs rm -f --

%check
make check
