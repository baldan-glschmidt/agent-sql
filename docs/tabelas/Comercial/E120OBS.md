# E120OBS

## Descrição

Vendas - Pedidos - Observações

---

## Resumo

- Campos: 30
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| SeqObs | Number(008,0) | Não | Sequência das observações do pedido |
| TipObs | String(001) | Não | Tipo da observação |
| CodMot | Number(006,0) | Sim | Código do motivo da observação |
| ObsPed | String(250) | Não | Texto da observação do pedido |
| ObsUsu | Number(010,0) | Sim | Usuário responsável pela entrada da observação |
| ObsDat | Date | Sim | Data da observação |
| ObsHor | Number(005,0) | Sim | Hora da observação |
| SolObs | String(250) | Sim | Solução dada a observação |
| SolUsu | Number(010,0) | Sim | Responsável pela solução da observação |
| SolDat | Date | Sim | Data da solução da observação |
| SolHor | Number(005,0) | Sim | Hora da solução da observação |
| SitObs | String(001) | Não | Situação da observação |
| AreObs | String(003) | Sim | Área da empresa que gerou a observação |
| AprRpr | String(001) | Sim | Aprovação do Pedido pela Área da empresa que gerou a observação |
| SeqIpd | Number(004,0) | Sim | Sequência de item de produto do pedido que gerou a observação |
| SeqIsp | Number(003,0) | Sim | Sequência do item de serviço do pedido que gerou a observação |
| TipInf | Number(001,0) | Sim | Tipo de Informação |
| USU_itema | Number(003,0) | Sim | Item A |
| USU_itemc | Number(007,0) | Sim | Item C |
| USU_itemb | Number(007,0) | Sim | Item B |
| USU_INDPRD | String(001) | Sim | Indica se será produzido |
| USU_VlrCshBckR | Number(015,5) | Sim | Valor Cashback Retroativo |
| USU_HashSHA256 | String(064) | Sim | Hash gerado pelo sistema que integrou o pedido |
| USU_DatAlt | Date | Sim | Data da última alteração do registro |
| USU_HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| USU_DatGer | Date | Sim | Data da geração do registro |
| USU_HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqObs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E120OBS_002

**Tabela:** E120PED

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |

