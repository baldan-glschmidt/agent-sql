# E001AGR

## Descrição

Tabelas - Transações - Parâmetros de Impostos da Transação

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTns | String(005) | Não | Código da transação |
| CodImp | String(003) | Não | Código do imposto |
| CalImp | String(001) | Sim | Indicativo se a transação calcula o Imposto |
| ImpDoc | String(001) | Sim | Opção de Cálculo na Nota Fiscal a ser efetuado com o valor do imposto |
| OcaFin | String(001) | Sim | Opção de Cálculo no Financeiro da Nota Fiscal a ser efetuado com o valor do imposto |
| CdfAgr | Number(006,0) | Sim | Código do dispositivo fiscal para o imposto agro |

---

## Chave Primária

- CodEmp
- CodTns
- CodImp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E001AGR_001

**Tabela:** E001TNS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTns | CodTns |

### IR_E001AGR_002

**Tabela:** E051IMP

| Origem | Destino |
|--------|---------|
| CodImp | CodImp |

