# E045CSO

## Descrição

Tabelas - Plano Contábil - Eliminações Saldos p/ Consolidação

---

## Resumo

- Campos: 8
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CtaRed | Number(007,0) | Não | Número reduzido da conta contábil |
| EmpEli | Number(004,0) | Não | Código da empresa de eliminação |
| CtaEli | Number(007,0) | Não | Código da conta contábil de eliminação na empresa consolidada |
| EmpCon | Number(004,0) | Não | Código da empresa de contra partida do saldo eliminado |
| CtaCon | Number(007,0) | Não | Código da conta contábil de contra partida do saldo eliminado |
| MesAno | Date | Não | Ano base de referência para eliminação |
| PerEli | Number(011,8) | Não | Percentual sobre o saldo da conta origem a eliminar |

---

## Chave Primária

- CodEmp
- CtaRed
- EmpEli
- CtaEli
- EmpCon
- CtaCon
- MesAno

---

## Índices

### E045CSOIndice1

**Tipo:** Não unico

Campos:
- EmpEli
- CtaEli

---

## Relacionamentos

### IR_E045CSO_001

**Tabela:** E045PLA

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CtaRed | CtaRed |

### IR_E045CSO_003

**Tabela:** E045PLA

| Origem | Destino |
|--------|---------|
| EmpEli | CodEmp |
| CtaEli | CtaRed |

