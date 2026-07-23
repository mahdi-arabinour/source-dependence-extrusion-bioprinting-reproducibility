
from __future__ import annotations

from typing import Iterable

import numpy as np
import pandas as pd


class TrainingOnlyBaselineRegressor:
    """
    Training-only baseline regressor.

    Supported strategies:
      - global_training_mean
      - global_training_median
      - source_training_mean_with_global_fallback
    """

    def __init__(
        self,
        strategy: str,
    ) -> None:

        supported = {
            "global_training_mean",
            "global_training_median",
            "source_training_mean_with_global_fallback",
        }

        if strategy not in supported:
            raise ValueError(
                f"Unsupported baseline strategy: {strategy}"
            )

        self.strategy = strategy
        self.global_value_: float | None = None
        self.source_means_: dict[str, float] = {}
        self.training_sources_: set[str] = set()
        self.is_fitted_: bool = False

    def fit(
        self,
        y: Iterable[float],
        sources: Iterable[str],
    ) -> "TrainingOnlyBaselineRegressor":

        y_series = pd.Series(
            y,
            dtype=float,
        ).reset_index(drop=True)

        source_series = pd.Series(
            sources,
            dtype="string",
        ).reset_index(drop=True)

        if len(y_series) != len(source_series):
            raise ValueError(
                "Target and source lengths do not match."
            )

        if y_series.isna().any():
            raise ValueError(
                "Training target contains missing values."
            )

        if source_series.isna().any():
            raise ValueError(
                "Training sources contain missing values."
            )

        if self.strategy == "global_training_median":
            self.global_value_ = float(
                y_series.median()
            )
        else:
            self.global_value_ = float(
                y_series.mean()
            )

        self.training_sources_ = set(
            source_series.astype(str)
        )

        if (
            self.strategy
            == "source_training_mean_with_global_fallback"
        ):

            training_frame = pd.DataFrame(
                {
                    "source": (
                        source_series.astype(str)
                    ),
                    "target": y_series,
                }
            )

            self.source_means_ = (
                training_frame
                .groupby("source")[
                    "target"
                ]
                .mean()
                .astype(float)
                .to_dict()
            )

        self.is_fitted_ = True

        return self

    def predict(
        self,
        sources: Iterable[str],
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:

        if not self.is_fitted_:
            raise RuntimeError(
                "The baseline regressor must be fitted first."
            )

        source_series = pd.Series(
            sources,
            dtype="string",
        ).astype(str)

        source_seen = (
            source_series.isin(
                self.training_sources_
            )
            .to_numpy(
                dtype=bool
            )
        )

        if (
            self.strategy
            == "source_training_mean_with_global_fallback"
        ):

            mapped_predictions = (
                source_series
                .map(
                    self.source_means_
                )
            )

            used_fallback = (
                mapped_predictions.isna()
                .to_numpy(
                    dtype=bool
                )
            )

            predictions = (
                mapped_predictions
                .fillna(
                    self.global_value_
                )
                .to_numpy(
                    dtype=float
                )
            )

        else:

            predictions = np.full(
                len(source_series),
                float(
                    self.global_value_
                ),
                dtype=float,
            )

            used_fallback = np.zeros(
                len(source_series),
                dtype=bool,
            )

        return (
            predictions,
            source_seen,
            used_fallback,
        )
