# Author: Matthew Bootsma
# Last edit: 2/01/2019
# this script will take a haps.vcf and print each individual's haplotype call on a line for each locus.
# should also function with a SNPs.vcf but not tested

#set working directory
import os
os.getcwd()
os.chdir("I:\WAE_RAD_Data\Analyses_development\GSI_and_Parentage_scripts")
# open file you are going to write new results to
out_file = open("TEST_vcf2ckmrsim_out.txt", "w")
# open vcf file read all lines into an array, close file
raw_vcf_file = open("TEST_populations.haps.vcf", "r")
raw_vcf_array = raw_vcf_file.readlines()
raw_vcf_file.close()
# for each line in vcf file
for i in raw_vcf_array:
    # this is trying to recognize the header line
    if i.startswith("#CHROM"):

        # hard code column names you wan
        out_file.write(
            "locus" + "\t" + "indv" + "\t" + "gene.copy" + "\t" + "allele" + "\n")
        header_line = i.rstrip().split("\t")
        # grabbing individual names for use in the next loop
        names = header_line[9:(len(header_line)+1)]
        # at this point we should have header line

    # use the if not # to go to the data
    elif "#" not in i:
        # split_ind_line is going to hold our genotype calls e.g., 0/2
        split_ind_line = i.rstrip().split("\t")
        #Store teh locus ID in variable locus_ID
        locus_ID = split_ind_line[0]
        #Store the haplotype alleles in an array, they will be delimited by ","
        haplotypes = split_ind_line[3]+","+split_ind_line[4]
        #immediately break this haplotype allele array into it's components for indexing down the line
        haplotypes = haplotypes.split(",")

        # iterates through individuals for each locus
        z = 0
        #y will be used for calling individual names for each line
        y = 0
        for j in split_ind_line:
            z = z + 1
            #we're only looking at values that hold a genotype call
            if z > 9 and z < (len(split_ind_line)+1):
                #this loop is to make an exception for missing genotypes,
                # which we expect to be "./."
                if j.startswith("."):
                    #first, print the locus name
                    out_file.write(split_ind_line[0] + "\t")
                    #next, print the individual name
                    out_file.write(names[y] + "\t")
                    #next, print a gene.copy ID (hap1 or 2?)
                    out_file.write("hap1" + "\t")
                    #next, prepare and print allele 1
                        #in this case, we expect it to be "./." or a missing call
                    out_file.write("NA" + "\n")
                    #proceed to print the second allele's information on a new line
                    # first, print the locus name
                    out_file.write(split_ind_line[0] + "\t")
                    # next, print the individual name
                    out_file.write(names[y] + "\t")
                    # next, print a gene.copy ID (hap1 or 2?)
                    out_file.write("hap2" + "\t")
                    #last, print the second allele call
                    out_file.write("NA" + "\n")
                    y = y + 1


                else:
                    #first, print the locus name
                    out_file.write(split_ind_line[0] + "\t")
                    #next, print the individual name
                    out_file.write(names[y] + "\t")
                    #next, print a gene.copy ID (hap1 or 2?)
                    out_file.write("hap1" + "\t")
                    #next, prepare and print allele 1
                        #split the genotype cell
                    gen_data = j.split("/")
                        #I'm expecting shit to get funky if i call an index directly using the
                        #   value stored in gen_data so I'm going to explicitly assign these to objects
                    index1 = int(gen_data[0])
                    index2 = int(gen_data[1])
                    out_file.write(haplotypes[index1] + "\n")
                    #proceed to print the second allele's information on a new line
                    # first, print the locus name
                    out_file.write(split_ind_line[0] + "\t")
                    # next, print the individual name
                    out_file.write(names[y] + "\t")
                    # next, print a gene.copy ID (hap1 or 2?)
                    out_file.write("hap2" + "\t")
                    #last, print the second allele call
                    out_file.write(haplotypes[index1] + "\n")
                    y = y + 1

out_file.close()  # script parse vcf file get alleles per individual
