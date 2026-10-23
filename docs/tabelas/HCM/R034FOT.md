# R034FOT

## Descrição

Foto do Colaborador

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa do colaborador |
| TipCol | Number(001,0) | Não | Tipo do colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| FotEmp | Image | Sim | Foto do Colaborador |
| DatFot | Date | Sim | Data da Foto |
| FlaFot | Number(001,0) | Sim | Flag da Foto |
| DatIdx | Date | Sim | Data da indexação da foto para reconhecimento facial |
| HorFot | Number(005,0) | Sim | Hora da Foto |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034FOT_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

