# E081VGE

## Descrição

Tabelas - Tabelas de Preço de Venda - Valores Garantia Estendida

---

## Resumo

- Campos: 29
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTpr | String(004) | Não | Código da tabela de preço |
| DatIni | Date | Não | Data validade inicial da tabela de preço |
| CodAgg | String(005) | Não | Código de agrupamento de materiais/produtos para garantia estendida |
| CodTge | Number(004,0) | Não | Código da Garantia Estendida |
| PrzTge | Number(004,0) | Não | Prazo de garantia estendida (em meses) |
| NumSeq | Number(009,0) | Não | Número sequencial do item na tabela de preços |
| VlrIni | Number(015,2) | Sim | Valor inicial da parcela protegida |
| VlrFim | Number(015,2) | Sim | Valor final da parcela protegida |
| DesTge | String(100) | Sim | Descrição da garantia estendida |
| TipTge | String(002) | Sim | Tipo de Garantia Estendida |
| VlrGar | Number(015,2) | Sim | Valor a ser cobrado do cliente pela garantia estendida |
| PerGar | Number(014,5) | Sim | Percentual a ser cobrado do cliente pela garantia estendida |
| VlrMul | Number(015,2) | Sim | Valor da multa em caso de cancelamento |
| VlrVen | Number(015,2) | Sim | Valor da venda do produto |
| VlrCus | Number(015,2) | Sim | Valor do custo do produto |
| PrzRec | Number(004,0) | Sim | Prazo de recuperação da garantia estendida (em meses) |
| PerRep | Number(014,5) | Sim | Percentual a ser pago ao representante para cálculo de comissão |
| PerGer | Number(014,5) | Sim | Percentual a ser pago ao gerente para cálculo de comissão |
| SitReg | String(001) | Sim | Situação do produto na tabela de preço |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| ObsItp | String(099) | Sim | Observação do item |
| ItePad | String(001) | Sim | Indicativo se o item é serviço padrão de garantia estendida |
| CodSer | String(014) | Sim | Código do serviço da tabela de preço |

---

## Chave Primária

- CodEmp
- CodTpr
- DatIni
- CodAgg
- PrzTge
- CodTge
- NumSeq

---

## Índices

### E081VGEINDICE1

**Tipo:** Não unico

Campos:
- CodEmp
- CodTpr
- DatIni
- CodSer

---

## Relacionamentos

### IR_E081VGE_002

**Tabela:** E081TPR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTpr | CodTpr |
| DatIni | DatIni |

