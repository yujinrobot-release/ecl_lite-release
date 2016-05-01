Name:           ros-indigo-ecl-sigslots-lite
Version:        0.61.4
Release:        1%{?dist}
Summary:        ROS ecl_sigslots_lite package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/ecl_sigslots_lite
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-ecl-config
Requires:       ros-indigo-ecl-errors
Requires:       ros-indigo-ecl-license
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-ecl-config
BuildRequires:  ros-indigo-ecl-errors
BuildRequires:  ros-indigo-ecl-license

%description
This avoids use of dynamic storage (malloc/new) and thread safety (mutexes) to
provide a very simple sigslots implementation that can be used for *very*
embedded development.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun May 01 2016 Daniel Stonier <d.stonier@gmail.com> - 0.61.4-1
- Autogenerated by Bloom

* Sun Jan 10 2016 Daniel Stonier <d.stonier@gmail.com> - 0.61.4-0
- Autogenerated by Bloom

* Wed Jan 06 2016 Daniel Stonier <d.stonier@gmail.com> - 0.61.3-0
- Autogenerated by Bloom

* Tue Nov 24 2015 Daniel Stonier <d.stonier@gmail.com> - 0.61.2-0
- Autogenerated by Bloom

* Sun Jul 26 2015 Daniel Stonier <d.stonier@gmail.com> - 0.61.1-0
- Autogenerated by Bloom

