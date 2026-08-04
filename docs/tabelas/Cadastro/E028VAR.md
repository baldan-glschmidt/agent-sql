# E028VAR

## Descrição

Integrações - Varejo - Parâmetros da Condição de Pagamento

---

## Resumo

- Campos: 15
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodCpg | String(006) | Não | Código da condição de pagamento |
| CodFpg | Number(002,0) | Sim | Código da forma de pagamento |
| DesCpg | String(050) | Sim | Descrição da condição de pagamento |
| DesFpg | String(030) | Sim | Descrição da forma de pagamento |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAtu | Date | Sim | Data da última alteração do registro |
| HorAtu | Number(005,0) | Sim | Hora da última alteração do registro |
| IndNeg | Number(001,0) | Sim | Indicativo de permissão para negociação no sistema de varejo |
| SitReg | String(001) | Não | Situação do registro |
| TxaJur | Number(005,2) | Sim | Percentual de juros conforme condição de pagamento escolhida. |

---

## Chave Primária

- CodEmp
- CodFil
- CodCpg

---

## Índices

### E028VARIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodCpg

---

## Relacionamentos

### IR_E028VAR_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E028VAR_002

**Tabela:** E028CPG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCpg | CodCpg |

