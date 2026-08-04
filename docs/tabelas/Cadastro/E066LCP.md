# E066LCP

## Descrição

Integrações - Varejo - Ligação Forma x Condição

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFpg | Number(002,0) | Não | Código da forma de pagamento |
| CodCpg | String(006) | Não | Código da condição de pagamento |
| SitReg | String(001) | Não | Situação do registro |
| ResDsc | String(001) | Sim | Indicativo de aplicação da restrição do percentual de desconto no uso desta condição |
| MaxDsc | Number(005,2) | Sim | Percentual máximo permitido de desconto para uso na venda com esta condição |

---

## Chave Primária

- CodEmp
- CodFil
- CodCpg
- CodFpg

---

## Índices

### E066LCPIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodCpg

---

## Relacionamentos

### IR_E066LCP_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E066LCP_003

**Tabela:** E028CPG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCpg | CodCpg |

