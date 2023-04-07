from setuptools import setup, find_packages

setup(
    name='phylofisher',
    version='1.2.7',
    packages=find_packages(),
    scripts={'phylofisher/fisher.py',
             'phylofisher/config.py',
             'phylofisher/working_dataset_constructor.py',
             'phylofisher/forest.py',
             'phylofisher/matrix_constructor.py',
             'phylofisher/matrix_constructor.smk',
             'phylofisher/informant.py',
             'phylofisher/apply_to_db.py',
             'phylofisher/install_deps.py',
             'phylofisher/select_taxa.py',
             'phylofisher/select_orthologs.py',
             'phylofisher/sgt_constructor.py',
             'phylofisher/sgt_constructor.smk',
             'phylofisher/prep_final_dataset.py',
             'phylofisher/utilities/purge.py',
             'phylofisher/utilities/build_database.py',
             'phylofisher/utilities/fast_site_remover.py',
             'phylofisher/utilities/mammal_modeler.py',
             'phylofisher/utilities/bipartition_examiner.py',
             'phylofisher/utilities/fast_taxa_remover.py',
             'phylofisher/utilities/aa_comp_calculator.py',
             'phylofisher/utilities/aa_recoder.py',
             'phylofisher/utilities/taxon_collapser.py',
             'phylofisher/utilities/genetic_code_examiner.py',
             'phylofisher/utilities/heterotachy.py',
             'phylofisher/utilities/random_resampler.py',
             'phylofisher/utilities/astral_runner.py',
             'phylofisher/utilities/rtc_binner.py',
             'phylofisher/utilities/backup_restoration.py',
             'phylofisher/utilities/explore_database.py',
             'phylofisher/utilities/gfmix_runner.py',
             'phylofisher/utilities/gfmix_mammal.smk',
             'phylofisher/gfmix.yaml',
             'phylofisher/mammal.yaml',
             'phylofisher/prequal.yaml',
             'phylofisher/mafft.yaml',
             'phylofisher/divvier.yaml',
             'phylofisher/trimal.yaml',
             'phylofisher/raxml.yaml',
             'phylofisher/bmge.yaml',
             },
    url='https://github.com/TheBrownLab/PhyloFisher',
    license='MIT',
    author='David Zihala',
    author_email='zihaladavid@gmail.com',
    description='PhyloFisher is a software package for the creation, analysis, and visualization of phylogenomic '
                'datasets that consist of protein sequences from eukaryotic organisms.'
)
