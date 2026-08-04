# E055IIF

## Descrição

Cadastros - Tributos - Parâmetros da apuração do ISS próprio das instituições financeiras

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodImp | String(003) | Não | Código do imposto |
| DatBas | Date | Não | Data base inicial de validade para apuração do valor base do imposto |
| CodRai | Number(007,0) | Não | Código da cidade RAIS utilizada para apuração do ISS Retido |
| FilOri | Number(005,0) | Não | Código da filial |
| FilCtb | Number(005,0) | Sim | Código da filial responsável pela contabilidade do município |
| UsuGer | Number(010,0) | Não | Usuário responsável pela geração do registro |
| DatGer | Date | Não | Data da geração do registro |
| HorGer | Number(005,0) | Não | Hora da geração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E055IIFIndice2

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodImp
- DatBas
- CodRai
- FilOri

---

## Relacionamentos

### IR_E055IIF_003

**Tabela:** E055PAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodImp | CodImp |

