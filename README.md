# The Bentley et al. (2023) citation-weighted disruption index, compared

Bentley, Valverde and colleagues (Advances in Complex Systems, 2023) proposed a citation-weighted disruption index, mCD5, and reported that under this measure the decline in disruptiveness documented by Park, Leahey and Funk (Nature, 2023) is not observed. Their paper reports no comparison between the two indices.

This repository contains that comparison. We implement mCD5 exactly as defined in Eq. (3) of the 2023 paper and compute it alongside the original CD index in two publicly available databases.

## Results

| Dataset   | Pearson r (annual series, 1930-2013) | Notes |
|-----------|------|------|
| PubMed    | 0.97 | Bentley et al.'s own analysis file, research articles only |
| SciSciNet | 0.90 | papers with zero recorded references excluded |

In both databases the two indices track each other closely, and the citation-weighted index declines as much as or more than the original. Because the SciSciNet run excludes all zero-reference works, that comparison does not depend on the records at issue in the recent Matters Arising exchange (Holst et al. 2026; Park, Leahey and Funk 2026, both in Nature).

We requested the paper's replication code and data from the authors in February 2024, and R. Alexander Bentley generously shared the original analysis code, which we used to verify this implementation. We shared a written rebuttal containing our assessment with Bentley in January 2025 and invited feedback.

## Method

mCD5(t) = (1/C_t) * sum_i c_it * CD5(i), with c_it computed as total citations divided by years since publication (citations counted through 2023; papers 1930-2013), following Eq. (3) and the citations-per-year construction used in the authors' own code. Pearson correlations are between the annual series of the two indices.

## Data

Both sources are public:
- PubMed / iCite: https://icite.od.nih.gov/ (the input file here follows the research-article file constructed by Bentley et al.)
- SciSciNet: https://doi.org/10.6084/m9.figshare.c.6076908

## Acknowledgment

We thank R. Alexander Bentley for generously sharing the original analysis code on request.

## License

MIT. Contact: Russell J. Funk, rfunk@umn.edu
