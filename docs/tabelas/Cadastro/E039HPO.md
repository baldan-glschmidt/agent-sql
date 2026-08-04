# E039HPO

## Descrição

Cadastros - Portadores - Históricos

---

## Resumo

- Campos: 14
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPor | String(004) | Não | Código do portador |
| CodFil | Number(005,0) | Não | Código da filial |
| SalDup | Number(015,2) | Sim | Saldo devedor de duplicatas dos clientes em poder do portador |
| SalOut | Number(015,2) | Sim | Saldo devedor de outros títulos dos clientes em poder do portador |
| SalCre | Number(015,2) | Sim | Saldo dos créditos de clientes em poder do portador |
| LimPor | Number(015,2) | Sim | Valor limite para saldo do portador |
| VlrMin | Number(015,2) | Sim | Valor mínimo de título aceito pelo portador |
| MinPro | Number(002,0) | Sim | Quantidade mínima de dias necessária para processamento no banco |
| CriRat | Number(001,0) | Não | Critério utilizado para rateio |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida - 1 |
| CtaRcr | Number(007,0) | Sim | Conta contábil reduzida - 2 |
| CtaFdv | Number(007,0) | Sim | Conta contábil reduzida - 3 |
| CtaFcr | Number(007,0) | Sim | Conta contábil reduzida - 4 |

---

## Chave Primária

- CodEmp
- CodPor
- CodFil

---

## Índices

### E039HPOIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil

---

## Relacionamentos

### IR_E039HPO_001

**Tabela:** E039POR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPor | CodPor |

### IR_E039HPO_002

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

