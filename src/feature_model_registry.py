
from __future__ import annotations

from typing import Any

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import ElasticNet, Ridge
from sklearn.svm import SVR


def build_feature_estimator(
    model_key: str,
    random_state: int,
):
    """Construct an unfitted locked estimator."""

    if model_key == "ridge":

        return Ridge(
            alpha=1.0,
            solver="lsqr",
            fit_intercept=True,
        )

    if model_key == "elastic_net":

        return ElasticNet(
            alpha=0.1,
            l1_ratio=0.5,
            fit_intercept=True,
            max_iter=50000,
            tol=1.0e-4,
            selection="cyclic",
            random_state=random_state,
        )

    if model_key == "random_forest":

        return RandomForestRegressor(
            n_estimators=300,
            max_depth=None,
            min_samples_leaf=1,
            max_features="sqrt",
            bootstrap=True,
            n_jobs=-1,
            random_state=random_state,
        )

    if model_key == "rbf_svr":

        return SVR(
            kernel="rbf",
            C=10.0,
            epsilon=0.1,
            gamma="scale",
            cache_size=1000,
        )

    raise KeyError(
        f"Unknown model key: {model_key}"
    )


def prefixed_model_parameters(
    parameters: dict[str, Any],
) -> dict[str, Any]:
    """Prefix parameters for a Pipeline model step."""

    return {
        f"model__{key}": value
        for key, value
        in parameters.items()
    }
