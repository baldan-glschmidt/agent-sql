# R134AVA

## Descrição

Turmas - Avaliação de Eficácia - Avaliado

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do curso de aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da turma |
| NumEmp | Number(004,0) | Não | Código da empresa do participante |
| TipCol | Number(001,0) | Não | Tipo colaborador participante |
| NumCad | Number(009,0) | Não | Cadastro do colaborador participante |
| EmpAvl | Number(004,0) | Sim | Código da empresa do avaliador |
| TipAvl | Number(001,0) | Sim | Tipo colaborador avaliador |
| CadAvl | Number(009,0) | Sim | Cadastro do colaborador avaliador |
| SitAva | Number(001,0) | Sim | Situação da avaliação |
| DatVen | Date | Sim | Data de vencimento para executar a avaliação |

---

## Chave Primária

- CodCua
- TmaCua
- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134AVA_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

