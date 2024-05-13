def ttest(df, label):

    e_types = df[label].unique()
    ttests = []

    for col in df:
        for i, e in enumerate(e_types):
            for i2, e2 in enumerate(e_types):
                if not col == label:
                    if pd.api.types.is_numeric_dtype(df[col]):
                        if i2 > i:
                            g1 = df[df[label] == e][col]
                            g2 = df[df[label] == e2][col]
                            t, p = ttest_ind(g1, g2)
                
                            ttests.append({'features': col, 'T-Statistic': t.round(4), 'P-Value': p.round(4)})

    return pd.DataFrame(ttests)

ttest(df, 'smoker')
