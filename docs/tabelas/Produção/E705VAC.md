# E705VAC

## Descrição

Ficha - Modelo - Variações Consumo de Componentes por Derivação

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodMdp | String(008) | Não | Código  da Máscara Derivação |
| CodVac | String(005) | Não | Código da variação p/ utilização no consumo do Modelo |
| DesVac | String(030) | Não | Descrição da variação |
| DerVa1 | String(007) | Não | Código da derivação a partir de |
| DerVa2 | String(007) | Não | Código da derivação até |
| CodFam | String(006) | Sim | Código da família de produto(Opcional) |
| CodFxa | String(015) | Sim | Código da Faixa da Grade |
| CodReg | Number(004,0) | Sim | Código da Regra |

---

## Chave Primária

- CodEmp
- CodMdp
- CodVac

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
