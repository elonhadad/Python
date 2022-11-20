"""
Student: elon hadad
Assignment no. 2
Program: genes.py
"""

def next_gene(i,s):
    '''find the gene,The function returns the start index of
    The gene and the index following the end of the gene.'''
    
    first_i = s.find("ATG",i)
    lst = []
    for index in range(first_i, len(s), 3):
        last_i = s.find("TAA", index, index+3)
        lst.append(last_i)
        last_i = s.find("TGA", index, index+3)
        lst.append(last_i)
        last_i = s.find("TAG", index, index+3)
        lst.append(last_i)
        if max(lst) > -1:
            break
    last_i = max(lst)
    last_i += 3
        
    if first_i < 0:
        return None
    return first_i, last_i


def get_genes(s):
    ''' Returns a list of all found genes from string'''
    
    lst = []
    i = 0
    while next_gene(i,s) != None:
        first,end = next_gene(i,s)
        lst.append(s[first:end])
        i = end
    return lst


def gene_to_protein(gene):
    symbol = {"A":["GCA","GCC","GCG","GCT"], "C":["TGC","TGT"], "D":["GAC","GAT"],"E":["GAA","GAG"], "F":["TTC","TTT"], 
              "G":["GGA","GGC","GGG","GGT"],"H":["CAC","CAT"], "I":["ATA","ATC","ATT"], "K":["AAA","AAG"], 
              "L":["CTA","CTC","CTG","CTT","TTA","TTG"], "M":["ATG"], "N":["AAC","AAT"], "P":["CCA","CCC","CCG","CCT"],
              "Q":["CAA","CAG"], "R":["AGA","AGG","CGA","CGC","CGG","CGT"], "S":["AGC","AGT","TCA","TCC","TCG","TCT"],
              "T":["ACA","ACC","ACG","ACT"], "V":["GTA","GTC","GTG","GTT"], "W":["TGG"], "Y":["TAC","TAT"]}

    lst2 = []
    count = 0
    mystr = ""
    for j in gene:
        mystr += j
        count += 1
        if count == 3:
            lst2.append(mystr)
            mystr = ""
            count = 0
    
    Protein = ""
    for i in lst2:
        for val in symbol:
            if i in symbol[val]:
                Protein += val
    return Protein

        
def get_proteins(genes):
    '''Receives a list of genes and returns a list of sequences
    Appropriate amino acids'''
    
    protein_lst = []
    for val in genes:
        protein_lst.append(gene_to_protein(val))
    return protein_lst


def main():
    while True:
        f_name = input("Please enter the file name: ")
        try:
            f = open(f_name, "r")
            break
        except FileNotFoundError as error:
            print(error)
    text = f.read()
    f.close()
    
    s = text
    genes = get_genes(s)
    newFilename = ""
    for val in f_name:
        if val == ".":
            break
        newFilename += val
        
    newfile = open(newFilename + "_proteins.txt", "w")
    newfile.write("\n".join(get_proteins(genes)))
    print("Found",len(get_proteins(genes)),"genes")
main()