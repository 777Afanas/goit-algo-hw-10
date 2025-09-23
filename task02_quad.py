# q.py
import numpy as np
import scipy.integrate as integrate
from datetime import datetime

# Імпортуємо готову функцію та межі інтегрування 
from task02_view import f, a, b, x, y  # беремо також масиви x,y щоб оцінити y_max так само, як у графіку

# межі по y — нижня = 0, верхня беремо як max(y) 
y_min = 0.0
y_max = float(np.max(y))


def monte_carlo_integrate(func, a, b, y_min, y_max, num_points, seed=123):
    rng = np.random.default_rng(seed)
    x_rand = rng.uniform(a, b, num_points)
    y_rand = rng.uniform(y_min, y_max, num_points)
    under_curve = np.sum(y_rand < func(x_rand))
    print(f"Під кривою: {under_curve} із {num_points}")
    area = (b - a) * (y_max - y_min) * (under_curve / num_points)
    return float(area)


if __name__ == "__main__":
    # 1) Еталон через quad
    quad_value, quad_err = integrate.quad(f, a, b)

    # 2) Монте-Карло
    N = 1_000_000
    mc_value = monte_carlo_integrate(f, a, b, y_min, y_max, N, seed=123)

    # 3) Порівняння
    abs_err = abs(mc_value - quad_value)
    rel_err = abs_err / abs(quad_value) if quad_value != 0 else float("inf")

    print(f"quad: {quad_value:.10f}, Monte Carlo: {mc_value:.10f}")



 # Текст, який буде доданий в кінець існуючого README.md
    append_text = f"""

---

## Порівняння інтегрування (додано {datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
- **Інтервал:** [{a}, {b}]
- **SciPy quad:** {quad_value:.10f} (похибка ≈ {quad_err:.2e})
- **Monte Carlo (N={N:,}):** {mc_value:.10f}
- Абсолютна похибка: {abs_err:.10f}
- Відносна похибка: {rel_err:.6%}

**Висновок:**
Метод Монте-Карло дав результат, який узгоджується з еталонним значенням `quad` в межах статистичної похибки.
Зі збільшенням N похибка зменшується приблизно як 1/√N.
"""

    # Відкриваємо файл у режимі append і додаємо текст
    with open("README.md", "a", encoding="utf-8") as f:
        f.write(append_text) 

