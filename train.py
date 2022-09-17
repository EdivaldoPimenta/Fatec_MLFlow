# Databricks notebook source
# DBTITLE 1,Imports
from sklearn import tree
from sklearn import model_selection
from sklearn import linear_model
from sklearn import ensemble
from sklearn import metrics

import mlflow

# COMMAND ----------

# DBTITLE 1,Dados
print("Obtendo dados...")

df = spark.table("sandbox_apoiadores.abt_dota_pre_match").toPandas()
df


# COMMAND ----------

# DBTITLE 1,Setup do experimento
exp_name = "/Users/di27pimenta@gmail.com/fatec_dota_Edivaldo"
mlflow.set_experiment(exp_name)

# COMMAND ----------

# DBTITLE 1,Definições de colunas
target = "radiant_win"
id_column = "match_id"

features = list(set(df.columns) - set ([target, id_column]))

# COMMAND ----------

# DBTITLE 1,Split de dados
X_train, X_tese, y_train, y_test = model_selection.train_test_split(df[features],df[target], test_size=0.2, random_state=42)

# COMMAND ----------

print("Geral: ",df[target].mean())
print("Treino: ", y_train.mean())
print("Teste: ", y_test.mean())
