# E045CSO_HIS

## Descrição

Tabelas - Histórico - Plano Contábil - Eliminações Saldos p/ Consolidação

---

## Resumo

- Campos: 8
- Chave Primária: 7 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodMpc | Number(004,0) | Não | Código do modelo de plano |
| CtaRed | Number(007,0) | Não | Número reduzido da conta contábil |
| EmpEli | Number(004,0) | Não | Código da empresa de eliminação |
| CtaEli | Number(007,0) | Não | Código da conta contábil de eliminação na empresa consolidada |
| EmpCon | Number(004,0) | Não | Código da empresa de contra partida do saldo eliminado |
| MesAno | Date | Não | Ano base de referência para eliminação |
| PerEli | Number(011,8) | Não | Percentual sobre o saldo da conta origem a eliminar |

---

## Chave Primária

- CodEmp
- CodMpc
- CtaRed
- EmpEli
- CtaEli
- EmpCon
- MesAno

---

## Índices

### E045CSO_HISIndice1

**Tipo:** Não unico

Campos:
- CodMpc

### E045CSO_HISIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodMpc
- CtaEli

---

## Relacionamentos

### IR_E045CSO_HIS_001

**Tabela:** E043MPC

| Origem | Destino |
|--------|---------|
| CodMpc | CodMpc |

### IR_E045CSO_HIS_004

**Tabela:** E045PLA_HIS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMpc | CodMpc |
| CtaEli | CtaRed |

