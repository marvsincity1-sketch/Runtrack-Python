# ============================================================
# JOB 10 — SIMULATION D'UN INVESTISSEMENT FINANCIER
# ============================================================

# ÉTAPE 1 — INVESTISSEMENT INITIAL

capital = 10000
annual_rate = 5

annual_gain = capital * annual_rate / 100

print("===== INVESTISSEMENT INITIAL =====")
print(f"Capital : {capital:.2f} €")
print(f"Taux annuel : {annual_rate} %")
print(f"Gain annuel : {annual_gain:.2f} €")


# ÉTAPE 2 — AJOUT DE CAPITAL ET AUGMENTATION DU TAUX

capital += 5000
annual_rate += 2

annual_gain = capital * annual_rate / 100

print("\n===== APRÈS AUGMENTATION =====")
print(f"Capital : {capital:.2f} €")
print(f"Taux annuel : {annual_rate} %")
print(f"Gain annuel : {annual_gain:.2f} €")


# ÉTAPE 3 — RETRAIT ET DIMINUTION DU TAUX

capital -= capital * 0.10
annual_rate -= 1

annual_gain = capital * annual_rate / 100

print("\n===== APRÈS RETRAIT =====")
print(f"Capital final : {capital:.2f} €")
print(f"Taux annuel : {annual_rate} %")
print(f"Gain annuel final : {annual_gain:.2f} €")