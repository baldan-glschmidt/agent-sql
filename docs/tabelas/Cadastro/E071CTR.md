# E071CTR

## Descrição

Tabelas - Royalties - Contratos

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CtrRoy | Number(004,0) | Não | Número do Contrato de Royalties |
| DesCtr | String(040) | Não | Descrição do Contrato de Royalties |
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| DatIni | Date | Não | Data de Início de vigência do contrato |
| DatFim | Date | Não | Data Final de Vigência do Contrato |

---

## Chave Primária

- CodEmp
- CtrRoy

---

## Índices

### E071CTRIndice1

**Tipo:** Não unico

Campos:
- CodFor

---

## Relacionamentos

### IR_E071CTR_003

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

