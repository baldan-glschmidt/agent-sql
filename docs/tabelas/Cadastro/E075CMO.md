# E075CMO

## Descrição

Tributos - Notas Fiscais de Entrada Matéria Prima - INOVAR-AUTO

---

## Resumo

- Campos: 17
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeCmo | Number(009,0) | Não | Identificação |
| SeqNfe | Number(009,0) | Não | Sequencial |
| IdeMon | Number(009,0) | Não | Identificação Montadora |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Sim | Código da derivação |
| CodIns | String(014) | Não | Código do produto |
| DerIns | String(007) | Sim | Código da derivação |
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| NumNfi | Number(009,0) | Não | Numero NF |
| DatEnt | Date | Não | Data da entrada |
| QtdEnt | Number(014,5) | Sim | Quantidade de compra matéria prima |
| CstIcm | String(003) | Sim | Situação Tributária ICMS |
| VlrCtb | Number(015,2) | Sim | Valor contábil |
| VlrIpi | Number(015,2) | Sim | Valor do IPI |
| VlrIim | Number(015,2) | Sim | Soma dos valores do imposto de importação dos itens da nota fiscal de saída |
| ParDed | Number(015,2) | Sim | Parcela dedutível |
| TipNfe | Number(002,0) | Não | Tipo Nota Fiscal |

---

## Chave Primária

- IdeCmo
- SeqNfe

---

## Índices

### E075CMOIndice1

**Tipo:** Não unico

Campos:
- IdeMon

---

## Relacionamentos

### IR_E075CMO_002

**Tabela:** E075MON

| Origem | Destino |
|--------|---------|
| IdeMon | IdeMon |

