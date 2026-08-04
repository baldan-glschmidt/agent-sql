# E440VPS

## Descrição

Compras - Notas Fiscais de Entrada - Valorização - Serviço

---

## Resumo

- Campos: 15
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
| SeqVps | Number(004,0) | Não | Sequência das valorizações para serviço na nota fiscal de entrada |
| SelSer | Number(001,0) | Sim | Indicativo de seleção do serviço |
| CodSer | String(014) | Sim | Código do serviço da nota fiscal de entrada |
| UniMed | String(003) | Sim | Unidade de medida do item da nota fiscal de entrada |
| QtdRec | Number(014,5) | Sim | Quantidade recebida do item da nota fiscal de entrada |
| VlrLiq | Number(015,2) | Sim | Valor líquido do item da nota fiscal de entrada |
| SeqIsc | Number(003,0) | Sim | Sequência do item na nota fiscal de entrada |
| SeqIte | Number(004,0) | Sim | Sequência ligação das valorizações para produto na nota fiscal de entrada |
| CplIsc | String(250) | Sim | Complemento da descrição do serviço |
| CodFam | String(006) | Sim | Código da família do item |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqVps

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440VPS_004

**Tabela:** E440NFC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |

