Summary:	A 2D Dynablaster clone
Summary(pl):	Klon Dynablaster w 2D
Name:		bombic
Version:	0.0.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/bombic/%{name}-%{version}-src.tar.gz
# Source0-md5:	ee0e0d4594baf902bb25ecc0cb62017c
URL:		http://bombic.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bombic is a Dynablaster clone. You must use bombs to break walls, collecting power-ups while avoiding the bomb flames and monsters.

%description -l pl
Bombic jest klonem gry Dynablaster. Musisz u¿ywaæ bomb do niszczenia murów oraz zbieraæ bonusy, które pozwol± ci unikaæ p³omieni i potworów.

%prep
%setup -q -n %{name}-%{version}-src

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
