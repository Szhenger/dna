# DNA

## Problem to Solve

DNA, the molecule that carries genetic information in all living organisms, has played a pivotal role in criminal justice for decades. Through the process of DNA profiling, forensic investigators can match a DNA sequence found at a crime scene to individuals, helping to identify suspects or exonerate the innocent. But how does this process work on a technical level? Given a sequence of DNA, how can we determine who the DNA belongs to?

In this problem, we are tasked with implementing a program that automates the DNA profiling process. Using a database of DNA sequences and short tandem repeats (STRs), your program will analyze an unknown DNA sample and identify which individual in the database it belongs to. This solution will help mimic real-world forensic techniques used to match genetic material to specific individuals.

In a file called `dna.py` in a folder named `dna`, that takes a DNA sequence as input and determines to whom it belongs by comparing it against a database of STRs.

## Background

DNA, or deoxyribonucleic acid, is composed of molecules called nucleotides arranged in a specific sequence to form a double helix. Every human cell contains billions of nucleotides, and each nucleotide consists of one of four bases: adenine (A), cytosine (C), guanine (G), or thymine (T). While certain portions of the DNA sequence are highly similar across all humans, other sections exhibit greater genetic diversity and vary significantly between individuals.

One such region where DNA shows high genetic diversity is in Short Tandem Repeats (STRs). An STR is a short sequence of bases that repeats consecutively at specific locations in an individual's genome. The number of repeats for a given STR can vary widely between people. For example, in the DNA sequences of Alice and Bob, Alice might have the STR AGAT repeated four times, while Bob has the same STR repeated five times.

Because the number of STR repeats differs across individuals, forensic investigators use these repeating sequences as genetic markers to create DNA profiles. By analyzing the STR patterns, investigators can match DNA samples to specific individuals, making STR analysis a powerful tool in criminal justice and personal identification.

Using a single STR for identification provides some degree of confidence, but to improve accuracy, multiple STRs are analyzed together. For instance, if the probability that two people share the same number of repeats for a single STR is 5%, analyzing 10 different STRs decreases the probability of a random match to approximately 1 in 1 quadrillion (assuming the STRs are independent). This means that if two DNA samples match in the number of repeats for several STRs, it is highly likely that they came from the same person.

The FBI’s CODIS (Combined DNA Index System) database, for example, uses 20 different STRs in its DNA profiling process to ensure the accuracy and reliability of its results.

In its simplest form, a DNA database can be represented as a CSV file, where each row corresponds to an individual and each column corresponds to a specific STR. Each cell contains the number of times the STR repeats for that individual, allowing the DNA profiles to be easily compared across multiple samples.

DNA profiling relies on the analysis of Short Tandem Repeats (STRs), specific sequences of DNA that repeat consecutively in an individual's genome. The number of consecutive repeats for each STR varies between individuals, making them valuable markers for identifying unique DNA profiles.

In a given database, individuals are represented by their STR counts for several key sequences. For example, Alice may have the STR AGAT repeated 28 times, AATG repeated 42 times, and TATC repeated 14 times, while Bob might have these same STRs repeated 17, 22, and 19 times, respectively. Given a new DNA sample, identifying to whom it belongs involves searching for the longest consecutive repeat of each STR in the sample and comparing those counts to the known profiles in the database.

For instance, if a DNA sample reveals the longest consecutive sequence of AGAT repeats 17 times, AATG repeats 22 times, and TATC repeats 19 times, it is likely that the DNA belongs to Bob. However, if the counts for the STRs do not match any individual in the database, then there is no match.

In real-world applications, analysts can focus on specific regions of the DNA where STRs are known to occur, but for this problem, your task is to write a program that will analyze an entire DNA sequence, compare its STR counts to a database of individuals, and determine to whom the DNA most likely belongs.

## Specification

TODO
