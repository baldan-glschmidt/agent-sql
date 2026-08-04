# E440CMC

## Descrição

Compras - Notas Fiscais de Entrada - Controle de Movimento de Cooperado

---

## Resumo

- Campos: 21
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificação do controle de movimento de cooperado |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| SeqIpc | Number(003,0) | Não | Sequência do item na nota fiscal de entrada |
| MovCoo | String(001) | Sim | Indicativo se o item da nota fiscal de entrada é movimento de cooperado |
| IdePrn | Number(009,0) | Sim | Identificação do cálculo da proporcionalidade do movimento de ato cooperado |
| TipNfe | Number(002,0) | Sim | Tipo de nota fiscal de entrada |
| DatEnt | Date | Sim | Data de entrada da nota fiscal de entrada |
| TnsPro | String(005) | Sim | Transação de produto do item da nota |
| CodPro | String(014) | Sim | Código do produto da nota fiscal de entrada |
| CodDer | String(007) | Sim | Código da derivação do produto da nota fiscal de entrada |
| QtdRec | Number(014,5) | Sim | Quantidade recebida do item da nota fiscal de entrada |
| VlrBru | Number(015,2) | Sim | Valor bruto do item da nota fiscal de entrada |
| VlrLiq | Number(015,2) | Sim | Valor líquido do item da nota fiscal de entrada |
| SitNfc | String(001) | Não | Situação da nota fiscal de entrada |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E440CMCIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqIpc

---

## Relacionamentos

### IR_E440CMC_006

**Tabela:** E440IPC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |
| SeqIpc | SeqIpc |

