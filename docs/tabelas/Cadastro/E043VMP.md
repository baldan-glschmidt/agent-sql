# E043VMP

## Descrição

Tabelas - Modelos de Planos - Períodos de Validade dos Modelos de Planos

---

## Resumo

- Campos: 4
- Chave Primária: 0 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodMpc | Number(004,0) | Não | Código do modelo de plano |
| DatIni | Date | Não | Data inicial do período |
| DatFim | Date | Não | Data final do período |

---

## Chave Primária

Não possui.

---

## Índices

### E043VMPindice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodMpc

### E043VMPIndice2

**Tipo:** Não unico

Campos:
- CodMpc

---

## Relacionamentos

### IR_E043VMP_001

**Tabela:** E043MPC

| Origem | Destino |
|--------|---------|
| CodMpc | CodMpc |

