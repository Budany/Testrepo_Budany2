材料：lab_jupyter_launch_site_location

学习内容：
巩固用folium产生地图，给地图添加标记

给一个dataframe根据已有列数值新增一列两个方法
方法1先创建一个新的列df['new_column']=''
df.loc[df['old_column']==1, 'new_column'] = 'green'
df.loc[df['old_column']==0, 'new_column'] = 'red'
方法2
def assign_marker_color(outcome):
  if outcome == 1:
    return 'green'
  else:
    return 'red'
df['new_column']=df['old_column'].apply(assign_marker_color)



