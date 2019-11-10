from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='4PCUw', model_segment=('FIRST:A','LAST:B'))
aln.append_model(mdl, align_codes='4PCUw', atom_files='4PCUw.pdb')
aln.append(file='target.ali', align_codes='target')
aln.align2d()
aln.write(file='aliall.ali', alignment_format='PIR')
aln.write(file='aliall.pap', alignment_format='PAP')
