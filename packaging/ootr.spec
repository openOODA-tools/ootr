Name:           ootr
Version:        0.1.0
Release:        1%{?dist}
Summary:        Streaming character set translator, squeezer, and complement mapping engine.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ootr
Source0:        ootr-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ootr is a sovereign, capability-bounded BYTE TRANSLATOR written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ootr
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ootr-uninstall

%files
/usr/bin/ootr
/usr/bin/ootr-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
