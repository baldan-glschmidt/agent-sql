# E099UXC

## Descrição

Cadastros - Usuários X Contas Internas Bloqueadas

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
| NumCco | String(014) | Não | Número da conta interna bloqueada |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodUsu
- NumCco

---

## Índices

### E099UXCIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- NumCco

---

## Relacionamentos

### IR_E099UXC_001

**Tabela:** E099USU

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodUsu | CodUsu |

### IR_E099UXC_002

**Tabela:** E600CCO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| NumCco | NumCco |

