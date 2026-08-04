# E081FCE

## Descrição

Tabelas - Tabela de Preços de Frete - Preços por Estados/Cidades

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTab | String(004) | Não | Código da tabela de preço frete |
| DatIni | Date | Não | Data início de validade da tabela de preço |
| SigUfs | String(002) | Não | Sigla do estado |
| CepIni | Number(008,0) | Não | Faixa inicial do CEP da cidade |
| VlrFre | Number(015,2) | Não | Valor do Frete |
| PerFre | Number(005,2) | Sim | Percentual Frete |
| VlrMin | Number(015,2) | Sim | Valor mínimo do frete |

---

## Chave Primária

- CodEmp
- CodTab
- DatIni
- SigUfs
- CepIni

---

## Índices

### E081FCEIndice1

**Tipo:** Não unico

Campos:
- SigUfs

---

## Relacionamentos

### IR_E081FCE_002

**Tabela:** E081VFR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTab | CodTab |
| DatIni | DatIni |

### IR_E081FCE_003

**Tabela:** E007UFS

| Origem | Destino |
|--------|---------|
| SigUfs | SigUfs |

