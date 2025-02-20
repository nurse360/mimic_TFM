import shap
from .columns import names


def predict_multi_label_proba(loaded_models, X_new):
    predictions_proba = {}
    for label, model in loaded_models.items():
        y_pred_proba_label = model.predict_proba(X_new)[:, 1]
        predictions_proba[label] = y_pred_proba_label
    return predictions_proba


def get_shap_values_with_features(model, X_new):
    shap_dict = {}
    feature_names = names

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_new)  # shape (N, num_features)

    for i in range(shap_values.shape[0]):

        for j, col_name in enumerate(feature_names):
            shap_dict[col_name] = float(shap_values[i, j])

    return shap_dict
