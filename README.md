## About
Workflow in getting related beetle genomes for the genome annotation of the ball-rolling dung beetle *Kheper lamarcki*. The workflow comes in two parts:
1. Downloading the proteomes from the NCBI database.
1. Processing the files for later use.

The scripts runs on the terminal.


## Installation
This program can be directly installed from github (green Code button, top right).

Make sure to change into the downloaded directory, the code should resemble something like this.
```bash=
cd Downloads/related_beetle_proteomes
```

### Conda environment
First make sure conda is installed. If you do not have conda, refer to online resources on how to install conda.
https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

Once installed, we can make a conda environment.

```bash=
conda create --name proteome
#activate
conda activate proteome
```
### Part 1: Proteome download
#### Dependencies
This part requires  NCBI's Entrez Direct (EDirect) terminal app to download the proteomes from their database. The following link can be used to download the terminal app.
```bash=
sh -c "$(curl -fsSL https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh)"
```
After installing it will  ask if you would like to automatically install the path variables. Select yes.

If it does not work refer the NCBI EDirect webpage https://www.ncbi.nlm.nih.gov/books/NBK179288/.



Once set up, activate EDirect in this terminal session with the following.

```bash=
export PATH=${HOME}/edirect:${PATH}
```


Wget is also required to download the proteomes. So on a mac, one has to install homebrew to install wget.
```bash=
#install homebrew (mac OS 13.1)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
#install wget
brew install wget
```
Should be good to run the first part of the workflow.

### Part 2: Proteome processing
### Python version
The python version for running this script is python= 3.12.1 
```bash=
conda install python= 3.12.1 
```

### Dependencies
The script runs with pip=24.0.

Update your dependencies, if you do not already have the versions for these dependencies.

```bash=
pip install --upgrade pip==24.0

pip install  tqdm==4.66.2
```

## Usage

### Part 1:  Proteome download
Here we are downloading all proteomes of suborder polyphaga in within the beetle order. 

First we are using esearch to find all species assemblies within the suborder polyphaga.
Then echoing the line of code for each species onto a file called esearch_related_beetles.txt
```bash=
#summary lists all information
#xtract to get the web link for data download
#then run a while loop to specifcally only get the protein file and place it in a folder called protein_data
esearch -db assembly -query 'Polyphaga[organism]' | esummary | xtract -pattern DocumentSummary -element Taxid | while read -r taxid; do echo "esearch -db assembly -query $taxid| esummary | xtract -pattern DocumentSummary -element FtpPath_RefSeq | while read -r url; do path=\$(echo \$url | perl -pe 's/(GC[FA]_\d+.*)/\1\/\1_protein.faa.gz/g'); wget -q --show-progress \$path -P protein_data; done">> esearch_related_beetles.txt;   done
```

To finally download all proteomes run the following.
```bash=
bash esearch_related_beetles.txt
```

### Part 1:  Proteome processing
### Input
The code is run with two required arguments; input and output folders.  
```bash=
    python rename_protein_file.py [-h] [-v] -i INPUT_FOLDER -o OUTPUT_FOLDER [-c CORES]
```
More information about optional flags can be found with the following help command.
```bash=
    pyramid_make.py -h
```

Run the following line of code on terminal to run the processing script.
```bash=
python rename_protein_file.py -i protein_data/ -o protein_data_rename -c 2
```

You should finally have a folder with all the files processed and in one place. 

