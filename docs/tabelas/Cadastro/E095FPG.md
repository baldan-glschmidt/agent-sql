# E095FPG

## Descrição

Cadastros - Fornecedores - Formas de Pagamento

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFpg | Number(002,0) | Não | Código da forma de pagamento |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodFor
- CodEmp
- CodFil
- CodFpg

---

## Índices

### E095FPGIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFpg

---

## Relacionamentos

### IR_E095FPG_000

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

### IR_E095FPG_002

**Tabela:** E095HFO

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E095FPG_003

**Tabela:** E066FPG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFpg | CodFpg |

