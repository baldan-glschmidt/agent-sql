# E032MRF

## Descrição

Cadastros - Financeiras - Motivos de retorno

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFin | Number(004,0) | Não | Código da financeira |
| NumSeq | Number(004,0) | Não | Número sequencial do registro |
| CodMot | String(007) | Sim | Código do motivo de retorno da financeira |
| DscMot | String(100) | Sim | Descrição do motivo de retorno da financeira |

---

## Chave Primária

- CodEmp
- CodFin
- NumSeq

---

## Índices

### E032MRFIndice1

**Tipo:** Não unico

Campos:
- CodEmp

---

## Relacionamentos

### IR_E032MRF_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

