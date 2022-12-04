# Tradeoff mapping equations and further detail

There are five different ways of calculating multiple service opportunities in the current version of Nature Braid:

- Equally weighted arithmetic
- Conservative
- Standard
- Weighted additive
- A combined "conservative and weighted additive" approach

For input into the tadeoff mapping, each service (*TS<sub>i</sub>*) takes a value of -1, 0, or 1

| Value | Meaning |
|--------------|-----------|
| -1 | Anticipated losses arising with change |
| 0 | No significant losses or gains associated with change |
| -1 | Gains ("wins") anticipated with change |

In the cases of both arithmetic and the standard calculations, both continuous and categorised tradeoff quantifications are calculated. In the case of the conservative and combined conservative/additive approaches, the calculations are by their nature categorised (ordinal) by definition.

For all the definitions following:
- *NonCat_OTS*: represents a normalised, continuous quantification
- *Cat_OTS*: the categorised (generally 5-way) value used for display

## Arithmetic calculations

The generic equation defining the arithmetic multiple criteria opportunity mapping is (Equation 1):

$$ NonCat_OTS = {\sum_{i=1}^{N} w_i TS_i \over \sum_{i=1}^{N} w_i} $$

where *N* represents the number of services being analysed and *w_i* represents the weights assigned to each service. 

In the case of equal weighting between all services (the equally weighted arithmetic option”, Equation 1 simplifies to (Equation 2):

$$ NonCat_OTS = {\sum_{i=1}^{N} TS_i \over N} $$

In "English", another way to think of Equation 2 is:

$$ NonCat_OTS = {wins_i - losses_i \over wins_i + losses_i + nochange_i} $$

Where:
- $wins_i$: Number of wins
- $losses_i$: Number of losses
- $nochange_i$: Number of "no change"

Using default user settings, the categorisation for either Equation 1 or 2 then proceeds as follows to define values for mapping:

| if-else | NonCat_OTS | Cat_OTS | Standard colour map |
|---|---|---|---|
| if | NonCat_OTS > 0.6 | Cat_OTS = 2 | Red |
| elseif | NonCat_OTS ∈ \[0.2, 0.6] | Cat_OTS = 1 | Orange |
| elseif | NonCat_OTS ∈ \[-0.2, 0.6] | Cat_OTS = 0 | Yellow |
| elseif | NonCat_OTS ∈ \[-0.6, -0.3] | Cat_OTS = -1 | Light green |
| elseif | NonCat_OTS < 0.6 | Cat_OTS = -2 | Dark green |

If users wish to change these fractional thresholds, this can be done by editing the TCT (tradeoff categorisation threshold) values in *user_settings.py*. The values must be є \[-1,1], TC1 and TC2 must be positive, and TC3 and TC4 must be negative. In this case, the categorisation for Equation 1 or Equation 2 is achieved by:

| if-else | NonCat_OTS | Cat_OTS | Standard colour map |
|---|---|---|---|
| if | NonCat_OTS > TCT1 | Cat_OTS = 2 | Red |
| elseif | NonCat_OTS ∈ \[TCT2, TCT1] | Cat_OTS = 1 | Orange |
| elseif | NonCat_OTS ∈ \[TCT3, TCT2] | Cat_OTS = 0 | Yellow |
| elseif | NonCat_OTS ∈ \[TCT4, TCT3] | Cat_OTS = -1 | Light green |
| elseif | NonCat_OTS < TCT4 | Cat_OTS = -2 | Dark green |

### Conservative valuation calculation

| if-else | Equation | Overall value |
|---|---|---|
| if | ${\sum_{i=1}^{N} (TS_i = - 1)}$  <= -2 | -2 |
| elseif | ${\sum_{i=1}^{N} (TS_i = - 1)}$  = -1 | -1 |
| elseif | ${\sum_{i=1}^{N} (TS_i = - 1)}$  = 0 | ${\sum_{i=1}^{N} (TS_i = - 1) \over N}$ |

## Analysis of the number of overall combinations versus number of individual combinations

The number of possible combinations is $3^N$ where *N* is the number of services being considered, which inflates very rapidly as the number of services increase. Summary combinations inflate less rapidly, but still quickly pose an issue for analysis.

Number of tradeoffs being considered:
| | 2 | 3 | 4 | 5 | 6 | 7 | 8 | N |
|---|---|---|---|---|---|---|---|---|
| Number of individual combinations | 9 | 27 | 81 | 243 | 729 | 2187 | 6581 | $3^N$ |
| Summary combinations | 6 | 10 | 15 | 21 | 28 | 36 | 45 | ${\sum_{i=1}^{N+1} i}$ |

More generally, if the number of categories considered in each individual service changes to C, the number of individual combinations is C to the power of N. This clearly inflates even more rapidly as C increases, as demonstrated in the following table:
