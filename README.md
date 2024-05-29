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



```bash=
esearch -db assembly -query 'Polyphaga[organism]' | esummary | xtract -pattern DocumentSummary -element SpeciesName | while read -r species; do echo "esearch -db assembly -query '$species[organism]'| esummary | xtract -pattern DocumentSummary -element FtpPath_RefSeq | while read -r url; do path=\$(echo \$url | perl -pe 's/(GC[FA]_\d+.*)/\1\/\1_protein.faa.gz/g'); wget -q --show-progress \$path -P protein_data; done">> esearch_related_beetles.txt;   done

esearch -db assembly -query 'Prosopocoilus inquinatus (beetles)[organism]'| esummary | xtract -pattern DocumentSummary -element FtpPath_RefSeq ; done

esearch -db assembly -query 'Scarabaeoidea[organism]' | esummary | xtract -pattern DocumentSummary -element Taxid | while read -r taxid; do echo "esearch -db assembly -query $taxid| esummary | xtract -pattern DocumentSummary -element FtpPath_Assembly | while read -r url; do path=\$(echo \$url | perl -pe 's/(GC[FA]_\d+.*)/\1\/\1_protein.faa.gz/g'); wget -q --show-progress \$path -P protein_data; break; done">> esearch_related_beetles.txt;   done

esearch -db assembly -query 'Scarabaeoidea[organism]' | esummary | xtract -pattern DocumentSummary -element Organism | while read -r orgo; do esearch -db assembly -query '$orgo[organism]'| esummary ;   done

esearch -db assembly -query 'Onthophagus taurus[organism]'| esummary | xtract -pattern DocumentSummary -element FtpPath_RefSeq | while read -r url; do path=$(echo $url | perl -pe 's/(GC[FA]_\d+.*)/\1\/\1_protein.faa.gz/g'); wget -q --show-progress $path -P protein_data; done

 esearch -db assembly -query 'Prosopocoilus inquinatus[organism]'| esummary | xtract -pattern DocumentSummary -element FtpPath_GenBank 


onthophagus_taurus[organism] latest_refseq[filter]

esearch -db assembly -query 'Scarabaeoidea[organism]' | esummary | xtract -pattern DocumentSummary -element Taxid | while read -r taxid; do echo "esearch -db assembly -query $taxid | esummary | xtract -pattern DocumentSummary -element FtpPath_RefSeq >> test_2.test" >> test.txt;   done

esearch -db assembly -query 'Scarabaeoidea[organism]' | esummary | xtract -pattern DocumentSummary -element Taxid | while read -r taxid; do echo $taxid hey ; esearch -db assembly -query $taxid | esummary | xtract -pattern DocumentSummary -element FtpPath_RefSeq ; echo $taxid; done
esearch -db assembly -query 'Scarabaeoidea[organism]' | esummary | xtract -pattern DocumentSummary -element Taxid | while read -r  taxid; do echo $taxid hey ; esearch -db assembly -query $taxid | esummary |xtract -pattern DocumentSummary -element FtpPath_RefSeq >> url.txt ;done



esearch -db assembly -query 'Scarabaeoidea[organism]' | esummary | xtract -pattern DocumentSummary -element Taxid | while read taxid; do esearch -db assembly -query $taxid | esummary | xtract -pattern DocumentSummary -element FtpPath_RefSeq  ; done

esearch -db assembly -query 'Scarabaeoidea[organism]' | esummary | xtract -pattern DocumentSummary -element Taxid | while read taxid; do esearch -db assembly -query $taxid | esummary | xtract -pattern DocumentSummary -element FtpPath_RefSeq  ; done

esearch -db assembly -query 'Scarabaeoidea[organism]' |
esummary |
xtract -pattern DocumentSummary -element Taxid |
while read taxid; do echo $taxid hey ; esearch -db assembly -query $taxid 
| esummary |
xtract -pattern DocumentSummary -element FtpPath_RefSeq | while read -r url; do path=$(echo $url | perl -pe 's/(GC[FA]_\d+.*)/\1\/\1_protein.faa.gz/g'); wget -q --show-progress "$path" -P protein_data ;  done  ; done



esearch -db assembly -query 'Scarabaeoidea[organism]' | esummary | xtract -pattern DocumentSummary -element Taxid | while read taxid; do echo $taxid hey | echo bob| while read bobby; do path=$(hey); echo "$path";  done  ; done


esearch -db assembly -query 'Scarabaeoidea[organism]' | esummary | xtract -pattern DocumentSummary -element Taxid > funfile.txt; cat funfile.txt | for file in funfile.txt; do echo $taxid ; esearch -db assembly -query $taxid | esummary | xtract -pattern DocumentSummary -element FtpPath_RefSeq | while read -r url; do path=$(echo $url | perl -pe 's/(GC[FA]_\d+.*)/\1\/\1_protein.faa.gz/g'); wget -q --show-progress "$path" -P protein_data ;  done  ; done
 > funfile.txt; cat funfile.txt


esearch -db assembly -query '22694951[organism] AND latest_refseq[filter]' | esummary | xtract -pattern DocumentSummary -element FtpPath_RefSeq | while read -r url; do path=$(echo $url | perl -pe 's/(GC[FA]_\d+.*)/\1\/\1_protein.faa.gz/g'); wget -q --show-progress "$path" -P protein_data ;  done

esearch -db assembly -query 'Scarabaeoidea[organism]' | esummary | xtract -pattern DocumentSummary -element Taxid | while read taxid; do echo $taxid; done

esearch -db assembly -query 'Scarabaeoidea[organism]' | esummary | xtract -pattern DocumentSummary -element Taxid | while read -r taxid; do esearch -db assembly -query '$taxid[taxid]'| esummary    done
```
