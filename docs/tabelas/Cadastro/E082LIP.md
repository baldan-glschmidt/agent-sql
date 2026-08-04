# E082LIP

## Descrição

Tabelas - Tabelas de Preços de Fornecedores - Log dos Itens de Produto

---

## Resumo

- Campos: 17
- Chave Primária: 10 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTpr | String(004) | Não | Código da tabela de preço |
| DatIni | Date | Não | Data validade inicial da tabela de preço |
| ProFor | String(030) | Não | Código do produto no fornecedor |
| QtdMax | Number(011,2) | Não | Faixa máxima para quantidade de compra válida para o preço |
| CodPro | String(014) | Não | Código do produto da tabela de preço |
| CodDer | String(007) | Não | Código da derivação da tabela de preço |
| DatAlt | Date | Não | Data da última alteração do registro |
| HorAlt | Number(005,0) | Não | Hora da última alteração do registro |
| SeqAlt | Number(004,0) | Não | Sequência da alteração do registro |
| PreBas | Number(021,10) | Não | Valor base do produto na tabela de preço |
| PerDsc | Number(005,2) | Sim | Percentual de desconto a ser concedido |
| SitReg | String(001) | Não | Situação do produto na tabela de preço |
| DatUct | Date | Sim | Data da última cotação/preço do produto |
| PreNor | Number(021,10) | Não | O preço normal do item é um indicativo que o preço base é um preço promocional na reposição depósito filiais |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| IndExc | String(001) | Sim | Indicativo de que o item foi excluído da tabela de preços |

---

## Chave Primária

- CodEmp
- CodTpr
- DatIni
- ProFor
- QtdMax
- CodPro
- CodDer
- DatAlt
- HorAlt
- SeqAlt

---

## Índices

### E082LIPIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodPro

---

## Relacionamentos

### IR_E082LIP_002

**Tabela:** E082TPR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTpr | CodTpr |
| DatIni | DatIni |

### IR_E082LIP_005

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

