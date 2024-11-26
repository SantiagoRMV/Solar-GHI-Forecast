from numpy import nan, select


def tolerance_range(first_dispatch:bool, real:float, gx:float) -> float:
    """
    Estimates the hourly tolerance range for variable generation plants
    for first dispatch and re-dispatch.

    Parameters
    ----------
    first_dispatch : bool
        Whether the tolerance range is estimated for the first dispatch
        (True) or re-dispatch (False).
    real : float
       Real energy accumulated during the 24 periods in units of [MWh].
    gx : float
        First dispatch or re-dispatch energy accumulated during the 24
        periods in units of [MWh].

    Returns
    -------
    hourly_tolerance_range : float
        Hourly deviation tolerance range in units of [dimensionless].
    """
    deviation = abs(gx - real) / gx

    if first_dispatch is True:
        conditions = [deviation <= 0.15,
                      (0.15 < deviation) & (deviation < 0.2),
                      (gx == 0.0) & (real != 0.0),
                      deviation >= 0.2]

        choices = [nan,
                   0.25 - deviation,
                   0.05,
                   0.05]
    else:
        conditions = [deviation <= 0.08,
                      (0.08 < deviation) & (deviation < 0.15),
                      (gx == 0.0) & (real != 0.0),
                      deviation >= 0.15]

        choices = [nan,
                   (110/7 - (5/7 * deviation * 100)) / 100,
                   0.05,
                   0.05]

    return select(condlist=conditions, choicelist=choices).item()