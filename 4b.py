import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files

uploaded = files.upload()
from scipy.stats import norm
uci_diabetes = pd.read_csv("uci_diabetes.csv")
plt.figure(figsize=(12,5))

# Glucose
plt.subplot(1,2,1)
sns.histplot(uci_diabetes["Glucose"], kde=True, stat="density")
x = np.linspace(uci_diabetes["Glucose"].min(), uci_diabetes["Glucose"].max(), 100)
plt.plot(x, norm.pdf(x,
                     uci_diabetes["Glucose"].mean(),
                     uci_diabetes["Glucose"].std()),
         'r', linewidth=2)
plt.title("Normal Curve - Glucose")

# BMI
plt.subplot(1,2,2)
sns.histplot(uci_diabetes["BMI"], kde=True, stat="density")
x = np.linspace(uci_diabetes["BMI"].min(), uci_diabetes["BMI"].max(), 100)
plt.plot(x, norm.pdf(x,
                     uci_diabetes["BMI"].mean(),
                     uci_diabetes["BMI"].std()),
         'r', linewidth=2)
plt.title("Normal Curve - BMI")

plt.tight_layout()
plt.show()
