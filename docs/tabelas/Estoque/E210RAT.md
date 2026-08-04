# E210RAT

## Descrição

Estoques - Rateios dos Movimentos

---

## Resumo

- Campos: 26
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto movimentado |
| CodDer | String(007) | Não | Código da derivação do produto movimentado |
| CodDep | String(010) | Não | Código do depósito movimentado |
| DatMov | Date | Não | Data da movimentação do estoque |
| SeqMov | Number(006,0) | Não | Sequência de movimento na data de movimentação |
| SeqRat | Number(004,0) | Não | Sequência do rateio do movimento |
| CodTns | String(005) | Sim | Código da transação |
| CodFil | Number(005,0) | Sim | Código da filial |
| MesAno | Date | Sim | Mês e ano de competência |
| CriRat | Number(001,0) | Não | Critério utilizado para rateio |
| SomSub | Number(001,0) | Não | Somar ou subtrair o valor no plano financeiro/centro de custos |
| NumPrj | Number(008,0) | Sim | Número do projeto |
| CodFpj | Number(004,0) | Sim | Código da fase do projeto |
| CtaFin | Number(007,0) | Sim | Conta financeira reduzida |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida |
| PerCta | Number(007,4) | Sim | Percentual rateado para a conta |
| VlrCta | Number(015,2) | Sim | Valor rateado para a conta |
| CodCcu | String(009) | Sim | Código do centro de custos |
| PerRat | Number(007,4) | Sim | Percentual rateado para o centro de custos |
| VlrRat | Number(015,2) | Sim | Valor rateado para o centro de custos |
| ObsRat | String(120) | Sim | Observação do rateio |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| TipOri | String(001) | Sim | Origem do Rateio |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- CodDep
- DatMov
- SeqMov
- SeqRat

---

## Índices

### E210RATIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- MesAno
- NumPrj
- CodFpj
- CtaFin

---

## Relacionamentos

### IR_E210RAT_005

**Tabela:** E210MVP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |
| CodDep | CodDep |
| DatMov | DatMov |
| SeqMov | SeqMov |

