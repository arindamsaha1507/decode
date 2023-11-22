"""Module containing the system of ordinary differential equations."""

# pylint: disable=unused-argument


def ode_func(t: float, x: list[float], p: dict[str, float]) -> list[float]:
    """
    Compute the derivatives of the ODE system at time t.

    Parameters:
        t (float): The current time.
        x (list[float]): The current state vector.
        p (dict[str, float]): The parameter values for the ODE system.

    Returns:
        list[float]: The derivatives of the state variables at time t.
    """
    sigma = p["sigma"]
    rho = p["rho"]
    beta = p["beta"]

    dxdt = sigma * (x[1] - x[0])
    dydt = x[0] * (rho - x[0]) - x[1]
    dzdt = x[0] * x[1] - beta * x[2]

    return [dxdt, dydt, dzdt]
