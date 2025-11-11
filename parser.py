@given(x=x_arrays(min_size=4))
@settings(max_examples=500)
def test_cumulative_monotonicity_nonnegative(x):
    y = np.abs(np.random.randn(len(x)))  # Non-negative values

    cum_simp = integrate.cumulative_simpson(y, x=x, initial=0)

    assert all(cum_simp[i] <= cum_simp[i+1] for i in range(len(cum_simp)-1)), \
        f"Simpson cumulative not monotonic for non-negative function"