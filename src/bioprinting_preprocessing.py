
from __future__ import annotations

import inspect
from collections.abc import Sequence

import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import MissingIndicator, SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def _simple_imputer(
    *,
    strategy: str,
    fill_value=None,
    add_indicator: bool = False,
) -> SimpleImputer:
    """Create a version-compatible SimpleImputer."""

    parameters = {
        "strategy": strategy,
        "add_indicator": add_indicator,
    }

    if fill_value is not None:
        parameters["fill_value"] = fill_value

    signature = inspect.signature(
        SimpleImputer
    )

    if (
        "keep_empty_features"
        in signature.parameters
    ):
        parameters[
            "keep_empty_features"
        ] = True

    return SimpleImputer(
        **parameters
    )


def _one_hot_encoder() -> OneHotEncoder:
    """Create a version-compatible sparse one-hot encoder."""

    parameters = {
        "handle_unknown": "ignore",
        "dtype": np.float64,
    }

    signature = inspect.signature(
        OneHotEncoder
    )

    if (
        "sparse_output"
        in signature.parameters
    ):
        parameters[
            "sparse_output"
        ] = True
    else:
        parameters[
            "sparse"
        ] = True

    return OneHotEncoder(
        **parameters
    )


def build_preprocessor(
    numeric_features: Sequence[str],
    categorical_features: Sequence[str],
    *,
    scale_numeric: bool,
) -> ColumnTransformer:
    """
    Build a leakage-safe preprocessing transformer.

    Numerical values:
      1. Median imputation fitted on training data only.
      2. Optional standardization fitted on training data only.
      3. One missingness indicator for every numerical feature.

    Categorical values:
      1. Constant missing-category imputation.
      2. One-hot encoding fitted on training data only.
      3. Unknown test categories are ignored safely.
      4. One missingness indicator for every categorical feature.

    No source identifiers, outcomes, clipping, feature selection,
    or publication information are added by this function.
    """

    numeric_features = list(
        numeric_features
    )

    categorical_features = list(
        categorical_features
    )

    if (
        not numeric_features
        and not categorical_features
    ):
        raise ValueError(
            "At least one feature is required."
        )

    transformers = []

    if numeric_features:

        numeric_steps = [
            (
                "median_imputer",
                _simple_imputer(
                    strategy="median",
                ),
            ),
        ]

        if scale_numeric:

            numeric_steps.append(
                (
                    "standard_scaler",
                    StandardScaler(),
                )
            )

        transformers.append(
            (
                "numeric_values",
                Pipeline(
                    numeric_steps
                ),
                numeric_features,
            )
        )

        transformers.append(
            (
                "numeric_missing_indicators",
                MissingIndicator(
                    features="all",
                    error_on_new=False,
                ),
                numeric_features,
            )
        )

    if categorical_features:

        categorical_pipeline = Pipeline(
            [
                (
                    "missing_category_imputer",
                    _simple_imputer(
                        strategy="constant",
                        fill_value="__MISSING__",
                    ),
                ),
                (
                    "one_hot_encoder",
                    _one_hot_encoder(),
                ),
            ]
        )

        transformers.append(
            (
                "categorical_values",
                categorical_pipeline,
                categorical_features,
            )
        )

        transformers.append(
            (
                "categorical_missing_indicators",
                MissingIndicator(
                    features="all",
                    error_on_new=False,
                ),
                categorical_features,
            )
        )

    return ColumnTransformer(
        transformers=transformers,
        remainder="drop",
        sparse_threshold=0.30,
        verbose_feature_names_out=True,
    )
