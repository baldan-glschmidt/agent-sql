# E020AID

## Descrição

Tabelas - Séries de Notas Fiscais - Autorização para Impressão de Documentos Fiscais

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| SeqSnf | Number(004,0) | Não | Seqüência da autorização para impressão de documentos fiscais |
| NumNfi | Number(009,0) | Não | Nº Inicial da seqüência de notas fiscais para a AIDF |
| NumNff | Number(009,0) | Não | Nº final da seqüência de notas fiscais para a AIDF |
| NumAid | String(015) | Não | Número da autorização para impressão de documentos fiscais |
| CodGra | Number(009,0) | Sim | Código da gráfica de geração dos formulários |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- SeqSnf

---

## Índices

### E020AIDIndice2

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodSnf
- NumNfi
- NumNff

---

## Relacionamentos

### IR_E020AID_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

