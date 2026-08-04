# E082ITS

## Descrição

Tabelas - Tabelas de Preços de Fornecedores - Itens de Serviço

---

## Resumo

- Campos: 13
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTpr | String(004) | Não | Código da tabela de preço |
| DatIni | Date | Não | Data validade inicial da tabela de preço |
| QtdMax | Number(011,2) | Não | Faixa máxima para quantidade de compra válida para o preço |
| CodSer | String(014) | Não | Código do serviço da tabela de preço |
| CodPro | String(014) | Não | Código do produto da tabela de preço |
| CodDer | String(007) | Não | Código da derivação da tabela de preço |
| PreBas | Number(021,10) | Não | Valor base do serviço na tabela de preço |
| PerDsc | Number(005,2) | Sim | Percentual de desconto a ser concedido |
| SitReg | String(001) | Não | Situação do produto na tabela de preço |
| DatUct | Date | Sim | Data da última cotação/preço do serviço |
| PrzPgt | Number(003,0) | Sim | Prazo de pagamento para Custos |
| ObsIts | String(100) | Sim | Itens de Serviço - Observação |

---

## Chave Primária

- CodEmp
- CodTpr
- DatIni
- QtdMax
- CodSer
- CodPro
- CodDer

---

## Índices

### E082ITSIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodSer

---

## Relacionamentos

### IR_E082ITS_002

**Tabela:** E082TPR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTpr | CodTpr |
| DatIni | DatIni |

### IR_E082ITS_004

**Tabela:** E080SER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodSer | CodSer |

