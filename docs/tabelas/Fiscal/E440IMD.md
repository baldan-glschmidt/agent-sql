# E440IMD

## Descrição

Compras - Notas Fiscais de Entrada - Itens de Manifesto Documento Fiscal

---

## Resumo

- Campos: 14
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSma | String(003) | Não | Código da série do manifesto |
| NumMan | Number(009,0) | Não | Número do manifesto |
| SeqImd | Number(003,0) | Não | Sequência do item no manifesto |
| TipNfe | Number(002,0) | Sim | Tipo de nota fiscal de entrada |
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| ChvNel | String(050) | Não | Chave de acesso da nota fiscal eletrônica |
| DatEmi | Date | Não | Data de emissão da nota fiscal de saída |
| PesBru | Number(014,5) | Sim | Peso bruto da nota fiscal de saída |
| Vlrliq | Number(015,2) | Sim | Total líquido da nota fiscal de saída |
| TipInc | String(001) | Não | Tipo de inclusão da nota fiscal |

---

## Chave Primária

- CodEmp
- CodFil
- CodSma
- NumMan
- SeqImd

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440IMD_006

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

### IR_E440IMD_008

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

