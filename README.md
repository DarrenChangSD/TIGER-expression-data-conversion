# TIGER-expression-data-conversion
> Author: Darren Chang @ UCSD Oncogenomics Lab

This project takes data from http://bioinfo.wilmer.jhu.edu/tiger/download/tss_spf_rsc.txt and turns it into a CSV file.

## Getting started
> Instructions to run from scratch but the converted CSV file is already available to download

Take the download.py and parse_EST.py and put them into your desired directory.

## Run download.py

Open a command line window and cd to the foplder that contains download.py and parse_EST.py. Once there run:

```shell
python download.py
```
This command will generate the tss_spf_rsc.txt file in your project directory.

## Run parse_EST.py

In the same directory run:

```shell
python parse_EST.py
```
This command will generate the tss_spf_rsc.csv file in your project directory.

## Done!

Now you should have the CSV file in your project directory ready to be used.
