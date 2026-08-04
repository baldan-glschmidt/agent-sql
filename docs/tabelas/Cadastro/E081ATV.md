# E081ATV

## Descrição

Tabelas - Atributos da Venda - Dados Gerais

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdcAtv | Number(009,0) | Não | Índice do atributo da venda |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodAtv | String(017) | Não | Código do atributo da venda |
| DesAtv | String(060) | Sim | Descrição completa do atributo da venda |
| AbrAtv | String(010) | Sim | Descrição abreviada do atributo da venda |
| DatIni | Date | Sim | Data da validade inicial |
| DatFin | Date | Sim | Data da validade final |
| IndAcu | String(001) | Sim | Indicativo se o atributo é acumulativo |
| ObsAtv | String(250) | Sim | Observação do atributo |
| SitAtv | String(001) | Não | Situação do registro |

---

## Chave Primária

- IdcAtv

---

## Índices

### E081ATV_UNIQUE

**Tipo:** Unico

Campos:
- CodEmp
- CodAtv

---

## Relacionamentos

### IR_E081ATV_001

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

