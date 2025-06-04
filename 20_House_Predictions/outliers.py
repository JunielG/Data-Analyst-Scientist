values_index = [738, 635, 420, 747, 1190, 1340, 1350, 581, 1061, 1298, 523, 898, 1182, 322, 934, 249, 313, 
               335, 451, 706, 1396, 378, 691, 185, 583, 297]
values_id = [739, 636, 421, 748, 1191, 1341, 1351, 582, 1062, 1299, 524, 899, 1183, 323, 935, 250, 314, 336,
            452, 707, 1397, 379, 692, 186, 584, 298]

# Drop index 691, 1182
#train_df.query('GarageArea >= 800 & SalePrice >= 700000')
# Drop index 523, 1298
#train_df.query('GrLivArea >= 4000 & SalePrice <= 300000')
# Drop index 297
#train_df.query('MasVnrArea >= 1200 & SalePrice <= 300000')
# Drop index 185, 583 
#train_df.query('YearBuilt <= 1920 & SalePrice >= 300000')
# Drop index 1182
# train_df.query('OverallCond == 5 & SalePrice >= 700000')
# Drop index 691
#train_df.query('OverallCond == 6 & SalePrice >= 600000')
# Drop index 378
# train_df.query('OverallCond == 2 & SalePrice >= 300000')
# Drop index 738
# train_df.query('BsmtFullBath == 3')
# train_df.query('LotArea >= 55000')
# Drop index 635
# train_df.query('BedroomAbvGr == 8') 
# train_df.query('GarageCars >= 3.5 & SalePrice <= 300000')
# Drop index 581, 1061, 1190, 1298
# train_df.query('GarageArea >= 1200 & SalePrice <= 300000')
# Drop index 523, 1298
# train_df.query('OverallQual >= 10 & SalePrice <= 300000') 
# Drop index 523, 1298
# train_df.query('`1stFlrSF` >= 3000 & SalePrice <= 300000')
# Drop index 898, 1182
# train_df.query('BsmtUnfSF <= 500 & SalePrice >= 600000')
# Drop index 322
# train_df.query('BsmtFinSF2 >= 1200 & SalePrice <= 400000')
# Drop index 1298
# train_df.query('BsmtFinSF1 >= 3000 & SalePrice <= 200000') 
# Drop this values index 934, 1298
# train_df.query('LotFrontage >= 300')
# stats.zscore(l['LotArea'].sort_values(ascending=True))
# Drop index 523, 1298
# train_df.query('TotalBsmtSF >= 4000 & SalePrice <= 200000') 

train_df = train_df[train_df.Id.isin(values_id) == False]

outliers = train_df.query("LandContour == 'Lvl' & SalePrice >= 282000")
train_df = train_df[train_df.Id.isin(outliers.Id) == False] 