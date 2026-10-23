# R011CBH

## Descrição

Contas do Banco de Horas

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodBhr | Number(005,0) | Não | Código do Banco de Horas |
| DatCri | Date | Não | Data de Criação da Conta |
| DatExt | Date | Sim | Data de Extinção da Conta |
| UsuFec | Number(010,0) | Sim | Usuário que Encerrou a Conta |
| DatFec | Date | Sim | Data do Fechamento |
| HorFec | Number(005,0) | Sim | Hora do Fechamento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodBhr
- DatCri

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R011CBH_003

**Tabela:** R011BHR

| Origem | Destino |
|--------|---------|
| CodBhr | CodBHr |

