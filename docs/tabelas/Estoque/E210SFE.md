# E210SFE

## Descrição

Estoques - Saldos Físicos Mensais

---

## Resumo

- Campos: 29
- Chave Primária: 6 campo(s)
- Índices: 2
- Relacionamentos: 5

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação do produto |
| CodDep | String(010) | Não | Código do depósito |
| MesAno | Date | Não | Mês e ano correspondente as informações |
| QtdEst | Number(014,5) | Sim | Quantidade física total do estoque no depósito |
| VlrEst | Number(015,2) | Sim | Valor total em estoque no depósito |
| QtdCfo | Number(014,5) | Sim | Quantidade consignada a fornecedor |
| VlrCfo | Number(015,2) | Sim | Valor total consignado a fornecedor |
| QtdCcl | Number(014,5) | Sim | Quantidade consignada a cliente |
| VlrCcl | Number(015,2) | Sim | Valor total consignado a cliente |
| PreMed | Number(021,10) | Sim | Preço médio |
| DatGer | Date | Sim | Data base da geração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geraçao do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UltMov | Date | Sim | Data último movimento |
| UltSeq | Number(006,0) | Sim | Sequência do último movimento na data de movimentação |
| SalMes | String(001) | Sim | Este saldo corresponde ao mês atual ou foi buscado de outro mês? |
| QtdEla | Number(014,5) | Sim | Quantidade física total do estoque em elaboração no depósito |
| VlrEla | Number(015,2) | Sim | Valor total do estoque em elaboração no depósito |
| PrmIcm | Number(015,6) | Sim | Preço Médio do valor total de ICMS |
| VlrIcm | Number(015,2) | Sim | Valor de ICMS |
| IcmAcf | Number(015,2) | Sim | Valor total de ICMS acumulado para a filial |
| QtdPrp | Number(014,5) | Sim | Quantidade física total do estoque próprio no depósito |
| VlrPrp | Number(015,2) | Sim | Valor total em estoque próprio no depósito |
| USU_vlricm | Number(015,2) | Sim | USU_vlricm |
| USU_icmacf | Number(015,2) | Sim | USU_icmacf |
| USU_prmicm | Number(015,6) | Sim | USU_prmicm |

---

## Chave Primária

- CodEmp
- CodFil
- CodPro
- CodDer
- CodDep
- MesAno

---

## Índices

### E210SFEIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodPro
- CodDer

### E210SFEIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodDep

---

## Relacionamentos

### IR_E210SFE_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E210SFE_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E210SFE_002

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

### IR_E210SFE_003

**Tabela:** E075DER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |

### IR_E210SFE_004

**Tabela:** E205DEP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodDep | CodDep |

