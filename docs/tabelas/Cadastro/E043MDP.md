# E043MDP

## Descrição

Controladoria - Gestão de Contabilidade - Transferência de Saldos de Plano de Contas Anterior

---

## Resumo

- Campos: 11
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodMpc | Number(004,0) | Não | Código do modelo de plano origem |
| SeqMpc | Number(006,0) | Não | Sequência de registro |
| DatVal | Date | Não | Data de validade do plano (Até) |
| CtaAnt | Number(009,0) | Não | Código reduzido da conta contábil origem |
| CodMpa | Number(004,0) | Sim | Código do modelo de plano destino |
| CtaAtu | Number(009,0) | Sim | Código reduzido da conta contábil destino |
| VlrIni | Number(015,2) | Sim | Valor do saldo inicial do período |
| IndIni | String(001) | Sim | Indicador da situação do saldo inicial |
| VlrMfu | Number(015,2) | Sim | (Valor do saldo inicial do período em moeda funcional |
| IndMfu | String(001) | Sim | Indicador da situaçãoo do saldo inicial em moeda funcional |

---

## Chave Primária

- CodEmp
- CodMpc
- SeqMpc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E043MDP_001

**Tabela:** E043MPC

| Origem | Destino |
|--------|---------|
| CodMpc | CodMpc |

### IR_E043MDP_005

**Tabela:** E043MPC

| Origem | Destino |
|--------|---------|
| CodMpa | CodMpc |

