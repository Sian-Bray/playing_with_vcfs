import argparse
parser = argparse.ArgumentParser(description="Removes lines with any missing data (no calls) from a .vcf file.")
parser.add_argument('-i', type=str,  metavar='input_file', required=True, help='Path to the input .vcf file')
parser.add_argument('-o', type=str, metavar='output_file', required=True, help='Name for the output .vcf file.')
args = parser.parse_args()

input_file=open(args.i, 'r')
input_length=len(input_file.readlines())
input_file.close

input_file=open(args.i, 'r')
file_line_count=0
output_file=open(args.o, 'w+')

while file_line_count < input_length:
	current_line=input_file.readline()
	if "./" not in current_line:
		output_file.write(current_line)
	file_line_count+=1