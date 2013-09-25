#%bcond_with internet
%bcond_without bootstrap
%global packname  GenomicRanges
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.12.5
Release:          1
Summary:          Representation and manipulation of genomic intervals
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/GenomicRanges_1.12.5.tar.gz
Requires:         R-methods R-IRanges 
%if %{with bootstrap}
Requires:         R-RUnit
%else
Requires:         R-RUnit R-BSgenome R-GenomicFeatures R-Rsamtools
Requires:         R-EatonEtAlChIPseq R-leeBamViews R-edgeR R-DESeq
Requires:         R-rtracklayer R-org.Sc.sgd.db
Requires:         R-BSgenome.Scerevisiae.UCSC.sacCer2 R-DEXSeq R-pasilla 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods
BuildRequires:    R-IRanges R-methods
BuildRequires:    R-BiocGenerics
%if %{with bootstrap}
BuildRequires:    R-RUnit
%else
BuildRequires:    R-RUnit R-BSgenome R-GenomicFeatures R-Rsamtools
BuildRequires:    R-EatonEtAlChIPseq R-leeBamViews R-edgeR R-DESeq
BuildRequires:    R-rtracklayer R-org.Sc.sgd.db
BuildRequires:    R-BSgenome.Scerevisiae.UCSC.sacCer2 R-DEXSeq R-pasilla 
%endif

%description
The ability to efficiently store genomic annotations and alignments is
playing a central role when it comes to analyze high-throughput sequencing
data (a.k.a. NGS data). The package defines general purpose containers for
storing genomic intervals as well as more specialized containers for
storing alignments against a reference genome.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
    %if %{with internet}
%check
%{_bindir}/R CMD check %{packname}
    %endif
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/unitTests


%changelog
* Wed Feb 22 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6.7-2
+ Revision: 778848
- Rebuild with proper dependencies

* Fri Feb 17 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6.7-1
+ Revision: 775765
- Import R-GenomicRanges
- Import R-GenomicRanges



