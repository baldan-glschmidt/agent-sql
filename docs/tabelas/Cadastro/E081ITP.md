# E081ITP

## Descrição

Tabelas - Tabelas de Preços de Venda - Itens de Produto

---

## Resumo

- Campos: 50
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTpr | String(004) | Não | Código da tabela de preço |
| DatIni | Date | Não | Data validade inicial da tabela de preço |
| CodPro | String(014) | Não | Código do produto da tabela de preço |
| CodDer | String(007) | Não | Código da derivação da tabela de preço |
| QtdMax | Number(011,2) | Não | Faixa máxima para quantidade de venda válida para o preço |
| PreBas | Number(021,10) | Não | Valor base do produto na tabela de preço |
| PerDsc | Number(005,2) | Sim | Percentual de desconto a ser concedido |
| PerLim | Number(005,2) | Sim | Percentual de desconto limite a ser concedido |
| PerCom | Number(005,2) | Sim | Percentual a acrescentar ou diminuir à comissão dos representantes |
| TolMai | Number(005,2) | Sim | Percentual de tolerância de preço a maior |
| TolMen | Number(005,2) | Sim | Percentual de tolerância de preço a menor |
| SitReg | String(001) | Não | Situação do produto na tabela de preço |
| IndExc | String(001) | Sim | Indicador se o item da tabela de preço é exceção no grupo |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| ProExt | String(030) | Sim | Código externo do produto |
| PreMt2 | Number(021,10) | Sim | Preço do metro quadrado (M2) |
| VlrCmo | Number(014,5) | Sim | Valor do custo da mão de obra |
| VlrCte | Number(014,5) | Sim | Valor do consumo teórico |
| VlrCpr | Number(014,5) | Sim | Valor do consumo praticado |
| PreOrc | Number(021,10) | Sim | Valor do preço orçado |
| DatOrc | Date | Sim | Data do orçamento |
| CodRep | Number(009,0) | Sim | Código do representante |
| CodPrb | String(014) | Sim | Código do produto base da tabela de preços |
| VltMai | Number(021,10) | Sim | Valor de tolerância para mais |
| VltMen | Number(021,10) | Sim | Valor de tolerância para menos |
| ObsItp | String(099) | Sim | Observação do item |
| UniMed | String(003) | Sim | Código da Unidade de Medida de Tributação |
| AcrFin | Number(005,2) | Sim | Percentual de acréscimo financeiro para produtos com tabela de preço no módulo de vendas |
| VenDsc | Number(005,2) | Sim | Percentual a acrescentar ou diminuir para formação do preço de venda |
| CprDsc | Number(005,2) | Sim | Percentual a acrescentar ou diminuir para formação do preço de compra |
| CodAgg | String(001) | Sim | Código de agrupamento de materiais/produtos para garantia estendida |
| TipCur | Number(001,0) | Sim | Indicativo do tipo de curso online para varejo |
| MgcMin | Number(015,6) | Sim | Percentual de margem de contribuição mínima |
| MgcLim | Number(015,6) | Sim | Percentual de margem de contribuição limite |
| MgcVen | Number(015,6) | Sim | Percentual de margem de contribuição mínima para os vendedores |
| MgcPro | Number(015,6) | Sim | Percentual de margem de contribuição para promoção |
| MgcCom | Number(015,6) | Sim | Percentual de margem de contribuição para comissão |
| PreRef | Number(024,12) | Sim | Preço de referência vinculada a margem de contribuição |
| PreCus | Number(021,10) | Sim | Preço de custo base para o cálculo |
| PrePro | Number(015,6) | Sim | Preço de referência para promoção |
| IndPro | String(001) | Sim | Indicativo se deve considerar como preço promocional para varejo |

---

## Chave Primária

- CodEmp
- CodTpr
- DatIni
- CodPro
- CodDer
- QtdMax

---

## Índices

### E081ITPIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodPro
- CodDer

---

## Relacionamentos

### IR_E081ITP_002

**Tabela:** E081TPR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTpr | CodTpr |
| DatIni | DatIni |

### IR_E081ITP_004

**Tabela:** E075DER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |

