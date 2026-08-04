# E140ISR

## Descrição

Vendas - Notas Fiscais de Saída - Itens de Serviço - Reforma tributária

---

## Resumo

- Campos: 26
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa da nota fiscal de saída |
| CodFil | Number(005,0) | Não | Código da filial da nota fiscal de saída |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqIsv | Number(003,0) | Não | Sequência do item de serviço da nota fiscal de saída |
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
| PerRcg | Number(008,4) | Sim | Percentual redutor de compra governamental |
| PerCgo | Number(008,4) | Sim | Percentual de compra governamental |
| VlrCgo | Number(013,2) | Sim | Valor de compra governamental |
| DedCre | String(001) | Sim | Deduz o valor do crédito presumido do valor total |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqIsv
- CodImp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140ISR_004

**Tabela:** E140ISV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |
| SeqIsv | SeqIsv |

### IR_E140ISR_005

**Tabela:** E027SCR

| Origem | Destino |
|--------|---------|
| IdeScr | IdeUni |

