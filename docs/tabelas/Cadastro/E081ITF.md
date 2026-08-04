# E081ITF

## Descrição

Tabelas - Tabelas de Preços de Venda - Itens por Faixa da Grade

---

## Resumo

- Campos: 23
- Chave Primária: 5 campo(s)
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
| CodFxa | String(015) | Não | Código da faixa da grade |
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
| ObsItf | String(100) | Sim | Itens por Faixa da Grade - Observação |

---

## Chave Primária

- CodEmp
- CodTpr
- DatIni
- CodPro
- CodFxa

---

## Índices

### E081ITFIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFxa

---

## Relacionamentos

### IR_E081ITF_002

**Tabela:** E081TPR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTpr | CodTpr |
| DatIni | DatIni |

### IR_E081ITF_004

**Tabela:** E084FXA

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFxa | CodFxa |

