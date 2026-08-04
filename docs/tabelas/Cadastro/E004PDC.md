# E004PDC

## Descrição

Parâmetros - Parametrização Tipo Nota Débito/Crédito - CBS/IBS

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | String(050) | Não | Identificador único alfanumérico |
| CodEmp | Number(004,0) | Não | Código da empresa |
| SigUfs | String(002) | Sim | Sigla do estado para parametrização |
| FinNot | Number(002,0) | Não | Finalidade da nota de débito ou crédito |
| TipNdb | Number(002,0) | Sim | Tipo da nota de débito |
| TipNcr | Number(002,0) | Sim | Tipo da nota de crédito |
| UsaImp | String(001) | Sim | Indica se executa cálculos de impostos via transação |
| UsaFin | String(001) | Sim | Indica se executa movimentação financeira conforme transação |
| UsaEst | String(001) | Sim | Indica se executa movimentação de estoque conforme transação |
| DatIni | Date | Não | Data inicial da vigência da parametrização |
| DatFim | Date | Sim | Data final da vigência da parametrização |

---

## Chave Primária

- IdeUni

---

## Índices

### E004TBSIndice1

**Tipo:** Unico

Campos:
- CodEmp
- SigUfs
- FinNot
- TipNdb
- TipNcr
- DatIni

### E004PDCIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- FinNot

### E004PDCIndice3

**Tipo:** Não unico

Campos:
- CodEmp
- SigUfs

---

## Relacionamentos

Nenhum relacionamento cadastrado.
