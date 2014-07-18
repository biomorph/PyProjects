__author__ = 'ravi'
from Bio import SeqIO

fastq_fh = open("rosalind_bfil.txt", 'rU')

quality_threshold = int(fastq_fh.readline().strip())

fastq_records = list(SeqIO.parse(fastq_fh,"fastq"))


for fastq_record in fastq_records:

    five_prime_trim = 0
    three_prime_trim = 0
    five_prime_counter = 0
    three_prime_counter = -1
    keep_trimming_5 = True
    keep_trimming_3 = True

    quality_array = fastq_record.letter_annotations.values()[0]
    while keep_trimming_5 or keep_trimming_3:

        if keep_trimming_5: five_prime_quality = quality_array[five_prime_counter]
        if keep_trimming_3: three_prime_quality = quality_array[three_prime_counter]

        if five_prime_quality < quality_threshold:
            five_prime_trim = five_prime_trim + 1
            five_prime_counter = five_prime_counter + 1
        else: keep_trimming_5 = False

        if three_prime_quality < quality_threshold:
            three_prime_trim = three_prime_trim + 1
            three_prime_counter = three_prime_counter - 1
        else: keep_trimming_3 = False

    if (five_prime_trim == 0  and three_prime_trim == 0):
        print fastq_record.format("fastq"),


    elif (len(fastq_record[five_prime_trim:-three_prime_trim].seq) > 0):
       print fastq_record[five_prime_trim:-three_prime_trim].format("fastq"),
