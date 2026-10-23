# R130CUS

## Descrição

Custos do Orçamento

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
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| CmpCus | Date | Não | Competência de Custos |
| SeqCus | Number(002,0) | Não | Sequência de Custos |
| CodOem | Number(008,0) | Sim | Código da Entidade |
| CodCid | Number(007,0) | Sim | Código da Cidade |
| TipRea | Number(003,0) | Sim | Tipo de Realização |
| CodIdm | Number(003,0) | Sim | Código do Índice |
| ObsCus | String(200) | Sim | Observação do Custo |

---

## Chave Primária

- CodCua
- CmpCus
- SeqCus

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R130CUS_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

