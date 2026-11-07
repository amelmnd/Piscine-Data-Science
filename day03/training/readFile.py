from sklearn.preprocessing import MinMaxScaler, StandardScaler
import matplotlib.pyplot as plt
import sys
import pandas as panda

if len(sys.argv) != 2:
    print("Usage : ./programme.py fichier.csv")
    sys.exit(1)

try:
    df = panda.read_csv(sys.argv[1])
except FileNotFoundError:
    print(f"Fichier introuvable : {sys.argv[1]}")
    sys.exit(1)

features = df.head(10)
data = df.drop(columns="espece")

print(features)

chats = df[df["espece"] == "chat"]
chiens = df[df["espece"] == "chien"]

fig, axes = plt.subplots(2, 2, figsize=(12, 6))   # 2 lignes, 3 colonnes
for ax, colonne in zip(axes.flat, chats):
    ax.hist(chats[colonne], bins=40, alpha=0.5, label="chat", color="orange")
    ax.set_title(colonne)
for ax, colonne in zip(axes.flat, chiens):
    ax.hist(chiens[colonne], bins=40, alpha=0.5, label="chiens", color="green")
    ax.set_title(colonne)

# ransforme espece en 0 (chat) / 1 (chien), puis affiche la corrélation de chaque colonne avec espece, triée de la plus forte à la plus faible.
df["espece"] = df["espece"].map({"chat": 0, "chien": 1})
df.corr()                 # le tableau de toutes les corrélations
df.corr()["poids"]        # la corrélation de chaque colonne avec le poids
# triée, de la plus forte à la plus faible

print(df.corr()["espece"].sort_values(ascending=False))
plt.legend(loc="best")
plt.tight_layout()
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(12, 6))   # 2 lignes, 3 colonnes
axes[0].scatter(chats["poids"], chats["taille"],
                label="chat", color="blue", alpha=0.5)
axes[0].scatter(chiens["poids"], chiens["taille"],
                label="chien", color="red", alpha=0.5)
axes[0].set_xlabel("poids")
axes[0].set_ylabel("taille")
axes[0].legend()

axes[1].scatter(chats["age"], chats["puce"],
                label="chat", color="blue", alpha=0.5)
axes[1].scatter(chiens["age"], chiens["puce"],
                label="chien", color="red", alpha=0.5)
axes[1].set_xlabel("age")
axes[1].set_ylabel("puce")
axes[1].legend()

print("-----------")

X_std = StandardScaler().fit_transform(data)       # un tableau numpy
# pour garder les noms de colonnes
X_std = panda.DataFrame(X_std, columns=data.columns)
print(X_std)

print("-----------")
X_norm = MinMaxScaler().fit_transform(data)
print(X_norm)
plt.show()
