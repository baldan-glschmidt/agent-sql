# E055ILC

## Descrição

Cadastros > Tributos > Lista de código LLC 116/03 para apuração do ISS

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 2
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
| SerImp | String(010) | Não | Tipo de Serviço no contexto fiscal baseado na LC 116/2003 |

---

## Chave Primária

- IdeUni

---

## Índices

### E055ILC_FKIndex1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodImp

### E055ILC_FKIndex2

**Tipo:** Não unico

Campos:
- CodEmp
- SerImp

---

## Relacionamentos

### IR_E055ILC_003

**Tabela:** E055PAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodImp | CodImp |

