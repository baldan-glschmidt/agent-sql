# E071ROY

## Descrição

Tabelas - Royalties

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
| CodEmp | Number(004,0) | Não | Empresa |
| CodRoy | Number(004,0) | Não | Código do Royalty |
| DesRoy | String(040) | Não | Descrição do Royalty |
| CtrRoy | Number(004,0) | Não | Contrato do Royalty |
| PerCom | Number(005,2) | Sim | Percentual Comercial |
| PerCus | Number(004,2) | Sim | Percentual de Custos |

---

## Chave Primária

- CodEmp
- CodRoy

---

## Índices

### E071ROYIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CtrRoy

---

## Relacionamentos

### IR_E071ROY_003

**Tabela:** E071CTR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CtrRoy | CtrRoy |

