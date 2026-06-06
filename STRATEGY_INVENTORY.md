# Vectorbt Strategy Inventory

Active import-safe optimization strategies in `vectorbt_strategies`.

- Total active strategies: 100
- Original cleaned strategies: 40
- Added batch 1: 40
- Added batch 2: 20
- Shared starting capital: `DEFAULT_INIT_CASH = 100_000`
- Strategy contract: `optimize_strategy(data, optimize_for="total_return_pct")`

| # | Strategy | File | Category | Status | Concept |
|---:|---|---|---|---|---|
| 1 | `adaptive_ema_volatility_opt` | `adaptive_ema_volatility_opt.py` | Volatility / Regime | Added batch 2 | Adaptive Ema Volatility |
| 2 | `adaptive_momentum_squeeze_opt` | `adaptive_momentum_squeeze_opt.py` | Trend / Momentum | Existing | Adaptive Momentum Squeeze |
| 3 | `adaptive_vortex_trend_opt` | `adaptive_vortex_trend_opt.py` | Trend / Momentum | Existing | Adaptive Vortex Trend |
| 4 | `adx_range_trend_filter_opt` | `adx_range_trend_filter_opt.py` | Trend / Momentum | Existing | Adx Range Trend Filter |
| 5 | `anchored_vwap_trend_opt` | `anchored_vwap_trend_opt.py` | Trend / Momentum | Added batch 1 | Anchored Vwap Trend |
| 6 | `aroon_trend_opt` | `aroon_trend_opt.py` | Trend / Momentum | Added batch 2 | Aroon Trend |
| 7 | `atr_channel_reversion_opt` | `atr_channel_reversion_opt.py` | Mean Reversion | Added batch 1 | Atr Channel Reversion |
| 8 | `atr_percentile_trend_opt` | `atr_percentile_trend_opt.py` | Breakout / Channel | Added batch 2 | Atr Percentile Trend |
| 9 | `autocorrelation_momentum_opt` | `autocorrelation_momentum_opt.py` | Trend / Momentum | Added batch 1 | Autocorrelation Momentum |
| 10 | `awesome_oscillator_divergence_opt` | `awesome_oscillator_divergence_opt.py` | Trend / Momentum | Existing | Awesome Oscillator Divergence |
| 11 | `body_range_strength_opt` | `body_range_strength_opt.py` | Trend / Momentum | Added batch 2 | Body Range Strength |
| 12 | `bollinger_bandwidth_expansion_opt` | `bollinger_bandwidth_expansion_opt.py` | Trend / Momentum | Added batch 2 | Bollinger Bandwidth Expansion |
| 13 | `bollinger_regime_adaptive_opt` | `bollinger_regime_adaptive_opt.py` | Regime Filter | Existing | Bollinger Regime Adaptive |
| 14 | `bollinger_squeeze_breakout_opt` | `bollinger_squeeze_breakout_opt.py` | Breakout / Channel | Existing | Bollinger Squeeze Breakout |
| 15 | `cci_trend_pullback_opt` | `cci_trend_pullback_opt.py` | Trend / Momentum | Added batch 1 | Cci Trend Pullback |
| 16 | `chaikin_money_flow_trend_opt` | `chaikin_money_flow_trend_opt.py` | Volume / Flow | Added batch 1 | Chaikin Money Flow Trend |
| 17 | `chandelier_exit_breakout_opt` | `chandelier_exit_breakout_opt.py` | Breakout / Channel | Added batch 1 | Chandelier Exit Breakout |
| 18 | `coppock_curve_opt` | `coppock_curve_opt.py` | Trend / Momentum | Added batch 1 | Coppock Curve |
| 19 | `decision_tree_ema_ml_opt` | `decision_tree_ema_ml_opt.py` | Machine Learning | Existing | Decision Tree Ema Ml |
| 20 | `dema_macd_trend_opt` | `dema_macd_trend_opt.py` | Trend / Momentum | Added batch 1 | Dema Macd Trend |
| 21 | `donchian_breakout_opt` | `donchian_breakout_opt.py` | Breakout / Channel | Existing | Donchian Breakout |
| 22 | `donchian_midline_reversion_opt` | `donchian_midline_reversion_opt.py` | Mean Reversion | Added batch 1 | Donchian Midline Reversion |
| 23 | `drawdown_recovery_opt` | `drawdown_recovery_opt.py` | Mean Reversion | Added batch 2 | Drawdown Recovery |
| 24 | `elder_ray_trend_opt` | `elder_ray_trend_opt.py` | Trend / Momentum | Added batch 1 | Elder Ray Trend |
| 25 | `ema_adx_cross_opt` | `ema_adx_cross_opt.py` | Trend / Momentum | Existing | Ema Adx Cross |
| 26 | `ema_atr_adx_opt` | `ema_atr_adx_opt.py` | Volatility / Regime | Existing | Ema Atr Adx |
| 27 | `ema_cross_bb_width_filter_opt` | `ema_cross_bb_width_filter_opt.py` | Trend / Momentum | Existing | Ema Cross Bb Width Filter |
| 28 | `ema_cross_resistance_breakouts_opt` | `ema_cross_resistance_breakouts_opt.py` | Breakout / Channel | Existing | Ema Cross Resistance Breakouts |
| 29 | `ema_cross_with_sizing_and_stop_opt` | `ema_cross_with_sizing_and_stop_opt.py` | Trend / Momentum | Existing | Ema Cross With Sizing And Stop |
| 30 | `ema_ppo_volume_trend_opt` | `ema_ppo_volume_trend_opt.py` | Volume / Flow | Existing | Ema Ppo Volume Trend |
| 31 | `ema_stop_target_grid_opt` | `ema_stop_target_grid_opt.py` | Trend / Momentum | Existing | Ema Stop Target Grid |
| 32 | `entropy_volatility_regime_opt` | `entropy_volatility_regime_opt.py` | Volatility / Regime | Added batch 1 | Entropy Volatility Regime |
| 33 | `fisher_transform_reversal_opt` | `fisher_transform_reversal_opt.py` | Mean Reversion | Added batch 2 | Fisher Transform Reversal |
| 34 | `force_index_momentum_opt` | `force_index_momentum_opt.py` | Volume / Flow | Added batch 1 | Force Index Momentum |
| 35 | `fractal_breakout_opt` | `fractal_breakout_opt.py` | Breakout / Channel | Added batch 1 | Fractal Breakout |
| 36 | `gap_reversal_opt` | `gap_reversal_opt.py` | Mean Reversion | Added batch 1 | Gap Reversal |
| 37 | `gmm_regime_filter_opt` | `gmm_regime_filter_opt.py` | Regime Filter | Existing | Gmm Regime Filter |
| 38 | `hammer_candle_reversal_opt` | `hammer_candle_reversal_opt.py` | Mean Reversion | Added batch 2 | Hammer Candle Reversal |
| 39 | `heikin_ashi_trend_opt` | `heikin_ashi_trend_opt.py` | Trend / Momentum | Existing | Heikin Ashi Trend |
| 40 | `hilbert_bollinger_stop_target_opt` | `hilbert_bollinger_stop_target_opt.py` | Trend / Momentum | Existing | Hilbert Bollinger Stop Target |
| 41 | `hma_trend_following_opt` | `hma_trend_following_opt.py` | Trend / Momentum | Added batch 1 | Hma Trend Following |
| 42 | `hurst_regime_ema_cross_opt` | `hurst_regime_ema_cross_opt.py` | Regime Filter | Existing | Hurst Regime Ema Cross |
| 43 | `ichimoku_cloud_opt` | `ichimoku_cloud_opt.py` | Trend / Momentum | Existing | Ichimoku Cloud |
| 44 | `inside_bar_breakout_opt` | `inside_bar_breakout_opt.py` | Breakout / Channel | Added batch 1 | Inside Bar Breakout |
| 45 | `intraday_volatility_breakout_opt` | `intraday_volatility_breakout_opt.py` | Breakout / Channel | Existing | Intraday Volatility Breakout |
| 46 | `kama_trend_pullback_opt` | `kama_trend_pullback_opt.py` | Trend / Momentum | Added batch 1 | Kama Trend Pullback |
| 47 | `keltner_breakout_trend_opt` | `keltner_breakout_trend_opt.py` | Breakout / Channel | Added batch 1 | Keltner Breakout Trend |
| 48 | `keltner_mean_reversion_opt` | `keltner_mean_reversion_opt.py` | Mean Reversion | Existing | Keltner Mean Reversion |
| 49 | `kst_momentum_opt` | `kst_momentum_opt.py` | Trend / Momentum | Added batch 2 | Kst Momentum |
| 50 | `linear_regression_slope_opt` | `linear_regression_slope_opt.py` | Trend / Momentum | Added batch 1 | Linear Regression Slope |
| 51 | `ma_envelope_reversion_opt` | `ma_envelope_reversion_opt.py` | Mean Reversion | Added batch 2 | Ma Envelope Reversion |
| 52 | `macd_histogram_reversal_opt` | `macd_histogram_reversal_opt.py` | Trend / Momentum | Added batch 1 | Macd Histogram Reversal |
| 53 | `macd_trend_opt` | `macd_trend_opt.py` | Trend / Momentum | Existing | Macd Trend |
| 54 | `median_breakout_filter_opt` | `median_breakout_filter_opt.py` | Breakout / Channel | Added batch 2 | Median Breakout Filter |
| 55 | `mfi_volume_reversion_opt` | `mfi_volume_reversion_opt.py` | Mean Reversion | Added batch 1 | Mfi Volume Reversion |
| 56 | `micro_pullback_breakout_opt` | `micro_pullback_breakout_opt.py` | Breakout / Channel | Added batch 2 | Micro Pullback Breakout |
| 57 | `momentum_atr_trailing_stop_opt` | `momentum_atr_trailing_stop_opt.py` | Volatility / Regime | Existing | Momentum Atr Trailing Stop |
| 58 | `moving_average_crossover_grid_opt` | `moving_average_crossover_grid_opt.py` | Trend / Momentum | Existing | Moving Average Crossover Grid |
| 59 | `moving_average_slope_stop_opt` | `moving_average_slope_stop_opt.py` | Trend / Momentum | Existing | Moving Average Slope Stop |
| 60 | `n_day_high_low_stop_opt` | `n_day_high_low_stop_opt.py` | Breakout / Channel | Added batch 1 | N Day High Low Stop |
| 61 | `obv_momentum_stop_target_opt` | `obv_momentum_stop_target_opt.py` | Volume / Flow | Existing | Obv Momentum Stop Target |
| 62 | `open_close_momentum_opt` | `open_close_momentum_opt.py` | Trend / Momentum | Added batch 1 | Open Close Momentum |
| 63 | `outside_bar_reversal_opt` | `outside_bar_reversal_opt.py` | Trend / Momentum | Added batch 1 | Outside Bar Reversal |
| 64 | `percentile_channel_breakout_opt` | `percentile_channel_breakout_opt.py` | Breakout / Channel | Added batch 1 | Percentile Channel Breakout |
| 65 | `pivot_range_breakout_opt` | `pivot_range_breakout_opt.py` | Breakout / Channel | Added batch 2 | Pivot Range Breakout |
| 66 | `pivot_stochastic_atr_opt` | `pivot_stochastic_atr_opt.py` | Mean Reversion | Existing | Pivot Stochastic Atr |
| 67 | `ppo_signal_cross_opt` | `ppo_signal_cross_opt.py` | Trend / Momentum | Added batch 1 | Ppo Signal Cross |
| 68 | `price_efficiency_ratio_opt` | `price_efficiency_ratio_opt.py` | Trend / Momentum | Added batch 2 | Price Efficiency Ratio |
| 69 | `price_volume_surge_opt` | `price_volume_surge_opt.py` | Volume / Flow | Added batch 2 | Price Volume Surge |
| 70 | `quantile_mean_reversion_opt` | `quantile_mean_reversion_opt.py` | Mean Reversion | Added batch 1 | Quantile Mean Reversion |
| 71 | `range_expansion_close_opt` | `range_expansion_close_opt.py` | Breakout / Channel | Added batch 1 | Range Expansion Close |
| 72 | `realized_volatility_breakout_opt` | `realized_volatility_breakout_opt.py` | Breakout / Channel | Added batch 1 | Realized Volatility Breakout |
| 73 | `regime_switching_trend_opt` | `regime_switching_trend_opt.py` | Regime Filter | Existing | Regime Switching Trend |
| 74 | `return_percentile_momentum_opt` | `return_percentile_momentum_opt.py` | Breakout / Channel | Added batch 2 | Return Percentile Momentum |
| 75 | `roc_acceleration_opt` | `roc_acceleration_opt.py` | Trend / Momentum | Added batch 1 | Roc Acceleration |
| 76 | `rolling_skew_reversion_opt` | `rolling_skew_reversion_opt.py` | Mean Reversion | Added batch 2 | Rolling Skew Reversion |
| 77 | `rsi_bollinger_reversion_opt` | `rsi_bollinger_reversion_opt.py` | Mean Reversion | Added batch 1 | Rsi Bollinger Reversion |
| 78 | `rsi_mean_reversion_opt` | `rsi_mean_reversion_opt.py` | Mean Reversion | Existing | Rsi Mean Reversion |
| 79 | `rsi_trend_confirmation_opt` | `rsi_trend_confirmation_opt.py` | Mean Reversion | Added batch 1 | Rsi Trend Confirmation |
| 80 | `stochastic_rsi_reversal_opt` | `stochastic_rsi_reversal_opt.py` | Mean Reversion | Added batch 1 | Stochastic Rsi Reversal |
| 81 | `stochastic_trend_opt` | `stochastic_trend_opt.py` | Mean Reversion | Existing | Stochastic Trend |
| 82 | `supertrend_atr_opt` | `supertrend_atr_opt.py` | Volatility / Regime | Added batch 1 | Supertrend Atr |
| 83 | `tema_crossover_atr_stop_opt` | `tema_crossover_atr_stop_opt.py` | Volatility / Regime | Added batch 1 | Tema Crossover Atr Stop |
| 84 | `trend_momentum_volume_rsi_opt` | `trend_momentum_volume_rsi_opt.py` | Mean Reversion | Existing | Trend Momentum Volume Rsi |
| 85 | `trend_strength_volatility_breakout_opt` | `trend_strength_volatility_breakout_opt.py` | Breakout / Channel | Existing | Trend Strength Volatility Breakout |
| 86 | `trend_volatility_breakout_opt` | `trend_volatility_breakout_opt.py` | Breakout / Channel | Existing | Trend Volatility Breakout |
| 87 | `triple_ema_sl_tp_opt` | `triple_ema_sl_tp_opt.py` | Trend / Momentum | Existing | Triple Ema Sl Tp |
| 88 | `tsi_momentum_opt` | `tsi_momentum_opt.py` | Trend / Momentum | Added batch 1 | Tsi Momentum |
| 89 | `ulcer_index_recovery_opt` | `ulcer_index_recovery_opt.py` | Mean Reversion | Added batch 2 | Ulcer Index Recovery |
| 90 | `ultimate_oscillator_trend_opt` | `ultimate_oscillator_trend_opt.py` | Trend / Momentum | Existing | Ultimate Oscillator Trend |
| 91 | `vol_cluster_reversion_opt` | `vol_cluster_reversion_opt.py` | Mean Reversion | Existing | Vol Cluster Reversion |
| 92 | `volatility_contraction_expansion_opt` | `volatility_contraction_expansion_opt.py` | Volatility / Regime | Added batch 1 | Volatility Contraction Expansion |
| 93 | `volatility_cooling_atr_opt` | `volatility_cooling_atr_opt.py` | Volatility / Regime | Existing | Volatility Cooling Atr |
| 94 | `volatility_scaled_breakout_opt` | `volatility_scaled_breakout_opt.py` | Breakout / Channel | Existing | Volatility Scaled Breakout |
| 95 | `volume_dryup_breakout_opt` | `volume_dryup_breakout_opt.py` | Breakout / Channel | Added batch 2 | Volume Dryup Breakout |
| 96 | `volume_price_trend_opt` | `volume_price_trend_opt.py` | Volume / Flow | Added batch 1 | Volume Price Trend |
| 97 | `vortex_cross_trend_opt` | `vortex_cross_trend_opt.py` | Trend / Momentum | Added batch 2 | Vortex Cross Trend |
| 98 | `vwap_deviation_reversion_opt` | `vwap_deviation_reversion_opt.py` | Mean Reversion | Added batch 1 | Vwap Deviation Reversion |
| 99 | `williams_r_breakout_opt` | `williams_r_breakout_opt.py` | Breakout / Channel | Added batch 1 | Williams R Breakout |
| 100 | `zscore_mean_reversion_opt` | `zscore_mean_reversion_opt.py` | Mean Reversion | Existing | Zscore Mean Reversion |
