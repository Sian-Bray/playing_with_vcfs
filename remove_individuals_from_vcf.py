#Input parameters
#vcf input, output name, individuals to remove
import argparse
parser = argparse.ArgumentParser(description='Removes individuals from a .vcf, even if they are mixed polyploidy!')
parser.add_argument('-i', type=str, required=True, help='path to the input .vcf')
parser.add_argument('-o', type=str, required=True, help='name of the output .vcf')
parser.add_argument('-l', type=str, required=True, help='list of individuals to be removed in a .txt file, 1 individual per line.')
args=parser.parse_args()

#Where are the individuals to be removed? Get index position when split at \t
input_file=open(args.i, 'r')
individuals=open(args.l, 'r').readlines()
index_list=list()

while True == True:
	current_line=input_file.readline()
	if current_line[0:6]=='#CHROM':
		header=current_line.split('\t')
		for individual in individuals:
			index_list.append(header.index(individual.replace('\n', '')))
		input_file.close
		break

input_file.close
index_list=sorted(index_list, key=int, reverse=True)

#remove the indexed positions from each line from the header onwards
input_file=open(args.i, 'r')
input_length=len(input_file.readlines())
input_file.close
input_file=open(args.i, 'r')
passed=False
output_file=open(args.o, 'w+')
line_count=0

while line_count < input_length:
	written_line=str()
	current_line=input_file.readline()
	if current_line[0:6]=='#CHROM':
		passed=True
	if passed==True:
		current_line_n=current_line.replace('\n', '')
		current_list=current_line_n.split('\t')
		for num in index_list:
			del current_list[num]
		for thing in current_list:
			written_line=written_line+thing+'\t'
		written_line=written_line+'\t\t'
		final_written_line=str(written_line)
		final_frozen_written_line=final_written_line.replace('\t\t\t', '\n')
		output_file.write(final_frozen_written_line)
	if passed==False:
		output_file.write(current_line)
	line_count+=1
