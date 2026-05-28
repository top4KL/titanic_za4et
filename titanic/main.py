import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'C:\Users\_top4_KL_\Desktop\titanic.csv')

# числовые признаки
numeric_cols = ['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']

# мтрица корреляции
corr_matrix = data[numeric_cols].corr()

print("Матрица корреляции:") #вывод числовой матрицы
print(corr_matrix.round(3))

# Визуализация с помощью  seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix,
            annot=True,
            cmap='RdBu_r',
            vmin=-1,
            vmax=1,
            center=0,
            fmt='.3f',
            square=True,
            linewidths=0.5)

plt.title('Корреляционная матрица', fontsize = 16)
plt.tight_layout()
plt.savefig('corr_matrix.png', dpi=300, bbox_inches='tight')
plt.show()