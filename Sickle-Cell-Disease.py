"""

This program simulates the effects of the Single Nucleotide Polymorphism that leads to sickle cell disease.
It also groups both mutated and normal DNA structures into corresponding amino acid groups.

This is done by:

1. Creating a function that translates a DNA sequence to its corresponding amino acid

2. Creating a function that reads in the external DNA.txt file. Two new text files are then created, one named normalDNA.txt 
and the other named mutatedDNA.txt.

   ● The file normalDNA.txt has the same DNA sequence as DNA.txt with the 'a'
     changed to an 'A'.
   ● The file mutatedDNA.txt has the same DNA sequence as DNA.txt with the 'a'
     changed to a 'T'.

3. Creating a function that reads in the two new text files and calls the original translate function in order 
   to classify the DNA values in each file to their corresponding amino acids. The amino acids of each file are
   then displayed to the user.   
"""

def translate(DNA):  # this function is given an input of a DNA sequence which is then categorised into its amino acid group
    n = 3
    x = [DNA[i:i+n] for i in range(0, len(DNA), n)]  # break the input up into groups of 3 
    AminoAcid = " " # this is where we'll store the input once converted to its Amino Acid
     
    for y in x:  # this for functions adds the input AminoAcid using an if elif else structure
       
     if y == "ATT" or y == "ATC" or y == "ATA":
        AminoAcid += " Isoleucine "
     elif y == "CTT" or y == "CTC" or y == "CTA" or y == "CTG" or y == "TTA" or y == "TTG":
        AminoAcid += "Leucine "
     elif y == "GTT" or y == "GTC" or y == "GTA" or y == "GTG":
        AminoAcid += " Valine "
     elif y == "TTT" or y == "TTC":
        AminoAcid += " Phenylalanine "
     elif y == "ATG":
        AminoAcid += " Methionine " 
     elif y == "TGT" or y == "TGC":
        AminoAcid += " Cysteine "    
     elif y == "GCT" or y == "GCC" or y == "GCA" or y == "GCG":
        AminoAcid += " Alanine "    
     elif y == "GGT" or y == "GGC" or y == "GGA" or y == "GGG":
        AminoAcid += " Glycine " 
     elif y == "CCT" or y == "CCC" or y == "CCA" or y == "CCG":
        AminoAcid += " Proline "   
     elif y == "ACT" or y == "ACC" or y == "ACA" or y == "ACG":
        AminoAcid += " Threonine "    
     elif y == "TCT" or y == "TCC" or y == "TCA" or y == "TCG" or y == "AGT" or y == "AGC":
        AminoAcid += " Serine " 
     elif y == "TAT" or y == "TAC":
        AminoAcid += " Tyrosine "   
     elif y == "TGG":
        AminoAcid += " Tryptophan "    
     elif y == "CAA" or y == "CAG":
        AminoAcid += " Glutamine " 
     elif y == "AAT" or y == "AAC":
        AminoAcid += " Asparagine "  
     elif y == "CAT" or y == "CAC":
        AminoAcid += " Histidine " 
     elif y == "GAA" or y == "GAG":
        AminoAcid += " Glutamic acid  " 
     elif y == "GAT" or y == "GAC":
        AminoAcid += " Aspartic acid  "  
     elif y == "AAA" or y == "AAG":
        AminoAcid += " Lysine "   
     elif y == "CGT" or y == "CGC" or y == "CGA" or y == "CGG" or y == "AGA" or y == "AGG":
        AminoAcid += " Arginine " 
     elif y == "TAA" or y == "TAG" or y == "TGA":
        AminoAcid += " Stop codons "      
    return AminoAcid # the above amino acid groupings were gathered from this source: http://www.endmemo.com/bio/codon.php
                        
def mutate():
    s = open("DNA.txt").read()  #open the file
    s = s.replace('a', 'A')      # replace the required charcter
    f = open("normalDNA.txt", 'w')    #create a new text file 
    f.write(s)
    f.close()
 
    x = open("DNA.txt").read()
    x = x.replace('a', 'T')
    y = open("mutatedDNA.txt", 'w')
    y.write(x)
    y.close()

mutate()    # calling the mutate function in order to create the normal and mutated .txt files 
   
def txtTranslate():  #this function reads the newly created .txt files and outputs both amino acid sequences 
    s = open("mutatedDNA.txt").read()
    s = s.replace('\r', '').replace('\n', '') #this removes the lines from the textfiles otherwsie they can't be input into Translate()
  
    f = open("normalDNA.txt").read()
    f = f.replace('\r', '').replace('\n', '')
    return "\nMutated DNA:  \n"+"\n"+translate(s)+"\n"+"\nNormal DNA:  \n"+"\n"+translate(f)+"\n" #calling the translate function
  
print(txtTranslate()) 
  
 





     
