from Bio import SeqIO
import random

# Function to read a FASTA file and separate entries by label


def read_fasta_file(file_path):
    label_1_entries = []
    label_0_entries = []

    with open(file_path, 'r') as fasta_file:
        for record in SeqIO.parse(fasta_file, 'fasta'):
            if "LABEL=1" in record.description:
                label_1_entries.append(record)
            elif "LABEL=0" in record.description:
                label_0_entries.append(record)

    return label_1_entries, label_0_entries


# Read both FASTA files
label_1_entries_dephospho, label_0_entries_dephospho = read_fasta_file(
    'train_Pos_Neg_ST.fasta')
label_1_entries_phospho, label_0_entries_phospho = read_fasta_file(
    'balanced_output_ST.fasta')

# Combine LABEL=1 entries from both datasets and shuffle them
label_1_entries = label_1_entries_dephospho + label_1_entries_phospho
random.shuffle(label_1_entries)

# Combine LABEL=0 entries from both datasets (if any)
label_0_entries = label_0_entries_dephospho + label_0_entries_phospho

# Merge the entries: LABEL=1 first, followed by LABEL=0
merged_entries = label_1_entries + label_0_entries

# Write the merged entries to a new FASTA file
with open('merged_output_D+P_balance_ST.fasta', 'w') as output_file:
    SeqIO.write(merged_entries, output_file, 'fasta')

print("Merged FASTA file has been created successfully.")
