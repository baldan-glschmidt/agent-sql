# R104MTJ

## Descrição

JR - Pedidos - Motivos

---

## Resumo

- Campos: 22
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodMtj | Number(003,0) | Não | Código do motivo do pedido |
| DesMtj | String(050) | Sim | Descrição do motivo do pedido |
| ObsMtj | String(255) | Sim | Observação do motivo do pedido |
| TipUso | String(001) | Sim | Pedido será utilizado na área trabalhista |
| TipVer | Number(002,0) | Sim | Tipo de Verba |
| RegEsp | Number(003,0) | Sim | Regra especial |
| TipOpe | Number(001,0) | Sim | Tipo de Operação do Pedido |
| IncFgt | String(001) | Sim | Incide p/ FGTS Mensal |
| IncIns | String(001) | Sim | Incide p/ INSS Reclamante |
| IncInE | String(001) | Sim | Incide p/ INSS Empresa |
| IncIRF | String(001) | Sim | Incide p/ IRRF |
| RefDSR | Number(003,0) | Sim | Reflexo DSR |
| RefFer | Number(003,0) | Sim | Reflexo Férias |
| Ref13s | Number(003,0) | Sim | Reflexo 13° salário |
| RefAvi | Number(003,0) | Sim | Reflexo Aviso Prévio |
| PerCal | Number(007,4) | Sim | Percentual para uso no cálculo da Hora Extra |
| LanHis | Number(001,0) | Sim | Lançar valores históricos todos os meses ou valerá o vigente |
| LanPer | Number(001,0) | Sim | Lançar % todos os meses ou valerá o vigente |
| ValHEx | Number(001,0) | Sim | Definir como deve calcular o valor das horas extras |
| ConRfl | String(001) | Sim | Considerar Reflexo DSR na média deste pedido |
| RgrJur | Number(003,0) | Sim | Regra de correção e juros |
| DesRes | String(010) | Sim | Descrição resumida do motivo do pedido |

---

## Chave Primária

- CodMtj

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
