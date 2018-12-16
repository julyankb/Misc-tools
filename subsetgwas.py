import gzip
# =============== USER INPUT ===============
# SNPs to be extracted from input file
rsid_list = ['rs123456789',
	'rs123456788',
        'rs123456787',
        'rs123456786',
        'rs123456785',
        'rs123456784',
        'rs123456783',
        'rs123456782',
        'rs123456781',
        'rs123456780']

# Path to GWAS summary statistics
filepath = '/Path/to/Phenotype-Gwas-SumStats.txt.gz'

# Reminder: python is zero-based indexing.
rsid_col = 1

# Delimiter in GWAS sumstats file
delimiter = '\t'
# ==========================================
snp_dict = {}
for snp in rsid_list:
        snp_dict[snp] = None

if filepath.split('.')[-1] == 'gz':
    with gzip.open(filepath, 'r') as infile:
        # Print header
        print(next(infile).rstrip())
        for line in infile:
            # No need to waste time splitting beyond column of interest
	    # Do .rstrip() in case rsid is last column
	    data = line.rstrip().split(delimiter, rsid_col+1)
            if data[rsid_col] in snp_dict:
                print(line.rstrip())
else:
    with open(filepath, 'r') as infile:
        print(next(infile).rstrip())
        for line in infile:
            data = line.rstrip().split(delimiter, rsid_col+1)
            if data[rsid_col] in snp_dict:
                print(line.rstrip())
