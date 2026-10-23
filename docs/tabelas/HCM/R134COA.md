# R134COA

## Descrição

Turmas - Conhecimentos Adquiridos

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso |
| TmaCua | Number(006,0) | Não | Código da Turma |
| FamCnc | String(004) | Não | Código da Família de Conhecimentos |
| CodCnc | String(005) | Não | Código do Conhecimento |
| NumRev | Number(006,0) | Sim | Revisão |
| ObsCon | String(500) | Sim | Observações do conhecimento |
| SelCon | String(001) | Sim | Selecionar |

---

## Chave Primária

- CodCua
- TmaCua
- FamCnc
- CodCnc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134COA_002

**Tabela:** R125FAM

| Origem | Destino |
|--------|---------|
| FamCnc | FamCnc |

### IR_R134COA_003

**Tabela:** R125CNC

| Origem | Destino |
|--------|---------|
| FamCnc | FamCnc |
| CodCnc | CodCnc |

