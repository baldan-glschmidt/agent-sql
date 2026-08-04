# E099UXT

## Descrição

Cadastros - Usuários X Transações Bloqueadas

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodUsu | Number(010,0) | Não | Código do Usuário |
| CodTns | String(005) | Não | Código da transação bloqueada para o usuário |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodUsu
- CodTns

---

## Índices

### E099UXTIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodTns

---

## Relacionamentos

### IR_E099UXT_001

**Tabela:** E099USU

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodUsu | CodUsu |

### IR_E099UXT_002

**Tabela:** E001TNS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTns | CodTns |

