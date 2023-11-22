"""Module containing the system of ordinary differential equations."""

# pylint: disable=unused-argument


def ode_func(t: float, x: list, p: dict) -> list:
    """
    Evaluates the system of ODEs at time t and state x with parameters p.
    """
    dxdt = p["sigma"] * (x[1] - x[0])
    dydt = x[0] * (p["rho"] - x[0]) - x[1]
    dzdt = x[0] * x[1] - p["beta"] * x[2]
    return [dxdt, dydt, dzdt]
