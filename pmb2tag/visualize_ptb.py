
from discodop import treebank
from discodop.treebank import incrementaltreereader
from discodop.tree import DrawTree
import sys

file_with_bracketed_ptb_sents = sys.argv[1]

with open(file_with_bracketed_ptb_sents) as f:
    for n, line in enumerate(f):
        if n > 7000: # visualize the first three trees
            break

        for tree, sent, comment in incrementaltreereader(line):
            origtree = tree.copy(True).freeze()
            print(DrawTree(origtree, sent).text())
            tree_before_extraction = str(
                treebank.writebrackettree(origtree, sent))
            print()

"""
# visualize trees inline:

inp = '(S (CC But) (SBAR-TMP (IN as) (S (NP-SBJ (PRP they)) (VP (VP (VBP hurl) (NP (NP (NNS fireballs)) (SBAR (WHNP (WDT that)) (S (VP (VBP smolder) (CONJP (RB rather) (IN than)) (VBP burn)))))) (, ,) (CC and) (VP (VBP relive) (NP (JJ old) (NNS duels)) (PP-LOC (IN in) (NP (DT the) (NN sun))))))) (, ,) (NP-SBJ (NP (PRP it))) (VP (VBZ \'s) (ADJP-PRD (JJ clear)) (SBAR (IN that) (S (NP-SBJ (JJS most)) (VP (VBP are) (ADVP-LOC-PRD (RB there)) (S-PRP (VP (TO to) (VP (VP (VB make) (S (NP-SBJ (PRP$ their) (NNS fans)) (VP (VB cheer) (ADVP-TMP (RB again))))) (CC or) (VP (VB recapture) (NP (NP (DT the) (NN camaraderie)) (PP (IN of) (NP (NP (NNS seasons)) (NP-TMP (JJ past)))))) (CC or) (VP (VB prove) (PP (TO to) (NP (NP (PRP themselves)) (CC and) (NP (PRP$ their) (NNS colleagues)))) (SBAR (IN that) (S (NP-SBJ (PRP they)) (ADVP-TMP (RB still)) (VP (VBP have) (NP (NP (PRP it)) (: --) (CC or) (NP (NP (NN something)) (ADJP (RB close) (PP (TO to) (NP (PRP it))))))))))))))))) (. .))'

for tree, sent, comment in incrementaltreereader(inp):
    origtree = tree.copy(True).freeze()
    print(DrawTree(origtree, sent).text())
"""

