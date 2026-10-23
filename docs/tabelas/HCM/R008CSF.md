# R008CSF

## Descrição

Abrangência de Filial para Saldo de Evento

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTab | Number(003,0) | Não | Código da Tabela Eventos |
| CodSal | Number(004,0) | Não | Código do Saldo |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |

---

## Chave Primária

- CodTab
- CodSal
- NumEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R008CSF_000

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |

### IR_R008CSF_003

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

