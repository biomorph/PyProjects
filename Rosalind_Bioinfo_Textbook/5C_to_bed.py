__author__ = 'ravi'

primer_fh = open("5C_primers.bed",'rU')

primer_dict = {}

for primer in primer_fh:
    primer_info = primer.split()
    primer_chr = primer_info[0]
    primer_start = primer_info[1]
    primer_stop = primer_info[2]
    primer_name = primer_info[3].split(":")[0]
    mod_primer_name = primer_name.rsplit("_",1)[0] + "_" +  primer_name.rsplit("_",1)[1].zfill(3) #adding leading zeroes to primer number at the end, like they are in the processed file for some reason
    primer_dict[mod_primer_name] = [primer_chr, int(primer_start), int(primer_stop)]

primer_fh.close()


processed_5C_data = open("GSE36203_processed_5C_seq_data.txt", 'rU')
processed_bed = open("processed.bed", 'w')

header = processed_5C_data.readline()
for line in processed_5C_data:
    interaction_info = line.split()
    primer1 = interaction_info[1]
    primer2 = interaction_info[2]
    es_pvalue1 = interaction_info[8]
    es_score1 = interaction_info[9]
    es_score2 = interaction_info[15]
    npc_score1 = interaction_info[21]
    npc_score2 = interaction_info [27]


    primer1_info = primer_dict[primer1]
    primer2_info = primer_dict[primer2]
    chrom = primer1_info[0]
    chromStart = str(min(primer1_info[1],primer2_info[1]))
    chromEnd = str(max(primer1_info[2],primer2_info[2]))
    name = primer1_info[0]+":"+str(primer1_info[1])+".."+str(primer1_info[2]) + "-" + primer2_info[0]+":"+str(primer2_info[1])+".."+str(primer2_info[2])
    score = ""
    if float(es_score1) > 0 and float(es_pvalue1) < 0.05: score = str(float(es_score1)*200)
    else: continue
    strand = "."
    thickStart = chromStart
    thickEnd = chromEnd
    reserved = "255,0,0"
    blockCount = "2"
    blockSizes = ""
    if int(chromStart) == primer1_info[1]: blockSizes = str(primer1_info[2]-primer1_info[1]) + "," + str(primer2_info[2]-primer2_info[1])
    else: blockSizes = str(primer2_info[2]-primer2_info[1]) + "," + str(primer1_info[2]-primer1_info[1])
    chromStarts = "0," + str(abs(primer1_info[1]-primer2_info[1]))
    processed_bed.write("\t".join([chrom,chromStart,chromEnd,name,score,strand,thickStart,thickEnd,reserved,blockCount,blockSizes,chromStarts,"\n"]))

