"""
Implementation of the citation-weighted disruption index of
Bentley, Valverde et al. (2023), Advances in Complex Systems,
Eq. (3):

    mCD5(t) = (1/C_t) * sum_i c_it * CD5(i)

where c_it is the average number of citations per year of focal
paper i (total citations divided by years since publication) and
C_t is the sum of c_it over all papers published in year t.
"""

def compute_bentley_cd_index(df, paper_year_col, paper_cd_col,
                             paper_citations_total_col, max_year):
    df = df[[paper_year_col, paper_cd_col, paper_citations_total_col]]
    df = df.assign(paper_citations_per_year=
                   df[paper_citations_total_col]/(max_year-df[paper_year_col]))
    df = df.assign(cd_X_citations_per_year=
                   df[paper_cd_col]*df["paper_citations_per_year"])
    yearly = df.groupby(paper_year_col).agg(
        r_weighted_cd=("cd_X_citations_per_year", "sum"),
        normalise=("paper_citations_per_year", "sum"),
        cd_mean=(paper_cd_col, "mean"))
    yearly = yearly.assign(r_weighted_cd_norm=
                           yearly.r_weighted_cd/yearly.normalise)
    return yearly
