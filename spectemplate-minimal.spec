Name:           
Version:        
Release:        0.fdr.1
Epoch:          0
Summary:        

Group:          
License:        
URL:            
Source0:        
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  
Requires:       

%description

# -----------------------------------------------------------------------------

%prep
%setup -q

# -----------------------------------------------------------------------------

%build
%configure
make %{?_smp_mflags}

# -----------------------------------------------------------------------------

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

# -----------------------------------------------------------------------------

%clean
rm -rf $RPM_BUILD_ROOT

# -----------------------------------------------------------------------------

%files
%defattr(-,root,root,-)
%doc


# -----------------------------------------------------------------------------

%changelog