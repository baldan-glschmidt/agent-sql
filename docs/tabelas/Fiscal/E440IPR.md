# E440IPR

## Descrição

Compras - Notas Fiscais de Entrada - Itens de Produto - Reforma tributária

---

## Resumo

- Campos: 24
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| SeqIpc | Number(003,0) | Não | Sequência do item na nota fiscal de entrada |
| IdeScr | Number(009,0) | Não | Identificador do cClassTrib |
| IdeLsf | Number(009,0) | Sim | Identificador de ligacão do cClassTrib |
| CodImp | String(003) | Não | Código do imposto |
| BasCal | Number(015,4) | Sim | Base Cálculo |
| AliImp | Number(007,4) | Sim | Percentual da Alíquota |
| PerDif | Number(007,4) | Sim | Percentual de Diferimento |
| VlrDif | Number(013,2) | Sim | Valor Diferimento |
| PerRed | Number(007,4) | Sim | Percentual de Redução |
| AliEfe | Number(007,4) | Sim | Alíquota Efetiva |
| IdeStr | Number(009,0) | Sim | cClassTrib de Trib. Regular caso não cumprida condição resolutiva/suspensiva |
| PerDes | Number(007,4) | Sim | Percentual de Tributação Regular |
| VlrDes | Number(013,2) | Sim | Valor de Tributação Regular |
| VlrImp | Number(013,2) | Sim | Valor Imposto |
| CodPci | String(003) | Sim | Código Interno |
| PerPci | Number(008,4) | Sim | Percentual do crédito presumido |
| VlrPci | Number(013,2) | Sim | Valor do crédito presumido |
| ConSus | String(001) | Sim | Crédito presumido em condição suspensiva |
| DedCre | String(001) | Sim | Deduz o valor do crédito presumido do valor total |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqIpc
- CodImp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440IPR_005

**Tabela:** E440IPC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |
| SeqIpc | SeqIpc |

### IR_E440IPR_006

**Tabela:** E027SCR

| Origem | Destino |
|--------|---------|
| IdeScr | IdeUni |

