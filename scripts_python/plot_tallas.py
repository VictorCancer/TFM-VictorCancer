import matplotlib.pyplot as plt
import numpy as np

mAP5095 = [71.2,74.4,75.7,76.2,75.7]
speed = [196.1,135.1,74.6,41.8,20.8]


mAP5095_11 = [76.5,77.4,77.6,78.0,78.5]
speed_11 = [212.8,117.6,47.2,36.8,18.1]


talla = ['n','S','M','L','X'] 


colors = {'n': 'red', 'S': 'blue', 'M': 'green','L':'orange','X':'black'}

fig, ax = plt.subplots()

line1, =ax.plot(speed, mAP5095, linestyle='-', color='gray', alpha=0.7, zorder=1)
scatter1 = ax.scatter(speed,mAP5095 , c = [colors[k] for k in talla])

line2, =ax.plot(speed_11, mAP5095_11, linestyle='-', color='blue', alpha=0.7, zorder=1)
scatter2 = ax.scatter(speed_11,mAP5095_11 , c = [colors[k] for k in talla])

scatter_legend_labels = colors.keys()
scatter_legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[label], markersize=10)
                           for label in scatter_legend_labels]


line_handles = [line1, line2]  
line_labels = ['YOLOv5', 'YOLOv11'] 
scatter_handles = scatter_legend_handles
scatter_labels = list(scatter_legend_labels)


legend_labels = colors.keys()
legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[label], markersize=10)
                  for label in legend_labels]


ax.legend(line_handles + scatter_handles, line_labels + scatter_labels,
          title="Modelo / Talla", title_fontproperties={'weight': 'bold'}, loc="lower left")

ax.grid(True, linestyle='--', alpha=0.7,zorder=0)




plt.ylabel('mAP50-95 (%)', fontweight='bold')
plt.xlabel('Velocidad (fps)', fontweight='bold')
plt.title('mAP50-95 vs Velocidad', fontweight='bold')

plt.show()
