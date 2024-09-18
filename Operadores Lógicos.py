## Operadores aritméticos
produto_1 = 20
produto_2 = 10

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

x = (10 + 5) * 4
y = (10 / 2) + 25 * ((2 - 2) ** 2)
print(x)
print(y)

## Operadores de comparação
saldo = 200
saque = 200

print(saldo == saque)
print(saldo != saque)
print(saldo > saque)
print(saldo >= saque)
print(saldo < saque)
print(saldo <= saque)

## Operadores de atribuição
saldo = 500
print(saldo)

saldo = 200
print(saldo)

saldo += 10
print(saldo)

saldo -= 5
print(saldo)

saldo //= 2
print(saldo)

saldo /= 2
print(saldo)

saldo *= 10
print(saldo)

saldo %= 4
print(saldo)

saldo **= 2
print(saldo)

## Operadores Lógicos
# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True

print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True or True)
print(True or False or False)
print(False or False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)

## Operadores de identidade
saldo = 1000
limite = 1000

print(saldo is limite)
print(saldo is not limite)

## Operadores de associação
frutas = ["limao", "uva"]
curso = "Curso de python"

print("laranja" not in frutas)
print("limao" in frutas)
print("Python" in curso)