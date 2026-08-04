# E081VPP

## Descrição

Tabelas - Tabelas de Preço de Venda - Valores Parcela Protegida

---

## Resumo

- Campos: 22
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTpr | String(004) | Não | Código da tabela de preço |
| DatIni | Date | Não | Data validade inicial da tabela de preço |
| NumSeq | Number(009,0) | Não | Número sequencial do item na tabela de preços |
| VlrIni | Number(015,2) | Sim | Valor inicial da parcela protegida |
| VlrFim | Number(015,2) | Sim | Valor final da parcela protegida |
| VlrSeg | Number(015,2) | Sim | Valor a ser cobrado do cliente pela parcela protegida |
| PerSeg | Number(014,5) | Sim | Percentual a ser cobrado do cliente pela parcela protegida |
| SitReg | String(001) | Sim | Situação do produto na tabela de preço |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| ObsItp | String(099) | Sim | Observação do item |
| PerRep | Number(014,5) | Sim | Percentual a ser pago ao representante para cálculo de comissão |
| PerGer | Number(014,5) | Sim | Percentual a ser pago ao gerente para cálculo de comissão |
| PerDev | Number(014,5) | Sim | Percentual a ser pago ao cliente em caso de devolução |
| VlrMul | Number(015,2) | Sim | Valor da multa em caso de cancelamento |
| VlrCus | Number(015,2) | Sim | Valor do custo do serviço de parcela protegida |
| CodSer | String(014) | Sim | Código do serviço da tabela de preço |

---

## Chave Primária

- CodEmp
- CodTpr
- DatIni
- NumSeq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E081VPP_002

**Tabela:** E081TPR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTpr | CodTpr |
| DatIni | DatIni |

