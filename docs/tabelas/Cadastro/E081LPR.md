# E081LPR

## Descrição

Tabelas - Tabelas de Preços de Venda - Log Validades

---

## Resumo

- Campos: 17
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTpr | String(004) | Não | Código da tabela de preço |
| DatIni | Date | Não | Data início de validade da tabela de preço |
| DatFim | Date | Não | Data final de validade da tabela de preço |
| UsaQtd | String(001) | Não | Indicativo se a tabela utiliza critério de preço por quantidade de venda |
| TolMai | Number(005,2) | Sim | Percentual de tolerância de preço a maior |
| TolMen | Number(005,2) | Sim | Percentual de tolerância de preço a menor |
| PerDsc | Number(005,2) | Sim | Percentual de desconto a ser concedido |
| PerCom | Number(005,2) | Sim | Percentual a acrescentar ou diminuir à comissão dos representantes |
| SitReg | String(001) | Não | Situação do registro |
| VltMai | Number(021,10) | Sim | Valor de tolerância para mais |
| VltMen | Number(021,10) | Sim | Valor de tolerância para menos |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Não | Data da última alteração do registro |
| HorAlt | Number(005,0) | Não | Hora da última alteração do registro |
| SeqAlt | Number(004,0) | Não | Sequência da alteração do registro |
| IndExc | String(001) | Sim | Indicativo de que o item foi excluído da tabela de preços |

---

## Chave Primária

- CodEmp
- CodTpr
- DatIni
- DatAlt
- HorAlt
- SeqAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E081LPR_001

**Tabela:** E081TAB

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTpr | CodTpr |

