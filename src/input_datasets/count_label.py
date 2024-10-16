from Bio import SeqIO

# Initialize counters for labels
label_1_count = 0
label_0_count = 0

# Initialize counters for S, T, Y in the middle position
label_1_S_count = 0
label_1_T_count = 0
label_1_Y_count = 0
label_0_S_count = 0
label_0_T_count = 0
label_0_Y_count = 0

# Read the FASTA file and count labels and middle residues
with open('merged_output_D+P_balance_Y.fasta', 'r') as fasta_file:
    for record in SeqIO.parse(fasta_file, 'fasta'):
        sequence = str(record.seq)
        middle_residue = sequence[len(sequence) // 2]
        if "LABEL=1" in record.description:
            label_1_count += 1
            if middle_residue == 'S':
                label_1_S_count += 1
            elif middle_residue == 'T':
                label_1_T_count += 1
            elif middle_residue == 'Y':
                label_1_Y_count += 1
        elif "LABEL=0" in record.description:
            label_0_count += 1
            if middle_residue == 'S':
                label_0_S_count += 1
            elif middle_residue == 'T':
                label_0_T_count += 1
            elif middle_residue == 'Y':
                label_0_Y_count += 1

print(f"Number of LABEL=1 entries: {label_1_count}")
print(f"  S: {label_1_S_count}")
print(f"  T: {label_1_T_count}")
print(f"  Y: {label_1_Y_count}")
print(f"Number of LABEL=0 entries: {label_0_count}")
print(f"  S: {label_0_S_count}")
print(f"  T: {label_0_T_count}")
print(f"  Y: {label_0_Y_count}")
