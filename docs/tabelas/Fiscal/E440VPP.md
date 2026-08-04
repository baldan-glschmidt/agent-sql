# E440VPP

## Descrição

Compras - Notas Fiscais de Entrada - Valorização - Produto

---

## Resumo

- Campos: 17
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| SeqVpp | Number(004,0) | Não | Sequência das valorizações para produto na nota fiscal de entrada |
| SelPro | Number(001,0) | Sim | Indicativo de seleção do produto |
| CodPro | String(014) | Sim | Código do produto da nota fiscal de entrada |
| CodDer | String(007) | Sim | Código da derivação do produto da nota fiscal de entrada |
| UniMed | String(003) | Sim | Unidade de medida de estoque do item da nota fiscal de entrada |
| QtdRec | Number(014,5) | Sim | Quantidade recebida do item da nota fiscal de entrada |
| VlrLiq | Number(015,2) | Sim | Valor líquido do item da nota fiscal de entrada |
| SeqIpc | Number(003,0) | Sim | Sequência do item na nota fiscal de entrada |
| SeqIte | Number(004,0) | Sim | Sequência ligação das valorizações para produto na nota fiscal de entrada |
| CplIpc | String(250) | Sim | Complemento da descrição do produto |
| PreMed | Number(021,10) | Sim | Preço médio do item na nota fiscal de entrada |
| CodFam | String(006) | Sim | Código da família do produto |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqVpp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440VPP_004

**Tabela:** E440NFC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |

