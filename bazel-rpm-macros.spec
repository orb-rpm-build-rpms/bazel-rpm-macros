# This package ships the RPM macros used to build other packages with Bazel.
# It is deliberately separate from the Bazel compiler package: Fedora may carry
# several parallel-installable Bazel versions (an unversioned default plus
# compat bazelN packages for older, WORKSPACE-based projects), and the macros
# are version-independent policy that a single package must own. This mirrors
# how go-rpm-macros is shipped separately from the golang compiler.

Name:           bazel-rpm-macros
Version:        1
Release:        1%{?dist}
Summary:        RPM macros for building packages with Bazel

License:        MIT
URL:            https://bazel.build/
Source0:        macros.bazel
Source1:        LICENSE

BuildArch:      noarch

# Pulling in the macros pulls in Bazel itself (and, through it, a JDK), so a
# package only needs "BuildRequires: bazel-rpm-macros" to build with %%bazel.
Requires:       bazel

%description
RPM macros that let Fedora packages build with Bazel. The %%bazel macro runs
Bazel offline against a vendored set of external modules, using the host JDK
and Fedora's standard compiler and linker flags, so that builds work inside
Fedora's network-isolated build environment.

%prep
# There is no source tarball to unpack; create an empty build directory and
# drop the license into it so %%license can pick it up.
%autosetup -c -T
cp -p %{SOURCE1} .

%install
install -Dpm 0644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.bazel

%files
%license LICENSE
%{_rpmmacrodir}/macros.bazel

%changelog
* Fri Oct 02 2026 bazel-rpm-macros <noreply@example.com> - 1-1
- Initial package: the %%bazel macro for offline Bazel builds.
