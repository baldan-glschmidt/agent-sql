# E002TXN

## Descrição

Cadastros - Finanças - Contas a Pagar/Receber - Relacionamento Tipo de Título X  Natura de Gastos

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 3
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTpt | String(003) | Não | Código do tipo do título a pagar |
| CodNtg | Number(004,0) | Não | Código da natureza de gasto |
| SitTxn | String(001) | Não | Situação do relacionamento |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- CodTpt
- CodNtg

---

## Índices

### E002TXNIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- SitTxn

### E002TXNIndice3

**Tipo:** Não unico

Campos:
- CodEmp
- CodNtg

### E002TXNIndice4

**Tipo:** Não unico

Campos:
- CodTpt

---

## Relacionamentos

### IR_E002TXN_001

**Tabela:** E002TPT

| Origem | Destino |
|--------|---------|
| CodTpt | CodTpt |

### IR_E002TXN_002

**Tabela:** E047NTG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodNtg | CodNtg |

