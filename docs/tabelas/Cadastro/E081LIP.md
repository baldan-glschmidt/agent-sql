# E081LIP

## Descrição

Tabelas - Tabelas de Preços de Venda - Log dos Itens de Produto

---

## Resumo

- Campos: 27
- Chave Primária: 9 campo(s)
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
| DatAlt | Date | Não | Data da última alteração do registro |
| HorAlt | Number(005,0) | Não | Hora da última alteração do registro |
| SeqAlt | Number(004,0) | Não | Sequência da alteração do registro |
| PreBas | Number(021,10) | Não | Valor base do produto na tabela de preço |
| PerDsc | Number(005,2) | Sim | Percentual de desconto a ser concedido |
| PerLim | Number(005,2) | Sim | Percentual de desconto limite a ser concedido |
| PerCom | Number(005,2) | Sim | Percentual a acrescentar ou diminuir à comissão dos representantes |
| TolMai | Number(005,2) | Sim | Percentual de tolerância de preço a maior |
| TolMen | Number(005,2) | Sim | Percentual de tolerância de preço a menor |
| SitReg | String(001) | Não | Situação do produto na tabela de preço |
| PreMt2 | Number(021,10) | Sim | Preço do metro quadrado (M2) |
| VlrCmo | Number(014,5) | Sim | Valor do custo da mão de obra |
| VlrCte | Number(014,5) | Sim | Valor do consumo teórico |
| VlrCpr | Number(014,5) | Sim | Valor do consumo praticado |
| PreOrc | Number(021,10) | Sim | Valor do preço orçado |
| DatOrc | Date | Sim | Data do orçamento |
| CodRep | Number(009,0) | Sim | Código do representante |
| IndExc | String(001) | Sim | Indicativo de que o item foi excluído da tabela de preços |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| VltMen | Number(021,10) | Sim | Valor de tolerância para menos |
| VltMai | Number(021,10) | Sim | Valor de tolerância para mais |

---

## Chave Primária

- CodEmp
- CodTpr
- DatIni
- CodPro
- CodDer
- QtdMax
- DatAlt
- HorAlt
- SeqAlt

---

## Índices

### E081LIPIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodPro
- CodDer

---

## Relacionamentos

### IR_E081LIP_002

**Tabela:** E081TPR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTpr | CodTpr |
| DatIni | DatIni |

### IR_E081LIP_004

**Tabela:** E075DER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |

