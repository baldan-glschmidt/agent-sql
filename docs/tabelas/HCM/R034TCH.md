# R034TCH

## Descrição

Tipo de veículos habilitados

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| TipVei | Number(002,0) | Não | Tipo do Veículo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- TipVei

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034TCH_003

**Tabela:** R088TPV

| Origem | Destino |
|--------|---------|
| TipVei | TipTpv |

