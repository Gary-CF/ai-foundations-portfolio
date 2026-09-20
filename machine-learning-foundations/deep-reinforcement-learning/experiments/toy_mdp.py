"""Deterministic checks for the worked examples; no third-party dependencies.

This is not a training benchmark or a CS285 assignment solution.
"""
import json
import math


def close(actual, expected):
    assert math.isclose(actual, expected, rel_tol=1e-10, abs_tol=1e-10), (actual, expected)


def main():
    gamma = 0.9
    v1 = 0.5 * 3
    v0 = 0.5 * 1 + 0.5 * gamma * v1
    close(v0, 1.175)
    v = [0.0, 0.0]
    path = [v[:]]
    for _ in range(5):
        v = [max(1, gamma * v[1]), 3.0]
        path.append(v[:])
    close(v[0], 2.7)
    mc = gamma * 3
    td = gamma * 1
    close(0.1 * mc, 0.27)
    close(0.1 * td, 0.09)
    delta1 = 3 - 2
    delta0 = 0 + gamma * 2 - 1
    gae = {str(lam): delta0 + gamma * lam * delta1 for lam in [0, 0.5, 1]}
    close(gae['1'], 1.7)
    close(gae['0.5'], 1.25)
    is_value = 0.9 * (0.5 / 0.9) * 1 + 0.1 * (0.5 / 0.1) * 3
    close(is_value, 2)
    p = 0.5
    gradients = [(1-p)*(1-0.5), (0-p)*(0-0.5)]
    close(gradients[0], 0.25)
    close(gradients[1], 0.25)
    def ppo(ratio, advantage):
        return min(ratio * advantage, min(1.2, max(0.8, ratio)) * advantage)
    close(ppo(1.5, 2), 2.4)
    close(ppo(0.5, -2), -1.6)
    close(1 + 0.9 * (2 - 0.2 * -0.5), 2.89)
    tau = 0.8
    expectile = 2 * tau
    close((1-tau) * expectile, tau * (2-expectile))
    # Both policies have full support: E_current[k3] equals exact KL value.
    current, reference = [0.75, 0.25], [0.5, 0.5]
    exact = sum(p * math.log(p / q) for p, q in zip(current, reference))
    k3 = sum(p * (q / p - math.log(q / p) - 1) for p, q in zip(current, reference))
    close(exact, k3)
    # A truncation may bootstrap, but may not propagate next episode's GAE.
    truncated_delta = 0 + gamma * 2 - 1
    close(truncated_delta + gamma * 0.95 * 0 * 999, 0.8)
    print(json.dumps({'status':'passed', 'checks':[
        'exact policy evaluation', 'value iteration', 'MC/TD targets',
        'GAE endpoints and middle value', 'importance sampling',
        'bandit score gradient and baseline', 'PPO positive/negative clipping',
        'SAC target', 'expectile stationarity', 'sample KL identity',
        'truncation versus trace continuation'],
        'value_iteration':path, 'policy_value':v0, 'gae':gae,
        'scope':'worked-example identities only; no deep RL training'}, indent=2))


if __name__ == '__main__':
    main()
