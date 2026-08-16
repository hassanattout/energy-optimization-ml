import sys
from pathlib import Path

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from generate_data import generate_dataset
from optimize import apply_peak_shaving


def test_dataset_generation_is_reproducible():
    first = generate_dataset(seed=42, days=2)
    second = generate_dataset(seed=42, days=2)
    pd.testing.assert_frame_equal(first, second)


def test_peak_shaving_reduces_peak_and_preserves_energy():
    df = generate_dataset(seed=42, days=7)
    optimized, metrics = apply_peak_shaving(df)

    assert metrics["peak_after"] < metrics["peak_before"]
    assert metrics["peak_reduction_percent"] > 0
    assert metrics["energy_balance_error"] == pytest.approx(0.0)
    assert len(optimized) == len(df)
