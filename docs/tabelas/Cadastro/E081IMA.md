# E081IMA

## Descrição

Tabelas - Tabelas de Preços de Venda - Itens por Modelo de Produto e Agrupamento de Preço

---

## Resumo

- Campos: 19
- Chave Primária: 5 campo(s)
- Índices: 2
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTpr | String(004) | Não | Código da tabela de preço |
| DatIni | Date | Não | Data validade inicial da tabela de preço |
| CodMod | String(014) | Não | Código do Modelo p/ Produto |
| CodAgm | String(005) | Não | Código de agrupamento de materiais/produtos para preço |
| PreBas | Number(021,10) | Não | Valor base do produto na tabela de preço |
| PerDsc | Number(005,2) | Sim | Percentual de desconto a ser concedido |
| PerLim | Number(005,2) | Sim | Percentual de desconto limite a ser concedido |
| PerCom | Number(005,2) | Sim | Percentual a acrescentar ou diminuir à comissão dos representantes |
| TolMai | Number(005,2) | Sim | Percentual de tolerância de preço a maior |
| TolMen | Number(005,2) | Sim | Percentual de tolerância de preço a menor |
| SitReg | String(001) | Não | Situação do produto na tabela de preço |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| ObsIma | String(100) | Sim | Itens por Modelo de Produto e Agrupamento de Preço - Observação |

---

## Chave Primária

- CodEmp
- CodTpr
- DatIni
- CodMod
- CodAgm

---

## Índices

### E081IMAIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodMod

### E081IMAIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodAgm

---

## Relacionamentos

### IR_E081IMA_002

**Tabela:** E081TPR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTpr | CodTpr |
| DatIni | DatIni |

### IR_E081IMA_003

**Tabela:** E700MOD

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMod | CodMod |

### IR_E081IMA_004

**Tabela:** E013AGP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodAgm | CodAgp |

