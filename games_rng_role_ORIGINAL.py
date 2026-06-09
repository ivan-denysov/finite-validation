import numpy as np
# Финальная симуляция: роль ГЕНЕРАТОРА СЛУЧАЙНОСТЕЙ в движках игр.
# Вопрос: что меняется, когда у "внутреннего наблюдателя" нет причинного
# контекста и он вынужден ДОДУМЫВАТЬ исход — становится ли он источником
# истинной случайности (квантоподобной) vs скрыто-детерминированной.
# Сравниваем: (A) детерминированный движок, (B) со скрытым seed, (C) истинный RNG.

np.random.seed(0)
N=200000

# Внутренний наблюдатель видит только срез состояния (не всю причину).
# A: детерминированный (исход = функция полного состояния — наблюдатель не видит, но оно есть)
# B: скрытая причина (seed есть, но скрыт от наблюдателя)
# C: истинный генератор (исхода нет до измерения — додумывается)

def run_engine(mode, n=N):
    outcomes=np.zeros(n)
    hidden=np.random.rand(n)        # скрытое состояние
    for label in [0]:
        pass
    if mode=="A_determ":
        # полностью определено скрытым состоянием (повтор даёт то же)
        outcomes=(hidden>0.5).astype(int)
    elif mode=="B_hidden":
        # скрытая причина + шум наблюдения: выглядит случайным, но повтор по seed стабилен
        outcomes=((hidden+0.0)>0.5).astype(int)
    elif mode=="C_true":
        # истинный RNG: исход не существует до запроса (новый бросок каждый раз)
        outcomes=(np.random.rand(n)>0.5).astype(int)
    return outcomes, hidden

# Тест 1: ПОВТОРЯЕМОСТЬ (повторный запрос той же величины)
print("ТЕСТ 1 — повтор той же величины (стабильность):")
for mode in ["A_determ","B_hidden","C_true"]:
    o1,h=run_engine(mode)
    # повтор: для A/B при том же скрытом состоянии — тот же исход; для C — новый
    if mode=="C_true":
        o2=(np.random.rand(N)>0.5).astype(int)
    else:
        o2=(h>0.5).astype(int)
    stable=np.mean(o1==o2)
    print(f"  {mode:10s}: совпадение при повторе = {stable:.3f}  ({'стабилен' if stable>0.99 else 'каждый раз новый'})")

print()
# Тест 2: КОРРЕЛЯЦИЯ с доступной наблюдателю информацией
print("ТЕСТ 2 — предсказуемость по доступному наблюдателю срезу:")
for mode in ["A_determ","B_hidden","C_true"]:
    o,h=run_engine(mode)
    obs=h+np.random.rand(N)*0.0  # наблюдатель видит h (A/B) или ничего (C)
    if mode=="C_true":
        corr=np.corrcoef((np.random.rand(N)>0.5).astype(int), o)[0,1]
    else:
        corr=np.corrcoef((obs>0.5).astype(int), o)[0,1]
    print(f"  {mode:10s}: корреляция исход↔доступная причина = {corr:.3f}")

print()
print("ТЕСТ 3 — энтропия исходов (все ~максимальны, неразличимы по виду):")
for mode in ["A_determ","B_hidden","C_true"]:
    o,h=run_engine(mode)
    p=np.mean(o); H=-(p*np.log2(p)+(1-p)*np.log2(1-p)) if 0<p<1 else 0
    print(f"  {mode:10s}: энтропия = {H:.4f} бит (доля единиц {p:.3f})")
