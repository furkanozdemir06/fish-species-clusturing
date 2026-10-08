# 🐟 Fish Species Clustering

An unsupervised machine learning project that groups fish based on their **physical characteristics** using K-Means clustering.

## 📌 Project Overview

The project includes:

- Exploratory Data Analysis
- Correlation analysis
- Feature scaling
- K-Means clustering
- Elbow Method
- Silhouette Score evaluation
- Cluster visualization

## 📊 Dataset

The dataset contains:

```text
4,080 rows
9 fish species
```

Main clustering features:

- `length`
- `weight`
- `w_l_ratio`

No missing values are reported.

## 🤖 Clustering

The project uses **K-Means** with standardized numerical features.

Best silhouette result:

```text
k = 3
Silhouette Score ≈ 0.633
```

The Elbow Method is then used to select:

```text
k = 4
```

for the final clustering model.

## 📈 Analysis

The notebook includes:

- Species distribution
- Length vs. weight analysis
- Correlation heatmap
- Elbow Method
- Silhouette comparison
- Final cluster visualization

## 🛠️ Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- K-Means
- StandardScaler
- Matplotlib
- Seaborn
- Yellowbrick
- Jupyter Notebook

## 🎯 Skills Demonstrated

- Unsupervised Learning
- K-Means Clustering
- Feature Scaling
- Cluster Evaluation
- Exploratory Data Analysis
- Data Visualization

---

Built with Python and Scikit-learn. 🐟📊
