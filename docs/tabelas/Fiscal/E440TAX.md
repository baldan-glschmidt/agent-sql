# E440TAX

## Descrição

Compras - Notas Fiscais de Entrada - Itens de Produtos - Taxas

---

## Resumo

- Campos: 34
- Chave Primária: 10 campo(s)
- Índices: 0
- Relacionamentos: 6

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| SeqIpc | Number(003,0) | Não | Sequência do item na nota fiscal de entrada |
| CodItx | Number(004,0) | Não | Código do item de taxa |
| TipPtx | Number(001,0) | Não | Tipo da taxa |
| DatIni | Date | Não | Data Inicial da Vigência |
| DatFim | Date | Não | Data Final da Vigência |
| VlrPtx | Number(018,5) | Sim | Valor da taxa para os tipos (1-Valor e 2-Valor por Peso) |
| PerPtx | Number(007,4) | Sim | Percentual da taxa para o tipo (3-Percentual) |
| DiaCar | Number(004,0) | Sim | Dias de carência |
| DiaPrd | Number(004,0) | Sim | Dias de periodicidade |
| AplPtx | Number(001,0) | Não | Aplicação da taxa |
| VlrTax | Number(015,2) | Sim | Valor da taxa calculado |
| CodTcc | String(003) | Sim | Código do tipo de conta |
| AplTcc | Number(002,0) | Sim | Aplicação do tipo da conta |
| NfcPro | Number(009,0) | Sim | Número da nota fiscal do produtor |
| IndVcr | String(001) | Não | Indicativo se o valor da taxa foi calculado por regra do usuário |
| IndVau | String(001) | Não | Indicativo se o valor da taxa foi alterado pelo usuário |
| IndGtt | String(001) | Não | Indicativo se gera título de taxa |
| FilTax | Number(005,0) | Sim | Código da filial do título gerado |
| NumTax | String(010) | Sim | Número do título gerado |
| TptTax | String(003) | Sim | Tipo de título da taxa gerado |
| TnsTax | String(005) | Sim | Código da transação do título gerado |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| DatAtu | Date | Sim | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Sim | Hora/minuto da última atualização do cadastro |
| QtdTax | Number(014,5) | Sim | Quantidade de taxa descontada em produto |
| IndTpr | String(001) | Sim | Indicativo se gera taxa em produto |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqIpc
- CodItx
- TipPtx
- DatIni
- DatFim

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440TAX_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E440TAX_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E440TAX_002

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

### IR_E440TAX_003

**Tabela:** E440NFC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |

### IR_E440TAX_005

**Tabela:** E440IPC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |
| SeqIpc | SeqIpc |

### IR_E440TAX_006

**Tabela:** E113ITX

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodItx | CodItx |

