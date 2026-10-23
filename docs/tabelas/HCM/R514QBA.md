# R514QBA

## Descrição

Matriz de Gestão - Quadrantes Base

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPer | Number(004,0) | Não | Perfil do Formulário de Matriz de Gestão |
| NumLin | Number(001,0) | Não | Define o número da linha na Matriz de Gestão |
| NumCol | Number(001,0) | Não | Define o número da coluna na Matriz de Gestão |
| SeqQua | Number(004,0) | Sim | Define a sequência do Quadrante (R514QUA) |

---

## Chave Primária

- CodPer
- NumLin
- NumCol

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R514QBA_000

**Tabela:** R514PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

