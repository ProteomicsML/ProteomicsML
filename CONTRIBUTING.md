---
output-file: contributing
---

# Contributing

This document describes how to contribute to the
[ProteomicsML](https://github.com/proteomicsml/proteomicsml) resource by adding new or
updating existing tutorials and/or datasets.


## Before you begin
At ProteomicsML, we pledge to act and interact in ways that contribute to an open,
welcoming, diverse, inclusive, and healthy community. By interacting with or
contributing to ProteomicsML at
[https://github.com/ProteomicsML](https://github.com/ProteomicsML) or at
[https://proteomicsml.org](https://proteomicsml.org),
you agree to our Code of Conduct. Violation of our Code of Conduct may ultimately lead
to a permanent ban from any sort of public interaction within the community.<br>
🤝 Read the [Code of Conduct](/code-of-conduct.html)<br>

If you have an idea for a new tutorial or dataset, or found a mistake, you are welcome
to communicate it with the community by opening a discussion thread in  GitHub
Discussions or by creating an issue.<br>
💬 Start a [discussion thread](https://github.com/ProteomicsML/ProteomicsML/discussions)<br>
💡 Open an [issue](https://github.com/ProteomicsML/ProteomicsML/issues/new/choose)<br>


## The ProteomicsML infrastructure

ProteomicsML uses the [Quarto](https://quarto.org/) system to publish a static website
from markdown and Jupyter IPython notebook files. All source files are maintained at
[ProteomicsML/ProteomicsML](https://github.com/proteomicsml/proteomicsml). Upon each
commit on the main branch (after merging a pull request), the website is rebuilt on
GitHub Actions and pushed to the [ProteomicsML/proteomicsml.github.io](https://github.com/ProteomicsML/proteomicsml.github.io)
repository, where it is hosted with GitHub Pages on the
[ProteomicsML.org](https://proteomicsml.org) website. See
[Website deployment](#website-deployment) for the full deployment workflow.

## How to contribute

### Development setup

1. Fork [ProteomicsML/ProteomicsML](https://github.com/proteomicsml/proteomicsml) on
   GitHub to make your changes.
2. Clone your fork of the repository to your local machine.
3. Install [Quarto](https://quarto.org/docs/get-started/) to build the website on your
   machine.
4. To preview the website while editing, run: `quarto preview . --render html`

Maintainers with write access to the repository can skip the first two steps and make a
new local branch instead. Direct commits to the `main` branch are not allowed.


### Adding/updating a tutorial

ProteomicsML tutorials are educational Jupyter notebooks that combine
fully functional code cells and descriptive text cells. The end result should be a
notebook that is easy to comprehend to anyone with a basic understanding of proteomics,
programming, and machine learning. When adding or updating a tutorial, please follow
these rules and conventions:

1. Title, filename, metadata, and subheadings

    a. Tutorials are grouped by data type: `Fragmentation`, `Ion mobility`,
       `Protein visibility`, and `Retention time`. Place your tutorial notebook in the appropriate directory in the repository. E.g., `tutorials/fragmentation`. If your
       tutorial is part of a new data type group, please open a new
       [discussion thread](https://github.com/ProteomicsML/ProteomicsML/discussions)
       first.

    b. The filename should be an abbreviated version of the tutorial title, formatted in
       kebab case (lowercase with `-` replacing spaces), for instance
       `title-of-tutorial.ipynb`.

    c. The following front matter metadata items are required (see the
       [Quarto Documentation](https://quarto.org/docs/tools/jupyter-lab.html#yaml-front-matter)
       for more info):

       - `title`: A descriptive sentence-like title
       - `authors`: All authors that significantly contributed to the tutorial
       - `date`: Use `last-modified` to automatically render the correct date

       :::{.callout-note}
       Unfortunately, YAML front matter is not rendered by Google Colab. Instead it is
       interpreted as plain markdown and the first cell of the notebook might look out
       of place when loaded into Google Colab. Nevertheless, the front matter results
       in a clean header on ProteomicsML.org, the primary platform for viewing
       tutorials.
       :::

    d. Quarto will render the title automatically from the metadata. Therefore, only
       subheadings should be included as markdown, starting at the second heading level
       (`##`).

    e. Add an `Open with Colab` badge directly after the front matter metadata. The
       badge should be hyperlinked to open the notebook in Colab directly from GitHub.
       This can be achieved by replacing `https://github.com/` with
       `https://colab.research.google.com/github/` in the full URL to the file on
       GitHub. Additionally, in this URL the filename should be prefixed with an
       underscore (`_`); see point 2 in [Website deployment](#website-deployment) for
       more info on notebook copies for Colab.

       For example:

       ```md
       [![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ProteomicsML/ProteomicsML/blob/main/tutorials/fragmentation/_nist-1-parsing-spectral-library.ipynb)
       ```
       renders as

       [![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ProteomicsML/ProteomicsML/blob/main/tutorials/fragmentation/_nist-1-parsing-spectral-library.ipynb)

       :::{.callout-note}
       The URL will not work (or be updated) until the pull request adding or updating
       the notebook is merged into the main branch.
       :::


2. Subject and contents

    a. Each tutorial should clearly show and describe one or more steps in a certain
       machine learning workflow for proteomics.

    b. Sufficiently describe each code cell and each step in the workflow.

    c. Tutorials should ideally be linked to a single ProteomicsML dataset from the
       same group.

    d. While multiple tutorials can be added for a single data type, make sure that
       each tutorial is sufficiently different from the others in terms of methodology
       and/or datasets used.

    e. All original publications that describe the methodologies, datasets, or tools
       that are used in the tutorial should be properly cited following to scientific
       publishing conventions. [TODO: add methodology]


3. Code cells and programming language

    a. Tutorials should work on all major platforms (Linux, Windows, macOS). An
       exception to this rule can be made if one or more tools central to the tutorial
       is not cross-platform.

    b. Per ProteomicsML convention, tutorials should use the Python programming
       language. Exceptions may be allowed if the other language is essential to the
       tutorial or methodology.

    c. ProteomicsML recommends Google Colab to interactively use tutorial notebooks.
       Therefore, all code should be backwards compatible with the Python version used
       by Google Colab. At time of writing, this is Python 3.7.

    d. Dependencies should ideally be installable with pip. A first code cell can be
       used to install all requirements using the Jupyter shell prefix `!`. For
       instance: `! pip install pandas`.

    e. Code should be easy to read. For Python, follow the PEP8 style guide where
       possible.

    f. Upon pull request (PR) creation, all expected output cells should be present.
       When rendering the ProteomicsML website, notebooks are not rerun. Therefore, as
       a final step before submitting your PR, restart the kernel, run all cells from
       start to finish, and save the notebook. See point 2 in
       [Website deployment](#website-deployment) for more info on notebook copies for
       Colab.


### Adding/updating a dataset

ProteomicsML datasets are community-curated proteomics datasets fit for machine
learning. Ideally, each dataset is accompanied by a tutorial. When adding or updating
a dataset, please follow these rules and conventions:


1. Dataset description and data files:

   a. Each dataset is represented as a single markdown file describing the dataset.

   b. The data itself can be added in one of three ways:
      i. If the dataset itself consists of one or more files, each smaller than 50 MB,
         they can be added in a subfolder with the same name as the markdown file.
         These files should be individually gzipped to save space and to prevent
         line-by-line tracking by Git.

         :::{.callout-note}
         Gzipped CSV files can very easily be read by Pandas into a DataFrame. Simply
         use the filename with the `.gz` suffix in the `pandas.read_csv()` function
         and Pandas will automatically unzip the file while reading.
         :::

      ii. Larger files can be added to the ProteomicsML FTP file server by the project
          maintainers. Please request this in your pull request.

      iii. Files that are already publicly and persistently stored elsewhere, can be
           represented by solely the markdown file. In this case, all tutorials using
           this dataset should start from the file(s) as is and include any required
           preprocessing steps.[TODO: List supported platforms]


2. Title, filename, and metadata:
   a. Datasets are grouped by data type: `Fragmentation`, `Ion mobility`,
      `Protein visibility`, or `Retention time`. Place your dataset and markdown
      description in the appropriate directory in the repository. E.g.,
      `tutorials/fragmentation`. If your dataset is part of a new data type group,
      please open a new
      [discussion thread](https://github.com/ProteomicsML/ProteomicsML/discussions)
      first.

   b. The filename / directory name should be an abbreviated version of the dataset
      title, formatted in kebab case (lowercase with `-` replacing spaces), for
      instance `title-of-dataset.md` / `title-of-dataset/`.

   c. The following front matter metadata items are required (see the
      [Quarto Documentation](https://quarto.org/docs/tools/jupyter-lab.html#yaml-front-matter)
      for more info):
         - `title`: A descriptive sentence-like title
         - `date`: Use `last-modified` to automatically render the correct date

   d. Quarto will render the title automatically from the metadata. Therefore, only
      subheadings should be included as markdown, starting at the second heading level
      (`##`).


3. Dataset description

   Download the readme template and fill out the details<br>
   - [Retention time](https://github.com/ProteomicsML/ProteomicsML/datasets/_templates/retention-time-template.md)<br>
   - [Fragmentation Intensity](https://github.com/ProteomicsML/ProteomicsML/datasets/_templates/fragmentation-intensity-template.md)<br>
   - [Ion Mobility](https://github.com/ProteomicsML/ProteomicsML/datasets/_templates/ion-mobility-template.md)<br>
   - [Detectability](https://github.com/ProteomicsML/ProteomicsML/datasets/_templates/protein-detectability-template.md)<br>


### Opening a pull request to add your contributions

- Commit and push your changes to your
[fork](https://help.github.com/articles/pushing-to-a-remote/).
- Open a
[pull request](https://help.github.com/articles/creating-a-pull-request/)
with these changes. Choose the pull request template that fits your changes best.
- The pull request should pass all the continuous integration tests which are
  automatically run by
  [GitHub Actions](https://github.com/proteomicsml/proteomicsml/actions).


## Website deployment

When a pull request is merged with the `main` branch, the following GitHub Actions are
triggered:

1. **Test website rendering**: The full website is rendered to check that no errors
   occur. This action should already have been run successfully for the pull
   request that implemented the changes. Nevertheless, merging could also introduce
   new issues.
2. **Update notebook copies**: A script is run to make copies of all tutorial
   notebooks with all output removed. The filenames of these copies are prepended with
   an underscore and should be used to open the notebooks interactively, e.g., in
   Google Colab.
3. **Publish website**: Quarto is used to render the static website, which is then
   force-pushed to the [ProteomicsML/proteomicsml.github.io](https://github.com/ProteomicsML/proteomicsml.github.io)
   repository. This repository is served on [proteomicsml.org](https://www.proteomicsml.org/)
   through GitHub Pages.
