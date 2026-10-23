# R104INC

## Descrição

JR - Definições Cálculo Reclamatória Trabalhista

---

## Resumo

- Campos: 26
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| GrpInc | Number(003,0) | Não | Código do Grupo de Definições |
| DesGrp | String(050) | Sim | Descrição do Grupo de Definições |
| PedFgt | Number(003,0) | Sim | Código do pedido de FGTS Mensal |
| Fgt13s | Number(003,0) | Sim | Código do pedido de FGTS 13° Salário |
| FgtFer | Number(003,0) | Sim | Código do pedido de FGTS Férias |
| PedIns | Number(003,0) | Sim | Código do pedido de INSS Reclamante |
| Ins13s | Number(003,0) | Sim | Código do pedido de INSS Reclamante - 13° Salário |
| PedInE | Number(003,0) | Sim | Código do pedido de INSS Empresa |
| InsE13 | Number(003,0) | Sim | Código do pedido de INSS Empresa - 13° Salário |
| PedIRF | Number(003,0) | Sim | Código do pedido de IRRF Mensal |
| Irf13s | Number(003,0) | Sim | Código do pedido de IRRF 13° Salário |
| IrfFer | Number(003,0) | Sim | Código do pedido de IRRF Férias |
| IrfPLR | Number(003,0) | Sim | Código do pedido de IRRF PLR |
| PedSal | Number(003,0) | Sim | Código do pedido de salário |
| PedRe1 | Number(003,0) | Sim | Código do pedido de reserva1 |
| PedRe2 | Number(003,0) | Sim | Código do pedido de reserva2 |
| PedRe3 | Number(003,0) | Sim | Código do pedido de reserva3 |
| ObsPed | String(700) | Sim | Observação sobre as definições |
| DefJur | Number(001,0) | Sim | Apuração da quantidade de meses de Juros |
| DefCor | Number(001,0) | Sim | Mês do índice de correção trabalhista |
| CalIRR | Number(001,0) | Sim | Considerar ou não os juros no cálculo do IRRF |
| IRRMes | String(001) | Sim | OBSOLETO - 5.6.1 - IRRF mensal ou acumulado |
| CorIRR | Number(001,0) | Sim | Definição da atualização monetária do IRRF Mensal |
| TipIrf | Number(001,0) | Sim | Tipo de cálculo do IRRF |
| IrfRra | Number(003,0) | Sim | Código do pedido de IRRF RRA |
| GerGps | Number(001,0) | Sim | Define se deve gerar GPS ao realizar integração da reclamatória trabalhista. |

---

## Chave Primária

- GrpInc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
