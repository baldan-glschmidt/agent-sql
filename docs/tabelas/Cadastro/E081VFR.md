# E081VFR

## Descrição

Tabelas - Tabela de Preços de Frete - Validades

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTab | String(004) | Não | Código da tabela de preço frete |
| DatIni | Date | Não | Data início de validade da tabela de preço |
| DatFim | Date | Não | Data final de validade da tabela de preço |
| SitReg | String(001) | Não | Situação |
| VlrMin | Number(015,2) | Sim | Valor mínimo do frete |
| VlrDes | Number(015,2) | Sim | Valor do despacho do frete |
| SecCat | Number(015,2) | Sim | Valor do SEC/CAT |
| VlrOut | Number(015,2) | Sim | Valor de outros para frete |

---

## Chave Primária

- CodEmp
- CodTab
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E081VFR_001

**Tabela:** E081TFR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTab | CodTab |

