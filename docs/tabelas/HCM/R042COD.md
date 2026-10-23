# R042COD

## Descrição

HomologNet - Informações de Códigos

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| TipCod | Number(001,0) | Não | Tipo de Código |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(005,0) | Não | Código do Evento |
| DesCod | String(150) | Sim | Descrição |
| CodHom | Number(003,0) | Sim | Código HomologNet |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- TipCod
- TabEve
- CodEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R042COD_002

**Tabela:** R042COL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

