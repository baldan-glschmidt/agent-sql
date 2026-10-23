# R088MOD

## Descrição

Modelos de Veículo

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| MarVei | String(015) | Não | Marca do Veículo |
| ModVei | String(015) | Não | Modelo do Veículo |
| PerInd | Number(005,2) | Sim | Percentual de Realização do Índice (Valor gasto por Km rodado) |
| ApeMod | String(030) | Sim | Apelido do Modelo de Veículo |
| QtdPas | Number(003,0) | Sim | Quantidade de Passageiros |
| TipMVe | Number(001,0) | Sim | Tipo de Veículo |
| CapTan | Number(003,0) | Sim | Capacidade do Tanque(Litros) |
| PotMod | Number(003,0) | Sim | Potência(CV) |
| CusKrd | Number(008,2) | Sim | Valor do Custo por Km Rodado |

---

## Chave Primária

- MarVei
- ModVei

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088MOD_000

**Tabela:** R088MAR

| Origem | Destino |
|--------|---------|
| MarVei | MarVei |

