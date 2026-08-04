# E019VST

## Descrição

Tabelas - Substituições de impostos - Validades

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTst | String(003) | Não | Código do tipo de ICMS Substituído |
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| DatIni | Date | Não | Data início de validade da tabela de substituição de impostos |
| SitReg | String(001) | Não | Situação do registro |

---

## Chave Primária

- CodTst
- CodEmp
- CodFil
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E019VST_000

**Tabela:** E019TST

| Origem | Destino |
|--------|---------|
| CodTst | CodTst |

