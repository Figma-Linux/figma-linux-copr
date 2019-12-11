Name:       figma-linux
Version:    0.6.1
Release:    2
Summary:    RPM package for figma-linux
License:    GPL2.0

URL:            https://github.com/Figma-Linux/%{name}
Source0:        https://github.com/Figma-Linux/%{name}/releases/download/v%{version}/%{name}-%{version}.zip
Source1:        https://raw.githubusercontent.com/ChugunovRoman/%{name}/master/resources/%{name}.desktop
Source2:        https://raw.githubusercontent.com/ChugunovRoman/%{name}/master/resources/icons/24x24.png
Source3:        https://raw.githubusercontent.com/ChugunovRoman/%{name}/master/resources/icons/36x36.png
Source4:        https://raw.githubusercontent.com/ChugunovRoman/%{name}/master/resources/icons/48x48.png
Source5:        https://raw.githubusercontent.com/ChugunovRoman/%{name}/master/resources/icons/64x64.png
Source6:        https://raw.githubusercontent.com/ChugunovRoman/%{name}/master/resources/icons/72x72.png
Source7:        https://raw.githubusercontent.com/ChugunovRoman/%{name}/master/resources/icons/96x96.png
Source8:        https://raw.githubusercontent.com/ChugunovRoman/%{name}/master/resources/icons/128x128.png
Source9:        https://raw.githubusercontent.com/ChugunovRoman/%{name}/master/resources/icons/192x192.png
Source10:       https://raw.githubusercontent.com/ChugunovRoman/%{name}/master/resources/icons/256x256.png
Source11:       https://raw.githubusercontent.com/ChugunovRoman/%{name}/master/resources/icons/384x384.png
Source12:       https://raw.githubusercontent.com/ChugunovRoman/%{name}/master/resources/icons/512x512.png

BuildRequires: unzip

%description
RPM package for figma-linux

%install
ls -la "%{SOURCE0}"
install -d $RPM_BUILD_ROOT/opt/%{name}
install -d $RPM_BUILD_ROOT/usr/share/applications/
install -m 755 "%{SOURCE1}" $RPM_BUILD_ROOT/usr/share/applications/%{name}.desktop

for size in 24 36 48 64 72 96 128 192 256 384 512; do
    install -d $RPM_BUILD_ROOT/usr/share/icons/hicolor/${size}x${size}/apps/
    install -m 755 /builddir/build/SOURCES/${size}x${size}.png $RPM_BUILD_ROOT/usr/share/icons/hicolor/${size}x${size}/apps/%{name}.png
done

unzip -q "%{SOURCE0}" -d $RPM_BUILD_ROOT/opt/%{name}

ls -la $RPM_BUILD_ROOT
ls -la $RPM_BUILD_ROOT/opt/%{name}

%post
ln -s /opt/figma-linux/figma-linux /usr/bin/figma-linux

%files
/opt/figma-linux/
/usr/share/applications/figma-linux.desktop
/usr/share/icons/hicolor/24x24/apps/figma-linux.png
/usr/share/icons/hicolor/36x36/apps/figma-linux.png
/usr/share/icons/hicolor/48x48/apps/figma-linux.png
/usr/share/icons/hicolor/64x64/apps/figma-linux.png
/usr/share/icons/hicolor/72x72/apps/figma-linux.png
/usr/share/icons/hicolor/96x96/apps/figma-linux.png
/usr/share/icons/hicolor/128x128/apps/figma-linux.png
/usr/share/icons/hicolor/192x192/apps/figma-linux.png
/usr/share/icons/hicolor/256x256/apps/figma-linux.png
/usr/share/icons/hicolor/384x384/apps/figma-linux.png
/usr/share/icons/hicolor/512x512/apps/figma-linux.png

%changelog
# let's skip this for now
