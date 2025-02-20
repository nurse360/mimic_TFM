import gradio as gr
import joblib
from ml_model.predictions import predict_multi_label_proba, get_shap_values_with_features
import ml_model.columns as mlc
import pandas as pd
import numpy as np
import plotly.express as px

# Cargar los modelos binarios
loaded_models = joblib.load("ml_model/xgb_binary_models_per_label.pkl")

pruebas = mlc.pruebas

# función de Gradio que recibe datos y devuelva predicciones + shap
def diagnose(edad, sexo, estado_civil, numero_diagnosticos, pruebas_anomalias):
    paciente = pd.DataFrame(0, index=range(1), columns=mlc.names)

    paciente["edad"] = int(edad)
    paciente["sexo"] = int(sexo)
    paciente["estado_civil_WIDOWED"] = int(estado_civil)
    paciente["estado_civil_SINGLE"] = int(estado_civil == 0)
    paciente["num_diagnosticos"] = int(numero_diagnosticos)

    paciente[[pruebas_anomalias]] = 1

    proba_dict = predict_multi_label_proba(loaded_models, paciente)

    proba_json = {k: v.tolist() if isinstance(v, np.ndarray) else v for k, v in proba_dict.items()}
    df_patologies = dict_to_table(proba_dict, columns=["Patología", "Riesgo(%)"])

    best_model = loaded_models[df_patologies["Patología"].iloc[0]]
    shap_dict = get_shap_values_with_features(best_model, paciente)

    # Ordenamos los items del diccionario por su valor (de mayor a menor) y tomamos los 5 primeros
    risk_factors = sorted_risk_factors(shap_dict, 5)
    df_risk_factors = pd.DataFrame(risk_factors.keys(), columns=["Factores"])

    barplot_patologies = create_barplot_data(proba_json, 30)
    # Crear la figura Plotly
    fig = create_plotly_figure(barplot_patologies)

    # Truncar caarcteres para que se vea parte del diagnostico en el dataframe
    df_patologies["Patología"] = df_patologies["Patología"].str[:60]+"..."

    return fig, df_patologies, df_risk_factors


def sorted_risk_factors(shap_dict, top_n=10):
    return dict(sorted(shap_dict.items(), key=lambda x: x[1], reverse=True)[:top_n])


def dict_to_table(prob_dict, columns):
    data = []
    for label, arr in prob_dict.items():
        # arr es una lista con un solo valor [0.1860...]
        value = float(arr[0])*100
        data.append([label, value])
    df = pd.DataFrame(data, columns=columns)

    return df.sort_values(by="Riesgo(%)", ascending=False)


def create_plotly_figure(df_barplot):

    fig = px.bar(
        df_barplot,
        x="icd_block",
        y="prob",
        color="icd_block",
        title="Probabilidad de patologías"
    )
    # Ajustar altura y margen inferior
    fig.update_layout(
        height=500,                # Alto total de la figura
        margin=dict(b=150),        # Aumenta margen inferior (b=bottom) para que se vean etiquetas
        xaxis=dict(tickangle=-45)  # Rotar etiquetas X si son largas
    )
    return fig


def create_barplot_data(probabilities_dict, max_chars=10):
    bar_data = []

    for label, value_array in probabilities_dict.items():
        prob_value = float(value_array[0])
        bar_data.append({
            "icd_block": label[:max_chars],
            "prob": prob_value
        })
    df = pd.DataFrame(bar_data)
    return df


with gr.Blocks(theme=gr.themes.Citrus()) as demo:
    with gr.Row():
        with gr.Column(scale=1, min_width=300):
            gr.Markdown("### Datos del paciente")
            edad = gr.Number(value=30, label="Edad", precision=0)
            sexo = gr.Radio(value=0, choices=[("Mujer", 0), ("Hombre", 1)], label="Sexo")
            estado_civil = gr.Radio(value=0, choices=[("Soltero", 0), ("Casado", 1)], label="Estado Civil")
            numero_diagnosticos = gr.Number(value=0, label="Número de Diagnósticos previos", precision=0)

            gr.Markdown("### Selección de pruebas de laboratorio"),
            dropdown_anomalias = gr.Dropdown(
                choices=pruebas,
                label="Pruebas con anomalías",
                multiselect=True,
                info="Pruebas de laboratorio fuera de rangos de normalidad"

            )
            boton_diagnostico = gr.Button("Generar diagnóstico")

        with gr.Column(scale=2, min_width=300):
            gr.Markdown("### Diagnóstico")
            histograma = gr.Plot(label="Riesgo de patologías")
            df_patologies = gr.Dataframe(value=pd.DataFrame(columns=["Patología", "Riesgo(%)"]), label="Patologías de mayor a menor riesgo para este paciente")
            df_risk_factors = gr.Dataframe(value=pd.DataFrame(columns=["Factor"]), label="Top 5 factores de riesgo para este paciente")

    boton_diagnostico.click(
        fn=diagnose,
        inputs=[edad, sexo, estado_civil, numero_diagnosticos, dropdown_anomalias],
        outputs=[histograma, df_patologies, df_risk_factors]
    )


if __name__ == "__main__":
    demo.launch()
