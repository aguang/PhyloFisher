from setuptools import setup, find_packages

setup(
    name='phylofisher',
    version='1.1.3',
    packages=find_packages(),
    scripts={'phylofisher/fisher.py',
             'phylofisher/config.py',
             'phylofisher/working_dataset_constructor.py',
             'phylofisher/forest.py',
             'phylofisher/matrix_constructor.py',
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
             'phylofisher/utilities/SR4_class_recoder.py',
             'phylofisher/utilities/taxon_collapser.py',
             'phylofisher/utilities/genetic_code_examiner.py',
             'phylofisher/utilities/heterotachy.py',
             'phylofisher/utilities/random_resampler.py',
             'phylofisher/utilities/astral_runner.py',
             'phylofisher/utilities/rtc_binner.py',
             'phylofisher/utilities/backup_restoration.py',
             'phylofisher/utilities/explore_database.py'
             },
    python_requires='==3.7.10',
    install_requires=['biopython==1.78',
                      'pyqt5==5.12.3',
                      'ete3==3.1.2',
                      'pandas==1.2.4',
                      'matplotlib==3.4.1',
                      'scipy==1.6.2',
                      'numpy==1.21.0'
                      ],
    url='https://github.com/TheBrownLab/PhyloFisher',
    license='MIT',
    author='David Zihala',
    author_email='zihaladavid@gmail.com',
    description='PhyloFisher is a software package for the creation, analysis, and visualization of phylogenomic '
                'datasets that consist of protein sequences from eukaryotic organisms.'
)
