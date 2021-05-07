import os, glob

# The following 8 arrays contain the extracted compile-time 
# configuration options from the xz using the "./configure --help"
optional_features = ["--disable%s" % p for p in ("-option-checking", 
                                                "-assembler",
                                                #"-xz",
                                                "-xzdec",
                                                "-lzmadec",
                                                "-lzmainfo",
                                                "-lzma-links",
                                                "-scripts",
                                                "-doc",
                                                "-silent-rules",
                                                "-dependency-tracking",
                                                "-libtool-lock",
                                                "-nls",
                                                "-rpath",
                                                "-largefile"
                                                )]              
optional_features_2 = ["--enable%s" % p for p in ("-debug",
                                                "-encoders=lzma1",
                                                "-encoders=lzma1,lzma2", # configure: error: LZMA2 requires that LZMA1 is also enabled.
                                                "-encoders=lzma1,delta", # an error !
                                                "-encoders=lzma1,x86",
                                                "-encoders=lzma1,powerpc",
                                                "-encoders=lzma1,ia64",
                                                "-encoders=lzma1,arm",
                                                "-encoders=lzma1,armthumb",
                                                "-encoders=lzma1,sparc",
                                                "-decoders=lzma1",
                                                "-decoders=lzma1,lzma2",
                                                "-decoders=lzma1,delta",
                                                "-decoders=lzma1,x86",
                                                "-decoders=lzma1,powerpc",
                                                "-decoders=lzma1,ia64",
                                                "-decoders=lzma1,arm",
                                                "-decoders=lzma1,armthumb",
                                                "-decoders=lzma1,sparc",
                                                "-match-finders=hc3",
                                                "-match-finders=hc4",
                                                "-match-finders=bt2",
                                                "-match-finders=bt3",
                                                "-match-finders=bt4",
                                                "-checks=crc32",
                                                "-checks=crc32,crc64", # configure: error: For now, the CRC32 check must always be enabled.
                                                "-checks=crc32,sha256", #configure: error: For now, the CRC32 check must always be enabled.
                                                #"-external-sha256", # configure: error: --enable-external-sha256 was specified but no supported external SHA-256 implementation was found
                                                "-small",
                                                "-threads=yes",
                                                "-threads=no",
                                                "-threads=posix",
                                                #"-threads=win95", # error
                                                #"-threads=vista", # error
                                                "-assume-ram=128",
                                                "-symbol-versions",
                                                "-sandbox=auto",
                                                "-sandbox=no",
                                                "-sandbox=capsicum",
                                                "-silent-rules",
                                                "-dependency-tracking",
                                                #"-shared",
                                                "-shared=no",
                                                "-static",
                                                #"-static=no",
                                                "-fast-install",
                                                "-fast-install=no",
                                                "-unaligned-access",
                                                "-unsafe-type-punning",
                                                #"-werror"
                                                ) ]

optional_packages = ["--with%s" % p for p in ("-pic=PIC",
                                            "-pic=non-PIC",
                                            "-aix-soname=aix",
                                            "-aix-soname=svr4",
                                            "-aix-soname=both",
                                            "-gnu-ld",
                                            "-gnu-ld=no",
                                            "-libiconv-prefix",
                                            "-libintl-prefix"
                                            ) ]


optional_packages_2 = ["--without%s" % p for p in ( "-libiconv-prefix",
                                                    "-libintl-prefix"
                                            ) ]



# Adding the single configurations to an array 
def extractDigits(lst):
    res = []
    for el in lst:
        sub = el.split(', ')
        res.append(sub)
    #print(res)
    return(res)
   

# All single configurations                   
single_configurations_01 = extractDigits(optional_features)
single_configurations_02 = extractDigits(optional_features_2)
single_configurations_03 = extractDigits(optional_packages)
single_configurations_04 = extractDigits(optional_packages_2)


# Adding the sample configuration sets (generated by FeatureIDE) to an array
sample_configurations = []

# for variant in glob.glob("measures/products/*.config"):
for variant in glob.glob("measures/products_2-200/*.config"):
    lineList = list()
    with open(variant) as f:
        for line in f:
            lineList = [line.rstrip('\n') for line in open(variant)]
        sample_configurations.append(lineList)

# print(sample_configurations)
print(*single_configurations_01,*single_configurations_02,*single_configurations_03,*single_configurations_04)

# All single and sample configurations, 
# which will be used to measure the changes on
# the binary size and number of gadgets in x264
all_options =  [*sample_configurations]