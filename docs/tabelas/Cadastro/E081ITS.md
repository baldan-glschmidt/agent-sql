# E081ITS

## Descrição

Tabelas - Tabelas de Preços de Venda - Itens de Serviço

---

## Resumo

- Campos: 21
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
| CodSer | String(014) | Não | Código do serviço da tabela de preço |
| QtdMax | Number(011,2) | Não | Faixa máxima para quantidade de venda válida para o preço |
| PreBas | Number(021,10) | Não | Valor base do serviço na tabela de preço |
| PerDsc | Number(005,2) | Sim | Percentual de desconto a ser concedido |
| PerCom | Number(005,2) | Sim | Percentual a acrescentar ou diminuir à comissão dos representantes |
| TolMai | Number(005,2) | Sim | Percentual de tolerância de preço a maior |
| TolMen | Number(005,2) | Sim | Percentual de tolerância de preço a menor |
| SitReg | String(001) | Não | Situação do serviço na tabela de preço |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| VltMai | Number(021,10) | Sim | Valor de tolerância para mais |
| VltMen | Number(021,10) | Sim | Valor de tolerância para menos |
| ObsIts | String(099) | Sim | Observação do item |
| UniMed | String(003) | Sim | Código da Unidade de Medida de Tributação |

---

## Chave Primária

- CodEmp
- CodTpr
- DatIni
- CodSer
- QtdMax

---

## Índices

### E081ITSIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodSer

---

## Relacionamentos

### IR_E081ITS_002

**Tabela:** E081TPR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTpr | CodTpr |
| DatIni | DatIni |

### IR_E081ITS_003

**Tabela:** E080SER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodSer | CodSer |

