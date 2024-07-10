import mdtraj as md
t = md.load('protein kinase domain.pdb')
t.save_xyz('protein kinase domain.xyz')