---
title: 'Efficient Data Storage with Bit packing'
published: 2026-09-15
draft: true
tags: ['computing', 'data-storage']
toc: true
cover:
  image: 'cover.png'
  alt: 'A cyberphunky machine.'
---

# Introduction

It was on a cold morning in Muizenberg, I was enjoying my cup of coffee, oozing with a lot of "beginner energy", excited on what I am currntly working on - my thesis project which is about writing a custom vector search database for genomics read mapping.
Sounds interesting right? Yes the energy was full writing some C++ code on the method that would be used for representing DNA sequence data.
The data structure to be used is a binary k-mer vector.
_k-mer_? What is that? I know that is probably what you are thinking right now, don't worry I'll give a brief overview on that in a bit, but for now just take it a list of zeros and ones.


I already implemented this datastructure but I noticed a spike in memory usage while running my sample code.
It was then I told my supervisors - I have two amazing supervisors btw :)- during the meeting we had that morning about the memory spike and they were like "Oh that is normal but you might want to read on bit packing".
The moment I heard the word "bit packing", I was like but my vector is already a `std::vector<uint8_t>` that is I have a list containing 1024 number of zeros and ones. _Isn't that the most optimal I can have?_ was the question that I asked next - since `std::vector<boo>` is also the same. But I was told that there is still room for improvement and it will be nice if I could explore on the topic -bit packing- and ask questions about it in our next meeting. _Yes I explored it and it was fun_

# k-mers substrings

If you have done some work with natural language processing (NLP) you might have used a k-mer without noticing, because they are not called _k-mers_ in NLP.
_k-mers_ are just the genomics siblings of _n-gram_.

In genomics, the DNA of an organism is represented as sequence strings corresponding to the different nucleotide bases, i,e _Adenine (A) Cytosine (C), Guanine (G) and Thymine (T)_, and these long sequence of characters are stored in _fasta/fastq_ files.

:::note
what fasta/fastq file aure used for is beyond the scope of this blog post.
:::

![A sample fastq file #pixelated](./fastq.png 'A sample fastq file')

From the above picture we are only concerned with the second line -the one with the `AACCTAG`-ish.

Now suppose we have a sequence say `ATGCTGAAG`, a k-mer of this sequence is a substring of length _k_.

For our sequence we will have the following:

| _k_ | k-mer substrings |
| --- | --- |
| 1 | {A, T, G, C, T, G, A, A, G} |
| 2 | {AT, TG, GC, CT, TG, GA, AA, AG} |
| 3 | {ATG, TGC, GCT, CTG, TGA, GAA, AAG}|
| 4 | {ATGC, TGCT, GCTG, CTGA, TGAA, GAAG} |
| 5 | {ATGCT, TGCTG, GCTGA, CTGAA, TGAAG} |
| 6 | {ATGCTG, TGCTGA, GCTGAA, CTGAAG} |
| 7 | {ATGCTGA, TGCTGAA, GCTGAAG} |
| 8 | {ATGCTGAA, TGCTGAAG} |
| 9 | {ATGCTGAAG} |

:::important
It is worth noting that for a sequence of length $L$, there are $L - k + 1$ number of overlapping k-mers.

Also for the DNA sequence space for any $k$ there are $2^{2k} = 4^k$ number of possible k-mers.
:::

# Binary vectors

Having only k-mers make no sense in our case, we need to have a representation for them.
This is where _k-mer binary vectors_ comes in.


