#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-micrometer
Version  : 1.1.3
Release  : 1
URL      : https://github.com/micrometer-metrics/micrometer/archive/v1.1.3.tar.gz
Source0  : https://github.com/micrometer-metrics/micrometer/archive/v1.1.3.tar.gz
Source1  : https://repo1.maven.org/maven2/io/micrometer/micrometer-core/1.1.3/micrometer-core-1.1.3.jar
Source2  : https://repo1.maven.org/maven2/io/micrometer/micrometer-core/1.1.3/micrometer-core-1.1.3.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-micrometer-data = %{version}-%{release}
Requires: mvn-micrometer-license = %{version}-%{release}

%description
# Micrometer Application Metrics
[![Build Status](https://circleci.com/gh/micrometer-metrics/micrometer.svg?style=svg)](https://circleci.com/gh/micrometer-metrics/micrometer)
[![Apache 2.0](https://img.shields.io/github/license/micrometer-metrics/micrometer.svg)](http://www.apache.org/licenses/LICENSE-2.0)

%package data
Summary: data components for the mvn-micrometer package.
Group: Data

%description data
data components for the mvn-micrometer package.


%package license
Summary: license components for the mvn-micrometer package.
Group: Default

%description license
license components for the mvn-micrometer package.


%prep
%setup -q -n micrometer-1.1.3

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-micrometer
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-micrometer/LICENSE
cp gradle/licenseHeader.txt %{buildroot}/usr/share/package-licenses/mvn-micrometer/gradle_licenseHeader.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/micrometer/micrometer-core/1.1.3
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/io/micrometer/micrometer-core/1.1.3/micrometer-core-1.1.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/micrometer/micrometer-core/1.1.3
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/io/micrometer/micrometer-core/1.1.3/micrometer-core-1.1.3.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/io/micrometer/micrometer-core/1.1.3/micrometer-core-1.1.3.jar
/usr/share/java/.m2/repository/io/micrometer/micrometer-core/1.1.3/micrometer-core-1.1.3.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-micrometer/LICENSE
/usr/share/package-licenses/mvn-micrometer/gradle_licenseHeader.txt
