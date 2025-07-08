import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# 讀取資料
df = pd.read_csv('raw_data/Salary_dataset.csv')
df.drop(columns=['Unnamed: 0'], inplace=True)

# 特徵與標籤
x = df[['YearsExperience']]
y = df[['Salary']]

# 切分資料集
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 訓練模型
model = LinearRegression()
model.fit(x_train, y_train)

# 訓練集預測與評估
y_train_pred = model.predict(x_train)
print("Training R²:", r2_score(y_train, y_train_pred))
print("Training MSE:", mean_squared_error(y_train, y_train_pred))

# ✅ 視覺化資料分佈與回歸線
plt.figure(figsize=(8, 6))
plt.scatter(x_train, y_train, color='blue', label='Training data')  # 原始資料點
plt.plot(x_train, y_train_pred, color='red', linewidth=2, label='Regression line')  # 回歸線
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary vs. Experience (Training Set)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()