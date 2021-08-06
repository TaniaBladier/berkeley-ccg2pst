#!/bin/bash

/usr/bin/python3 /home/tania/Dropbox/pmb2tag-frames/berkeley-ccg2pst/pmb2tag/preprocess_pmb.py /home/tania/Dropbox/pmb2tag-frames/data/pmb-3.0.0-en-gold-p31.parse.tags /home/tania/Dropbox/pmb2tag-frames/data/31_pmb_in_ccgbank_format.pmb

python2 /home/tania/Dropbox/pmb2tag-frames/berkeley-ccg2pst/convert.py /home/tania/Dropbox/pmb2tag-frames/data/31_pmb_in_ccgbank_format.pmb -prefix=/home/tania/Dropbox/pmb2tag-frames/data/31_pmb_in_ccgbank_format.pmb -verbose -method=markedup /home/tania/Dropbox/pmb2tag-frames/berkeley-ccg2pst/markedup

/usr/bin/python3 /home/tania/Dropbox/pmb2tag-frames/berkeley-ccg2pst/pmb2tag/visualize_ptb.py /home/tania/Dropbox/pmb2tag-frames/data/31_pmb_in_ccgbank_format.pmb.auto