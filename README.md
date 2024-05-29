# download fasta file online

install
```bash=
sh -c "$(curl -fsSL https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh)"
```
yes to automatically istall path variables

then activate EDirect in this terminal session with 

```bash=
export PATH=${HOME}/edirect:${PATH}
```

example run

```bash=
esearch -db nucleotide -query "NC_030850.1" | efetch -format fasta 
```

get all taxids of scarabaeus

```bash=
 esearch -db taxonomy -query "scarabaeus" | efetch -format xml | xtract -pattern TaxId -element TaxId 
```

need wget, so had to install homebrew to install wget
```bash=
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install wget
```

then tes trun downloading onthophagus taurus proteome

esearch to find assembly, specifcally the last one of onthophagus
essumary has all information
xtract to get the web link to get data from
then run a while loop to specifcally only get the protein file and place it in a folder called protein_data

```bash=
esearch -db assembly -query 'txid166361[organism] AND latest_refseq[filter]' | esummary | xtract -pattern DocumentSummary -element FtpPath_RefSeq | while read -r url; do path=$(echo $url | perl -pe 's/(GC[FA]_\d+.*)/\1\/\1_protein.faa.gz/g'); wget -q --show-progress "$path" -P protein_data ; done
```


```bash=
esearch -db assembly -query 'Scarabaeoidea[organism]' | esummary | xtract -pattern DocumentSummary -element Taxid | while read -r taxid; do echo "esearch -db assembly -query $taxid| esummary | xtract -pattern DocumentSummary -element FtpPath_RefSeq | while read -r url; do path=\$(echo \$url | perl -pe 's/(GC[FA]_\d+.*)/\1\/\1_protein.faa.gz/g'); wget -q --show-progress \$path -P protein_data; done">> esearch_related_beetles.txt;   done
```
echos the line for each taxid to test.txt. then run that  

```bash=
bash test.txt
```

