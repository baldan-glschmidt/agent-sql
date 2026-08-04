# E081TPR

## Descrição

Tabelas - Tabelas de Preços de Venda - Validades

---

## Resumo

- Campos: 22
- Chave Primária: 3 campo(s)
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
| DatRea | Date | Sim | Data do reajuste processado sobre a tabela |
| PerRea | Number(008,5) | Sim | Percentual do último reajuste processado sobre a tabela |
| SitReg | String(001) | Não | Situação do registro |
| MinRea | Number(015,2) | Sim | Valor Mínimo de Reajuste |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| VltMai | Number(021,10) | Sim | Valor de tolerância para mais |
| VltMen | Number(021,10) | Sim | Valor de tolerância para menos |
| AcrFin | Number(005,2) | Sim | Percentual de acréscimo financeiro para produtos com tabela de preço no módulo de vendas |
| VenDsc | Number(005,2) | Sim | Percentual a acrescentar ou diminuir para formação do preço de venda |
| CprDsc | Number(005,2) | Sim | Percentual a acrescentar ou diminuir para formação do preço de compra |
| ObsTpr | String(100) | Sim | Validades - Observação |

---

## Chave Primária

- CodEmp
- CodTpr
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E081TPR_001

**Tabela:** E081TAB

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTpr | CodTpr |

