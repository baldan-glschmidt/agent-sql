# R104REF

## Descrição

JR - Réu(Pessoa Física)

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodPrc | Number(007,0) | Não | Código da Ação |
| EmpReu | Number(004,0) | Não | Empresa do réu |
| TipCol | Number(001,0) | Não | Tipo do colaborador réu da ação |
| NumCad | Number(009,0) | Não | Código do colaborador réu da ação |
| SeqRef | Number(003,0) | Sim | Sequência do Réu |

---

## Chave Primária

- NumEmp
- CodPrc
- EmpReu
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104REF_001

**Tabela:** R104PRJ

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |

