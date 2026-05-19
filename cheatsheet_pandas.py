

# merge
df.merge(df2, left_on='ticker', right_on='symbol', how='left')
df.merge(df2, on=['date', 'ticker'], how='inner')
df.merge(df2, on='ticker', suffixes=('_px', '_vol'))


# groupby


# agg：每个ticker一行，共3行
df.groupby('ticker')['return'].agg('mean')
# ticker
# AAPL    0.025
# GOOG    0.015
# MSFT    0.010

# transform：结果与原df等长，5行，每行填入该ticker的组内均值
df['group_mean'] = df.groupby('ticker')['return'].transform('mean')
#   ticker  return  group_mean
# 0   AAPL    0.02       0.025
# 1   AAPL    0.03       0.025
# 2   GOOG   -0.01       0.015
# 3   GOOG    0.04       0.015
# 4   MSFT    0.01       0.010




# pivot, pivot_table
weights_daily = weights_with_attribute.groupby(['date', atrribute])['weight'].sum().reset_index()
weights_pivot = weights_daily.pivot(index='date', columns=atrribute, values='weight').fillna(0)

## AAPL 在同一天出现两次
## ValueError: Index contains duplicate entries, cannot reshape
df.pivot(index='date', columns='ticker', values='ret')

## pivot_table：重复了就聚合，默认取均值
df.pivot_table(index='date', columns='ticker', values='ret')


# melt
row_sums = weights_pivot.sum(axis=1)
weights_pivot = weights_pivot.div(row_sums, axis=0).fillna(0)

weights_long = weights_pivot.reset_index().melt(
    id_vars='date',
    var_name=atrribute,
    value_name='weight'
)





# concat
pd.concat([df1, df2])  ## append rows
pd.concat([df1, df2], axis=1)  ## append columns


# clip
s = pd.Series([-5, 1, 2, 50, 3, 100])
s.clip(lower=0, upper=10)


# cut：等距切（区间宽度相同，每组样本量可能不同）
pd.cut(s, bins=4)
pd.cut(s, bins=[0, 25, 50, 75, 100], labels=['低', '中', '中高', '高'])

df['price_bucket'] = pd.cut(df['price'],
                             bins=[70, 90, 100, 110, 140],
                             labels=['<90', '90-100', '100-110', '>110'])
df.groupby('price_bucket')['volume'].sum()

# qcut
s = pd.Series([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
pd.qcut(s, q=4, labels=['Q1','Q2','Q3','Q4'])
df['factor_group'] = pd.qcut(df['factor'], q=5, labels=[1,2,3,4,5])


# rank
s = pd.Series([30, 10, 20, 10, 40])
s.rank()

df['factor_rank'] = df.groupby('date')['factor'].rank(pct=True)

# 组合用法：rank + clip 做双重处理
df['factor_clean'] = (
    df.groupby('date')['factor']
      .transform(lambda x: x.rank(pct=True))  # 截面排名
      .clip(0.05, 0.95)                         # 去掉极端分位
)


# rolling
s.rolling(window=3, min_periods=1).mean()
df['ret_a'].rolling(60).corr(df['ret_b'])
df['ret'].rolling(20).apply(lambda x: pd.Series(x).skew())


# expanding
df['cummax']   = df['price'].expanding().max()



df['factor_clean'] = (
    df.groupby('date')['factor']
      .transform(lambda x: x.clip(x.quantile(0.05), x.quantile(0.95)))  # ① winsorize
      .fillna(df.groupby('date')['factor'].transform('median'))           # ② 填充NaN
      .pipe(lambda x: x.groupby(df['date']).transform(                    # ③ 截面zscore
          lambda g: (g - g.mean()) / g.std()))
)


df['factor_clean'] = (
    df.groupby('date')['factor']
      .transform(lambda x: x.clip(x.quantile(0.05), x.quantile(0.95)))  # ① winsorize
      .fillna(df.groupby('date')['factor'].transform('median'))           # ② 填NaN
      .pipe(lambda x: x.groupby(df['date']).transform(                    # ③ 截面rank
          lambda g: g.rank(pct=True)))
      .pipe(lambda x: x.groupby(df['date']).transform(                    # ④ 截面zscore
          lambda g: (g - g.mean()) / g.std()))
)


# pipe
# df) 写成 df.pipe(f)
# 价值在于链式调用时保持代码可读性