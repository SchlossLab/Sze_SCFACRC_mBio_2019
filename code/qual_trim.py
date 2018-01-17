#!python

# This is re-written python code to accomplish two tasks
	# Convert SRA to fastq
	# Run quality control over each read per sample

############## Internal parameters used by all functions is program ########################

# Import needed libraries
import os, sys

# Set up working directory
workdir = "data/raw/"

# Set up shortcuts for keys and other download components
# These are changed to match Geoff's SRA data
asp = "/home/marcsze/.aspera/cli/etc/asperaweb_id_dsa.openssh"
sra_nih = "anonftp@ftp-private.ncbi.nlm.nih.gov:/sra/sra-instant/reads/ByStudy/sra"
database = "SRP"
seq_dir = "SRP108"
study = "SRP108915"

############################################################################################

# Function that takes command line arguments
def command_line():
	commands = sys.argv
	metagenome_sample_file = commands[1]
	
	return metagenome_sample_file

# Function to read in samples in stated text file for samples of interest
def create_samples_to_download(keep_file_name):

	temp_samples = []
	temp_file = open(keep_file_name, 'r')

	for line in temp_file:

		temp_samples.append(line.strip('\n'))

	return(temp_samples)


# Cycles through and downloads each sample in d_files and moves it to appropriate directory
def download_files(keep_files):

	for files in keep_files:

	# Runs the actual download
	os.system("ascp -QTr -k 1 -l 1G -i %s %s/%s/%s/%s/%s/ %s" % 
		(asp, sra_nih, database, seq_dir, study, files, workdir))
	# Moves file back up a directory
	os.system("mv %s%s/%s.sra %s" % (workdir, files, files, workdir))
	# Removes extra empty directory
	os.system("rm -r %s%s" % (workdir, files))
	
	print("Completed downloading and moving sample: %s" % (files))


#for files in chr(range(9)):



# Convert the sra file to fastq files (one forward (F) and one reverse (R))
#for i in os.listdir(workdir):
	
#	if "sra" in i:

#		os.system("fastq-dump --split-files %s%s -O %s" % (workdir, i, workdir))


# Quality filter and toss out reads that don't make the cut 
# -t quality filter of nucleotide (trimmed from the end of sequence)
# -Q average quality cutoff of sequence
# -l minimum length of sequence if shorter after trimming it is tossed
#for fastq_sample in d_files:
    
 #   os.system("sickle pe -f %s%s_1.fastq -r %s%s_2.fastq \
#-t sanger -o %s%s_qf_1.fastq -p %s%s_qf_2.fastq \
#-s %s%s_qf.orphan.fastq -q 30 -l 75" % 
#    	(workdir, fastq_sample, workdir, fastq_sample, 
#    		workdir, fastq_sample, workdir, fastq_sample, 
#    		workdir, fastq_sample))
    
#    print("Completed quality filtering of sample %s" % (fastq_sample))




# Run the actual program

def main():
	meta_genome_file_name = command_line()
	samples_to_download = create_samples_to_download(meta_genome_file_name)
	download_files(samples_to_download)


if __name__ == '__main__': main()