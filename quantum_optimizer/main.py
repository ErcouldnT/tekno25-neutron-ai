import json
from qiskit_aer.primitives import Sampler as AerSampler
# from qiskit_aer import Aer
from qiskit_algorithms.utils import algorithm_globals

from qiskit.algorithms.minimum_eigensolvers import QAOA
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit_optimization.problems import QuadraticProgram
from qiskit.algorithms.optimizers import COBYLA

# 0. Veriyi dosyadan al
with open("data.json") as f:
    data = json.load(f)

# 1. Sabit seed
algorithm_globals.random_seed = 42

# 2. Optimizasyon problemi tanımı
problem = QuadraticProgram()
problem.binary_var('bor')        # x: bor yoğunluğu (0=düşük, 1=yüksek)
problem.binary_var('temp')       # y: sıcaklık (0=düşük, 1=yüksek)
problem.binary_var('neutron')    # z: nötron akısı (0=normal, 1=yüksek)

# 3. Maliyet fonksiyonu (minimize edilecek)
problem.minimize(
    linear=data["linear"],
    quadratic={tuple(eval(k)): v for k, v in data["quadratic"].items()}
)

# 4. QAOA kur
optimizer = COBYLA()
sampler = AerSampler()
sampler.options.shots = 512
qaoa = QAOA(optimizer=optimizer, sampler=sampler, reps=2)

# 5. Çözümle
meo = MinimumEigenOptimizer(qaoa)
result = meo.solve(problem)

# 6. Sonuç
print("\n🧠 Optimal Settings for Reactor (Binary Form):")
print("bor (0=low, 1=high)     :", int(result.x[0]))
print("temp (0=low, 1=high)    :", int(result.x[1]))
print("neutron (0=low, 1=high) :", int(result.x[2]))
print("Minimum cost (risk score):", result.fval)
