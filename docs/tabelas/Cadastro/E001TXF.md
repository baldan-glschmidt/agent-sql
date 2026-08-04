# E001TXF

## Descrição

Tabelas - Transação - Ligação Transação X Conta Financeira

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTns | String(005) | Não | Código da transação |
| CtaFin | Number(007,0) | Não | Número reduzido da conta financeira |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodTns
- CtaFin

---

## Índices

### E001TXFIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CtaFin

---

## Relacionamentos

### IR_E001TXF_001

**Tabela:** E001TNS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTns | CodTns |

### IR_E001TXF_002

**Tabela:** E091PLF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CtaFin | CtaFin |

