# E028NCP

## Descrição

Tabelas - Condição de Pagamento - Controle Alteração Automática

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodCpg | String(006) | Não | Código da condição de pagamento que deve ser alterada |
| NovCpg | String(006) | Não | Código da nova condição de pagamento que deve ser assumida |

---

## Chave Primária

- CodEmp
- CodCpg
- NovCpg

---

## Índices

### E028NCPIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- NovCpg

---

## Relacionamentos

### IR_E028NCP_001

**Tabela:** E028CPG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCpg | CodCpg |

### IR_E028NCP_002

**Tabela:** E028CPG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| NovCpg | CodCpg |

