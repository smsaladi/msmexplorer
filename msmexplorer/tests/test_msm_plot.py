import numpy as np
from msmbuilder.msm import MarkovStateModel, BayesianMarkovStateModel
from matplotlib.axes import SubplotBase
from seaborn.apionly import JointGrid

from ..plots import plot_pop_resids, plot_msm_network, plot_timescales, plot_implied_timescales

rs = np.random.RandomState(42)
data = rs.randint(low=0, high=10, size=100000)
msm = MarkovStateModel()
msm.fit(data)
bmsm = BayesianMarkovStateModel()
bmsm.fit(data)


def test_plot_pop_resids():
    ax = plot_pop_resids(msm)

    assert isinstance(ax, JointGrid)


def test_plot_msm_network():
    ax = plot_msm_network(msm)

    assert isinstance(ax, SubplotBase)


def test_plot_timescales_msm():
    ax = plot_timescales(msm, n_timescales=3, xlabel='x', ylabel='y')

    assert isinstance(ax, SubplotBase)


def test_plot_timescales_bmsm():
    ax = plot_timescales(bmsm)

    assert isinstance(ax, SubplotBase)


def test_plot_implied_timescales():
    lag_times = [1, 50, 100, 250, 500, 1000, 5000]
    msm_objs = []
    for lag in lag_times:
        # Construct MSM
        msm = MarkovStateModel(lag_time=lag, n_timescales=5)
        msm.fit(data)
        msm_objs.append(msm)
    ax = plot_implied_timescales(msm_objs)
    assert isinstance(ax, SubplotBase)
