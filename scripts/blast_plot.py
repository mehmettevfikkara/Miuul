import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

blast_G_Muris = pd.read_csv("/Users/mehmettevfikkara/PycharmProjects/Miuul/output/blastn/G_intestinalis/G_muris.blastn", sep='\t', header=None)
blast_S_Salmonicida = pd.read_csv("/Users/mehmettevfikkara/PycharmProjects/Miuul/output/blastn/G_intestinalis/S_salmonicida.blastn", sep='\t', header=None)

blast_G_Muris.columns = ["qseqid", "sseqid", "pident", "length", "mismatch", "gapopen", "qstart",
                         "qend", "sstart", "send", "evalue", "bitscore"]

blast_S_Salmonicida.columns = ["qseqid", "sseqid", "pident", "length", "mismatch", "gapopen", "qstart",
                               "qend", "sstart", "send", "evalue", "bitscore"]


num_hits_blast_G_muris = len(blast_G_Muris)
num_hits_blast_S_salmonicida = len(blast_S_Salmonicida)

print("Number of hits for Giardia İntestinalis vs Giardia Muris: ", num_hits_blast_G_muris)
print("Number of hits for Giardia İntestinalis vs Spironucleus Salmonicida: ", num_hits_blast_S_salmonicida)

sns.histplot(data=blast_G_Muris, x="pident")

plt.show()