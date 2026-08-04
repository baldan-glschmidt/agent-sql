# E000NFC_FLT

## Descrição

Tabelas - Recebimento de Documentos Eletrônicos - Notas Fiscais de Entrada - Dados Gerais

---

## Resumo

- Campos: 13
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumInt | String(020) | Não | Número do Documento Externo (Integrado) |
| DatEnt | Date | Sim | Data da Entrada da Nota |
| DatEmi | Date | Sim | Data de emissão da nota fiscal de entrada |
| ObsNfc | String(1000) | Sim | Texto da observação |
| PesBru | Number(021,10) | Sim | Peso bruto da nota fiscal de entrada |
| Vlrliq | Number(015,2) | Sim | Total líquido da nota fiscal de entrada |
| VlrFin | Number(015,2) | Sim | Valor líquido da nota fiscal para o financeiro |
| SeqOrm | Number(005,0) | Sim | Sequência do endereço de origem da mercadoria |
| SitInt | Number(001,0) | Sim | Status da Integração |
| RetInt | String(1000) | Sim | Retorno da Integração |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumInt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
